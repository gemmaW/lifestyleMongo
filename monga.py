import pandas as pd
from pymongo import MongoClient
import json
import dateutil.parser
import unicodecsv as csv
from operator import itemgetter
import sheets
import newSheets
from datetime import datetime, timedelta, date
import plotGraph

def _connect_mongo(host, port, username, password, db):
    """ A util for making a connection to mongo """

    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)


    return conn[db]


def read_mongo(my_start_str, my_end_str, db, collection, query, host, port, username, password, no_id):
    """ Read from Mongo and Store into DataFrame """

    # Connect to MongoDB
    db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)

    my_starttime = dateutil.parser.parse(my_start_str)
    my_endtime = dateutil.parser.parse(my_end_str)

    query = { "isoCreatedDateTime" : { '$gte': my_starttime, '$lt': my_endtime }, "basketStatus" : "BUY_NOW_COMPLETED" }

    # Make a query to the specific DB and Collection
    cursor = db[collection].find(query)

    # Expand the cursor and construct the DataFrame
    df = pd.DataFrame(list(cursor))

    # Delete the _id
    if no_id:
        del df['_id']

    return df


def generic_regroup(values, keys):
    groups = dict()
    valkeys = [k for k in values[0] if k not in key]
    for d in values:
        key = tuple(d[k] for k in keys)
        if key in groups:
            group = groups[key]
            for k in valkeys:
                group[k] += d[k]
        else:
            groups[key] = d.copy()
    return list(groups.values())


my_start_str = "2016-07-12T00:00:00Z"
my_end_str = "2016-07-12T23:59:59Z"

def mongo_call(startDate, endDate):

    my_start_str = startDate + "T00:00:00Z"
    my_end_str = endDate + "T23:59:59Z"

    x = read_mongo(my_start_str, my_end_str, 'lifestyle-checkout', 'basket', { "orderId" : 600460597 }, '10.10.20.153', 27017, 'reportsUser', 'ch*ckoUt20*6', True)

    y = x.products.values

    total_bookingFee = 0
    total_commission = 0
    total_gtv = 0
    total_transactions = 0
    meal_deals = 0
    total_tickets = 0
    mylist = [['ID', 'Date', 'Performance', 'Total Price', 'Booking Fee', 'Commission Amount', 'Margin %', 'No of Tickets', 'Meal Deal', 'Restaurant Price PP', 'Discounts', 'Platform', 'Restoration Levy']]
    filename = 'sales_' + my_start_str[:10] + '_' + my_end_str[:10] + '.csv'


    list_of_shows=[]
    showsDict = {}
    for item in y:
        parsed_json = json.dumps(item[0], indent=4)
        j = json.loads(parsed_json)

        try:
            promoMessage = j["tickets"][0]["discounts"][0]
        except:
            promoMessage = ""

        list_of_shows.append(j["performance"]["name"])
        final_shows = list(set(list_of_shows))
        key = j["performance"]["name"]
        value = [float(j["displayPrices"]["grandTotal"]),int(j["tickets"][0]["quantity"]), promoMessage]
        showsDict.setdefault(key, []).append(value)



    for item in y:
        parsed_json = json.dumps(item[0], indent=4)
        j = json.loads(parsed_json)
        try:
            md = j["restaurant"]["mealCode"]
            restaurantPPP = j["restaurant"]["pricePerPerson"]
            meal_deals += 1
            #print parsed_json
            #raw_input("Press Enter to continue...")
        except:
            md = "False"
            restaurantPPP = "False"
        try:
            promoMessage = j["tickets"][0]["discounts"][0]
        except:
            promoMessage = ""

        try:
            if j['tickets'][0]['fees'][0]['name'] == "restoration levy":
                restorationLevy = j['tickets'][0]['fees'][0]['value']*int(j["tickets"][0]["quantity"])
                commission = j['tickets'][0]['fees'][1]['value']*int(j["tickets"][0]["quantity"])
            else:
                commission = j['tickets'][0]['fees'][0]['value']*int(j["tickets"][0]["quantity"])
                restorationLevy = j['tickets'][0]['fees'][1]['value']*int(j["tickets"][0]["quantity"])
            bookingFee = j['tickets'][0]['fees'][2]['value']*int(j["tickets"][0]["quantity"])
            vat = 1.20 #Price after tax divided by 1.20 = Price before tax
            netGrandTotal = float(j["displayPrices"]["grandTotal"])/vat
            margin = (1-(netGrandTotal-(commission+bookingFee))/netGrandTotal)*100
        except:
            restorationLevy = 0
            commission = 0
            bookingFee = 0
            margin = 0

        #print x.orderId[total_transactions], x.isoLastModifiedDateTime[total_transactions].strftime("%Y-%m-%d %H:%M"), j["performance"]["name"], float(j["displayPrices"]["grandTotal"]), int(j["tickets"][0]["quantity"]), md, restaurantPPP, promoMessage, j["financeData"]["productSourceSystem"]
        mylist.append([x.orderId[total_transactions], x.isoLastModifiedDateTime[total_transactions].strftime("%Y-%m-%d %H:%M"), j["performance"]["name"], float(j["displayPrices"]["grandTotal"]), bookingFee, commission, margin, int(j["tickets"][0]["quantity"]), md, restaurantPPP, promoMessage, j["financeData"]["productSourceSystem"], restorationLevy])
        #print j['displayPrices']
        #print float(j["displayPrices"]["grandTotal"])
        total_transactions += 1
        total_gtv = total_gtv + float(j["displayPrices"]["grandTotal"])
        total_tickets = total_tickets + int(j["tickets"][0]["quantity"])
        total_commission = total_commission + commission
        total_bookingFee = total_bookingFee + bookingFee

    data_packet = [mylist, filename, total_gtv, total_transactions, total_tickets, meal_deals, total_commission, total_bookingFee, vat, showsDict]
    return data_packet


def create_docs(mylist, filename, total_gtv, total_transactions, total_tickets, meal_deals, total_commission, total_bookingFee, vat, showsDict):
    myfile = open(filename, 'wb')
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    print(mylist)
    mylist.insert(0, [''])
    mylist.insert(0, ['# ----------------------------------------'])
    mylist.insert(0, ['# No. of Meal Deals: '+str(meal_deals)])
    mylist.insert(0, ['# Total Tickets: '+str(total_tickets)])
    mylist.insert(0, ['# Total Transactions: '+str(total_transactions)])
    mylist.insert(0, ['# Margin %: '+str((1-(total_gtv/vat-(total_commission+total_bookingFee))/(total_gtv/vat))*100)])
    mylist.insert(0, ['# Total Margin: '+str(total_commission+total_bookingFee)])
    mylist.insert(0, ['# Total GTV: '+str(total_gtv)])
    mylist.insert(0, ['# End Date: '+my_end_str])
    mylist.insert(0, ['# Start Date: '+my_start_str])
    mylist.insert(0, ['# 01_Sales Overview'])
    mylist.insert(0, ['# ----------------------------------------'])


    mylist.append([''])
    mylist.append([''])
    mylist.append(['Name','TTV','Tickets'])


    showsList =[]
    for k,v in showsDict.items():
        ttv = [item[0] for item in v]
        tickets = [item[1] for item in v]
        # print k,ttv
        showsList.append([k,"%.2f" % round(sum(ttv),2),sum(tickets)])
        #wr.writerow((k,("%.2f" % round(sum(ttv),2)),sum(tickets)))

    sortedList = sorted(showsList, key=itemgetter(2), reverse=True)
    for i in sortedList:
        mylist.append(i)

    for i in mylist:
        wr.writerow(i)

    sheets.main(mylist)


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def main():
    mainList = mongo_call("2016-07-13", "2016-07-13")
    create_docs(mainList[0], mainList[1], mainList[2], mainList[3], mainList[4], mainList[5], mainList[6], mainList[7], mainList[8], mainList[9])


def ls_summary():
    start_date = date(2016, 7, 7)
    end_date = date(2016, 7, 14)
    budget, lastYear = newSheets.main()
    print("ly:")
    print(lastYear)
    print("budget:")
    print(budget)
    budgetPlot = {}
    for single_date in daterange(start_date, end_date):
        lyDate = (single_date - timedelta(days=365))
        mainList = mongo_call(single_date.strftime("%Y-%m-%d"), single_date.strftime("%Y-%m-%d"))
        budget[single_date.strftime("%d/%m/%Y")].append(str(mainList[2]))
        budget[single_date.strftime("%d/%m/%Y")].append(str(lastYear[lyDate.strftime("%d/%m/%Y")][1]))
        budgetPlot[single_date.strftime("%d/%m/%Y")] = budget[single_date.strftime("%d/%m/%Y")]
        print(budget[single_date.strftime("%d/%m/%Y")])
    plotGraph.trace_graph(budgetPlot)


ls_summary()





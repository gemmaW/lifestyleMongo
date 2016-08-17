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
from dateutil import tz



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

    # METHOD 1: Hardcode zones:
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('Europe/London')

    my_start_str = startDate + "T00:00:00"
    my_end_str = endDate + "T23:59:59"

    x = read_mongo(my_start_str, my_end_str, 'lifestyle-checkout', 'basket', { "orderId" : 600460597 }, '10.10.20.153',
                   27017, 'reportsUser', 'ch*ckoUt20*6', True)

    x.to_csv("mongo_dump.csv", sep='\t', encoding='utf-8')

    y = x.products.values

    #f = open('y.txt', 'w')
    #f.write(json.dumps(y))
    #f.close()

    total_bookingFee = 0
    total_commission = 0
    total_gtv = 0
    total_transactions = 0
    meal_deals = 0
    total_tickets = 0
    mylist = [['ID', 'Date', 'Performance', 'Total Price', 'Booking Fee', 'Commission Amount', 'Margin %',
               'No of Tickets', 'Meal Deal', 'Restaurant Price PP', 'Discounts', 'Platform', 'Restoration Levy',
               'Venue', 'User Agent', 'Referrer', 'Supplier Key', 'ENTA Reference', 'Performance Date & Time',
               'Supplier Group', 'Price Per Ticket', 'Restaurant Name', 'Restaurant Code']]
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
            meal_deals += int(j["tickets"][0]["quantity"])
            #print parsed_json not used
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

        try:
            referer = j["originSource"]["referer"]
        except:
            referer = ""

        try:
            agent = j["originSource"]["userAgent"]
        except:
            agent = ""

        try:
            supplier = j["financeData"]["supplier"]["supplierName"]
        except:
            supplier = ""

        try:
            supplierKey = j["financeData"]["supplier"]["supplierKey"]
        except:
            supplierKey = ""

        try:
            entaRef = j["financeData"]["bookingReference"]
        except:
            entaRef = ""

        try:
            perfYear = str(j["performance"]["startDate"]["date"]["year"])
        except:
            perfYear = ""

        try:
            perfMonth = str(j["performance"]["startDate"]["date"]["month"])
        except:
            perfMonth = ""

        try:
            perfDay = str(j["performance"]["startDate"]["date"]["day"])
        except:
            perfDay = ""

        try:
            perfHour = str(j["performance"]["startDate"]["time"]["hour"])
        except:
            perfHour = ""

        try:
            perfMin = str(j["performance"]["startDate"]["time"]["minute"])
        except:
            perfMin = ""

        try:
            officeCode = j["financeData"]["officeCode"]
        except:
            officeCode = ""

        try:
            pricePerTkt = j["displayPrices"]["pricePerTicket"]
        except:
            pricePerTkt = ""

        try:
            restaurantName = j["restaurant"]["name"]
        except:
            restaurantName = ""

        try:
            restaurantId = j["restaurant"]["restaurantId"]
        except:
            restaurantId = ""

        perfDateG = perfYear + "-" + perfMonth + "-" + perfDay + " " + perfHour + ":" + perfMin

        times = (str(x.isoLastModifiedDateTime[total_transactions])).split(":")
        donetime = times[0] + ":" + times[1]

        # utc = datetime.utcnow()
        utc = datetime.strptime(donetime, '%Y-%m-%d %H:%M')

        # Tell the datetime object that it's in UTC time zone since
        # datetime objects are 'naive' by default
        utc = utc.replace(tzinfo=from_zone)

        # Convert time zone to London
        londonTime = utc.astimezone(to_zone)
        timeString = londonTime.strftime('%Y-%m-%d %H:%M')

        # print x.orderId[total_transactions], x.isoLastModifiedDateTime[total_transactions].strftime("%Y-%m-%d %H:%M"),
        # j["performance"]["name"], float(j["displayPrices"]["grandTotal"]), int(j["tickets"][0]["quantity"]), md,
        # restaurantPPP, promoMessage, j["financeData"]["productSourceSystem"]
        mylist.append([str(x.orderId[total_transactions]), timeString, j["performance"]["name"],
                       float(j["displayPrices"]["grandTotal"]), bookingFee, commission, margin, int(j["tickets"][0]
                                                                                                    ["quantity"]), md,
                       restaurantPPP, promoMessage, j["financeData"]["productSourceSystem"], restorationLevy, supplier,
                       agent, referer, supplierKey, entaRef, perfDateG, officeCode, pricePerTkt, restaurantName,
                       restaurantId])
        # print j['displayPrices']
        # print float(j["displayPrices"]["grandTotal"])
        total_transactions += 1
        total_gtv = round(total_gtv + float(j["displayPrices"]["grandTotal"]),2)
        total_tickets = total_tickets + int(j["tickets"][0]["quantity"])
        total_commission = round(total_commission + commission,2)
        total_bookingFee = total_bookingFee + bookingFee

    data_packet = [mylist, filename, total_gtv, total_transactions, total_tickets, meal_deals, total_commission,
                   total_bookingFee, vat, showsDict, startDate, endDate]
    return data_packet


def create_docs(mylist, filename, total_gtv, total_transactions, total_tickets, meal_deals, total_commission,
                total_bookingFee, vat, showsDict, startDate, endDate):
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
    mylist.insert(0, ['# End Date: '+endDate])
    mylist.insert(0, ['# Start Date: '+startDate])
    mylist.insert(0, ['# 01_Sales Overview'])
    mylist.insert(0, ['# ----------------------------------------'])

    mylist.append([''])
    mylist.append([''])
    mylist.append(['Name', 'TTV', 'Tickets'])

    showsList = []
    for k,v in showsDict.items():
        ttv = [item[0] for item in v]
        tickets = [item[1] for item in v]
        # print k,ttv
        showsList.append([k, "%.2f" % round(sum(ttv), 2), sum(tickets)])
        # wr.writerow((k,("%.2f" % round(sum(ttv),2)),sum(tickets)))

    sortedList = sorted(showsList, key=itemgetter(2), reverse=True)
    for i in sortedList:
        mylist.append(i)

    for i in mylist:
        wr.writerow(i)

    sheets.main(mylist)


def create_finance(mylist, filename, total_gtv, total_transactions, total_tickets, meal_deals, total_commission,
                   total_bookingFee, vat, showsDict, startDate, endDate):
    myfile = open(filename, 'wb')
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    mylist.append([''])
    mylist.append([''])
    mylist.append(['Name', 'TTV', 'Tickets'])

    showsList = []
    for k,v in showsDict.items():
        ttv = [item[0] for item in v]
        tickets = [item[1] for item in v]
        # print k,ttv
        showsList.append([k, "%.2f" % round(sum(ttv), 2), sum(tickets)])
        # wr.writerow((k,("%.2f" % round(sum(ttv),2)),sum(tickets)))

    sortedList = sorted(showsList, key=itemgetter(2), reverse=True)
    for i in sortedList:
        mylist.append(i)

    for i in mylist:
        wr.writerow(i)

    sheets.main(mylist)
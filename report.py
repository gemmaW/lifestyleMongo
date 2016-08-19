import monga
import pandas as pd
from pymongo import MongoClient
import dateutil.parser
import unicodecsv as csv
from operator import itemgetter
import sheets
import newSheets
from datetime import datetime, timedelta, date
import plotGraph
import datetime
import time

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def ls_summary():
    startDate = datetime.datetime.strptime("2016,08,08", "%Y,%m,%d")
    endDate = datetime.datetime.strptime("2016,08,15", "%Y,%m,%d")

    # start_date = date(2016, 7, 16)
    # end_date = date(2016, 7, 18)
    budget, lastYear = newSheets.main()
    # print("ly:")
    # print(lastYear)
    # print("budget:")
    # print(budget)
    budgetPlot = {}
    for single_date in daterange(startDate, endDate):
        lyDate = (single_date - timedelta(days=365))
        mainList = monga.mongo_call(single_date.strftime("%Y-%m-%d"), single_date.strftime("%Y-%m-%d"))
        budget[single_date.strftime("%d/%m/%Y")].append(str(mainList[2]))
        budget[single_date.strftime("%d/%m/%Y")].append(str(lastYear[lyDate.strftime("%d/%m/%Y")][1]))
        budgetPlot[single_date.strftime("%d/%m/%Y")] = budget[single_date.strftime("%d/%m/%Y")]
        # print("---------------")
        # print(single_date.strftime("%d/%m/%Y"))
        # print(budget[single_date.sctrftime("%d/%m/%Y")])
        # print(lyDate)
    plotGraph.trace_graph(budgetPlot)


def sales_by_show():
    mainList = monga.mongo_call("2016-08-18", "2016-08-19")
    monga.create_docs(mainList[0], mainList[1], mainList[2], mainList[3], mainList[4], mainList[5], mainList[6],
                      mainList[7], mainList[8], mainList[9], mainList[10], mainList[11])


def hourly_heatmap():
    mainList = monga.mongo_call("2016-08-08", "2016-08-14")
    plotGraph.hourly_heat(mainList[0][1:])


def today_sales():
    to_day = (time.strftime("%Y-%m-%d"))
    mainList = monga.mongo_call(to_day, to_day)
    print("Total GTV: " + (str(mainList[2])))
    print("Total Bookings:" + (str(mainList[3])))
    print("Total Tickets:" + (str(mainList[4])))
    print("Total Commission: " + (str(mainList[6])))


def quick_sales():
    mainList = monga.mongo_call("2016-08-15", "2016-08-19")
    print("Total GTV: " + (str(mainList[2])))
    print("Total Bookings:" + (str(mainList[3])))
    print("Total Tickets:" + (str(mainList[4])))
    print("Total Commission: " + (str(mainList[6])))


def show_sales():
    mainList = monga.mongo_call("2016-06-01", "2016-08-13")
    showD = mainList[9]
    showX = input('Enter the show (must be precise): ')
    v = showD[showX]
    gtv = [item[0] for item in v]
    tickets = [item[1] for item in v]
    print("Show: " + str(showX))
    print("Total GTV:" + str(sum(gtv)))
    print("Total Tickets:" + str(sum(tickets)))


def show_of_the_month():
    mainList = monga.mongo_call("2016-08-01", "2016-08-31")
    showD = mainList[9]
    sotmShow = "In the Heights"
    v = showD[sotmShow]
    gtv = [item[0] for item in v]
    tickets = [item[1] for item in v]
    print("SOTM: " + str(sotmShow))
    print("Total GTV:" + str(sum(gtv)))
    print("Total Tickets:" + str(sum(tickets)))


def fringe():
    mainList = monga.mongo_call("2016-08-15", "2016-08-31")
    showG = mainList[9]
    comedyShow = "The Fringe Comedy Awards Show"
    g = showG[comedyShow]
    gtv = [item[0] for item in g]
    tickets = [item[1] for item in g]
    print("Show Update: " + str(comedyShow))
    print("Total GTV:" + str(sum(gtv)))
    print("Total Tickets:" + str(sum(tickets)))


def sunny_afternoon():
    mainList = monga.mongo_call("2016-08-17", "2016-08-19")
    showD = mainList[9]
    saleShow = "Sunny Afternoon"
    g = showD[saleShow]
    gtv = [item[0] for item in g]
    tickets = [item[1] for item in g]
    print("Show Update: " + str(saleShow))
    print("Total GTV:" + str(sum(gtv)))
    print("Total Tickets:" + str(sum(tickets)))


def nineteen84_the_play():
    mainList = monga.mongo_call("2016-08-17", "2016-08-17")
    showD = mainList[9]
    saleShow = "1984 The Play"
    g = showD[saleShow]
    gtv = [item[0] for item in g]
    tickets = [item[1] for item in g]
    print("Show Update: " + str(saleShow))
    print("Total GTV:" + str(sum(gtv)))
    print("Total Tickets:" + str(sum(tickets)))


def hobsons_choice():
    mainList = monga.mongo_call("2016-08-17", "2016-08-18")
    showD = mainList[9]
    saleShow = "Hobson's Choice"
    g = showD[saleShow]
    gtv = [item[0] for item in g]
    tickets = [item[1] for item in g]
    print("Show Update: " + str(saleShow))
    print("Total GTV:" + str(sum(gtv)))
    print("Total Tickets:" + str(sum(tickets)))


def american_idiot():
    mainList = monga.mongo_call("2016-08-19", "2016-08-19")
    showD = mainList[9]
    saleShow = "American Idiot"
    g = showD[saleShow]
    gtv = [item[0] for item in g]
    tickets = [item[1] for item in g]
    print("Show Update: " + str(saleShow))
    print("Total GTV:" + str(sum(gtv)))
    print("Total Tickets:" + str(sum(tickets)))


def go_between():
    mainList = monga.mongo_call("2016-08-20", "2016-08-20")
    showD = mainList[9]
    saleShow = "The Go-Between"
    g = showD[saleShow]
    gtv = [item[0] for item in g]
    tickets = [item[1] for item in g]
    print("Show Update: " + str(saleShow))
    print("Total GTV:" + str(sum(gtv)))
    print("Total Tickets:" + str(sum(tickets)))


def the_truth():
    mainList = monga.mongo_call("2016-08-21", "2016-08-21")
    showD = mainList[9]
    saleShow = "The Truth"
    g = showD[saleShow]
    gtv = [item[0] for item in g]
    tickets = [item[1] for item in g]
    print("Show Update: " + str(saleShow))
    print("Total GTV:" + str(sum(gtv)))
    print("Total Tickets:" + str(sum(tickets)))


def woman_in_black():
    mainList = monga.mongo_call("2016-08-22", "2016-08-22")
    showD = mainList[9]
    saleShow = "The Woman In Black"
    g = showD[saleShow]
    gtv = [item[0] for item in g]
    tickets = [item[1] for item in g]
    print("Show Update: " + str(saleShow))
    print("Total GTV:" + str(sum(gtv)))
    print("Total Tickets:" + str(sum(tickets)))


def jersey_boys():
    mainList = monga.mongo_call("2016-08-23", "2016-08-23")
    showD = mainList[9]
    saleShow = "Jersey Boys"
    g = showD[saleShow]
    gtv = [item[0] for item in g]
    tickets = [item[1] for item in g]
    print("Show Update: " + str(saleShow))
    print("Total GTV:" + str(sum(gtv)))
    print("Total Tickets:" + str(sum(tickets)))


def other_half():
    mainList = monga.mongo_call("2016-08-24", "2016-08-24")
    showD = mainList[9]
    saleShow = "How the Other Half Loves"
    g = showD[saleShow]
    gtv = [item[0] for item in g]
    tickets = [item[1] for item in g]
    print("Show Update: " + str(saleShow))
    print("Total GTV:" + str(sum(gtv)))
    print("Total Tickets:" + str(sum(tickets)))


def funny_girl():
    mainList = monga.mongo_call("2016-08-25", "2016-08-25")
    showD = mainList[9]
    saleShow = "Funny Girl"
    g = showD[saleShow]
    gtv = [item[0] for item in g]
    tickets = [item[1] for item in g]
    print("Show Update: " + str(saleShow))
    print("Total GTV:" + str(sum(gtv)))
    print("Total Tickets:" + str(sum(tickets)))


def days_out():
    mainList = monga.mongo_call("2016-08-17", "2016-08-17")
    daysOutId = mainList[0]
    daysOutShow = "630"
    g = daysOutId[daysOutShow]
    gtv = [item[0] for item in g]
    tickets = [item[1] for item in g]
    monga.create_docs(mainList[0], mainList[1], mainList[2], mainList[3], mainList[4], mainList[5], mainList[6],
                      mainList[7], mainList[8], mainList[9], mainList[10], mainList[11])


def mega_friday():
    mainList = monga.mongo_call("2016-08-26", "2016-08-26")
    showD = mainList[9]
    saleShowOne = "Sunny Afternoon"
    g = showD[saleShowOne]
    gtv1 = [item[0] for item in g]
    tickets1 = [item[1] for item in g]
    saleShowTwo = "1984 The Play"
    g = showD[saleShowTwo]
    gtv2 = [item[0] for item in g]
    tickets2 = [item[1] for item in g]
    saleShowThree = "Hobson's Choice"
    g = showD[saleShowThree]
    gtv3 = [item[0] for item in g]
    tickets3 = [item[1] for item in g]
    saleShowFour = "American Idiot"
    g = showD[saleShowFour]
    gtv4 = [item[0] for item in g]
    tickets4 = [item[1] for item in g]
    saleShowFive = "The Go-Between"
    g = showD[saleShowFive]
    gtv5 = [item[0] for item in g]
    tickets5 = [item[1] for item in g]
    saleShowSix = "The Truth"
    g = showD[saleShowSix]
    gtv6 = [item[0] for item in g]
    tickets6 = [item[1] for item in g]
    saleShowSeven = "The Woman In Black"
    g = showD[saleShowSeven]
    gtv7 = [item[0] for item in g]
    tickets7 = [item[1] for item in g]
    saleShowEight = "Jersey Boys"
    g = showD[saleShowEight]
    gtv8 = [item[0] for item in g]
    tickets8 = [item[1] for item in g]
    saleShowNine = "How the Other Half Loves"
    g = showD[saleShowNine]
    gtv9 = [item[0] for item in g]
    tickets9 = [item[1] for item in g]
    saleShowTen = "Funny Girl"
    g = showD[saleShowTen]
    gtv10 = [item[0] for item in g]
    tickets10 = [item[1] for item in g]
    print("Mega Friday: GTV for all shows from the fortnight: £" + str(sum(gtv1+gtv2+gtv3+gtv4+gtv5+gtv6+gtv7+gtv8+gtv9+
                                                                           gtv10)))
    print("Mega Friday: Tickets for all shows from the fortnight: " + str(sum(tickets1+tickets2+tickets3+tickets4+
                                                                              tickets5+tickets6+tickets7+tickets8+
                                                                              tickets9+tickets10)))


def bi_monthly_finance():
    mainList = monga.mongo_call("2016-08-15", "2016-08-16")
    monga.create_finance(mainList[0], mainList[1], mainList[2], mainList[3], mainList[4], mainList[5], mainList[6],
                      mainList[7], mainList[8], mainList[9], mainList[10], mainList[11])


def choose_report():
    # input = raw_input
    userChoice = int(input('Choose a report: /n (1) summary (2) sales by show (3) hourly (4) today (5) quick check '
                           '(6) show spot (7) SOTM (8) Bi-Monthly Finance (9) Fringe (10) Sunny Afternoon (11) 1984 '
                           '(12) Hobsons Choice (13) American Idiot (14) Go-Between (15) The Truth '
                           '(16) Woman in Black (17) Jersey Boys (18) Other Half Loves (19) Funny Girl '
                           '(20) Mega Friday (21) Days Out '))
    if userChoice == 1:
        ls_summary()
    if userChoice == 2:
        sales_by_show()
    if userChoice == 3:
        hourly_heatmap()
    if userChoice == 4:
        today_sales()
    if userChoice == 5:
        quick_sales()
    if userChoice == 6:
        show_sales()
    if userChoice == 7:
        show_of_the_month()
    if userChoice == 8:
        bi_monthly_finance()
    if userChoice == 9:
        fringe()
    if userChoice == 10:
        sunny_afternoon()
    if userChoice == 11:
        nineteen84_the_play()
    if userChoice == 12:
        hobsons_choice()
    if userChoice == 13:
        american_idiot()
    if userChoice == 14:
        go_between()
    if userChoice == 15:
        the_truth()
    if userChoice == 16:
        woman_in_black()
    if userChoice == 17:
        jersey_boys()
    if userChoice == 18:
        other_half()
    if userChoice == 19:
        funny_girl()
    if userChoice == 20:
        mega_friday()
    if userChoice == 21:
        days_out()


choose_report()



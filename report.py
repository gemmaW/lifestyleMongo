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


# def show_report():
#     mainList = monga.mongo_call("2016-07-25", "2016-07-25")
#     monga.create_docs(mainList[0], mainList[1], mainList[2], mainList[3], mainList[4], mainList[5], mainList[6], mainList[7], mainList[8], mainList[9], mainList[10], mainList[11])


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
    mainList = monga.mongo_call("2016-08-15", "2016-08-15")
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
    mainList = monga.mongo_call("2016-08-08", "2016-08-15")
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


def bi_monthly_finance():
    mainList = monga.mongo_call("2016-08-15", "2016-08-16")
    monga.create_finance(mainList[0], mainList[1], mainList[2], mainList[3], mainList[4], mainList[5], mainList[6],
                      mainList[7], mainList[8], mainList[9], mainList[10], mainList[11])


def choose_report():
    # input = raw_input
    userChoice = int(input('Choose a report: /n (1) summary (2) sales by show (3) hourly (4) today (5) quick check '
                           '(6) show spot (7) SOTM (8) Bi-Monthly Finance (9) Fringe '))
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

choose_report()

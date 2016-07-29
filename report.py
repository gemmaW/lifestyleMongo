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
import calendar


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


# def show_report():
#     mainList = monga.mongo_call("2016-07-25", "2016-07-25")
#     monga.create_docs(mainList[0], mainList[1], mainList[2], mainList[3], mainList[4], mainList[5], mainList[6], mainList[7], mainList[8], mainList[9], mainList[10], mainList[11])


def ls_summary():
    startDate = datetime.datetime.strptime("2016,07,18", "%Y,%m,%d")
    endDate = datetime.datetime.strptime("2016,07,25", "%Y,%m,%d")

    # start_date = date(2016, 7, 16)
    # end_date = date(2016, 7, 18)
    budget, lastYear = newSheets.main()
    # print("ly:")
    # print(lastYear)
    # print("budget:")
    # print(budget)
    budgetPlot = {}
    for single_date in daterange(startDate, endDate):
        lyDate = (single_date - timedelta(days=364))
        mainList = monga.mongo_call(single_date.strftime("%Y-%m-%d"), single_date.strftime("%Y-%m-%d"))
        budget[single_date.strftime("%d/%m/%Y")].append(str(mainList[2]))
        budget[single_date.strftime("%d/%m/%Y")].append(str(lastYear[lyDate.strftime("%d/%m/%Y")][1]))
        budgetPlot[single_date.strftime("%d/%m/%Y")] = budget[single_date.strftime("%d/%m/%Y")]
        print("---------------")
        print(single_date.strftime("%d/%m/%Y"))
        # print(budget[single_date.strftime("%d/%m/%Y")])
        print(lyDate)
    plotGraph.trace_graph(budgetPlot)


def sales_by_show():
    mainList = monga.mongo_call("2016-07-28", "2016-07-29")
    monga.create_docs(mainList[0], mainList[1], mainList[2], mainList[3], mainList[4], mainList[5], mainList[6], mainList[7], mainList[8], mainList[9], mainList[10], mainList[11])

# ls_summary()
# sales_by_show()


def hourly_heatmap():
    mainList = monga.mongo_call("2016-07-18", "2016-07-24")
    plotGraph.hourly_heat(mainList[0][1:])


def today_spot():
    to_day = (time.strftime("%d/%m/%Y"))
    mainList = monga.mongo_call(to_day, to_day)
    print("Total GTV:" + "£" + (str(mainList[2])))
    print("Total Bookings:" + (str(mainList[3])))
    print("Total Tickets:" + (str(mainList[4])))
    print("Total Commission:" + "£" + (str(mainList[6])))


def quick_spot():
    mainList = monga.mongo_call("2016-06-01", "2016-06-30")
    print("Total GTV:" + "£" + (str(mainList[2])))
    print("Total Bookings:" + (str(mainList[3])))
    print("Total Tickets:" + (str(mainList[4])))
    print("Total Commission:" + "£" + (str(mainList[6])))


# def spot_check():
#     try:
#         year1 = str(input('Enter a year: (START) (' + str(date.today().year) + '): '))
#     except:
#         year1 = str(date.today().year)
#     if year1 == '':
#         year1 = str(date.today().year)
#         print(year1)
#         month1 = input('Enter a month: (START) ')
#         day1 = input('Enter a day: (START) ')
#     try:
#         year2 = str(input('Enter a year: (END) (' + str(date.today().year) + '): '))
#     except:
#         year2 = str(date.today().year)
#     if year2 == '':
#         year2 = str(date.today().year)
#         print(year2)
#         month2 = input('Enter a month: (END) ')
#         day2 = input('Enter a day: (END) ')
#
#
#     mainList = monga.mongo_call(startTime, endTime)
#     print("Total GTV:" + "£" + (str(mainList[2])))
#     print("Total Bookings:" + (str(mainList[3])))
#     print("Total Tickets:" + (str(mainList[4])))
#     print("Total Commission:" + "£" + (str(mainList[6])))


def sotm_show():
    # monthInput = input('Enter the first day of the month you require (yyyy-mm-dd): ')
    # # get the last day of the month from input
    # getLastD = calendar.monthrange(2016, 7)
    # print(getLastD)
    #
    # mainList = monga.mongo_call(str(monthInput), "2016-07-31")
    mainList = monga.mongo_call("2016-08-01", "2016-08-31")
    showD = mainList[9]
    sotmShow = input('Enter the show (must be precise): ')
    v = showD[sotmShow]
    gtv = [item[0] for item in v]
    tickets = [item[1] for item in v]
    print("SOTM: " + str(sotmShow))
    print("Total GTV:" + "£" + str(sum(gtv)))
    print("Total Tickets:" + str(sum(tickets)))


def choose_report():
    # input = raw_input
    userChoice = int(eval(input('Choose a report: /n (1) summary (2) sales by show (3) hourly (4) today (5) quick spot (6) SOTM ')))
    if userChoice == 1:
        ls_summary()
    if userChoice == 2:
        sales_by_show()
    if userChoice == 3:
        hourly_heatmap()
    if userChoice == 4:
        today_spot()
    if userChoice == 5:
        quick_spot()
    if userChoice == 6:
        sotm_show()
choose_report()

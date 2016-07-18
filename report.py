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



def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def show_report():
    mainList = monga.mongo_call("2016-07-13", "2016-07-13")
    monga.create_docs(mainList[0], mainList[1], mainList[2], mainList[3], mainList[4], mainList[5], mainList[6], mainList[7], mainList[8], mainList[9], mainList[10], mainList[11])


def ls_summary():
    start_date = date(2016, 7, 16)
    end_date = date(2016, 7, 18)
    budget, lastYear = newSheets.main()
    # print("ly:")
    # print(lastYear)
    # print("budget:")
    # print(budget)
    budgetPlot = {}
    for single_date in daterange(start_date, end_date):
        lyDate = (single_date - timedelta(days=365))
        mainList = monga.mongo_call(single_date.strftime("%Y-%m-%d"), single_date.strftime("%Y-%m-%d"))
        budget[single_date.strftime("%d/%m/%Y")].append(str(mainList[2]))
        budget[single_date.strftime("%d/%m/%Y")].append(str(lastYear[lyDate.strftime("%d/%m/%Y")][1]))
        budgetPlot[single_date.strftime("%d/%m/%Y")] = budget[single_date.strftime("%d/%m/%Y")]
        # print(budget[single_date.strftime("%d/%m/%Y")])
    plotGraph.trace_graph(budgetPlot)


def input_show_report():
    year1 = str(input('Enter a year (' + str(date.today().year) + '): '))
    print(year1)
    if year1 is False:
        year1 = date.today().year
    month1 = str(input('Enter a month: '))
    day1 = str(input('Enter a day: '))
    startDate = datetime.strptime(year1 + "-" + month1 + "-" + day1, "%Y-%m-%d")
    year2 = str(input('Enter a year: '))
    month2 = str(input('Enter a month: '))
    day2 = str(input('Enter a day: '))
    endDate = datetime.strptime(year2 + "-" + month2 + "-" + day2, "%Y-%m-%d")
    mainList = monga.mongo_call(year1 + "-" + month1 + "-" + day1, year2 + "-" + month2 + "-" + day2)
    monga.create_docs(mainList[0], mainList[1], mainList[2], mainList[3], mainList[4], mainList[5], mainList[6], mainList[7], mainList[8], mainList[9], mainList[10], mainList[11])

# ls_summary()
input_show_report()

# def get_date_input():
#     year = int(input('Enter a year'))
#     month = int(input('Enter a month'))
#     day = int(input('Enter a day'))
#     date1 = datetime.date(year, month, day)

# def input_ls_summary():
#     start_d = input('Enter a start date (YYYY-MM-DD): ')
#     end_d = input("Enter an end date (YYYY-MM-DD): ")
#     budget, lastYear = newSheets.main()
#     print("ly:")
#     print(lastYear)
#     print("budget:")
#     print(budget)
#     budgetPlot = {}
#     for single_date in daterange(start_d, end_d):
#         lyDate = (single_date - timedelta(days=365))
#         mainList = monga.mongo_call(single_date.strftime("%Y-%m-%d"), single_date.strftime("%Y-%m-%d"))
#         budget[single_date.strftime("%d/%m/%Y")].append(str(mainList[2]))
#         budget[single_date.strftime("%d/%m/%Y")].append(str(lastYear[lyDate.strftime("%d/%m/%Y")][1]))
#         budgetPlot[single_date.strftime("%d/%m/%Y")] = budget[single_date.strftime("%d/%m/%Y")]
#         # print(budget[single_date.strftime("%d/%m/%Y")])
#     plotGraph.trace_graph(budgetPlot)
#
# def get_date_from_user():
#     s_date = input('Enter the start date: ', )
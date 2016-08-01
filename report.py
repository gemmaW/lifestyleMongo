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
from sys import version_info
# from builtins import input


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def ls_summary():
    startDate = datetime.strptime("2016,07,25", "%Y,%m,%d")
    endDate = datetime.strptime("2016,08,01", "%Y,%m,%d")
    #
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
        # print(budget[single_date.strftime("%d/%m/%Y")])
        # print(lyDate)
    plotGraph.trace_graph(budgetPlot)


def sales_by_show():
    mainList = monga.mongo_call("2016-07-25", "2016-07-31")
    monga.create_docs(mainList[0], mainList[1], mainList[2], mainList[3], mainList[4], mainList[5], mainList[6], mainList[7], mainList[8], mainList[9], mainList[10], mainList[11])

# ls_summary()
# sales_by_show()

def hourly_heatmap():
    mainList = monga.mongo_call("2016-07-25", "2016-07-31")
    plotGraph.hourly_heat(mainList[0][1:])




def choose_report():
    input = raw_input
    userChoice = int(eval(input('Choose a report: /n (1) summary (2) sales by show (3) spotcheck (4) hourly')))
    if userChoice == 1:
        ls_summary()
    if userChoice == 2:
        sales_by_show()
    if userChoice == 4:
        hourly_heatmap()
choose_report()


# def spot_check():

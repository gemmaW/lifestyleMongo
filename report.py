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
from builtins import input



def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def show_report():
    mainList = monga.mongo_call("2016-07-13", "2016-07-13")
    monga.create_docs(mainList[0], mainList[1], mainList[2], mainList[3], mainList[4], mainList[5], mainList[6], mainList[7], mainList[8], mainList[9], mainList[10], mainList[11])


def ls_summary():
    # # input function in 2 and 3 is different
    # if version_info < (3, 0):
    #     input = raw_input
    # blank input inserted to create pause effect for user input on report choice
    input(" ")
    try:
        year1 = str(input('Enter a year: (' + str(date.today().year) + '): '))
    except:
        year1 = str(date.today().year)
    if year1 == '':
        year1 = str(date.today().year)
    print(year1)
    month1 = input('Enter a month: ')
    day1 = input('Enter a day: ')
    startDate = datetime.strptime(str(year1 + "," + month1 + "," + day1), "%Y,%m,%d")
    try:
        year2 = str(input('Enter a year: (' + str(date.today().year) + '): '))
    except:
        year2 = str(date.today().year)
    if year2 == '':
        year2 = str(date.today().year)
    print(year2)
    month2 = str(input('Enter a month: '))
    day2 = str(input('Enter a day: '))
    endDate = datetime.strptime(year2 + "," + month2 + "," + day2, "%Y,%m,%d")
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
        lyDate = (single_date - timedelta(days=364))
        mainList = monga.mongo_call(single_date.strftime("%Y-%m-%d"), single_date.strftime("%Y-%m-%d"))
        budget[single_date.strftime("%d/%m/%Y")].append(str(mainList[2]))
        budget[single_date.strftime("%d/%m/%Y")].append(str(lastYear[lyDate.strftime("%d/%m/%Y")][1]))
        budgetPlot[single_date.strftime("%d/%m/%Y")] = budget[single_date.strftime("%d/%m/%Y")]
        print(budget[single_date.strftime("%d/%m/%Y")])
        print(lyDate)
    plotGraph.trace_graph(budgetPlot)


def sales_by_show():
    # blank input inserted to create pause effect for user input on report choice
    input(" ")
    try:
        year1 = str(input('Enter a year: (START) (' + str(date.today().year) + '): '))
    except:
        year1 = str(date.today().year)
    if year1 == '':
        year1 = str(date.today().year)
    print(year1)
    month1 = input('Enter a month: (START) ')
    day1 = input('Enter a day: (START) ')
    # startDate = datetime.strptime(str(year1 + "-" + month1 + "-" + day1), "%Y-%m-%d")
    try:
        year2 = str(input('Enter a year: (END) (' + str(date.today().year) + '): '))
    except:
        year2 = str(date.today().year)
    if year2 == '':
        year2 = str(date.today().year)
    print(year2)
    month2 = str(input('Enter a month: (END) '))
    day2 = str(input('Enter a day: (END) '))
    # endDate = datetime.strptime(year2 + "-" + month2 + "-" + day2, "%Y-%m-%d")
    mainList = monga.mongo_call(year1 + "-" + month1 + "-" + day1, year2 + "-" + month2 + "-" + day2)
    monga.create_docs(mainList[0], mainList[1], mainList[2], mainList[3], mainList[4], mainList[5], mainList[6], mainList[7], mainList[8], mainList[9], mainList[10], mainList[11])

# ls_summary()
# sales_by_show()


def chooseReport():
    userChoice = int(eval(input('Choose a report: (1) summary (2) sales by show ')))
    print("Press enter to begin. You will then be asked to select your date range, starting with the year")
    if userChoice == 1:
        ls_summary()
    if userChoice == 2:
        sales_by_show()

chooseReport()


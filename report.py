import monga
import pandas as pd
from pymongo import MongoClient
import dateutil.parser
import unicodecsv as csv
from operator import itemgetter
import sheets
import newSheets
from datetime import datetime, timedelta
import plotGraph
import datetime
import time

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def ls_summary():
    startDate = datetime.datetime.strptime("2016,08,01", "%Y,%m,%d")
    endDate = datetime.datetime.strptime("2016,09,01", "%Y,%m,%d")

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
        # print("---------------")
        # print(single_date.strftime("%d/%m/%Y"))
        # print(budget[single_date.sctrftime("%d/%m/%Y")])
        # print(lyDate)
    plotGraph.trace_graph(budgetPlot)


def sales_by_show():
    mainList = monga.mongo_call("2016-09-06", "2016-09-06")
    monga.create_docs(mainList[0], mainList[1], mainList[2], mainList[3], mainList[4], mainList[5], mainList[6],
                      mainList[7], mainList[8], mainList[9], mainList[10], mainList[11])


def hourly_heatmap():
    mainList = monga.mongo_call("2016-08-22", "2016-09-28")
    plotGraph.hourly_heat(mainList[0][1:])


def spa_heatmap():
    plotGraph.hourly_spa_heat()


def today_sales():
    to_day = (time.strftime("%Y-%m-%d"))
    print(to_day)
    # wow_to_day = (datetime.date.today()-datetime.timedelta(days=7))
    # print(wow_to_day)
    mainList = monga.mongo_call(to_day, to_day)
    # mainList2 = monga.mongo_call(wow_to_day, wow_to_day)
    print("Total GTV: " + (str(mainList[2])))
    print("Total Bookings:" + (str(mainList[3])))
    print("Total Tickets:" + (str(mainList[4])))
    print("Total Commission: " + (str(mainList[6])))
    # print("Total WoW GTV: " + (str(mainList2[2])))
    # print("Total WoW Bookings:" + (str(mainList2[3])))
    # print("Total WoW Tickets:" + (str(mainList2[4])))
    # print("Total WoW Commission: " + (str(mainList2[6])))


def quick_sales():
    mainList = monga.mongo_call("2016-09-05", "2016-09-05")
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
    mainList = monga.mongo_call("2016-08-31", "2016-09-30")
    showD = mainList[9]
    sotmShow = "Wicked"
    v = showD[sotmShow]
    gtv = [item[0] for item in v]
    tickets = [item[1] for item in v]
    print("SOTM: " + str(sotmShow))
    print("Total GTV:" + str(sum(gtv)))
    print("Total Tickets:" + str(sum(tickets)))


def fringe():
    mainList = monga.mongo_call("2016-08-05", "2016-09-11")
    showG = mainList[9]
    comedyShow = "The Fringe Comedy Awards Show"
    g = showG[comedyShow]
    gtv = [item[0] for item in g]
    tickets = [item[1] for item in g]
    print("Show Update: " + str(comedyShow))
    print("Total GTV:" + str(sum(gtv)))
    print("Total Tickets:" + str(sum(tickets)))


def railway_children():
    mainList = monga.mongo_call("2016-09-06", "2016-09-06")
    showD = mainList[9]
    saleShow = "The Railway Children"
    g = showD[saleShow]
    gtv = [item[0] for item in g]
    tickets = [item[1] for item in g]
    print("Show Update: " + str(saleShow))
    print("Total GTV:" + str(sum(gtv)))
    print("Total Tickets:" + str(sum(tickets)))


# def specific_show_sales():
#     mainList = monga.mongo_call("2016-08-31", "2016-09-01")
#     showD = mainList[9]
#     saleShow = "Wicked"
#     g = showD[saleShow]
#     gtv = [item[0] for item in g]
#     tickets = [item[1] for item in g]
#     monga.create_docs(mainList[0], mainList[1], mainList[2], mainList[3], mainList[4], mainList[5], mainList[6],
#                       mainList[7], mainList[8], showD, mainList[10], mainList[11])



# def days_out():
#     mainList = monga.mongo_call("2016-08-17", "2016-08-17")
#     daysOutId = mainList[0]
#     daysOutShow = "630"
#     g = daysOutId[daysOutShow]
#     gtv = [item[0] for item in g]
#     tickets = [item[1] for item in g]
#     monga.create_docs(mainList[0], mainList[1], mainList[2], mainList[3], mainList[4], mainList[5], mainList[6],
#                       mainList[7], mainList[8], mainList[9], mainList[10], mainList[11])


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
    print("MEGA FRIDAY: GTV for all shows from the fortnight: £" + str(sum(gtv1+gtv2+gtv3+gtv4+gtv5+gtv6+gtv7+gtv8+gtv9+
                                                                           gtv10)))
    print("MEGA FRIDAY: Tickets for all shows from the fortnight: " + str(sum(tickets1+tickets2+tickets3+tickets4+
                                                                              tickets5+tickets6+tickets7+tickets8+
                                                                              tickets9+tickets10)))
    print(saleShowOne + ": GTV= " + str(sum(gtv1)) + " Tickets= " + str(sum(tickets1)))
    print(saleShowTwo + ": GTV= " + str(sum(gtv2)) + " Tickets= " + str(sum(tickets2)))
    print(saleShowThree + ": GTV= " + str(sum(gtv3)) + " Tickets= " + str(sum(tickets3)))
    print(saleShowFour + ": GTV= " + str(sum(gtv4)) + " Tickets= " + str(sum(tickets4)))
    print(saleShowFive + ": GTV= " + str(sum(gtv5)) + " Tickets= " + str(sum(tickets5)))
    print(saleShowSix + ": GTV= " + str(sum(gtv6)) + " Tickets= " + str(sum(tickets6)))
    print(saleShowSeven + ": GTV= " + str(sum(gtv7)) + " Tickets= " + str(sum(tickets7)))
    print(saleShowEight + ": GTV= " + str(sum(gtv8)) + " Tickets= " + str(sum(tickets8)))
    print(saleShowNine + ": GTV= " + str(sum(gtv9)) + " Tickets= " + str(sum(tickets9)))
    print(saleShowTen + ": GTV= " + str(sum(gtv10)) + " Tickets= " + str(sum(tickets10)))




def bi_monthly_finance():
    mainList = monga.mongo_call("2016-08-15", "2016-08-16")
    monga.create_finance(mainList[0], mainList[1], mainList[2], mainList[3], mainList[4], mainList[5], mainList[6],
                      mainList[7], mainList[8], mainList[9], mainList[10], mainList[11])


def choose_report():
    # input = raw_input
    userChoice = int(input('Choose a report: /n (1) summary (2) sales by show (3) hourly (4) today (5) quick check '
                           '(6) show spot (7) SOTM (8) Bi-Monthly Finance (9) Fringe (10) Sunny Afternoon (11) '
                           'Mega Friday  (12) Specific Show Detail (13) spa heat'))

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
        mega_friday()
    # if userChoice == 12:
    #     specific_show_sales()
    if userChoice == 13:
        spa_heatmap()


choose_report()



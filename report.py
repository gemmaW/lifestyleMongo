import monga
import newSheets
from datetime import datetime, timedelta, time
import plotGraph
import datetime
import time
import csv
import pandas as pd

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def ticketing_summary():
    startDate = datetime.datetime.strptime("2016,09,27", "%Y,%m,%d")
    endDate = datetime.datetime.strptime("2016,09,28", "%Y,%m,%d")

    budget, lastYear = newSheets.main()
    budgetPlot = {}
    for single_date in daterange(startDate, endDate):
        lyDate = (single_date - timedelta(days=364))
        mainList = monga.mongo_call(single_date.strftime("%Y-%m-%d"), single_date.strftime("%Y-%m-%d"))
        budget[single_date.strftime("%d/%m/%Y")].append(str(mainList[2]))
        budget[single_date.strftime("%d/%m/%Y")].append(str(lastYear[lyDate.strftime("%d/%m/%Y")][1]))
        budgetPlot[single_date.strftime("%d/%m/%Y")] = budget[single_date.strftime("%d/%m/%Y")]
    plotGraph.trace_graph(budgetPlot)


def spa_summary():
    # with open('spa.csv', 'r') as spa_f:
    #     reader = csv.reader(spa_f)
    #     included_cols = [10]
    #     for row in reader:
    #         spa_tov = list(row[i] for i in included_cols)
    #         print(spa_tov)

    df = pd.read_csv('spa.csv')
    spa_tov = df['TOV']


    startDate = datetime.datetime.strptime("2016,08,29", "%Y,%m,%d")
    endDate = datetime.datetime.strptime("2016,09,04", "%Y,%m,%d")

    budget, lastYear = newSheets.spa_main()
    budgetPlot = {}
    for single_date in daterange(startDate, endDate):
        lyDate = (single_date - timedelta(days=364))
        mainList = sum(spa_tov)
        budget[single_date.strftime("%d/%m/%Y")].append(str(mainList[0]))
        budget[single_date.strftime("%d/%m/%Y")].append(str(lastYear[lyDate.strftime("%d/%m/%Y")][1]))
        budgetPlot[single_date.strftime("%d/%m/%Y")] = budget[single_date.strftime("%d/%m/%Y")]
    plotGraph.trace_graph_spa(budgetPlot)


def exp_summary():
    startDate = datetime.datetime.strptime("2016,08,29", "%Y,%m,%d")
    endDate = datetime.datetime.strptime("2016,09,04", "%Y,%m,%d")

    budget, lastYear = newSheets.exp_main()
    budgetPlot = {}
    for single_date in daterange(startDate, endDate):
        lyDate = (single_date - timedelta(days=364))
        mainList = monga.mongo_call(single_date.strftime("%Y-%m-%d"), single_date.strftime("%Y-%m-%d"))
        budget[single_date.strftime("%d/%m/%Y")].append(str(mainList[2]))
        budget[single_date.strftime("%d/%m/%Y")].append(str(lastYear[lyDate.strftime("%d/%m/%Y")][1]))
        budgetPlot[single_date.strftime("%d/%m/%Y")] = budget[single_date.strftime("%d/%m/%Y")]
    plotGraph.trace_graph_exp(budgetPlot)


def sales_by_show():
    mainList = monga.mongo_call("2016-09-26", "2016-09-28")
    monga.create_docs(mainList[0], mainList[1], mainList[2], mainList[3], mainList[4], mainList[5], mainList[6],
                      mainList[7], mainList[8], mainList[9], mainList[10], mainList[11])


def hourly_heatmap():
    mainList = monga.mongo_call("2016-09-19", "2016-09-25")
    plotGraph.hourly_heat(mainList[0][1:])


def spa_heatmap():
    plotGraph.hourly_spa_heat()


def exp_heatmap():
    plotGraph.hourly_exp_heat()


def today_sales():
    to_day = (time.strftime("%Y-%m-%d"))
    print(to_day)
    mainList = monga.mongo_call(to_day, to_day)
    print("Total GTV: " + (str(mainList[2])))
    print("Total Bookings:" + (str(mainList[3])))
    print("Total Tickets:" + (str(mainList[4])))
    print("Total Commission: " + (str(mainList[6])))


def quick_sales():
    mainList = monga.mongo_call("2016-09-27", "2016-09-27")
    print("Total GTV: " + (str(mainList[2])))
    print("Total Bookings:" + (str(mainList[3])))
    print("Total Tickets:" + (str(mainList[4])))
    print("Total Commission: " + (str(mainList[6])))


def show_sales():
    mainList = monga.mongo_call("2016-06-01", "2016-09-21")
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
    mainList = monga.mongo_call("2016-09-12", "2016-09-18")
    showG = mainList[9]
    comedyShow = "The Fringe Comedy Awards Show"
    g = showG[comedyShow]
    gtv = [item[0] for item in g]
    tickets = [item[1] for item in g]
    print("Show Update: " + str(comedyShow))
    print("Total GTV:" + str(sum(gtv)))
    print("Total Tickets:" + str(sum(tickets)))


def mamma_mia():
    mainList = monga.mongo_call("2016-09-19", "2016-09-20")
    showD = mainList[9]
    saleShow = "Mamma Mia!"
    g = showD[saleShow]
    gtv = [item[0] for item in g]
    tickets = [item[1] for item in g]
    print("Show Update: " + str(saleShow))
    print("Total GTV:" + str(sum(gtv)))
    print("Total Tickets:" + str(sum(tickets)))


def meal_deal_sale():
    mainList = monga.mongo_call("2016-09-14", "2016-09-18")
    showD = mainList[9]
    saleShowOne = "The Railway Children"
    g = showD[saleShowOne]
    gtv1 = [item[0] for item in g]
    tickets1 = [item[1] for item in g]
    saleShowTwo = "Sunny Afternoon"
    g = showD[saleShowTwo]
    gtv2 = [item[0] for item in g]
    tickets2 = [item[1] for item in g]
    saleShowThree = "In the Heights"
    g = showD[saleShowThree]
    gtv3 = [item[0] for item in g]
    tickets3 = [item[1] for item in g]
    saleShowFour = "The Dresser"
    g = showD[saleShowFour]
    gtv4 = [item[0] for item in g]
    tickets4 = [item[1] for item in g]
    saleShowFive = "The Last Tango"
    g = showD[saleShowFive]
    gtv5 = [item[0] for item in g]
    tickets5 = [item[1] for item in g]
    saleShowSix = "Beautiful"
    g = showD[saleShowSix]
    gtv6 = [item[0] for item in g]
    tickets6 = [item[1] for item in g]
    saleShowSeven = "The Libertine"
    g = showD[saleShowSeven]
    gtv7 = [item[0] for item in g]
    tickets7 = [item[1] for item in g]
    saleShowEight = "The Bodyguard"
    g = showD[saleShowEight]
    gtv8 = [item[0] for item in g]
    tickets8 = [item[1] for item in g]
    saleShowNine = "Thriller Live"
    g = showD[saleShowNine]
    gtv9 = [item[0] for item in g]
    tickets9 = [item[1] for item in g]
    print("Meal Deal Sale: GTV for all shows: £" + str(sum(gtv1+gtv2+gtv3+gtv4+gtv5+gtv6+gtv7+gtv8+
                                                                              gtv9)))
    print("Meal Deal Sale: Tickets for all shows: " + str(sum(tickets1+tickets2+tickets3+tickets4+
                                                                                 tickets5+tickets6+tickets7+tickets8+
                                                                                 tickets9)))

    print(saleShowEight + ": GTV= " + str(sum(gtv8)) + " Tickets= " + str(sum(tickets8)))
    print(saleShowTwo + ": GTV= " + str(sum(gtv2)) + " Tickets= " + str(sum(tickets2)))
    print(saleShowOne + ": GTV= " + str(sum(gtv1)) + " Tickets= " + str(sum(tickets1)))
    print(saleShowSix + ": GTV= " + str(sum(gtv6)) + " Tickets= " + str(sum(tickets6)))
    print(saleShowNine + ": GTV= " + str(sum(gtv9)) + " Tickets= " + str(sum(tickets9)))
    print(saleShowSeven + ": GTV= " + str(sum(gtv7)) + " Tickets= " + str(sum(tickets7)))
    print(saleShowFour + ": GTV= " + str(sum(gtv4)) + " Tickets= " + str(sum(tickets4)))
    print(saleShowThree + ": GTV= " + str(sum(gtv3)) + " Tickets= " + str(sum(tickets3)))
    print(saleShowFive + ": GTV= " + str(sum(gtv5)) + " Tickets= " + str(sum(tickets5)))


def get_emails():
    monga.email_addresses()


def check_time():
    print(time.strftime("%H:%M:%S"))


def bi_monthly_finance():
    mainList = monga.mongo_call("2016-08-15", "2016-08-16")
    monga.create_finance(mainList[0], mainList[1], mainList[2], mainList[3], mainList[4], mainList[5], mainList[6],
                      mainList[7], mainList[8], mainList[9], mainList[10], mainList[11])


def choose_report():
    # input = raw_input
    userChoice = int(input('Choose a report: /n (1) Ticketing Summary (2) Sales by Show (3) Ticketing Hourly (4) Today '
                           '(5) Quick Check (6) Show Spot (7) SOTM (8) Bi-Monthly Finance (9) Fringe (10) Mamma '
                           'Mia (11) Meal Deal Sale (12) Spa Hourly (13) Experiences Hourly (14) Get Emails (15) '
                           'Spa Summary (16) Experiences Summary (17) Check Time '))

    if userChoice == 1:
        ticketing_summary()
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
        mamma_mia()
    if userChoice == 11:
        meal_deal_sale()
    if userChoice == 12:
        spa_heatmap()
    if userChoice == 13:
        exp_heatmap()
    if userChoice == 14:
        get_emails()
    if userChoice == 15:
        spa_summary()
    if userChoice == 16:
        exp_summary()
    if userChoice == 17:
        check_time()


choose_report()


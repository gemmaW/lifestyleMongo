import monga
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

    budget, lastYear = newSheets.main()
    budgetPlot = {}
    for single_date in daterange(startDate, endDate):
        lyDate = (single_date - timedelta(days=364))
        mainList = monga.mongo_call(single_date.strftime("%Y-%m-%d"), single_date.strftime("%Y-%m-%d"))
        budget[single_date.strftime("%d/%m/%Y")].append(str(mainList[2]))
        budget[single_date.strftime("%d/%m/%Y")].append(str(lastYear[lyDate.strftime("%d/%m/%Y")][1]))
        budgetPlot[single_date.strftime("%d/%m/%Y")] = budget[single_date.strftime("%d/%m/%Y")]
    plotGraph.trace_graph(budgetPlot)


def sales_by_show():
    mainList = monga.mongo_call("2016-09-07", "2016-09-07")
    monga.create_docs(mainList[0], mainList[1], mainList[2], mainList[3], mainList[4], mainList[5], mainList[6],
                      mainList[7], mainList[8], mainList[9], mainList[10], mainList[11])


def hourly_heatmap():
    mainList = monga.mongo_call("2016-08-30", "2016-09-06")
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
    mainList = monga.mongo_call("2016-09-05", "2016-09-06")
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
    mainList = monga.mongo_call("2016-09-05", "2016-09-11")
    showG = mainList[9]
    comedyShow = "The Fringe Comedy Awards Show"
    g = showG[comedyShow]
    gtv = [item[0] for item in g]
    tickets = [item[1] for item in g]
    print("Show Update: " + str(comedyShow))
    print("Total GTV:" + str(sum(gtv)))
    print("Total Tickets:" + str(sum(tickets)))


def railway_children():
    mainList = monga.mongo_call("2016-09-05", "2016-09-07")
    showD = mainList[9]
    saleShow = "The Railway Children"
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
    saleShowTwo = "Charlie Chocolate Factory"
    g = showD[saleShowTwo]
    gtv2 = [item[0] for item in g]
    tickets2 = [item[1] for item in g]
    saleShowThree = "Sunny Afternoon"
    g = showD[saleShowThree]
    gtv3 = [item[0] for item in g]
    tickets3 = [item[1] for item in g]
    saleShowFour = "In The Heights"
    g = showD[saleShowFour]
    gtv4 = [item[0] for item in g]
    tickets4 = [item[1] for item in g]
    saleShowFive = "The Dresser"
    g = showD[saleShowFive]
    gtv5 = [item[0] for item in g]
    tickets5 = [item[1] for item in g]
    saleShowSix = "Mamma Mia"
    g = showD[saleShowSix]
    gtv6 = [item[0] for item in g]
    tickets6 = [item[1] for item in g]
    saleShowSeven = "Cirque Eloize iD"
    g = showD[saleShowSeven]
    gtv7 = [item[0] for item in g]
    tickets7 = [item[1] for item in g]
    print("Meal Deal Sale: GTV for all shows from the fortnight: £" + str(sum(gtv1+gtv2+gtv3+gtv4+gtv5+gtv6+gtv7)))
    print("Meal Deal Sale: Tickets for all shows from the fortnight: " + str(sum(tickets1+tickets2+tickets3+tickets4
                                                                                 +tickets5+tickets6+tickets7)))
    print(saleShowOne + ": GTV= " + str(sum(gtv1)) + " Tickets= " + str(sum(tickets1)))
    print(saleShowTwo + ": GTV= " + str(sum(gtv2)) + " Tickets= " + str(sum(tickets2)))
    print(saleShowThree + ": GTV= " + str(sum(gtv3)) + " Tickets= " + str(sum(tickets3)))
    print(saleShowFour + ": GTV= " + str(sum(gtv4)) + " Tickets= " + str(sum(tickets4)))
    print(saleShowFive + ": GTV= " + str(sum(gtv5)) + " Tickets= " + str(sum(tickets5)))
    print(saleShowSix + ": GTV= " + str(sum(gtv6)) + " Tickets= " + str(sum(tickets6)))
    print(saleShowSeven + ": GTV= " + str(sum(gtv7)) + " Tickets= " + str(sum(tickets7)))


def get_emails():
    monga.email_addresses()


def bi_monthly_finance():
    mainList = monga.mongo_call("2016-08-15", "2016-08-16")
    monga.create_finance(mainList[0], mainList[1], mainList[2], mainList[3], mainList[4], mainList[5], mainList[6],
                      mainList[7], mainList[8], mainList[9], mainList[10], mainList[11])


def choose_report():
    # input = raw_input
    userChoice = int(input('Choose a report: /n (1) summary (2) sales by show (3) hourly (4) today (5) quick check '
                           '(6) show spot (7) SOTM (8) Bi-Monthly Finance (9) Fringe (10) The Railway Children (11) '
                           'Mega Friday  (12) Spa hourly (13) Experiences hourly (14) Get Emails '))

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
        railway_children()
    if userChoice == 11:
        meal_deal_sale()
    if userChoice == 12:
        spa_heatmap()
    if userChoice == 13:
        exp_heatmap()
    if userChoice == 14:
        get_emails()


choose_report()


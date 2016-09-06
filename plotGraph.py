import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from datetime import datetime, timedelta, date
import collections
import csv

plotly.tools.set_credentials_file(username='gluzio', api_key='quey0vtequ')


def trace_graph(value):

    # print(value)

    xValues = []
    trace1Values = []
    trace2Values = []
    trace3Values = []

    for k in value:
        # print(str(k))
        s = datetime.strptime(str(k), "%d/%m/%Y")
        xValues.append(s.strftime("%Y-%m-%d"))
        trace1Values.append(value[k][3])
        trace2Values.append(value[k][1])
        trace3Values.append(value[k][2])


    trace1 = go.Bar(
        x=xValues,
        y=trace2Values,
        name='Theatre Budget',
        marker=dict(
            color='rgba(249,102,214, 1.0)',
        )
    )
    trace2 = go.Bar(
        x=xValues,
        y=trace1Values,
        name='Last Year',
        marker=dict(
            color='rgba(165,142,252, 0.8)',
        )
    )
    trace3 = go.Bar(
        x=xValues,
        y=trace3Values,
        name='Theatre Actual',
        marker=dict(
            color='rgba(31,183,233, 0.6)',
        )
    )
    data = [trace1, trace2, trace3]
    layout = go.Layout(
        barmode='overlay'
    )

    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='Theatre Budget')


def hourly_heat(values):
    # print(values)

    # transactions hourly heatmap
    dayDict = {}
    hourDict = {}
    daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for row in values:
        # print(row)
        day = datetime.strptime(row[1][:10], '%Y-%m-%d').strftime('%A')
        dayDict.setdefault(day, []).append(row[1][11:13])
    print(dayDict)
    #for d in daysOfWeek:

    monday = collections.Counter(dayDict['Monday'])
    tuesday = collections.Counter(dayDict['Tuesday'])
    wednesday = collections.Counter(dayDict['Wednesday'])
    thursday = collections.Counter(dayDict['Thursday'])
    friday = collections.Counter(dayDict['Friday'])
    saturday = collections.Counter(dayDict['Saturday'])
    sunday = collections.Counter(dayDict['Sunday'])
    #print wednesday
    #print dayDict
    yList = []
    dualList = []
    default_value = 0
    for i in range(24):
        # print("%02d" % (i,))
        hourList = []
        hourList.append(monday.get("%02d" % (i,), "0"))
        hourList.append(tuesday.get("%02d" % (i,), "0"))
        hourList.append(wednesday.get("%02d" % (i,), "0"))
        hourList.append(thursday.get("%02d" % (i,), "0"))
        hourList.append(friday.get("%02d" % (i,), "0"))
        hourList.append(saturday.get("%02d" % (i,), "0"))
        hourList.append(sunday.get("%02d" % (i,), "0"))
        dualList.append(hourList)
        yList.append("%02d" % (i,))
    # print(dualList)
    # print(yList)

    data = [
        go.Heatmap(
            z=dualList,
            x=daysOfWeek,
            y=yList,
            colorscale = [
                [
                    0,
                    "rgb(0, 0, 155)"
                ],
                [
                    0.35,
                    "rgb(0, 108, 255)"
                ],
                [
                    0.5,
                    "rgb(98, 255, 146)"
                ],
                [
                    0.6,
                    "rgb(255, 147, 0)"
                ],
                [
                    0.7,
                    "rgb(255, 47, 0)"
                ],
                [
                    1,
                    "rgb(216, 0, 0)"
                ]
            ],
        )
    ]

    layout = go.Layout(
        title='Ticket Transactions Per Hour',
        xaxis = dict(title='Day of Week'),
        yaxis = dict(title='Hour of Day')
    )


    fig = go.Figure(data=data, layout=layout)

    py.plot(fig, filename='ticketing-heatmap')


def hourly_spa_heat():
    with open('spa.csv', 'r') as f:
        reader = csv.reader(f)
        values = list(reader)

    # print(values)

    # transactions hourly heatmap
    dayDict = {}
    hourDict = {}
    daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for row in values[1:]:
        # print(row)
        day = datetime.strptime(row[1][:10], '%Y-%m-%d').strftime('%A')
        dayDict.setdefault(day, []).append(row[1][11:13])
    print(dayDict)
    #for d in daysOfWeek:

    monday = collections.Counter(dayDict['Monday'])
    tuesday = collections.Counter(dayDict['Tuesday'])
    wednesday = collections.Counter(dayDict['Wednesday'])
    thursday = collections.Counter(dayDict['Thursday'])
    friday = collections.Counter(dayDict['Friday'])
    saturday = collections.Counter(dayDict['Saturday'])
    sunday = collections.Counter(dayDict['Sunday'])
    #print wednesday
    #print dayDict
    yList = []
    dualList = []
    default_value = 0
    for i in range(24):
        # print("%02d" % (i,))
        hourList = []
        hourList.append(monday.get("%02d" % (i,), "0"))
        hourList.append(tuesday.get("%02d" % (i,), "0"))
        hourList.append(wednesday.get("%02d" % (i,), "0"))
        hourList.append(thursday.get("%02d" % (i,), "0"))
        hourList.append(friday.get("%02d" % (i,), "0"))
        hourList.append(saturday.get("%02d" % (i,), "0"))
        hourList.append(sunday.get("%02d" % (i,), "0"))
        dualList.append(hourList)
        yList.append("%02d" % (i,))
    # print(dualList)
    # print(yList)

    data = [
        go.Heatmap(
            z=dualList,
            x=daysOfWeek,
            y=yList,
            colorscale = [
                [
                    0,
                    "rgb(0, 0, 155)"
                ],
                [
                    0.35,
                    "rgb(0, 108, 255)"
                ],
                [
                    0.5,
                    "rgb(98, 255, 146)"
                ],
                [
                    0.6,
                    "rgb(255, 147, 0)"
                ],
                [
                    0.7,
                    "rgb(255, 47, 0)"
                ],
                [
                    1,
                    "rgb(216, 0, 0)"
                ]
            ],
        )
    ]

    layout = go.Layout(
        title='Spa Transactions Per Hour',
        xaxis = dict(title='Day of Week'),
        yaxis = dict(title='Hour of Day')
    )


    fig = go.Figure(data=data, layout=layout)

    py.plot(fig, filename='spa-heatmap')
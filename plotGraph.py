import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import datetime

plotly.tools.set_credentials_file(username='gluzio', api_key='quey0vtequ')


def trace_graph(value):

    print(value)

    xValues = []
    trace1Values = []
    trace2Values = []
    trace3Values = []

    for k in value:
        # print(str(k))
        s = datetime.datetime.strptime(str(k), "%d/%m/%Y")
        xValues.append(s.strftime("%Y-%m-%d"))
        trace1Values.append(value[k][3])
        trace2Values.append(value[k][1])
        trace3Values.append(value[k][2])


    trace1 = go.Bar(
        x=xValues,
        y=trace1Values,
        name='Last Year'
    )
    trace2 = go.Bar(
        x=xValues,
        y=trace2Values,
        name='Theatre Budget'
    )
    trace3 = go.Bar(
        x=xValues,
        y=trace3Values,
        name='Theatre Actual'
    )
    data = [trace1, trace2, trace3]
    layout = go.Layout(
        barmode='bar'
    )

    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='Theatre Budget')
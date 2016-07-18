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
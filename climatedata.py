import csv
import plotly
plotly.tools.set_credentials_file(username='cubicr00t', api_key='ybPqSeQJYPushK03K9qs')
import plotly.plotly as py
import plotly.graph_objs as go
from numpy import arange,array,ones
from scipy import stats
import datetime
import time

def badToGood(dateStr):
    try:
        return datetime.datetime.strptime(dateStr, '%Y-%m-%d')
    except ValueError:
        try:
            return datetime.datetime.strptime(dateStr, '%m/%d/%y')
        except ValueError:
            print 'hehe xd'
    return 'hehe xd'


globaltemp = open('GlobalTemperatures.csv', 'r')
globaltempcsv = csv.reader(globaltemp)
globaltempcsv.next()

dates = []
avgtemp = []
for row in globaltempcsv:
    if row[1] != '':
        dates.append(row[0])
        avgtemp.append(float(row[1]))
#print dates
#print avgtemp
trace0 = go.Scatter(
    x = dates,
    y = avgtemp,
    mode = 'markers',
    name = 'Temperatures'
)
#data = [trace0]
#py.plot(data, filename = 'temp-scatter', auto_open=True)
# countrytemp = open('GlobalLandTemperaturesByCountry.csv', 'r')
# countrytempcsv = csv.reader(countrytemp)
#
# germanydate = []
# germanytemp = []
# for row in countrytempcsv:
#     if row[3] == 'Germany':
#         if row[1] != '':
#             germanydate.append(row[0])
#             germanytemp.append(float(row[1]))
#     else:
#         pass
#print germanytemp
#print germanydate
#dt = datetime.datetime.strptime("2018-08-07", '%Y-%m-%d')
#dt2 = datetime.datetime.strptime("8/7/18", '%m/%d/%y')
mindate = datetime.datetime.strptime("1750-01-01", '%Y-%m-%d').date()
# unixtime = time.mktime(dt.timetuple())
xi = []
for i in dates:
    dt = badToGood(i).date()
    delta = (dt - mindate).days
    xi.append(delta)
A = array([xi, ones(max(xi))])
slope, intercept, r_value, std_err, p_value = stats.linregress(xi,avgtemp)
line = [float(slope) * x + intercept for x in xi]

# trace1 = go.Scatter(
#     x = germanydate,
#     y = germanytemp,
#     mode = 'markers',
#     name = 'Temperature trendline'
# )
trace2 = go.Scatter(
    x = dates,
    y = line,
    mode = 'lines',
    name = 'Temperature trendline'
)

dataglobal = [trace0, trace2]

layoutglobal = go.Layout(
    title = 'Global Temperature vs Time',
    xaxis = dict(
        title = 'Date (years)',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis = dict(
        title = 'Temperature (degrees celsius)',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
figglobal = go.Figure(data = dataglobal, layout = layoutglobal)
py.plot(figglobal, filename = 'globaltemp-scatter', auto_open=True)

co2data = open('co2-mm-mlo.csv','r')
co2csv = csv.reader(co2data)
co2csv.next()

co2dates = []
co2molfrac = []
for row in co2csv:
    co2dates.append(row[0])
    co2molfrac.append(float(row[3]))

mindateco2 = datetime.datetime.strptime("1958-03-01", '%Y-%m-%d').date()

xii = []
for i in co2dates:
    dtco2 = badToGood(i).date()
    deltaco2 = (dtco2 - mindateco2).days
    xii.append(deltaco2)
A = array([xii, ones(max(xii))])
slope, intercept, r_value, std_err, p_value = stats.linregress(xii,co2molfrac)
lineco2 = [float(slope) * x + intercept for x in xii]

trace3 = go.Scatter(
    x = co2dates,
    y = co2molfrac,
    mode = 'markers',
    name = 'CO2 mole fraction',
)
trace4 = go.Scatter(
    x = co2dates,
    y = lineco2,
    mode = 'lines',
    name = 'CO2 trendline'
)

dataco2 = [trace3,trace4]

layoutco2 = go.Layout(
    title = 'CO2 vs Time',
    xaxis = dict(
        title = 'Date (years)',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis = dict(
        title = 'CO2 (mole fraction in ppm)',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
figco2 = go.Figure(data = dataco2, layout = layoutco2)

py.plot(figco2, filename = 'co2molfrac-scatter', auto_open=True)

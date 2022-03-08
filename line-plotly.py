import plotly.graph_objects as go
import csv

violations=[]
with open("resultados-4.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lines in csv_reader:
        violations.append(lines[4])
        
t=list(range(0, 501))
fig = go.Figure(data=go.Scatter(x=t, y=violations))

fig.update_layout(xaxis_title='Generations', yaxis_title='Number of violations')

fig.show()
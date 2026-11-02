from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv') # Lee el archivo csv con los datos de población por país y año

app = Dash() #crea la aplicación Dash

# Requires Dash 2.17.0 or later
app.layout = [
    html.H1(children='Title of Dash App', style={'textAlign':'center'}), #Crea la pagina con html y el titulo
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'), #Crea el menú desplegable con las opciones de país
    dcc.Graph(id='graph-content') #Crea el gráfico, pero toda la información del gráfico se genera en la función update_graph
]

@callback( #Se maneja la interacción del menú desplegable con el gráfico
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value] #Filtra los datos para el país seleccionado
    return px.line(dff, x='year', y='pop') #luego genera el gráfico de línea con los datos filtrados

if __name__ == '__main__':
    app.run(debug=True) #Para que corra python DASH.py y se pueda ver en el navegador
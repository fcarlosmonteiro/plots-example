from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool, LegendItem, Legend
from bokeh.layouts import layout

def create_column_data_source(categorias, risco_baixo_valores, risco_medio_valores, risco_alto_valores, indicador_escore_valores):
    return ColumnDataSource(data=dict(
        categorias=categorias,
        risco_baixo=risco_baixo_valores,
        risco_medio=risco_medio_valores,
        risco_alto=risco_alto_valores,
        indicador_escore=indicador_escore_valores
    ))

def create_figure(categorias, source, cores, width=800, height=600):
    p = figure(x_range=categorias, width=width, height=height, title="Escores por dimensão",
               toolbar_location=None, tools="")
    p.x_range.range_padding = 0.1

    bars = p.vbar_stack(stackers=['risco_baixo', 'risco_medio', 'risco_alto'], x='categorias', width=0.4,
                        color=cores[:3], source=source)
    escore = p.vbar(x='categorias', top='indicador_escore', width=0.2, color='black', source=source)
    p.add_tools(HoverTool(tooltips=[("Indicador de Escore", "@indicador_escore")], renderers=[escore]))

    p.xgrid.grid_line_color = None
    p.axis.minor_tick_line_color = None
    p.outline_line_color = None
    p.y_range.start = 0

    return p, bars, escore

def create_legend(p, bars, escore):
    legend_items = [
        LegendItem(label='Risco Baixo', renderers=[bars[0]]),
        LegendItem(label='Risco Médio', renderers=[bars[1]]),
        LegendItem(label='Risco Alto', renderers=[bars[2]]),
        LegendItem(label='Indicador de Escore', renderers=[escore])
    ]
    
    legend = Legend(items=legend_items, orientation="horizontal", location="bottom_left")
    p.add_layout(legend, 'below')
    p.legend.label_text_font_size = '8pt'
    p.legend.spacing = 0
    p.legend.padding = 0
    p.legend.margin = 0

def plot_risk_scores(categorias, risco_baixo_valores, risco_medio_valores, risco_alto_valores, indicador_escore_valores, cores):
    source = create_column_data_source(categorias, risco_baixo_valores, risco_medio_valores, risco_alto_valores, indicador_escore_valores)
    p, bars, escore = create_figure(categorias, source, cores)
    create_legend(p, bars, escore)

    output_file("escores_por_dimensao.html")
    show(layout([p], sizing_mode='fixed'))

# Definindo os valores para passar como parâmetros
categorias = ['Comunidade', 'Escola', 'Estudante', 'Familia', 'Profissionais']
risco_baixo_valores = [1.56, 1.42, 2.21, 2.32, 3.64]
risco_medio_valores = [2.44, 1.68, 1.79, 1.68, 1.58]
risco_alto_valores = [3.5, 2.1, 2.5, 2.9, 4.0]
indicador_escore_valores = [3.4, 1.42, 2.21, 3.32, 3.64]
cores = ['#B2EDB0', '#FFF9B6', '#F0A2A2']

# Chamada da função principal com os valores definidos
plot_risk_scores(categorias, risco_baixo_valores, risco_medio_valores, risco_alto_valores, indicador_escore_valores, cores)

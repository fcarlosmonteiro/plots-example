import geopandas as gpd
from bokeh.plotting import figure, show, output_file
from bokeh.models import GeoJSONDataSource, HoverTool, TapTool, CustomJS, Div
from bokeh.layouts import column

url = "https://raw.githubusercontent.com/jonates/opendata/master/arquivos_geoespaciais/unidades_da_federacao.json"

gdf = gpd.read_file(url)

populacao = {
    'ACRE': '900 mil',
    'ALAGOAS': '3 milhões',
    'AMAPÁ': '850 mil',
    'AMAZONAS': '4 milhões',
    'BAHIA': '15 milhões',
    'CEARÁ': '9 milhões',
    'DISTRITO FEDERAL': '3 milhões',
    'ESPÍRITO SANTO': '4 milhões',
    'GOIÁS': '7 milhões',
    'MARANHÃO': '7 milhões',
    'MATO GROSSO': '3 milhões',
    'MATO GROSSO DO SUL': '2 milhões',
    'MINAS GERAIS': '21 milhões',
    'PARÁ': '8 milhões',
    'PARAÍBA': '4 milhões',
    'PARANÁ': '11 milhões',
    'PERNAMBUCO': '9 milhões',
    'PIAUÍ': '3 milhões',
    'RIO DE JANEIRO': '17 milhões',
    'RIO GRANDE DO NORTE': '3 milhões',
    'RIO GRANDE DO SUL': '11 milhões',
    'RONDÔNIA': '1.8 milhões',
    'RORAIMA': '600 mil',
    'SANTA CATARINA': '7 milhões',
    'SÃO PAULO': '46 milhões',
    'SERGIPE': '2 milhões',
    'TOCANTINS': '1.6 milhões'
}

gdf['Populacao'] = gdf['NM_ESTADO'].map(populacao)

output_file("mapa_do_Brasil_interativo.html")

geosource = GeoJSONDataSource(geojson=gdf.to_json())

p = figure(title="Mapa do Brasil", width=800, height=600, background_fill_color="white", tools="")

p.toolbar.logo = None
p.toolbar_location = None

states = p.patches("xs", "ys", source=geosource, line_color="black", line_width=0.5, fill_alpha=1)

hover = HoverTool()
hover.tooltips = [("Estado", "@NM_ESTADO"), ("População", "@Populacao")]
p.add_tools(hover)

info_div = Div(text="", width=400)

tap = TapTool()
p.add_tools(tap)

callback = CustomJS(args=dict(p=p, info_div=info_div), code="""
    var selected_state = cb_data.source.selected.indices[0];
    if (selected_state !== undefined) {
        var state_name = p.source.data['NM_ESTADO'][selected_state];
        var population = p.source.data['Populacao'][selected_state];
        info_div.text = "<div style='color: black;'>Estado: " + state_name + "<br>População: " + population + "</div>";
    } else {
        info_div.text = "";
    }
""")

tap.callback = callback

p.axis.visible = False

layout = column(p, info_div)

show(layout)

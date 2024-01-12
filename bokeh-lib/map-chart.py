import geopandas as gpd
from bokeh.plotting import figure, show, output_file
from bokeh.models import GeoJSONDataSource, HoverTool, TapTool, CustomJS, Div
from bokeh.layouts import column

# URL do GeoJSON
url = "https://raw.githubusercontent.com/jonates/opendata/master/arquivos_geoespaciais/unidades_da_federacao.json"

# Carregar o GeoJSON diretamente do URL
gdf = gpd.read_file(url)

# Adicionar informações de população fictícias com base no censo populacional aproximado
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

# Mapear os valores de população fictícia para o DataFrame GeoPandas
gdf['Populacao'] = gdf['NM_ESTADO'].map(populacao)

# Inicializar a saída do Bokeh para um arquivo HTML
output_file("mapa_do_Brasil_interativo.html")

# Criar uma fonte de dados GeoJSON para Bokeh
geosource = GeoJSONDataSource(geojson=gdf.to_json())

# Criar a figura Bokeh sem ferramentas
p = figure(title="Mapa do Brasil", width=800, height=600, background_fill_color="white", tools="")

# Remover logo e barra de ferramentas
p.toolbar.logo = None
p.toolbar_location = None

# Adicionar os estados ao gráfico
states = p.patches("xs", "ys", source=geosource, line_color="black", line_width=0.5, fill_alpha=1)

# Adicionar a ferramenta Hover para mostrar informações sobre os estados
hover = HoverTool()
hover.tooltips = [("Estado", "@NM_ESTADO"), ("População", "@Populacao")]
p.add_tools(hover)

# Criar uma Div para mostrar informações ao clicar em um estado
info_div = Div(text="", width=400)

# Adicionar a ferramenta Tap para dar zoom e mostrar informações adicionais ao clicar em um estado
tap = TapTool()
p.add_tools(tap)

# Criar um JavaScript callback para tratar o evento de clique em um estado
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

# Personalizar a aparência do mapa (opcional)
p.axis.visible = False

# Criar um layout com o mapa e a Div de informações
layout = column(p, info_div)

# Mostrar o layout
show(layout)

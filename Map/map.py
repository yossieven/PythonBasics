import folium
import pandas

data = pandas.read_csv("volcanos.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

html = """
<p style="color:red"><b>Volcano name:</b></p>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
<p style="color:red; line-height: normal"><b>Height: </b></p>%s m

"""


def color_producer(el):
    if el <= 1000:
        return 'green'
    elif 1000 < el < 2000:
        return 'orange'
    else:
        return 'red'


my_map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="Volcano")
fg2 = folium.FeatureGroup(name="Population")
for lt, ln, nm, el in zip(lat, lon, name, elev):
    elevStr = str(el) + " m"
    iframe = folium.IFrame(html=html % (nm, nm, el), width=200, height=150)
    fg.add_child(
        folium.Marker(location=[lt, ln], popup=folium.Popup(iframe),
                      icon=folium.Icon(icon="fire", color=color_producer(el))))

fg2.add_child(folium.GeoJson(data=open("world.json", mode="r", encoding="utf-8-sig").read(),
                             style_function=lambda x: {"fillColor": "green" if x['properties']['POP2005'] < 10000000
                             else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000
                             else "red"}))
my_map.add_child(fg)
my_map.add_child(fg2)
my_map.add_child(folium.LayerControl())
my_map.save("map.html")

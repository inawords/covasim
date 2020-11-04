import requests
import pandas as pd

"""
get current data from Vorarlberg Covid Dashboard and save it as csv
"""
response = requests.get(url="https://services7.arcgis.com/4ipPlG34BuOOqa4W/arcgis/rest/services/COVID19_V_VBG/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=datum%20asc&outSR=102100&resultOffset=0&resultRecordCount=32000&resultType=standard&cacheHint=true")
json = response.json()
data = json['features']
data = pd.json_normalize(data)
df = pd.DataFrame(data)
df.to_csv('./dashboard.csv')
print('finished')


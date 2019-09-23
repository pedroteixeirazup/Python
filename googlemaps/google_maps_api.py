import googlemaps
from pandas import DataFrame, read_csv, ExcelFile, ExcelWriter
import matplotlib as plt
import pandas as pd 


# Requires API key 
gmaps = googlemaps.Client(key='AIzaSyDTgBrXscEaRfAJh3tBPF2uaP_besCWG8Q') 
  
# Solve problems 1 and 2 
def time_distance(origin, destiny):
    my_dist = gmaps.distance_matrix(origin,destiny)['rows'][0]['elements'][0] 

    return  my_dist['duration']['text']



# Solve porblem 3
def check_radius(position1, position2, radius):
    data = gmaps.distance_matrix(position1,position2)['rows'][0]['elements'][0]
    distance_between = data['distance']['text'].split()

    if float(distance_between[0]) > float(radius):
        return False
    
    return True



#Solve problem 4
def coord_highway(km_init, km_finish, highway):
    x = 0
    list_lat_long = []

    for i in range(km_init, km_finish + 1):
        address = 'km ' + str(i) + ' ' + highway
        data = gmaps.geocode(address)
        list_lat_long.append(data[0]['geometry']['location'])

    return list_lat_long 



#Reading Xls File
def reader():
    file = r'data/read.xls'
    df = pd.read_excel(file)

    road, kmIni, kmFinal = df['Rodovia'], df['Km Inicial'], df['Km Final']

    return road,kmIni,kmFinal

#Get coord from the init of the road
def coordInit(km_init,highway):
    addressInit = 'km ' + str(km_init) + ' ' + highway
    dataInit = gmaps.geocode(addressInit)
    
    if len(dataInit) == 0:
        return 'Empty', 'Empty'

    lat = dataInit[0]['geometry']['location']['lat']
    lng = dataInit[0]['geometry']['location']['lng']

    return lat, lng

#Get coord of the final of the road
def coordFin(km_finish,highway):
    address = 'km ' + str(km_finish) + ' ' + highway
    dataFinish = gmaps.geocode(address)
     
    if len(dataFinish) == 0:
        return 'Empty','Empty'
  
    lat = dataFinish[0]['geometry']['location']['lat']
    lng = dataFinish[0]['geometry']['location']['lng']

    return lat, lng

#Write lat and lng on a xls file
def writeXls():
    highway, km_ini, km_fin = reader()
    latIniArray = list()
    lngIniArray = list()
    latFinArray = list()
    lngFinArray = list()
    for x in range(len(highway)):
        print(highway[x],km_ini[x], km_fin[x])
        latIni, lngIni = coordInit(km_ini[x],highway[x])
        latFin, lngFin = coordFin(km_fin[x],highway[x])
        latIniArray.append(latIni)
        lngIniArray.append(lngIni)
        latFinArray.append(latFin)
        lngFinArray.append(lngFin)

    # print(latIniArray, lngFinArray)
    
    df = DataFrame({
        'Latitude Inicio': latIniArray,
        'Longitude Inicio': lngIniArray,
        'Latitude Fim': latFinArray,
        'Longitude Fim': lngFinArray
    })

    writer = ExcelWriter('lat_lng.xls')
    df.to_excel(writer,'Sheet1', index=False)
    writer.save()
        

writeXls()
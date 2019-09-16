import googlemaps 

# Requires API key 
gmaps = googlemaps.Client(key='YOUR-KEY') 
  
# Solve problems 1 and 2 
def time_distance(origin, destiny):
    my_dist = gmaps.distance_matrix(origin,destiny)['rows'][0]['elements'][0] 
    return  my_dist['duration']['text']




# Solve problem 3
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


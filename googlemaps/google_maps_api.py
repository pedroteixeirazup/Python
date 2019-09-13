import googlemaps 

'''Distance Matrix API'''  
# Requires API key 
gmaps = googlemaps.Client(key='YOUR-KEY') 
  
# Solve problems 1 and 2 
def time_distance(origin, destiny):
    my_dist = gmaps.distance_matrix(origin,destiny)['rows'][0]['elements'][0] 
    print(my_dist['duration']) 
    # return  my_dist['duration']['text']

# Inputs got distance matrix api
# print('Enter with lat and long of your origin: ') 
# origin = input()

# print('Enter with lat and long of your destination: ')
# destiny = input()

# time_distance('Araguari','Paracatu')


# Solve porblem 3
def check_radius(position1, position2, radius):
    data = gmaps.distance_matrix(position1,position2)['rows'][0]['elements'][0]
    distance_between = data['distance']['text'].split()

    if float(distance_between[0]) > float(radius):
        return False
    
    return True

# print(check_radius('40.654564, -73.6565','40.564564, -73.6565',30))
# print(check_radius('Sao Paulo','Uberlandia',30))



#Solve problem 4
def coord_highway(km_init, km_finish, highway):
    x = 0
    list_lat_long = []

    for i in range(km_init, km_finish + 1):
        address = 'km ' + str(i) + ' ' + highway
        data = gmaps.geocode(address)
        list_lat_long.append(data[0]['geometry']['location'])

    return list_lat_long 

lista = coord_highway(217, 236, 'SP-052')
print(lista)
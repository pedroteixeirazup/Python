# importing googlemaps module 
import googlemaps 
  
# Requires API key 
gmaps = googlemaps.Client(key='AIzaSyBQ5dcUgP4E9ZS_Dy59XcmpRd3M91DOh6U') 
  
# # Requires cities name 
# my_dist = gmaps.distance_matrix('40.65454,-73.5454','40.654465,-80.54564')['rows'][0]['elements'][0] 

def getlatlong(origin, destiny):
    my_dist = gmaps.distance_matrix(origin,destiny)['rows'][0]['elements'][0] 
    print(my_dist) 

# # Printing the result 
# print(my_dist)
print('Enter with lat and long of your origin: ') 
origin = raw_input()

print('Enter with lat and long of your destination: ')
destiny = raw_input()

getlatlong(origin,destiny)


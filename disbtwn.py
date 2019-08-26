import math
import sys


EARTH_RADIUS = 6371
print(sys.argv)

def deg_to_rad(inDeg):
    return inDeg * math.pi / 180

def find_distance(origin, dest):
    # find differance
    dif = {}
    for key in dest:
        if key in dest:
            dif[key] = dest[key] - origin[key]

    # convert difference to radians
    for key in dif:
        dif[key] = deg_to_rad(dif[key])

    a = math.sin(dif['lat'] / 2) \
        * math.sin(dif['lat'] / 2) \
        + math.cos(deg_to_rad(origin['lat'])) \
        * math.cos(deg_to_rad(dest['lat'])) \
        * (math.sin(dif['long'] / 2) \
        * math.sin(dif['long'] / 2))

    c = math.atan2(math.sqrt(a), math.sqrt(1-a)) * 2

    return EARTH_RADIUS * c

def find_distance_opt(origin, dest):
    p = 0.017453292519943295 # pi / 180
    a = 0.5 - math.cos((dest['lat'] - origin['lat']) * p)/2 \
        + math.cos(origin['lat'] * p) \
        * math.cos(dest['lat'] * p) \
        * (1 - math.cos((dest['long'] - origin['long']) * p)) / 2
    return 12742 * math.asin(math.sqrt(a))

# start with origin and destination
origin = {'lat': float(sys.argv[1]), 'long': float(sys.argv[2])}
dest = {'lat': float(sys.argv[3]), 'long': float(sys.argv[4])}

print(find_distance(origin, dest))
print(find_distance_opt(origin, dest))

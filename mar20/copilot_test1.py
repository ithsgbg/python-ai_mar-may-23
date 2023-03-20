def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_ = n**0.5 + 1
    i = 3
    while i <= max_:
        if n % i == 0:
            return False
        i += 2
    return True

# Test all numbers from 1 to 100
for i in range(1, 101):
    if is_prime(i):
        print(i, "is prime")
    else:
        print(i, "is not prime")
        
# calculate the disctance between two coordinates using the Harvesine formula
def calulate_distance(lat1, lon1, lat2, lon2):
    from math import radians, cos, sin, asin, sqrt
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km

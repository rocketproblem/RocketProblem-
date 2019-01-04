
#Here is the data set for the first two problems 
rockets = {'rocket11': {'fuel': None, 'distance': 1590, 'weight': 175},
'rocket10': {'fuel': None, 'distance': 1392, 'weight': 445},
'rocket5': {'fuel': None, 'distance': 268, 'weight': 347},
'rocket4': {'fuel': None, 'distance': 1174, 'weight': 381},
'rocket3': {'fuel': None, 'distance': 327, 'weight': 146},
'rocket2': {'fuel': None, 'distance': 1223, 'weight': 93},
'rocket9': {'fuel': None, 'distance': 1684, 'weight': 382},
'rocket8': {'fuel': None, 'distance': 1206, 'weight': 477},
'rocket7': {'fuel': None, 'distance': 110, 'weight': 20},
'rocket6': {'fuel': None, 'distance': 533, 'weight': 131},
'rocket1': {'fuel': None, 'distance': 426, 'weight': 148}}

fuel = [639971, 1162112, 484687, 4496253, 934538, 708052, 23647, 5776215, 6467175, 6223146, 2814527]

#These are the growth in fuel for distance and weight
fuelfordis = 20 
growthforweight = 10

#This function is used to figure out the predicted value for fuel usage of a rocket
def expectedfuel(distance, weight):
    return int((fuelfordis + (weight * growthforweight)) * distance)

#Here we link the fuel to the rockets
for x in rockets:
    expected = expectedfuel(rockets[x]['distance'], rockets[x]['weight']) 
    for y in fuel:
        if y in range((expected - 1000), (expected + 1000)):
            rockets[x]['fuel'] = y

print(rockets)

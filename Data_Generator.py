rockets = {
    'rocket1' : {'distance' : 50, 'weight' : 100, 'fuel' : None},
    'rocket2' : {'distance' : 75, 'weight' : 297, 'fuel' : None},
    'rocket3' : {'distance' : 98, 'weight' : 14, 'fuel' : None},
    'rocket4' : {'distance' : 165, 'weight' : 29, 'fuel' : None},
    'rocket5' : {'distance' : 191, 'weight' : 68, 'fuel' : None},
    'rocket6' : {'distance' : 98, 'weight' : 60, 'fuel' : None},
    'rocket7' : {'distance' : 141.65, 'weight' : 40, 'fuel' : None},
    'rocket8' : {'distance' : 419, 'weight' : 80, 'fuel' : None},
}

fuel = [50000, 225000, 15000, 51975, 133175, 59800, 56660, 343320]

fuelfordis = 20 
growthforweight = 10

def expectedfuel(distance, weight):
    return int((fuelfordis + (weight * growthforweight)) * distance)


import random 
totalrejects = 0
for x in range(9, 20):
    name = "rocket" + str(x)
    distance = random.randrange(50, 2000)
    weight = random.randrange(10, 500)
    newfuel = random.randrange((expectedfuel(distance, weight) - 1000), (expectedfuel(distance, weight) + 1000))
    create = True
    for y in rockets:
        if rockets[y]['distance'] == distance or rockets[y]['weight'] == weight:
            create = False
    for y in fuel:
        if newfuel in range(y - 2100, y + 2100):
            create = False
    if create:
        rockets[name] = {'distance' : distance, 'weight' : weight, 'fuel' : None} 
        fuel.append(newfuel)
    else:
        print("rejected:\ndistance: {}\nweight: {}\nfuel: {}".format(distance, weight, newfuel))
        totalrejects += 1

print(rockets)
print(fuel)
print("rejected {} in total".format(totalrejects))
print("Now have {} total data sets".format(len(fuel)))
if len(fuel) != len(rockets):
    raise Exception("For some reason the data sets fuel and rockets don't line up")
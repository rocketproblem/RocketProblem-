#The empty data sets that we will fill in with this problem. 
rockets = {

}

fuel = []

#Here is the calculation for the expected fuel value so that we have accurate fuel relationships (to the rockets)
fuelfordis = 20 
growthforweight = 10

def expectedfuel(distance, weight):
    return int((fuelfordis + (weight * growthforweight)) * distance)

#We can use the module "random" to create random values. 
import random 
rocketsgen = 0
#We want to try and generate 20 rockets so we want to create a while loop that keeps going until we have 20
while rocketsgen < 21:
    x = rocketsgen
    #We want the new name of the rocket to be rocket + n. Everytime this loop runs we increase the var rocketsgen which x is set to, so we can use x
    name = "rocket" + str(x)
    #We want random values for the distance and weight. 
    distance = random.randrange(50, 2000)
    weight = random.randrange(10, 500)
    #Based off of the expected fuel for the rocket with the above distance and weight, we get a value in a range of 1000 up and down from that point. 
    #To get that random value we can use "randrange" from the module "random" to pick a random int in a range of numbers
    newfuel = random.randrange((expectedfuel(distance, weight) - 1000), (expectedfuel(distance, weight) + 1000))
    #We now want to go through a series of checks to make sure that the rocket and fuel doesn't intersect with the possible values of fuel for other already generated rockets
    create = True
    #This check is to make sure that the distance and weight of the rocket hasn't been used yet
    for y in rockets:
        if rockets[y]['distance'] == distance or rockets[y]['weight'] == weight:
            create = False
    #This check is to make sure that the fuel value that was picked isn't in a range of numbers that would cause problems for generators that look at possible fuel values for other rockets.
    for y in fuel:
        if newfuel in range(y - 2100, y + 2100):
            create = False
    #If the above checks worked and the var "create" is still true, it adds the rocket. 
    if create:
        rockets[name] = {'distance' : distance, 'weight' : weight, 'fuel' : None} 
        fuel.append(newfuel)
        rocketsgen += 1
    

print(rockets)
print(fuel)

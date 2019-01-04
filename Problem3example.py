"""
Make a generator that is able to generate different rockets (with distance and weight) and different fuel values that corrispond 
to the generated rockets. Your previous program should be able to put the values back together. Again, an example program will be 
attached for you if you need some help.
"""

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
#We should keep track of the amount of rockets generated 
rocketsgen = 0
#We want to try and generate 20 rockets. How can we loop over something for that amount of time, try using a while loop and the above var
#while _______:
    #How can we generate the name of the rocket so it is rocket + whatever rocket number we are on
    #name = w
    #Use the "randrange" module from the module "random" to get a random number from a range. you can do this by: random.randrange(x, y)
    #distance = x
    #weight = y
    #How can we also get a random value for fuel that is in the expected range (1000 each way from the mathimatically predicted) hint: use the random.randrange
    #newfuel = z
    #We now want to go through a series of checks to make sure that the rocket and fuel doesn't intersect with the possible values of fuel for other already generated rockets
    
    #First we should check to see if the distance or weight hasn't been used before in the current rockets... we can loop through dictionaries like lists using a for loop

    #Now we need to check to see if the fuel value we picked is too close to a different fuel value already have. This is to make sure that we don't mistake two fuel values for different rockets
    #We can use the in range() checker to make sure that the fuel isn't in a certain range

    #If the above checks worked, we need to add the rocket!
    #if ________:
        rockets[name] = {'distance' : distance, 'weight' : weight, 'fuel' : None} 
        fuel.append(newfuel)
    

print(rockets)
print(fuel)

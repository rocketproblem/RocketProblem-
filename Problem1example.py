"""
Our first problem requires you to create a program that sorts through our rocket distance an weight data and 
link them to the seperated fuel data. All we know is that every 50 km an empty rocket will take 1000 kg of fuel. 
However, for every kg more cargo, the rocket will require 10 kg more fuel for each km. (You do not need to worry 
about more fuel creating more weight). The biggest problem is the fuel consumption can vary 1000 kg up or down from 
the mathimatical predicted value. Watch Out! If you find yourself needing a bit of guidence you can referance the 
example files. After you have solved the problem, you can look at the solutions to check your answer. Good Luck!
"""


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

#These are the growth in fuel for distance and weight (These are found based on the set values for fuel burned per distance and per kg of weight)
fuelfordis = 20 
growthforweight = 10


#Here we link the fuel to the rockets
for x in rockets: #This for loop is for going through the different rockets
    expected = "___"#Here you should put an equation that gets the exact predicted value for the fuel of a rocket based on distance and weight
    #Now we need to check to see if any of the values in "fuel" vary up or down by 1000 from the predicted value. Remeber we can use a "for" loop to look at everything and the function "range()" to look at a range of numbers.
    #After, we need to change the "None" value of the rocket "x" to the value of the fuel we found above

print(rockets)

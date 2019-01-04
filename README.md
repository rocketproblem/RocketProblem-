# RocketProblem-
A simple application of some Python topics

Backstory:

  Hello scientist. Sorry, I look so messy - a thief got into our data banks and now all of our information
for our rockets have been scrambled. Luckily, he didn’t steal anything, or we would have been in deep trouble.
Our people are chasing after him and his crew now - none of us are sure what he wanted, but he might have been 
working with a rival company, or be selling secrets to other countries. With the data scrambled, all of our
rockets will crash because we can’t match up the values. This also means that our scientists on the International
Space Station are trapped until further notice. Thank god we sent out a rocket with supplies before this tragedy.
It will take some work, but hopefully, we can reorganize the data and continue to explore space.

Problem 1: 

Our first problem requires you to create a program that sorts through our rocket distance an weight data and link them to 
the seperated fuel data. All we know is that every 50 km an empty rocket will take 1000 kg of fuel. However, for every kg 
more cargo, the rocket will require 10 kg more fuel for each km. (You do not need to worry about more fuel creating more
weight). The biggest problem is the fuel consumption can vary 1000 kg up or down from the mathimatical predicted value. Watch Out! If you find yourself needing a bit of guidence you can referance the example files. After you have solved the 
problem, you can look at the solutions to check your answer. Good Luck!  

Here is the data set for the first problem:
(you can put this into your file. Remember: you should make a program that figures out which values in "fuel" go with which
rocket in "rockets". You should end with the "None" values for the "fuel" of the rockets being replaced with the corrisponding 
fuel values for the rocket in the "fuel" list.  

rockets = {
'rocket1': {'fuel': None, 'distance': 426, 'weight': 148}, 
'rocket2': {'fuel': None, 'distance': 1223, 'weight': 93}, 
'rocket3': {'fuel': None, 'distance': 327, 'weight': 146}, 
'rocket4': {'fuel': None, 'distance': 1174, 'weight': 381}, 
'rocket5': {'fuel': None, 'distance': 268, 'weight': 347}, 
'rocket6': {'fuel': None, 'distance': 533, 'weight': 131}, 
'rocket7': {'fuel': None, 'distance': 110, 'weight': 20}, 
'rocket8': {'fuel': None, 'distance': 1206, 'weight': 477}, 
'rocket9': {'fuel': None, 'distance': 1684, 'weight': 382}, 
'rocket10': {'fuel': None, 'distance': 1392, 'weight': 445}, 
'rocket11': {'fuel': None, 'distance': 1590, 'weight': 175}, 
} 
 
fuel = [639971, 1162112, 484687, 4496253, 934538, 708052, 23647, 5776215, 6467175, 6223146, 2814527] 


Problem 2:
  For an extension to problem 1, try to create another list that contains all the fuel values that don't work with the 
 data for the rockets. There is an example file that you can referance for a starting point. Good Luck! 
 (You should be able to sort out three numbers from the list below) 
 
fuel = [484687, 983245, 89432, 5776215, 708052, 23647, 6467175, 639971, 4496253, 6223146, 1162112, 934538, 2814527, 32432]


Problem 3: 
  If you are looking for a bit of a (unrelated) challenge problem try this: Make a generator that is able to generate 
 different rockets (with distance and weight) and different fuel values that corrispond to the generated rockets. Your
previous program should be able to put the values back together. Again, an example program will be attached for you if you
need some help. 


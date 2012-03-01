"""
Cubes
=====
* Create a list of ints using range, or create a list of ints using literals
(range(10) or [1,2,3])... assign it to a variable named numbers
* Create an empty list called cubes
* Iterate through the numbers list using a for loop
* For every number, cube it and append it to the cubes list
* Print out "Numbers: [your numbers list]"
* Print out "Cubes: [your cubes list]"

Example Output:
Numbers: [0, 1, 2, 3]
Cubes: [0, 1, 8, 27]
"""
numbers = [1,2,3]
cubes = []
for x in numbers:
		cubes.append(x*x*x)
print "numbers %s" % (numbers) 
print "cubes %s" % (cubes) 




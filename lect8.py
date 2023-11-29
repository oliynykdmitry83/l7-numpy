#  Guidance:
#  Comments made by hash symbol are not executed and mostly contain some explanation or theory
#  Other comments by set of triple double quotes """some code""" are interactive part of code you can play with
#  Be aware that they Always! go in pairs so to comment/uncomment code you need to keep that in your mind.
#  You can put a # in front of """ to comment the comment  



#  To "install" NumPy go to "Tools" -> "Packages" -> Numpy -> install




##################  NumPy Methods  #####################


# ############################################################
#
# Sorting Values
# 
# We can use NumPy to organise data within our array/matrix,  these use the .sort() method.
# The below script goes through some examples of these:

"""
import numpy as np

npArray = np.array([34, 2, 35, 33, 12, 54, 24, 46])

npAvarage = np.average(npArray)
npMin = np.min(npArray)
npMax = np.max(npArray)
npSize = npArray.size  # .size is in core Python

print("Avarage: ", npAvarage)
print("Minimum: ", npMin)
print("Maximum: ", npMax)
print("Size of Array: ", npSize)

npSortedAsending = np.sort(npArray)
print(npSortedAsending)

npSortedDescending = -np.sort(-npArray)
print(npSortedDescending)
"""

###############################################################################

# Random
#
# You can use NumPy to generate random values too, similar to how you can do so within the random library.
# Syntax is shown below:

"""
import numpy as np

ranNumber = np.random.rand(10)
print(ranNumber)

    #sample output:
    # [0.85575163, 0.05040093, 0.7102702, 0.03855975, 0.35728328, 0.53939736, 
    # 0.23432606, 0.45416568, 0.43985665, 0.52917647]

ranNumber2 = np.random.randint(0, 10, 6)
print(ranNumber2)
    #sample output:
    # [2, 0, 4, 3, 0, 8]

ranNumber3 = np.random.default_rng(12)      #random generator
ranInts = ranNumber3.integers(low = 0, high = 10, size = 6)
print(ranNumber3)
print(type(ranNumber3))
print(ranInts)

""" 
# Arange
# 
# This method wiil provide numbersat evently spaced intervals. For instance:
# 

"""
import numpy as np

exampleRange = np.arange(0, 40, 2)
print(exampleRange)

    #output:
    #[0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38]

"""    

# Zeros, Ones and Empty
#
# There will be times within Python where you may want to initialise an array in memory to store
# predetermined values. Can be used as part of machine learning, you may come across some of the following comands:
#   
#   •np.ones()
#   •np.zeros()
#   •np.empty()
#
# The full syntax of these are below:
# 
#   np.ones(shape =  , dtype = )
#   np.ones     - the function name;
#   shape =     - A tuple of values specifying the shape;
#   dtype =     - The data type of the output


#   Let's look for some examples of these:

"""
import numpy as np

onesArray = np.ones(shape = 8)
zeroArray = np.zeros(shape = 8)
emptyArray = np.empty(shape = 8)

print(onesArray)
print(zeroArray)
print(emptyArray)

"""

# the otput should be:
# [1. 1. 1. 1. 1. 1. 1. 1.]
# [0. 0. 0. 0. 0. 0. 0. 0.]
# [0. 0. 0. 0. 0. 0. 0. 0.]

# Note that even though it appears that the emptyArray has stored zeros, this is not the case in memory
# (example futher down) - This method will output uninitialised/arbitrary data.

# We can see this in action by providing each of the above methods a datatype,
# such as by doing the following:

"""
import numpy as np

onesArray = np.ones(shape = 8, dtype = int)
print(onesArray)

zeroArray = np.zeros(shape = 8, dtype = int)
print(zeroArray)

emptyArray = np.empty(shape = 8, dtype='int32')
print(emptyArray)


    # This should return back the following:
    #
    # [1 1 1 1 1 1 1 1]
    # [0 0 0 0 0 0 0 0]
    # [1634692198, 2037653620, 539780464, 1970233953, 1697783924, 540422445, 1830841961, 544502639] 
    #
    # When we create an empty array we are asking Python to allocate memory but we are not telling it what values to store.
    # Therefore it should be much quicker to allocate an empty array than one filled with zeroes for example. 
    # If you create an empty array and dispalay its contents, you should find whatever values the computer previously stored at those adresses.
    # It's your resposibility as the programmer to take that into account. In practice, when I tried to demonstrate this all the values turned out
    # to be zeroes. This is probably because some operating systems automaticly initialise memory when they allocate it to programs. 
    #  
"""


# Typically,  using np.empty() will be quicker for a large matrices, due to machine not needing to
# initialise every element with a specific value. 


# The following code will contain a range of exercises using NumPy, 
# it is recommended that you start at the top and work your way down in stages to help support your development 

#########################################################################################

# NumPy exercises

# Task 01 - Create an array
#  
# Using NumPy, create an array wich contains the below numbers, you should print this out the screen in order to test
# [1 4 6 8 7 2 3 9 10 13 5]


# Displaying odd numbers
#  
# Using the array you've created, display only odd numbers that are within the array e.g.
# [1 7 3 9 13 5]

# creating a Matrix
#  
# Create an identity matrix with the dimentions of 4*4. The below shows the example output of this:
#  
# [[1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1]]


######################## Mathmatical Arrays ############################
#  
# Within the following challenges (all labelled Math #value), use the below code at the start:

"""
# Import NumPy in order to be used
import numpy as np

# Creates an array of data
randomArray = np.array([[1005, 2154, 1123,6524],
                        [1136, 8874, 4665, 4785],
                        [3365, 9564, 4474, 5632],
                        [1111, 3354, 6625, 2247],
                        [1679, 4652, 6431, 1465]])
""" 


############################################################################

# Math #1
# Display the avarage of the above array

# Math #2
# Start by displaying the numbers within the 3rd column with this array.
# Using these values, provide the avarage value of the third column within this array
# Display this value to 2 decimal places

# Math #3
# Provide the avarage value of the first 2 rows withing this array. 

# Math #4
# Provide the minimum and maximun value withing this array


##############################################################################

# NumPy Challenge Scenario:
#
# Student Grade Tracker
# 
# 15 students have been provided with grades. The max mark avaliable is 100.
# Allow for the user to put these values into a NumPy array.
# 
# Once this has been completed, you will need to complete the following using this dataset:
#   • Work out the minimum, maximun and avarage grade.
#   • Sort the grades in ascending order
#   • All points will be provided with 2 extra marks, display the output for this.
#   • Display the top three  and lowest three grades scored.
#
# Also if you can, save and retrieve this data back from a file after you have used it.

############################################################################################



######################### Some more ways of dealing with arrays ############################

# Accessing/Changing specific elements, rows, columns, etc

# In the next examples uncomment a block of code(by commenting out the triple quote, using #""") and uncomment each print()
# function at one time to get the right output. Because if you uncomment all print functions at the same time it'll
# be difficult to follow what line of code is related to the received ouput.

"""
import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

# Get a specific element [r, c]
#print(a[1, 5])

# Get a specific row 
#print(a[0, :])

# Get a specific column
#print(a[:, 2])

# Getting a little more fancy [startindex:endindex:stepsize]
#print(a[0, 1:-1:2])

a[1,5] = 20

a[:,2] = [1,2]
#print(a)

b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
#print(b)

# Get specific element (work outside in)
#print(b[0,1,1])

# replace 
b[:,1,:] = [[9,9],[8,8]]
#print(b)

"""


############## Initializing Different Types of Arrays #######################

"""

import numpy as np

# All 1s matrix
a = np.ones((4,2,2), dtype='int32')
print(a)

# Any other number
b = np.full((2,2), 99)
#print(b)

# Any other number (full_like)
c = np.full_like(a, 4)
#print(c)

# Random decimal numbers
d = np.random.rand(4,2)
#print(d)

# Random Integer values
e = np.random.randint(-4,8, size=(3,3))
#print(e)

###################################################################################

# Repeat an array
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3, axis=0)
#print(r1)

output = np.ones((5,5))
#print(output)

z = np.zeros((3,3))
z[1,1] = 9
#print(z)

output[1:-1,1:-1] = z
#print(output)

"""

##################### Be careful when copying arrays!!! ###############################

"""
import numpy as np

a = np.array([1,2,3])
b = a.copy()            # try to run this block of code without .copy() to see the difference
b[0] = 100

print(a)

"""

############################## Mathematics ########################################################

"""
import numpy as np

a = np.array([1,2,3,4])
print(a)

b = a + 2
print(b)

c = a - 2
print(c)

d = a * 2
print(d)

e = a ** 2
print(e)

f = np.cos(a)
print(f)

# For a lot more (https://docs.scipy.org/doc/numpy/reference/routines.math.html)

"""

################################ Linear Algebra ######################################


"""

import numpy as np

a = np.ones((2,3))
print(a)

b = np.full((3,2), 2)
print(b)

res = np.matmul(a,b)
print(res)

# Find the determinant
c = np.identity(3)
d = np.linalg.det(c)

print(c)
print(d)

## Reference docs (https://docs.scipy.org/doc/numpy/reference/routines.linalg.html)

# Determinant
# Trace
# Singular Vector Decomposition
# Eigenvalues
# Matrix Norm
# Inverse
# Etc...

"""

################################### Reorganizing Arrays ######################################

"""
import numpy as np

before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

#after = before.reshape((2,3))
#print(after)                   # why do we have an error?

#enotherAfter = before.reshape((4,2))
#print(enotherAfter)

# Vertically stacking vectors

v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

res = np.vstack([v1,v2,v1,v2])
print(res)

# Horizontal  stack

h1 = np.ones((2,4))
h2 = np.zeros((2,2))

hres = np.hstack((h1,h2))
print(hres)

"""

############################################# Miscellaneous ##############################

"""

import numpy as np

#Load Data from File

filedata = np.genfromtxt('data.txt', delimiter=',')
filedata = filedata.astype('int32')
print(filedata)

# Boolean Masking and Advanced Indexing

res = (~((filedata > 50) & (filedata < 100)))
print(res)

"""








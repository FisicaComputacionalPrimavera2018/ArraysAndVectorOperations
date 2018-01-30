import math

#### FUNCTIONS
# The name of the function is "norm"
# Input: array x
# Output: the norm of x
def norm(x):

	tmp = 0
	for v in x:

        	tmp += v*v

	norm_x = math.sqrt(tmp)
	return norm_x

def vectorSum(x, y):

	#z = x + y This doesn't work!

	# First we check if the dimensions of x and y
	# are the same
	if len(x) != len(y):
		return "ERROR"

	# Now, we know the dimensions are the same
	
	# We create an empty (zeros) vector z, which as the 
	# same dimensions as x and y
	z = [0]*len(x)

	# Next step, calculate the components of z
	for i in range(0, len(z)):

		z[i] = x[i] + y[i]

	#z = [ x[0]+y[0], x[1]+y[1], x[2]+y[2] ]
	
	return z # return the sum

def scalarProduct(x, y):

        if len(x) != len(y):
                return "ERROR"
	r = 0
	for i in range(0, len(x)):

		r = x[i]*y[i]

	return r	

# Define some three-dimensional vectors
x = [5, 3, 5]
y = [5.5, 6, 8]
z = [2, 0, 6.6]

# EX1: compute the norm of x,y,z

# First method
norm_x = math.sqrt(x[0]*x[0] + x[1]*x[1] + x[2]*x[2])
print norm_x

# Second method
tmp = 0
for v in x:

	tmp += v*v

norm_x = math.sqrt(tmp)
print norm_x

# Third method: using the function "norm"
print norm(x)
print norm(y)
print norm(z)

print vectorSum(x, y)

print scalarProduct(x, y)


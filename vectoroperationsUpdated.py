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

	#z = x + y This doesn't work for arrays!

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

def angle(x, y):

	return math.acos(scalarProduct(x,y) / (norm(x)*norm(y)))
	


# Define some three-dimensional vectors
x = [5, 3, 5]
y = [5.5, 6, 8]
z = [2, 0, 6.6]

# norm
print norm(x)

# sum
print vectorSum(x, y)

# scalar product
print scalarProduct(x, y)

# angle (homework)
norm_x = norm(x)
norm_y = norm(y)
n = scalarProduct(x,y)
#print  math.acos(n/(norm_x*norm_y))

# shorter way:
#print  math.acos(scalarProduct(x,y) / (norm(x)*norm(y)))

# even shorter
angle1 = angle(x, y)
print angle1


#print angle(x, y)

# convert to degrees
#print math.degrees(angle(x, y))

# angle of vector A between x,y,z axis
A = [5, 6, 11]
alpha_1 = angle(A, [1, 0, 0])
alpha_2 = angle(A, [0, 1, 0])
alpha_3 = angle(A, [0, 0, 1])
print alpha_1, alpha_2, alpha_3

# vector product (homework)


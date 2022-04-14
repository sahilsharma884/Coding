# Define for conversion decimal to hexadecimal
# For example: 27 -> 1B, 427 -> 1AB
def Dec2Hexa(X):
	sum_hexaX = 0
	while X >= 16:
		rem = X % 16
		if rem != 0:
			sum_hexaX += rem
		X = X // 16
	
	if X != 0:
		sum_hexaX += X
	
	return sum_hexaX


# Define GCD
def GCD(X,Y):
	'''
	Parameters:
	X : large number (int)
	Y : small number (int)
	'''

	while(Y):
		X, Y = Y, X % Y
	
	return X

if __name__ == '__main__':
	# Store test case
	T = int(input())
	for t in range(T):
		# Store range L and R
		L,R = list(map(int,input().split(' ')))
		# Intialize counter to zero for tracking number of condition satisfy GCD(X,F(X)) > 1
		count = 0
		# Iterate over range L to R
		for X in range(L,R+1):
			# If GCD(X,F(X)) > 1, then increment counter otherwise move to next range value
			if GCD(X,Dec2Hexa(X)) > 1:
				count += 1
		# Display output
		print(count)

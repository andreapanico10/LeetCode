# https://leetcode.com/problems/sqrtx/?envType=study-plan-v2&envId=top-interview-150

# SQRT(X)
 
# Version 1: BINARY SEARCH
# INPUT: integer

# OUTPUT:  return the square root of x rounded down to the nearest integer

import sys


def binary_search(a_min, a_max, value):
		
		if value <= 1:
			return value
			
		if (a_min >= a_max):
			return a_min - 1 # TO RETURN THE NEAREST INTEGER (-1)
		
		else:
					
			middle = (a_max + a_min)//2
			
			if middle*middle == value:
				return middle
				
			else:
		
				if value >= middle*middle:
					return binary_search(middle+1, a_max, value)
				else:
					return binary_search(a_min, middle, value)
			
def sqrt(x_min = 0, x_max = 1, value=1):
	
	if type(value) != int or value < 0:
		sys.exit(f"Exit {sys.argv[0]}: Invalid input")
	
	sqrt = binary_search(x_min, x_max, value) 
	print(sqrt)
	return(sqrt)
	
if __name__ == "__main__":
	sqrt()
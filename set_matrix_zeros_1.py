# https://leetcode.com/problems/set-matrix-zeroes/?envType=study-plan-v2&envId=top-interview-150

# 73. Set Matrix Zeroes

# VERSION 1

# INPUT: mxn integer matrix,  
# OUTPUT:if an element is 0, set is entire row and column = 0

import numpy as np
import sys 

def set_matrix_zeros(matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]):
	# matrix dimensions
	n, m = len(matrix), len(matrix[0]) 
	
	zeros_indexes = []
	
	for row_idx, i in enumerate(matrix):
		for col_idx, j in enumerate(i):
			if j == 0:
				zeros_indexes.append(row_idx *m + col_idx)	 
	
	for zero_idx in zeros_indexes:
		
		for row_idx, i in enumerate(matrix):
			for col_idx, j in enumerate(i):
				
				idx = row_idx *m + col_idx
			
				# Correct the column 
				if zero_idx % m == idx%m:
					matrix[row_idx][col_idx] = 0
				
				# Correct the row
				if idx//m == zero_idx // m:
					matrix[row_idx][col_idx] = 0
							
	
	''' 
	Not in place solution
	
	plain_matrix = np.ravel(matrix)
	zeros_index = [idx for idx, num in enumerate(plain_matrix) if num == 0] 
	'''
	return(matrix)
	
if __name__ == "__main__":
	set_matrix_zeros()
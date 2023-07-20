from set_matrix_zeros_1 import set_matrix_zeros

def test():
	assert [[1,0,1],[0,0,0],[1,0,1]] == set_matrix_zeros([[1,1,1],[1,0,1],[1,1,1]])
	assert [[0,0,0,0],[0,4,5,0],[0,3,1,0]] == set_matrix_zeros([[0,1,2,0],[3,4,5,2],[1,3,1,5]]) 
	

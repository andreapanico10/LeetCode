# https://leetcode.com/problems/combinations/?envType=study-plan-v2&envId=top-interview-150

# 77. Combinations

# VERSION 1

# INPUT: Given 2 integers n and k
# OUTPUT: Return all possible combinations of k numbers chosen from range [1, n]
# Not relevant the order

import sys

def combinations(n=5, k=3):
	
	if k <= 0:
		sys.exit("k can't be less than 0")
		
	if k > n:
		sys.exit("k can't be > 20 by problem restrictions")
	
	all_combinations = set()
	
	j = 0
	i = j+1
	data = [*range(1,n+1)]
	
	while j < len(data):
		i = j+1
		while i <= len(data):
			if (i+k-1 <= len(data)):
				combination = [data[j]] + list(data[i:i+k-1]) 
				all_combinations.add(tuple(combination))
				
			elif j > len(data) - k+1:
				combination = list(data[j:len(data)]) + list(data[:k-1 - (len(list(data[j:len(data)])) - 1)])
				combination = sorted(combination)
				all_combinations.add(tuple(combination))
				
			i += 1
		j += 1
		
	# from set of tuples to list of list
	all_combinations = ([list(tup) for tup in list(all_combinations)])
	return all_combinations
	
	
if __name__ == "__main__":
	print(combinations())
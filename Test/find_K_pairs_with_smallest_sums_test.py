from find_K_pairs_with_smallest_sums_1 import find_k_pairs_with_smallest_sums


def test():
	assert [[1,2],[1,4],[1,6]] == find_k_pairs_with_smallest_sums([1,7,11], [2,4,6], 3)
	assert [[1,1],[1,1]] == find_k_pairs_with_smallest_sums([1,1,2], [1,2,3], 2) 
	assert [[1,3],[2,3]] == find_k_pairs_with_smallest_sums([1,2], [3], 3) 
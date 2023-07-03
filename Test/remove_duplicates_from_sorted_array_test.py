#from pytest import Raise
from remove_duplicates_from_sorted_array_1 import remove_duplicates

def test_1():
	nums = [1,1,2]
	expected_nums = [1,2]

	k = remove_duplicates(nums)
	assert k == len(expected_nums)
	for i in range(k):
		assert nums[i] == expected_nums[i]
	

def test_2():
	nums = [0,0,1,1,1,2,2,3,3,4]
	expected_nums = [0,1,2,3,4]

	k = remove_duplicates(nums)
	assert k == len(expected_nums)
	for i in range(k):
		assert nums[i] == expected_nums[i]
	

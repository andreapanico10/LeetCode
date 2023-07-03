# link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150
# Remove duplicates --> and then return k = len(nums)

# Version 1: use of not in is slower than Version 2

# Binary search implemented by me is slower
def binary_search(list, target):
    ''' Returns only a boolean condition'''
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return binary_search(list[midpoint + 1:], target)
            if list[midpoint] >= target:
                return binary_search(list[:midpoint], target) 

def remove_duplicates(nums=[0,0,1,1,1,2,2,3,3,4]):
	#Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

	k = 0
	for i,num in enumerate(nums):
		if num not in nums[:k]:
			nums[k] = nums[i]
			k += 1
	return(k)

if __name__ == "__main__":
	remove_duplicates()		
			
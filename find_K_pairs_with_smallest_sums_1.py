# Find K Pairs with Smallest Sums

# VERSION 1

# INPUT: arrays num1 e num2 sorted in increasing order, k 

# (u,v) u from num1 and v from num2 

# OUTPUT: k pairs (u1, v1)...(uk, vk) with the smallest sums

def get_all_pairs(nums1, nums2):
	all_pairs = []
	all_pairs_dict = []
	id = 0
	for num1 in nums1: 
		for num2 in nums2:
		
			all_pairs_dict.append({"id" : id, "value" : num1+num2})
			all_pairs.append([num1, num2]) 
			id += 1
	return all_pairs, all_pairs_dict

def find_k_pairs_with_smallest_sums(nums1=[1,7,11], nums2=[2,4,6], k=3):
	all_pairs, all_pairs_dict = get_all_pairs(nums1, nums2)
	all_pairs_dict = (sorted(all_pairs_dict, key=lambda d: d['value']))
	pairs = []
		
	for i in range(min(k,len(all_pairs))):
		id = all_pairs_dict[i]["id"]
		pairs.append(all_pairs[id])	
		
	return(pairs)
	
if __name__ == "__main__":
	find_k_pairs_with_smallest_sums()
	
	
### PROBLEM WITH THIS VERSION 1: MEMORY LIMIT EXCEDEED
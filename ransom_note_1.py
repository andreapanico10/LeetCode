# https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150

#383. Ransom Note

# VERSION: 1  Beats 91% in runtime

# INPUT: 2 strings ransomNote and magazine
# OUTPUT: return true if ransomNote can be constructed by using the letters from magazine and false otherwise
#         Each letter in magazine can only be used once in ransomNote.

def ransom_note(ransomNote, magazine):
	for letter in ransomNote:
		if letter not in magazine:
			return False
		else:
		 	magazine = magazine.replace(letter, '', 1)
	return True
	
	

if __name__ == "__main__":
	print(ransom_note("aa", "aab"))

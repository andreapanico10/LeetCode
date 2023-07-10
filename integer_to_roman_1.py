# https://leetcode.com/problems/integer-to-roman/?envType=study-plan-v2&envId=top-interview-150

# 12. Integer to Roman

# VERSION 1

# HINT for version 2:
'''
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            # If n in list then add the roman value to result variable
            while n <= num:
                r += num_map[n]
                num-=n
        return r
'''

# INPUT:Given an integer 
# OUTPUT: convert it to a roman numeral

import sys

def lecter_conversion(number, main_lecter, middle_lecter, next_lecter):
		
		if number <=3:
			return main_lecter*number
		elif number == 4:
			return main_lecter + middle_lecter
		elif number < 9:
			return middle_lecter + number%5*main_lecter 
		else:
			return main_lecter + next_lecter
	
def convertion(ten_power, number):

	# Units
	if ten_power == 0:	
			
		return lecter_conversion(number, "I", "V", "X")
	
	# Tens
	elif ten_power == 1:
		
		return lecter_conversion(number, "X", "L", "C")

	# Hundreds
	elif ten_power == 2:
		
		return lecter_conversion(number, "C", "D", "M")
	
	# Thousands
	elif ten_power == 3:
		if number <= 3: 
			return (number)*"M" 	
		
	 
	
def integer_to_roman(num=1):
	
	if num > 3999:
		sys.exit("Max num: 3999")
		
	roman_number = ""
	for i, str_num in enumerate(reversed(str(num))):
		roman_number = convertion(i, int(str_num)) + roman_number
	return roman_number
	

if __name__ == "__main__":
	integer_to_roman()
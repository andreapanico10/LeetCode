# https://leetcode.com/problems/minimum-genetic-mutation/?envType=study-plan-v2&envId=top-interview-150
# Minimum Genetic Mutation
# Version 1

# gene string = 8 chars from "A" "C" "G" "T"

# Mutation from startgene to endgene

# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# Valid mutations are in a bank
# INPUT: startGene, endGene and the gene bank bank
# OUTPUT: return the minimum number of mutations needed to mutate from startGene to endGene

#If there is no such a mutation, return -1.


def minimum_genetic_mutation(start_gene="AACCGGTT", end_gene="AAACGGTA", bank=["AACCGGTA","AACCGCTA","AAACGGTA"]):
	if end_gene not in bank:
		return -1
		
	else:
		# THE SOLUTION IS ABOUT DYNAMIC PROGRAMMING, PROBABLY LCS (LONGEST COMMMON SUBSTRING), BUT FOR NOW PROCEDE AS WE CAN
		
		differences = 0
		
		for (char_start_gene, char_end_gene) in zip(start_gene, end_gene):
			if char_start_gene != char_end_gene:
				differences += 1
		return differences
		
	# TOTALMENTE SBAGLIATO L'APPROCCIO OVVIAMENTE... 
	# YOU HAVE TO FIND A POSSIBLE SEQUENCE THAT LEAD TO THE SOLUTION BY 1 MUTATION(regular) AT TIME
			
if __name__ == "__main__":
	minimum_genetic_mutation(start_gene, end_gene, bank)
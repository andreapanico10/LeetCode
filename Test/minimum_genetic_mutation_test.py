from minimum_genetic_mutation_1 import minimum_genetic_mutation	


def test():
	assert 1 == minimum_genetic_mutation("AACCGGTT","AACCGGTA",["AACCGGTA"])
	assert 2 == minimum_genetic_mutation("AACCGGTT", "AAACGGTA",["AACCGGTA","AACCGCTA","AAACGGTA"])
	assert -1 == minimum_genetic_mutation("AACCTTGG", "AATTCCGG", ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"])
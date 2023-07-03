from sqrt import sqrt

def test():
	assert 4 == sqrt(0,16,16)
	assert 2 == sqrt(0,4,4)
	assert 2 == sqrt(0,8,8)
	assert 0 == sqrt(0,0,0)
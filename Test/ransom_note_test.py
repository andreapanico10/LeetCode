from ransom_note_1 import ransom_note

def test():
	assert True == ransom_note("aa", "aab")
	assert False == ransom_note("aa", "ab")

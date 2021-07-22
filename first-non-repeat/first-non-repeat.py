def firstNonRepeatingCharacter(string):
    # make a dict of letters
	letters = {}
	for i in range(len(string)):
		if string[i] in letters:
			letters[string[i]].append(i)
		else:
			letters[string[i]] = [i]
	for i in range(len(string)):
		if len(letters[string[i]]) == 1:
			return i
    return -1
def minimumCharactersForWords(words):
    # Write your code here.
	# make a dict of all of the unique letteres and the counts
	def getLetterCount(word):
		output = {}
		for letter in word:
			if letter not in output:
				output[letter] = 0
			output[letter] += 1
		return output

	def updateMax(letters, max_letters):
		for letter in letters:
			if letter in max_letters:
				max_letters[letter] = max(letters[letter], max_letters[letter])
			else:
				max_letters[letter] = letters[letter]
		return max_letters
	max_letters = {}
	for word in words:
		letter_count = getLetterCount(word)
		max_letters = updateMax(letter_count, max_letters)
	output = []
	for letter in max_letters:
		freq = max_letters[letter]
		for i in range(freq):
			output.append(letter)
	return output

	#TODO: examine O(n) runtime
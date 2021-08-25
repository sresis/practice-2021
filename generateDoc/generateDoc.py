def generateDocument(characters, document):
    # O(n + m) time
	char_dict = {}
	doc_dict = {}
	for char in characters:
		if char not in char_dict:
			char_dict[char] = 0
		char_dict[char] += 1
	for char in document:
		if char not in char_dict:
			return False
		elif char not in doc_dict:
			doc_dict[char] = 0
		doc_dict[char] += 1
		if doc_dict[char] > char_dict[char]:
			return False
    return True

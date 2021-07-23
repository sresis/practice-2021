def reverseWordsInString(string):
	# loop through char until reach a space
	output = []
	curr = ''
	for char in string:
		if char != ' ':
			curr += char
		else:
			output.append(curr)
			output.append(' ')
			curr = ''
	output.append(curr)
	# now need to reverse in place
	start = 0
	end = len(output) -1
	while start < end:
		output[start], output[end] = output[end], output[start]
		start += 1
		end -= 1
	return ('').join(output)

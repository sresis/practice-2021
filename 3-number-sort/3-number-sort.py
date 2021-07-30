def threeNumberSort(array, order):
	# for each number...increment til end
	place = 0
	for i in range(len(order)):
		for j in range(len(array)):
			if array[j] == order[i]:
				array[j], array[place] = array[place], array[j]
				place += 1

    return array

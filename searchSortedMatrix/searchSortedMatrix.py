def searchInSortedMatrix(matrix, target):
    row = 0
	  col = len(matrix)
    while row < len(matrix) and col >= 0:
		if matrix[row][col] == target:
			return [row, col]
		elif matrix[row][col] < target:
			row += 1
		else:
			col -= 1
	return [-1, -1]

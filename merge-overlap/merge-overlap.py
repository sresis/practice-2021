# O(n log n time)..O(n) space
def mergeOverlappingIntervals(intervals):
	# first sort all intervals
	intervals.sort()
	output = []
	if len(intervals) > 0:
		curr = intervals[0]
	else:
		return [[]]
	for i in range(1, len(intervals)):
		# assess if can append to existing, or create new
		if intervals[i][0] <= curr[1]:
			# handle if the max is diff
			curr[1] = max(curr[1], intervals[i][1])
		else:
			output.append(curr)
			# need to change?
			curr = intervals[i]
	output.append(curr)
	return output
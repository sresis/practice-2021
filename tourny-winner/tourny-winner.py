def tournamentWinner(competitions, results):
    # Write your code here.
	team_points = {}
	# score points for each
	for i in range(len(competitions)):
		if results[i] == 0:
			winner = competitions[i][1]
		else:
			winner = competitions[i][0]
		if winner not in team_points:
			team_points[winner] = 0
		team_points[winner] += 3
	return max(team_points, key=lambda k: team_points[k])



# My implementation
def tournament_winner1(competitions, results):
    scores = {}
    best_team = ""

    for i in range(0, len(competitions)):
        winner = None

        if results[i] == 0:
            winner = competitions[i][1]
        elif results[i] == 1:
            winner = competitions[i][0]

        if winner:
            if winner in scores:
                scores[winner] += scores[winner]
            else:
                scores[winner] = 1

            if best_team:
                if scores[winner] > scores[best_team]:
                    best_team = winner
            else:
                best_team = winner

    print(scores)
    return best_team

# O(n) time
# O(k) space (k-teams)
HOME_TEAM_WON = 1
def tournament_winner2(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    def updateScores(team, points, scores):
        if team not in scores:
            scores[team] = 0
        scores[team] += points

    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition

        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        updateScores(winningTeam, 3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam

    return currentBestTeam


print(tournament_winner1([
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
], [0, 0, 1]))

print(tournament_winner2([
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
], [0, 0, 1]))

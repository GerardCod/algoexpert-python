def tournamentWinner(competitions, results):
    """
        ### Description
        tournamentWinner returns the team with the best score.

        ### Parameters
        - competitions: matrix containing the teams' names in each match.
        - results: list containing the result of every competition.

        ### Returns
        The name of the best team.
    """
    competitors = {"": 0}
    bestTeam = ""
    currentMatch = 0

    while currentMatch < len(results):
        winner = competitions[currentMatch][0] if results[currentMatch] == 1 else competitions[currentMatch][1]

        if winner in competitors:
            competitors[winner] = competitors[winner] + 3
        else:
            competitors[winner] = 3

        if competitors[bestTeam] < competitors[winner]:
            bestTeam = winner

        currentMatch += 1

    return bestTeam


if __name__ == "__main__":
    competitions = [
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"]
    ]

    results = [0, 0, 1]

    print(tournamentWinner(competitions, results))

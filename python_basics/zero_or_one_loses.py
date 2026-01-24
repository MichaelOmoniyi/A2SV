class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        scoreboard = {}
        
        for losers in matches:
            scoreboard[losers[1]] = scoreboard.get(losers[1], 0) + 1

        for winners in matches:
            scoreboard[winners[0]] = scoreboard.get(winners[0], 0)

        return [sorted([winner for winner, point in scoreboard.items() if point == 0]), sorted([loser for loser, point in scoreboard.items() if point == 1])]
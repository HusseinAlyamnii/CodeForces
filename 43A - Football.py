n = int(input())
scores = {}

for _ in range(n):
    team = input().strip()
    if team in scores:
        scores[team] += 1
    else:
        scores[team] = 1

winner = max(scores, key=scores.get)
print(winner)

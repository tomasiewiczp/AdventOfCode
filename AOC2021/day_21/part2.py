from collections import Counter

roll_possibilities = Counter(
    sum_ for sum_ in (a + b + c for a in [1,2,3] for b in [1,2,3] for c in [1,2,3])
)
# roll_possibilities: {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}

memo = {}

def quantum_dirac(p1_pos, p1_score, p2_pos, p2_score, is_p1_turn):
    key = (p1_pos, p1_score, p2_pos, p2_score, is_p1_turn)
    if key in memo:
        return memo[key]
    if p1_score >= 21:
        return (1, 0)
    if p2_score >= 21:
        return (0, 1)
    total_p1, total_p2 = 0, 0
    for roll_sum, universes in roll_possibilities.items():
        if is_p1_turn:
            new_p1_pos = ((p1_pos + roll_sum - 1) % 10) + 1
            new_p1_score = p1_score + new_p1_pos
            p1_wins, p2_wins = quantum_dirac(new_p1_pos, new_p1_score, p2_pos, p2_score, False)
        else:
            new_p2_pos = ((p2_pos + roll_sum - 1) % 10) + 1
            new_p2_score = p2_score + new_p2_pos
            p1_wins, p2_wins = quantum_dirac(p1_pos, p1_score, new_p2_pos, new_p2_score, True)
        total_p1 += p1_wins * universes
        total_p2 += p2_wins * universes
    memo[key] = (total_p1, total_p2)
    return memo[key]

p1, p2 = quantum_dirac(5, 0, 9, 0, True)
print(max(p1, p2))
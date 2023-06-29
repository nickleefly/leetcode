def solution(R, V):
    minimal_A, minimal_B, balance = 0, 0, 0
    for receiver, amount in zip(R, V):
        if receiver == 'A':
            balance += amount
            minimal_B = min(-balance, minimal_B)
        else:
            balance -= amount
            minimal_A = min(balance, minimal_A)

    return [-minimal_A, -minimal_B]


R = 'BAABA'
V = [2, 4, 1, 1, 2]
print(solution(R, V))

def solution(S, C):
    cost_f, i, flag = 0, 1, 0

    for i in range(1, len(S)):
        cur, c_cost = S[i], C[i]
        prev, p_cost = S[i-1], C[i-1]
        prev_i, cost_i = 0, 0
        if ind == 1:
            prev, p_cost = prev_i, cost_i
        if cur == prev:
            if c_cost >= p_cost:
                cost_f += p_cost
                prev_i, cost_i = 0, 0
                flag = 0
            if c_cost < p_cost:
                cost_f += c_cost
                flag = 1
                prev_i, cost_i = prev, p_cost
        else:
            prev_i, cost_i = 0, 0
            flag = 0
    return cost_f


S = 'ababa'
C = [10, 5, 10, 5, 10]
"""
S='bccdb' C=[0,1,2,3,4,5]
S='aabbcc' C=[1,2,1,2,1,2]
"""
print(solution(S, C))

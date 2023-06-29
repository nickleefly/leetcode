def solution(A):
    bit = [0 for i in range(32)]
    N = len(A)

    for i in range(N):
        x = 31

        # check until array element becomes zero
        while (A[i] > 0):
            # check if the last bit is set
            if (A[i] & 1 == 1):
                # increment frequency
                bit[x] += 1

            # divide array element by 2
            A[i] = A[i] >> 1

            # decrease the bit position
            x -= 1

    # size of the largest possible subset
    return max(bit)


A = [13, 7, 2, 8, 3]
print(solution(A))

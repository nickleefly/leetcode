def fibonacci_recur(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci_recur(n-1) + fibonacci_recur(n-2)


def fibonacci(n: int) -> int:
    if n <= 1:
        return n

    prev_prev = 0
    prev = 1
    curr = 1

    for i in range(2, n+1):
        curr = prev + prev_prev
        prev_prev = prev
        prev = curr

    return curr

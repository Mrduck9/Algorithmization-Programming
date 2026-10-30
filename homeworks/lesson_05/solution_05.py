def step_score(steps, k, lower, upper):
    n = len(steps)
    window = sum(steps[:k])
    score = 0

    if window < lower:
        score -= 1
    elif window > upper:
        score += 1

    for i in range(k, n):
        window += steps[i] - steps[i - k]
        if window < lower:
            score -= 1
        elif window > upper:
            score += 1
    return score


def decrypt(code, k):
    n = len(code)

    if k == 0:
        return [0] * n

    result = [0] * n

    if k > 0:
        window = sum(code[1:k + 1])
        for i in range(n):
            result[i] = window
            window -= code[(i + 1) % n]
            window += code[(i + k + 1) % n]
    else:
        m = -k
        window = sum(code[n - m:])
        for i in range(n):
            result[i] = window
            window -= code[(i - m) % n]
            window += code[i % n]
    return result

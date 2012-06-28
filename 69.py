m = 1
N = 1000001
is_prime = [False, False] + [True for i in range(N)]
for i in range(2, N):
    if is_prime[i] is True:
        m *= i
        if m > N:
            print m / i
            break
        for j in range(i * i, N, i):
            is_prime[j] = False


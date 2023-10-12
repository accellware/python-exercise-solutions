def TriBulle(S):
    i = 0
    j = 0
    mi = 0
    for i in range(len(S) - 1):
        for j in range(i + 1, len(S)):
            if S[i] > S[j]:
                value = S[i]
                S[i] = S[j]
                S[j] = value

    return S

S = TriBulle([15, 18, 25, 64, 22, 10, 5, 3, 9, 14])

print('Tri a Bulle: ', S)
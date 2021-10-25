def TriSelection(S):
    i = 0
    j = 0
    mi = 0
    for i in range(len(S) - 1):
        minimum = S[i]
        index = i
        for j in range(i + 1, len(S)):
            if S[j] < minimum:
                minimum = S[j]
                index = j
        
        S[index] = S[i]
        S[i] = minimum

    return S

S = TriSelection([15, 18, 25, 64, 22, 10, 5, 3, 9, 14])

print('Tri Selection: ', S)
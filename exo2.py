def Dichotomie(S, x):
    start = 0
    end = len(S) - 1
    mid = int((end - start) / 2)
    while end != start:
        value = S[mid]
        if value == x:
            return mid
        else:
            if x > value:
                start = mid + 1
            else:
                end = mid
        mid = int((end - start) / 2) + start
    
    return -1

nb = int(input('Chose a number: '))
x = int(input('Elem to search for: '))
s = range(1, nb + 1)

index = Dichotomie([1, 3, 5, 9, 10, 11, 18, 29, 30, 50], x)

print('Elem index: %i' % index)
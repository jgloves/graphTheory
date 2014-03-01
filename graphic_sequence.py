
def havel_hakimi(sequence):
    n = sequence[0] + 1
    for i in range(1, n):
        sequence[i] = sequence[i] - 1
    del sequence[0]
    return sorted(sequence, reverse=True)

def graphic_sequence(sequence):
    if sequence[0] == 0:
        return True
    else:
        if sequence[-1] < 0:
            return False
        else:
            if len(sequence) < sequence[0] + 1 : 
                return False
            else:
                return graphic_sequence(havel_hakimi(sequence))

graphic_sequence([3, 2, 3, 2, 1, 1])

graphic_sequence([2,2,2,2,3,3])

graphic_sequence([1, 0])

graphic_sequence([0])

graphic_sequence([1])


graphic_sequence([2,2,2,2])




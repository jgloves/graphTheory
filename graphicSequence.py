# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

def havelHakimi(sequence):
    n = sequence[0] + 1
    for i in range(1, n):
        sequence[i] = sequence[i] - 1
    del sequence[0]
    return list(reversed(sorted(sequence)))

# <codecell>

def graphicSequence(sequence):
    if sequence[0] == 0:
        return True
    else:
        if sequence[-1] < 0:
            return False
        else:
            if len(sequence) < sequence[0] + 1 : 
                return False
            else:
                return graphicSequence(havelHakimi(sequence))

# <codecell>

graphicSequence([3, 2, 3, 2, 1, 1])

# <codecell>

graphicSequence([2,2,2,2,3,3])

# <codecell>

graphicSequence([1, 0])

# <codecell>

graphicSequence([0])

# <codecell>

graphicSequence([1])

# <codecell>

graphicSequence([2,2,2,2])

# <codecell>



"""The following is an implementation of a recursive algorithm
based on a result of Havel(1955) and Hakimi(1961) that decides 
whether a non-increasing sequence of non-negative integers 
is a graphic sequence.

A graphic sequence is a sequence of integers that is the 
degree sequence of some simple graph.

The degree sequence of a graph is the sequence formed by arranging
the graph's vertex degrees in non-increasing order.

Reference: Graph Theory and Its Applications, 2nd edition by Gross and Yellen."""
	
def havel_hakimi(sequence):
    """Prepares the "next" sequence for graphic_sequence() to test.
    
    Note: 
    	Returns a sequence that is graphic if and only if 
    	the input sequence is graphic. This is necessary for 
    	recursion in the graphic_sequence() module.
    
    args:
    	sequence: a list of integers
    
    returns:
    	another sequence
    """
    n = sequence[0] + 1
    for i in range(1, n):
        sequence[i] = sequence[i] - 1
    del sequence[0]
    return sorted(sequence, reverse=True)


def graphic_sequence(sequence):
    """Determines whether sequence is a graphic sequence.
    
    args:
    	sequence: a list of integers
    
    returns:
    	True if sequence is a graphic sequence
    	False if sequence is not a graphic sequence
    """
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
                
if __name__ == "__main__":
	
	# some examples for testing
	
	graphic_sequence([3, 2, 3, 2, 1, 1]) #True
	
	graphic_sequence([2,2,2,2,3,3]) #True
	
	graphic_sequence([1, 0]) #False
	
	graphic_sequence([0]) #True
	
	graphic_sequence([1]) #False
	
	graphic_sequence([2,2,2,2]) #True




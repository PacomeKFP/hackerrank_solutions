def flippingBits(n):
    """return 2**32-1-n"""
    # binary_transcription:
    rests = []
    quotient = n
    # converting in simple binary
    while quotient > 1:
        rests.append(quotient % 2)
        quotient = quotient // 2 
    rests.append(1)
    
    # adding zero to complete on 32 bits
    rests += [0]*(32-len(rests))
    # interchanging bites in rests
    for i in range(len(rests)):
        rests[i] = 1 if rests[i] == 0 else 0

    # returning the int to the decimal   base
    nbr = sum([rests[i]*(2**i)for i in range(len(rests)) ])
    return nbr

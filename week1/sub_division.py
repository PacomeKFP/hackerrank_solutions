def birthdays(s, d, m):
    
    nbr = 0
    for i in range(len(s)-m+1):
        segment = s[i: i+m]
        if sum(segment) == d:
            nbr += 1
    
    return nbr

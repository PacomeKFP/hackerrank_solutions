def timeConversion(s: str):
    # Write your code here
    is_morning = (s.count('AM') >= 1)

    # decompose the time:
    decomposition = list(map(int, [s[0:2], s[3:5], s[6:8]]))

    if is_morning:
        decomposition[0] %= 12
    else:
        decomposition[0] %= 12
        decomposition[0] += 12   
    result = ':'.join(str('%.2i' % part) for part in decomposition)
    return result

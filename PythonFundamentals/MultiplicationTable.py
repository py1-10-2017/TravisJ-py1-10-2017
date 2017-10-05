l = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for i in range(0, len(l)):
    result = []
    if i == 0:
        result.append('x  ')
    elif len(str(i)) == 1:
        result.append(str(i) + "  ")
    elif len(str(i)) == 2:
        result.append(str(i) + " ")

    for x in range(1, len(l)):
        num = l[i] * l[x]
        if len(str(num)) == 1:
            result.append("  " + str(num))
        elif len(str(num)) == 2:
            result.append(" " + str(num))
        else:
            result.append(str(num))
    print ' '.join(y for y in result)

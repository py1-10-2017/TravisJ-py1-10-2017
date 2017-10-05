def odd_even(num1, num2):

    for i in range(num1, num2):
        if i % 2 == 0:
            print "Number is " + str(i) + ". This is an even number."
        else:
            print "Number is " + str(i) + ". This is an odd number."


#odd_even(1, 2000)


a = [2, 4, 10, 16]


def multiply(lst, mult):
    newLst = []
    for i in range(0, len(lst)):
        newLst.append(lst[i] * mult)
    return newLst


b = multiply(a, 5)
print b

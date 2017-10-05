num = 10
perfect_square_arr = []
while num * num < 100000:
    perfect_square_arr.append(num * num)
    num += 1

for x in xrange(100, 1000):
    # print x
    found = False
    for i in xrange(0, len(perfect_square_arr)):
        if perfect_square_arr[i] == x:
            found = True
    if found == True:
        print x, "bar"

    prime = True
    for i in xrange(2, x / 2):
        if x % i == 0:
            prime = False
    if prime == True:
        print x, "foo"

    if prime == False and found == False:
        print x, "foobar"

l = ['magical', 'unicorns']
#l = [2, 3, 1, 7, 4, 12]
#l = ['magical unicorns', 19, 'hello', 98.98, 'world']
length = len(l)
strings = ""
numbers = []

for i in range(0, length):
    if type(l[i]) is int:
        numbers.append(l[i])
    if type(l[i]) is str:
        strings += l[i] + " "

if len(strings) > 0 and len(numbers) > 0:
    print "The list you entered is of mixed type."
    print "Strings:", strings
    print "Numbers:", sum(numbers)
elif len(strings) > 0 and len(numbers) == 0:
    print "The list you entered is of type string."
    print "Strings:", strings
elif len(strings) == 0 and len(numbers) > 0:
    print "The list you entered is of type int."
    print "Numbers:", sum(numbers)

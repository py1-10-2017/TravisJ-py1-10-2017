# Test case 1
# list_one = [1, 2, 5, 6, 2]
# list_two = [1, 2, 5, 6, 2]

# Test case 2
# list_one = [1, 2, 5, 6, 5]
# list_two = [1, 2, 5, 6, 5, 3]

# Test case 3
# list_one = [1, 2, 5, 6, 5, 16]
# list_two = [1, 2, 5, 6, 5]

# Test case 4
list_one = ['celery', 'carrots', 'bread', 'milk']
list_two = ['celery', 'carrots', 'bread', 'cream']

if sorted(list_one) == sorted(list_two):
    print "Lists are the same."
else:
    print "Lists are different."

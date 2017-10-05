# Find and Replace:
words = "It's thanksgiving day. It's my birthday, too!"

print words.find('day', 1)
print words.replace('day', 'month', 1)

#Min and Max
x = [2, 54, -2, 7, 12, 98]
print min(x)
print max(x)

#First and Last
x = ["hello", 2, 54, -2, 7, 12, 98, "world"]
print x[0]
print x[len(x) - 1]

# New list
x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
x = sorted(x)
a = x[:len(x) / 2]
b = x[len(x) / 2:]

b.insert(0, a)

print b

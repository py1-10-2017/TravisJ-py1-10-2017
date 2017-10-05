a = [4, 6, 1, 3, 5, 7, 25]
b = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]


# Part 1
def draw_stars(lst):
    for i in range(0, len(lst)):
        s = ""
        for x in range(lst[i]):
            s += "*"
        print s


# Part 2
def draw_stars_p2(lst):
    for i in range(0, len(lst)):
        s = ""
        if type(lst[i]) == str:
            for x in range(len(lst[i])):
                s += lst[i][0].lower()
            print s

        elif type(lst[i]) == int:
            for x in range(lst[i]):
                s += "*"
            print s


draw_stars(a)
draw_stars_p2(b)

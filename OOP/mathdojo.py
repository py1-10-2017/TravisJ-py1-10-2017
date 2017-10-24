class MathDojo(object):
    def __init__(self):
        self.total = 0

    def add(self, *args):
        local_total = 0
        for arg in args:
            if type(arg) == list or type(arg) == tuple:
                lst_sum = sum(arg)
                local_total += lst_sum
            else:
                local_total += arg
        self.total += local_total
        return self

    def subtract(self, *args):
        local_total = 0
        for arg in args:
            if type(arg) == list or type(arg) == tuple:
                lst_sum = sum(arg)
                local_total += lst_sum
            else:
                local_total += arg
        self.total -= local_total
        return self

    def result(self):
        print self.total


# md = MathDojo()

# md.add(2).add(2, 5).subtract(3, 2).result()

md = MathDojo()

md.add([1], 3, 4).add([3, 5, 7, 8], [2, 4.3, 1.25]
                      ).subtract(2, (2, 3), [1.1, 2.3]).result()

class Product(object):
    def __init__(self, item_name, weight, brand, cost):
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"

    def add_tax(self, decimal):
        tax = decimal * self.cost
        self.price = tax + self.cost
        return self

    def sell(self):
        self.status = "sold"
        return self

    def return_item(self, reason):
        if reason == "returned in box":
            self.status = "for sale"
            return self
        if reason == "box damaged":
            discount = self.price * .2
            self.price = self.price - discount
            self.status = "for sale"
            return self
        if reason == "defective":
            self.price = 0
            self.status = "defective"
            return self

    def display_info(self):
        print "Price: ", self.price
        print "Item:", self.item_name
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Cost:", self.cost
        print "Status:", self.status
        print "---------------------"


gold = Product('gold', '1lb', 'Goldfinger', 100)

# gold.add_tax(.10).sell().display_info()

# gold.return_item('defective').display_info()

#gold.add_tax(.1).sell().return_item('box damaged').display_info()
gold.add_tax(.1).sell().display_info()

gold.add_tax(.1).sell().return_item('returned in box').display_info()

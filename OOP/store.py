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


class Store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner

    def add_product(self, product):
        self.products.append(product)
        return self

    def remove_product(self, product_name):
        self.products.remove(product_name)
        return self

    def inventory(self):
        for product in self.products:
            print "Product name:", product.item_name
            print "Weight:", product.weight
            print "Brand:", product.brand
            print "Cost:", product.cost
            print "----------------"


macbook = Product("MacBook", "2lbs", "Apple", 2500)
xps = Product("XPS13", "1.75lbs", "Dell", 1350)
yoga = Product("Yoga", "2.1lbs", "Lenovo", 899)
alienware = Product("Alienware 17", "9lbs", "Dell", 3499)


store_1 = Store([macbook, xps], "Seattle, WA", "Travis")

store_2 = Store([yoga, alienware], "Snoqualmie, WA", "Rebecca")

# store_1.add_product(yoga).inventory()

# store_1.remove_product(xps).inventory()

# store_2.inventory()

store_2.add_product(macbook).remove_product(yoga).inventory()

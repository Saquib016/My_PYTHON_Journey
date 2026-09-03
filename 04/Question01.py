class Products:
    count  = 0
    def __init__(self,name,price):
        self.name = name
        self.price= price
        Products.count+=1
    def get_count(self):
        print(f"Totel Item Created = {self.count}")
    def get_info(self):
        print(f"price of {self.name} is {self.price}")
    @staticmethod

    def discount(price,disc):
        disc = price - price*(disc/100)
        print(f"Discounted Price = {disc}")
p1 = Products("Phone",1000)
p1.get_info()
p1.get_count()
p1.discount(10000,12 )
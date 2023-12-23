class encap():
    def __init__(self):
        self.price=100 #price is a data

    def maxprice(self):
        print("The max price is {}".format(self.price))
    def setprice(self,price):
        self.price=price

ram=encap()
ram.price=200
print(ram.price)

ram.maxprice()
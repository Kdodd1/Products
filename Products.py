class products:
    def __init__(self, price, itemName, weight, brand, status="for sale"):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        self.status = status
        
    def sell(self):
        self.status = 'sold'
        return self
        
    def addTax(self, tax):
        self.price = tax + self.price
        return self
            
    def returnItem(self, reasonForReturn):
        if reasonForReturn == 'like new':
            self.status = 'for sale'
        if reasonForReturn == 'defective':
            self.status = 'defective'
            self.price = 0
        if reasonForReturn == 'opened':
            self.status = "used"
            self.price = self.price-(self.price *.2)
        return self
            
    def displayInfo(self):
        print('Item: ' + self.itemName + "\nCost: $" + str(self.price) + "\nWeight: " + str(self.weight) + "lbs" "\nBrand: " + 
              self.brand + "\nStatus:" + self.status)

#Example input
banana = products(2, 'banana', .25, "Wal-mart")
tv = products(1000, 'tv', 20.2, "Sony")

banana.addTax(.25).sell().displayInfo()
tv.addTax(20.).returnItem('opened').displayInfo()



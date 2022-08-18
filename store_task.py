class Products:
    def __init__(self):
        prod_ids = ''
        names = ''
        price = 0
        stock = 0
        self._prod_id = prod_ids
        self._name = names
        self._price = price
        self._stock = stock

    def get_items(self):
        print(f"Prod ID -- {self._prod_id},\
                Prod Name -- {self._name},\
                Prod Price -- {self._price}$,\
                Prod Qnt -- {self._stock}KG")

    def set_items(self):
        self._prod_id = input("Enter Id : ")
        self._name = input("Enter Name : ").title()
        self._price = int(input("Enter Price : "))
        self._stock = int(input("Enter Quantity : "))

    def search_by_id(self, prod_ids):
        if self._prod_id == prod_ids:
            return True
        else:
            return False

    def search_by_name(self, names):
        if self._name == names.title():
            return True
        else:
            return False

    def sell(self):
        print("\n***** Sell *****\n")
        print("Quantity of Product in stock is:", self._stock)
        qnt = int(input("Enter Qty:"))
        if self._stock >= qnt:
            amt = qnt * self._price
            print("\nYour Amount:", amt, "$\n")

            self._stock -= qnt
        else:
            print("\nLess Stock\n")

    def purchase(self):
        print("\n***** Purchase *****\n")
        qnt = int(input("Enter Qty of Product You Want To Purchase: "))
        self._stock += qnt


n = int(input("Enter Total Products: "))
stock_list = []
for i in range(n):
    prod_list = Products()
    prod_list.set_items()
    stock_list.append(prod_list)

while True:
    print("\nYour Choice\n\n1.Show All Products\n2.Search By ID\n3.Search By Name\n4.Sell\n5.Purchase\n6.Exit")
    ch = int(input("\nEnter Your Choice: "))
    if ch == 1:
        for c in stock_list:
            c.get_items()

    elif ch == 2:
        prod_id = input("Enter Product ID for Search: ")
        found = False
        for c in stock_list:
            found = c.search_by_id(prod_id)
            if found:
                c.get_items()
                break
        if not found:
            print("\nRecord Not Found..")

    elif ch == 3:
        name = input("Enter Product Name: ")
        count = 0
        for c in stock_list:
            found = c.search_by_name(name)
            if found:
                c.get_items()
                count += 1

        if count == 0:
            print("Product Not Found..")
        else:
            print("Product Found: ", count)

    elif ch == 4:
        sell_item = input("Enter product name: ")
        for c in stock_list:
            found = c.search_by_name(sell_item)
            if found:
                c.sell()
                c.get_items()
            else:
                print("No product!")

    elif ch == 5:
        name = input("Enter Product Name You Want To Purchase: ")
        for c in stock_list:
            found = c.search_by_name(name)
            if found:
                c.purchase()
                c.get_items()
            else:
                print("Product Not Found")

    elif ch == 6:
        break
    else:
        print("Invalid Choice")

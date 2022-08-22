import shelve
from tabulate import tabulate


class Products:
    def __init__(self, sku, prod_name,
                 price, pay_price, stock):
        self.sku = sku
        self.prod_name = prod_name
        self.price = price
        self.pay_price = pay_price
        self.stock = stock

    def __repr__(self):
        with shelve.open("products.db", writeback=True) as db_prod:
            table = []
            headers = ['Prod SKU', 'Prod Name',
                       'Prod Price', 'Pay Price', 'Stock']
            for pr in db_prod.values():
                table.append([pr.sku, pr.prod_name,
                              pr.price, pr.pay_price, pr.stock])

        return tabulate(table, headers, tablefmt="fancy_grid",
                        stralign="left", numalign="left")

# class Sell:
#     def __init__(self, sku, prod_name, price, pay_price, stock):
#         self.product = Products(sku, prod_name,
#                                 price, pay_price, stock)
#
#     def __repr__(self):
#         with shelve.open("sell.db", writeback=True) as db_sell:
#             db_sell["stock"] = self.product.stock
#             table = []
#             headers = ['PRODUCT sku', 'PRODUCT name',
#                        'PRODUCT price', 'PRODUCT pay_price', 'stock']
#             for b in db_prod.values():
#                 table.append([b.sku, b.name,
#                               b.price, b.pay_price, b.stock])
#
#         return tabulate(table, headers, tablefmt="fancy_grid",
#                         stralign="left", numalign="right")


class Stock:
    def __init__(self):
        self.db_prod = shelve.open("products.db", writeback=True)

    def add_prod(self):
        sku = input("Enter Prod SKU: ")
        prod_name = input("Enter Prod Name: ")
        price = input("Enter Prod Price: ")
        pay_price = input("Enter Pay Price: ")
        stock = input("Enter Qty: ")
        products = Products(sku, prod_name,
                            price, pay_price, stock)
        self.db_prod[products.sku] = products
        return "Product was successfully added."

    def search_prod(self):
        name = input("Prod Name: ")
        count = 0
        for pr in self.db_prod.values():
            if name == pr.prod_name:
                count += 1

        if count == 0:
            print(f'No product found with "{name}" name!')
        else:
            print(f'Found {count} product with "{name}" name!')

        table = []
        headers = ['SKU', 'Prod Name',
                   'Prod Price', 'Pay Price', 'Qty']
        for pr in self.db_prod.values():
            if name == pr.prod_name:
                table.append([pr.sku, pr.prod_name,
                              pr.price, pr.pay_price, pr.stock])

        return tabulate(table, headers, tablefmt="fancy_grid",
                        stralign="left", numalign="left")

    # def add_sell_product(self):
    #     name = input("name: ")
    #     stock = int(input("Qty: "))
    #     for pr in self.db_prod.values():
    #         print("ok")
    #         if name == pr.name and pr.stock >= stock:
    #             print("ok")
    #             self.db_prod[pr.name] = Sell(stock)
    #
    #             # self.db_prod[pr.sku] = \
    #             #     Product(pr.sku, pr.name,
    #             #           pr.price, pr.pay_price, pr.stock)
    #             print(f'The sell was successfully implemented. Total cost: ${int(stock) * int(pr.pay_price)}')
    #             break
    #     else:
    #         return "This Product is not available now."

    def exit_func(self):
        self.db_prod.close()
        return exit()

    def show_menu(self):
        return ("a   - Add or update product\n"
                "s   - Search product\n"
                # "sell   - Sell product\n"
                "x   - Exit")

    def menu(self):
        all_actions = {
            "a": self.add_prod,
            "s": self.search_prod,
            # "sell": self.add_sell_product,
            "x": self.exit_func}

        return all_actions.get(input("Please choose one of the these actions: "), lambda: "Invalid input!")()


if __name__ == '__main__':
    b = Stock()
    while True:
        print(b.show_menu())
        print(b.menu())

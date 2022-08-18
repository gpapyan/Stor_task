items = []

while True:
    print("\nYour Choice\n\n1.Show All Products\n2.Add Product\n3.Purchase\n4.Search\n5.Exit")
    opt = input('\nEnter OPT: ')

    if opt == '1':
        print(f"Total stock is {len(items)}")
        while len(items) != 0:
            print('Available items.')
            for item in items:
                for key, value in item.items():
                    print(f"{key} : {value}")
            break

    elif opt == '2':
        item = {}

        item['name'] = input('Enter Prod Name: ').lower()

        while True:
            try:
                item['qty'] = int(input('Enter Qty of Prod: '))
                break
            except ValueError:
                print('Enter Valid Quantity')

        while True:
            try:
                item['price'] = int(input('Enter Price of Prod: '))
                break
            except ValueError:
                print('Enter Valid Price')
        print('Prod has been added')
        items.append(item)
        print(items)

    elif opt == '3':
        print(items)
        purchases = input('What item you want to purchase enter Name: ')
        for item in items:
            if purchases.lower() == item['name'].lower():
                if item['qty'] != 0:
                    print(f"Your product price is {item['price']} at checkout")
                    item['qty'] -= 1
                else:
                    print('Out of stock')
    elif opt == '4':
        found = input('Enter Searching Prod Name: ')
        for item in items:
            if found.lower() == item['name'].lower():
                print(f'The {found} Prod Was Found ')
                print(item)
            else:
                print('Prod Not Found')

    elif opt == '5':
        print('\nYou Enter Exit Code\n')
        break
    else:
        print("Error - Program is Closed")
        break

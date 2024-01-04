items = [
    {
        'code':1,
        'name':'crisp_1',
        'price':0.50
    },
    {
        'code':2,
        'name':'crisp_2',
        'price':0.50
    },
    {
        'code':3,
        'name':'chocolate_1',
        'price':0.75
    },
    {
        'code':4,
        'name':'chocolate_2',
        'price':0.80
    },
    {
        'code':5,
        'name':'sweets_1',
        'price':0.40
    },
    {
        'code':6,
        'name':'sweets_2',
        'price':0.60

    },  
    {
        'code':7,
        'name':'sandwich_1',
        'price':1.20
    },
    {
        'code':8,
        'name':'sandwich_2',
        'price':1.40
    },
    {
        'code':9,
        'name':'drink_1',
        'price':0.95
    },
    {
        'code':10,
        'name':'drink_2',
        'price':1.50
    },
]

is_quit = False
item = ''

while is_quit == False:
    print("Welcome to the vending machine")
    for i in items:
        print(f"Item Name: {i['name']} - Price: {i['price']} - code: {i['code']}")

    query = int(input("Enter the code number of the item you want to get: "))
    for i in items:
        if query == i['code']:
            item = i
    if item == '':
        print('INVALID CODE')
    else:
        print(f"Great, {item['name']} will cost you {item['price']} dollars")

        price = int(input(f"Enter {item['price']} dollars to purchase: "))
        if price == item['price']:
            print(f"Thank you for buying here is your {item['name']}")
        elif price > item['price']:
            print(f"Thank you for buying here is your {item['name']}")
            print(price - item['price'])
            print("your change is", price - item['price'])
        else:
            print(f"Please enter only {item['price']} dollars")

    query = input("To quit the machine enter q and to continue buying enter anything: ")
    if query == 'c':
        is_quit = False
    else:
        is_quit = True
    print('')
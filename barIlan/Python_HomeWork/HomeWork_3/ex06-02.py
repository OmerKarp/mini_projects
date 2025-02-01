import pandas as pd
import numpy as np


class GroceryShopping:
    def __init__(self, name):
        self.my_shop_items = 0
        self.my_bill = 0
        self.name = name
        print(f"Welcome to my store {self.name}")

    def shop_items(self):
        my_shop = {'item': ['soap', 'toothbrush', 'apple', 'kiwi', 'water', 'juice', 'milk', 'coffee', 'chips', 'eggs'],
                   'amount': [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
                   'price': [2, 2.3, 1.5, 3.4, 2, 4, 3, 7, 2, 4.5]}
        df = pd.DataFrame(my_shop)
        df = df.set_index('item')
        self.my_shop_items = df


class Client(GroceryShopping):
    def __init__(self, name):
        super().__init__(name)

    def delete_items(self, item_added, item_amount):
        self.my_shop_items.loc[item_added, 'amount'] -= item_amount

    def bill(self, item_added, item_amount):
        self.my_bill += self.my_shop_items.loc[item_added, 'price'] * item_amount

    def buy(self):
        self.shop_items()
        while True:
            buy = input('do you want to buy?(yes/no)')
            if buy.lower() == 'no':
                print(f'\nYour bill is: {self.my_bill}$')
                print('Thank you for shopping with us')
                break
            elif(buy.lower()=='yes'):
                print('\n')
                print(self.my_shop_items)
                item_added = input('\nAdd an item:')
                if(item_added not in self.my_shop_items.index):
                    print("you entered an item that is not on the menu...please try again")
                    continue
                item_amount = int(input("Add quantity: "))
                if(self.my_shop_items.loc[item_added, 'amount']<item_amount):
                    print(f"we dont have enough of {item_added} for your request...please try again")
                    continue
                self.delete_items(item_added.lower(), item_amount)
                self.bill(item_added.lower(), item_amount)
                print(f"added {item_amount} of {item_added} succsesfully!")
            else:
                print("you need to enter yes OR no, Try again\n")



class Manager(GroceryShopping):
    def __init__(self, name):
        super().__init__(name)
        self.shop_items()

    def addItem(self, itemName, itemAmount, itemPrice):
        new_row = {'item': itemName, 'amount': itemAmount, 'price': itemPrice}
        new_df = pd.DataFrame([new_row])
        new_df = new_df.set_index('item')
        self.my_shop_items = pd.concat([self.my_shop_items, new_df])

    def refillItem(self,item,amountAdded):
        self.my_shop_items.loc[item,'amount']=self.my_shop_items.loc[item,'amount']+amountAdded
    def changePrice(self,item,newPrice):
        self.my_shop_items.loc[item, 'price'] = newPrice
    def deleteAnItem(self,itemDroped):
        self.my_shop_items = self.my_shop_items.drop(axis='index',index=itemDroped)


omer = Manager("omer")
omer.deleteAnItem('eggs')
omer.refillItem('milk',2)
omer.changePrice('milk',12)
omer.addItem('gavish',10,10)
print(omer.my_shop_items)

doron = Client("Doron")
doron.buy()

class Item:
    def __init__(self, name:str, price:float, quantity=0):
        #Chek price and quantity
        assert price >=0, f"Il prezzo {price} è minore di zero!"
        assert price >=0, f"La quantità {quantity} è minore di zero!"

        self.name=name
        self.price=price
        self.quantity=quantity

    def calculate_total_price(self):
        return self.price * self.quantity
    
# How to create an instance of a class
item1 = Item("Phone",100,5)
item2 = Item("Laptop",1000,3)

# Calling methods from instances of a class:
print(item1.calculate_total_price())
print(item2.calculate_total_price())
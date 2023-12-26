class Item:
    pay_rate = 0.8 # The pay rate after 20_# discount
    def __init__ (self, name:str, price: float, quantity = 0):
        # Run validations to received arguments
        assert price >= 0, f"Price {price} is not greater or equal to zero!"
        assert quantity >= 0 , f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item("Phone", 50, 3)
item2 = Item("Laptop", 250, 4)

# Item 1
print("Quantity = ", item1.quantity)
print(f"Current Price = {item1.price}")
print("Discount = ", item1.pay_rate)
item1.apply_discount()  # Apply discount
print(f"Price minus discount = {item1.price}")  # New price
print("Total amount = ", item1.calculate_total_price())  # Calculate Price
print("______________________________________________")

# Item 2
item2.pay_rate = 0.5
print("Quantity = ", item2.quantity)
print(f"Current Price = {item2.price}")
print("Discount = ", item2.pay_rate)
item2.apply_discount()  # Apply discount
print(f"Price minus discount = {item2.price}")  # New price
print("Total amount = ", item2.calculate_total_price())  # Calculate Price



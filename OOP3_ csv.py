import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20_# discount
    all = []
    def __init__ (self, name:str, price: float, quantity = 0):

        # Run validations to received arguments
        assert price >= 0, f"Price {price} is not greater or equal to zero!"
        assert quantity >= 0 , f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)  # conver into a list

            # Instantiate the instances
            for item in items:
                Item(
                    name=item.get('name'),
                    price=float(item.get('price')),
                    quantity=float(item.get('quantity')),
                )
    @staticmethod
    def is_integer(num):
        # we will count the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):   #if the num is an instance of a float
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    # Representing the object when printing in the console
    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"


class Phone(Item):
    all = []
    def __init__(self, name: str, price: float, quantity=0, broken_phones = 0):
        # Call to super function to have access to all attributes / methods
        super().__init__(name, price, quantity)

        # Run validations to received arguments
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones

        # Actions to execute
        Phone.all.append(self)

Item.instantiate_from_csv()
print(Item.all)

phone1 = Phone('jscPhoneV10', 500, 5, 1)
print(phone1.calculate_total_price())
phone2 = Phone('jscPhoneV20', 700, 5, 1 )

print(Item.all)

#
# https://www.youtube.com/watch?v=Ej_02ICOIgs
#  Hour 1:27

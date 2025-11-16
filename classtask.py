class temperature:
    def __init__(self, celsius):
        self.celsius = float(celsius)   # Convert to float
        
    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32
    
    def to_kelvn(self):
        return self.celsius + 273.15

user_input = input("Enter Celsius: ")
obj = temperature(user_input)

print("Fahrenheit:", obj.to_fahrenheit())
print("Kelvin:", obj.to_kelvn())



class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
class cartitem(product):
    def __init__(self, product, quantity):
        self.product = product
        self.quanitity = quantity
        
    def total_item(self):
        return self.product.price * self.quanitity

p1 = product("Shirt", 1500)
item1 = cartitem(p1, 3)

print("Product Name:", item1.product.name)
print("Product Price:", item1.product.price)
print("Quantity:", item1.quanitity)
print("Total Price:", item1.total_item())


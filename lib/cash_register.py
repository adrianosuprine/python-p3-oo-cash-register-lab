#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction_price = 0
    
  def add_item(self,title,price,quantity=1):
    
    transaction_price = price * quantity
    self.total += transaction_price
    self.last_transaction_price = transaction_price 
    # extend mothod used for appending an item to the list
    self.items.extend([title] * quantity)
    
  def apply_discount(self):
    if self.discount > 0 :
      
      self.total -= (self.total * self.discount) // 100
          
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")
  
  def void_last_transaction(self):
      if self.last_transaction_price > 0:
        self.total -= self.last_transaction_price
       
        
        self.items.pop()
        
      else :
        print("No transactions")
          
# Create an instance of the CashRegister class
my_cash_register = CashRegister(discount=10)

# Add items to the register
my_cash_register.add_item("Justin's Peanut Butter Cups", 2, 2)
my_cash_register.add_item("Peanut Butter ", 2.5, 2)


# Apply discount
my_cash_register.apply_discount()

# Void last transaction
my_cash_register.void_last_transaction()

# Print the total
print(f"Cash Register: ${my_cash_register.items}")
print(f"Current total: ${my_cash_register.total}")
  

  
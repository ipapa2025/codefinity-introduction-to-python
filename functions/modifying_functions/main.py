def apply_discount(price, discount= 0.05):
    discount_price=price*(1-discount)
    return discount_price

def apply_tax(price, tax=0.07):
    tax_amount = price*(1+tax)
    return tax_amount

def calculate_total(price, discount=0.05, tax=0.07): 
    discounted = apply_discount(price, discount)
    total = apply_tax(discounted,tax)
    return total

total_price = calculate_total(120)

print(f"Total cost with default discount and tax: ${total_price}")

total_price = calculate_total(price=100,discount=0.10,tax=0.08)
    
print(f"Total cost with custom discount and tax: ${total_price}")    
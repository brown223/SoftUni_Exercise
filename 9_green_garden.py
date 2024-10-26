area = float(input())

price_per_square_meter = 7.61

total_price = area * price_per_square_meter
discount = total_price * 0.18

print(f"The final price is: {total_price - discount} lv.")
print(f"The discount is: {discount} lv.")

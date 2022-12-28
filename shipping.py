weight = 4.8

#Ground shipping
ground_flat_charge = 20.00
if(weight <= 2):
  price_per_pound = 1.50
elif(weight <= 6):
  price_per_pound = 3.00
elif(weight <= 10):
  price_per_pound = 4.00
else:
  price_per_pound = 4.75

total_ground_cost = ground_flat_charge + (price_per_pound * weight)
print(f'{total_ground_cost:.2f}')

#premium ground shipping
premium_ground_shipping_cost = 125.00
print("Ground Shipping Premiunm $",f'{premium_ground_shipping_cost:.2f}')
print()


#Drone Shipping
if(weight <= 2):
  price_per_pound = 4.50
elif(weight <= 6):
  price_per_pound = 9.00
elif(weight <= 10):
  price_per_pound = 12.00
else:
  price_per_pound = 14.25

drone_cost = price_per_pound * weight
print(f'{drone_cost:.2f}')
# Ben krehbiel
# 02/04/2025
# Usps 

def weight_conversion(weight):
    if weight <= 2:
        shipping_cost = weight * 1.50  
    elif weight > 2 and weight <= 6: 
        shipping_cost = weight * 3.00  
    elif weight > 6 and weight <= 10:
        shipping_cost = weight * 4.00  
    else:
        shipping_cost = weight * 4.75  

    return shipping_cost  

# Mainline
weight = float(input("Enter Weight: "))
shipping_cost = weight_conversion(weight)
print("Shipping charge: $", format(shipping_cost, ".2f"))
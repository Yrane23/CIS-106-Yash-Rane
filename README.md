# CIS-106-Yash-Rane
ps3p1
#input phase
exam_score_1 = float(input("Enter exam score 1: "))
exam_score_2 = float(input("Enter exam score 2: "))


#process phase
weighted_score_1 = exam_score_1 * 0.6
weighted_score_2 = exam_score_2 * 0.4
total_score = weighted_score_1 + weighted_score_2

#output phase
print("Total score", total_score)

PS3p2
#input phase
purchase_price_per_share = float(input("Enter the purchase price per share: "))
current_stock_price = float(input("Enter the current stock price: "))
quantity_of_stock = int(input("Enter the quantity of stock: "))


#process phase
purchase_value = purchase_price_per_share * quantity_of_stock
current_value = current_stock_price * quantity_of_stock
value_change = current_value - purchase_value


#output phase
print("Increase (or decrease) in value of the stock:", value_change)

PS3P3

#input phase 
total_meal_cost = float(input("Enter the total for the meal: "))

#15% tip 
tip_15_percent = total_meal_cost * 0.15
total_with_tip_15_percent = total_meal_cost + tip_15_percent

#output for 15% tip
print("\nWith 15% Tip:")
print("Total:", format(total_meal_cost, '.2f'))
print("Tip:", format(tip_15_percent, '.2f'))
print("Total with Tip:", format(total_with_tip_15_percent, '.2f'))


#18% tip
tip_18_percent = total_meal_cost * 0.18
total_with_tip_18_percent = total_meal_cost + tip_18_percent

#output for 18% tip
print("With 18% Tip:")
print("Total:", format(total_meal_cost, '.2f'))
print("Tip:", format(tip_18_percent, '.2f'))
print("Total with Tip:", format(total_with_tip_18_percent, '.2f'))


#20% tip
tip_20_percent = total_meal_cost * 0.20
total_with_tip_20_percent = total_meal_cost + tip_20_percent

#output for 20% tip
print("With 20% Tip:")
print("Total:", format(total_meal_cost, '.2f'))
print("Tip:", format(tip_20_percent, '.2f'))
print("Total with Tip:", format(total_with_tip_20_percent, '.2f'))

PS3P4
#input phase
first_name = input("Enter first name: ")
steps_walked = int(input("Enter number of steps walked in a day: "))

#process phase 
calories_burned = steps_walked * 0.25

#output phase
print("First name:", first_name)
print("Calories burned:", calories_burned)

PS3P5
#input phase 
fixed_costs = float(input("Enter fixed costs: "))
price_per_unit = float(input("Enter price per unit: "))
cost_per_unit = float(input("Enter cost per unit: "))

#process phase
break_even_point = fixed_costs / (price_per_unit - cost_per_unit)

#output phase 
print("Break even point:", break_even_point)


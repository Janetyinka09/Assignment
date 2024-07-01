selling_price_of_good_1 = int(input(" enter your selling price for good 1")) 
selling_price_of_good_2 = int(input(" enter your selling price for good 2")) 
selling_price_of_good_3 = int(input(" enter your selling price for good 3")) 
selling_price_of_good_4 = int(input(" enter your selling price for good 4")) 
selling_price_of_good_5 = int(input(" enter your selling price for good 5")) 

cost_price_of_good_1 = int(22500)
cost_price_of_good_2 = int(5000)
cost_price_of_good_3 = int(90000) 
cost_price_of_good_4 = int(1900)
cost_price_of_good_5 = int(5900) 
total_selling_price = int(selling_price_of_good_1 + selling_price_of_good_2 + selling_price_of_good_3 + selling_price_of_good_4 + selling_price_of_good_5)
total_cost_price = int(cost_price_of_good_1 + cost_price_of_good_2 + cost_price_of_good_3 + cost_price_of_good_4 + cost_price_of_good_5) 

if total_selling_price > total_cost_price: 
    print("Profit") 
else: 
    print("Loss")
user_input = input(" select your card type .... 1) regular, 2) silver, 3)gold, 4) platinum: ") 
user_card1 = "R" 
user_card2 = "S" 
user_card3 = "G" 
user_card4 = "P" 
cost = int(input("enter the cost of the product")) 
silver_discount = int((5/100) * cost )
gold_discount = int((10/100) * cost )
platinum_discount = int((15/100) * cost) 
if cost>1000:
    print("you are to pay" , silver_discount) 
elif cost>2000:
    print("you are to pay" , gold_discount)
elif user_input == "1":
    user_card = user_card1 
    print("you are to pay" , cost) 
elif user_input=="2":
    user_card = user_card2
    print("you are to pay" , silver_discount) 
elif user_input=="3":
    user_card = user_card3
    print("you are to pay" , gold_discount) 
elif user_input == "4":
    user_card = user_card4
    print("you are to pay" , platinum_discount) 
else:
    print("your user type is not valid") 

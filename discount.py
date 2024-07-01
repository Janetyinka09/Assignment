user_input = input(" select your card type .... 1) regular, 2) silver, 3)gold, 4) platinum: ") 
user_card1 = "R" 
user_card2 = "S" 
user_card3 = "G" 
user_card4 = "P" 
cost = int(input("enter the cost of the product")) 
silver = int((5/100) * cost )
gold = int((10/100) * cost )
platinum = int((15/100) * cost)
if user_input == "1":
    user_card = user_card1 
    print("you are to pay" , cost) 
elif user_input=="2":
    user_card = user_card2
    print("you are to pay" , silver) 
elif user_input=="3":
    user_card = user_card3
    print("you are to pay" , gold) 
elif user_input == "4":
    user_card = user_card4
    print("you are to pay" , platinum) 
else:
    print("your user type is not valid") 
#code to know if a name starts with a capital letter or not 

user_name = input("Please input your name :")
first_letter = (user_name[0])
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
if first_letter in capital_letters:
    print("The first letter of your name starts with a Capital letter.")
else:
    print("The first letter of your name does not start with a Capital letter.")
essay = input("Enter your essay:") 
essay_count = essay.replace(" " , "").replace("," , "") .replace("." , "") 
number_of_words = len(essay) // 6
print(f"The number of words in your essay is {number_of_words} ")
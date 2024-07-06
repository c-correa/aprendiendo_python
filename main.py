#implementation the diferents list comprehenstions 

#1.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_v2 = [i ** 2 for i in range(len(numbers)) if i % 2 != 0]
print(numbers_v2)
#2.
text = ["hola", "como", "estas?"]
text_v2 = [i.upper() for i in text]
print(text_v2)
#3.
number_in_text = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]
converting_text_to_number = [+i for i in range(len(number_in_text))]
print(converting_text_to_number)

# Dictonary comprehenstions
#1.
dic = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
new_dic = { value: key for key, value in dic.items() }
print(new_dic)
#2.
converting_list_to_dic = { i: i **2  for i in range(len(numbers)) }
print(converting_list_to_dic)
#3.
dic_v2 = {"a":1, "b":2, "c":3, "d":4, "e":5}
filter = {key: value for key, value in dic_v2.items() if value > 4}
print(filter)

#combined
#1.

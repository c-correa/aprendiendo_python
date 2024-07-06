#implementation the diferents list comprehenstions 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
text = ["hola", "como", "estas?"]
number_in_text = ["1", "2", "3", "4", "9", "6", "7"]
dic = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 9}

#1.
numbers_v2 = [i ** 2 for i in range(len(numbers)) if i % 2 != 0]
print(numbers_v2)
#2.
text_v2 = [i.upper() for i in text]
print(text_v2)
#3.
converting_text_to_number = [+i for i in range(len(number_in_text))]
print(converting_text_to_number)

# Dictonary comprehenstions
#1.
new_dic = { value: key for key, value in dic.items() }
print(new_dic)
#2.
converting_list_to_dic = { i: i **2  for i in range(len(numbers)) }
print(converting_list_to_dic)
#3.
filter = {key: value for key, value in dic.items() if value > 4}
print(filter)

#combined
#1.
list_of_tuples = {(key, value) for key, value in dic.items()}
print(list_of_tuples)
#2.
list_to_dic = {text[i]: len(text[i]) for i in range(len(text))}
print(list_to_dic)
#3.
converting_string = [str(value) for key, value in dic.items()]
print(converting_string)
# Or
converting_string = [str(value) for value in dic.values()]
print(converting_string)

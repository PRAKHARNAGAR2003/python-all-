lucky_number = [10,20,30,40,50]
names = ["Prakhar", "Minato", "Itachi","Jiraya"]
# print(names)
# names.extend(lucky_number) # it will join the the two lists .
# names.append("shisui") # it will add an item at the end of the list.
# names.insert(2,"Pain") # it will add the element at the mentioned index position.
# names.remove("jiraya") # it will remove the element which is mentioned.
# # names.clear() # It will give us an empty list.
# # names.pop() # it will remove any random element form the list.
# print(names.index("Minato")) # it will tell the index number of the value in the list.
# print(names.count("Pain")) # It will count the number of times any value is appeared in the list.

names.sort()
lucky_number.reverse()
names2 = names.copy()

print(lucky_number)
print(names2)

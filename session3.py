# print(2 * 2)
# print("hi " * 3)
# print(3 * "hi ")


shopping_list = []
shopping_list.append("mashroom")
shopping_list.append("paper")
print(shopping_list)

new_item = input("Enter the product's name: ")
shopping_list.append(new_item)
print(shopping_list)

print(shopping_list[1])
shopping_list[1] = "pen"
print(shopping_list)

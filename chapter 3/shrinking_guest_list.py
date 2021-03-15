list = ['Altria', 'Bradamante', 'Melt']
message = "I would like to invite you to dinner, "
print(message + list[0] + ', ' + list[1] + ' and ' + list[2])
print(f"It seems that {list[1]} couldn't make it")
not_available = list.pop(1)
list.insert(0, 'Hokusai')
list.insert(2, 'Kingprotea')
list.append('Tamamo')
print(message + list[0])
print(message + list[1])
print(message + list[2])
print(message + list[3])
print(message + list[4])

message2 = "I am very sorry, but I wouldn't be able to invite you for dinner, "
no_chair = list.pop(-1)
print(message2 + no_chair)
no_chair = list.pop(-1)
print(message2 + no_chair)
no_chair = list.pop(-1)
print(message2 + no_chair)

message3 = "You are still invited, "
print(message3 + f"{list[0]} and {list[1]}")
del list
print(list)
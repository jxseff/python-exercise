list = ['Altria', 'Bradamante', 'Melt']
message = "I would like to invite you to dinner, "
print(message + list[0] + ', ' + list[1] + ' and ' + list[2])
print(f"It seems that {list[2]} couldn't make it")
not_available = list.pop(2)
list.insert(0, 'Hokusai')
list.insert(2, 'Kingprotea')
list.append('Tamamo')
print(message + list[0])
print(message + list[1])
print(message + list[2])
print(message + list[3])
print(message + list[4])
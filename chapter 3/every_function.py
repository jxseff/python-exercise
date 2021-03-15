list = ['gbf', 'fgo', 'genshin', 'bandori', 'honkai', 'priconne']

sorted(list)
print(list[2])
sorted(list, reverse = True)
print(list[3])
list.sort()
print(list[1])
list.sort(reverse = True)
print(list[0])
list[0] = 'danmemo'
print(list)
list[-1] = 'sifas'
list.append('dragalia')
list.insert(3, 'exos')
del list[2]
removed = list.pop(1)
print(removed)
quit = 'danmemo'
list.remove(quit)
print(list)
print(len(list))
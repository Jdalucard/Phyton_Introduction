list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

list1.append(10)
print(list1)
list1.extend(list2)
print(list1)
list1.reverse()
print(list1)
print(len(list1))
order = list1.sort()
print(list1)
list1.insert(4, 100)
print(list1)
order2 = list1.sort(reverse=True)
print(list1)
list2.pop(1)
print(list2)
list1.pop(-1)
print(list1)
list1.remove(100)
print(list1)

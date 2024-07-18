#Convert the list [1, 2, 3, 4, 5] to [2, 4, 6, 8, 10] with list comprehension

li = [1,2,3,4,5]
li = [i*2 for i in li]
print(li)
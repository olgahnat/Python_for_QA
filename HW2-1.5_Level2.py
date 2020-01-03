from operator import add
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
#this code add lists elements
add_list1_list2 = list(map(add, list1, list2))
add_list3 = list(map(add, add_list1_list2, list3))
#print (unit_list)
list_all = list1 + list2 + list3
list_all.reverse()
print ("This is result of unioned lists in reversed order: \n", list_all, "\nThis is sum of all lists elements: \n",add_list3)
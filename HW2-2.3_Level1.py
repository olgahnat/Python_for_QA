def rem_list(list):
  """takes a list and returns a new list that contains all the elements
  of the first list minus all the duplicates"""
  fin_list = []

  for i in list:
    if i not in fin_list:
      fin_list.append(i)

  print(fin_list)


input_string = input("Enter a list numbers or elements separated by comma: ")
list = input_string.split(",")

rem_list(list)

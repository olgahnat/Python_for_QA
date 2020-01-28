def my_function(inp_string):
  """takes a comma-separated string and returns the last element (separated by the last comma)
  or the entire string, if there is no comma in it."""
  #search for character after last comma
  res = inp_string.split(',')[-1]
  if (res == None):
    print(inp_string)
  else:
    print(res)


inp_string = input('Entar a string: ')
my_function(inp_string)

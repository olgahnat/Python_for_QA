def my_function(inp_string):
  """takes a string and returns its first 10 characters concatenated with the last 10 characters"""
  first_10 = inp_string[0:10]
  last_10 = inp_string[len(inp_string) - 10:len(inp_string)]
  final = first_10 + last_10
  print(final)

inp_string = input('Entar a string to be concatenated: ')
my_function(inp_string)


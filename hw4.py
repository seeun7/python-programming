def rep_char(c,n):
  print(c*n)
name='Hello '+str(input('Input his/her name:'))+','
def draw_line_string(name):
  welcome='Welcome to Seoul.'
  d= len(name) if (len(name) > len(welcome)) else len(welcome)
  rep_char('-',d)
  print(name)
  print(welcome)
  rep_char('-',d)
draw_line_string(name)
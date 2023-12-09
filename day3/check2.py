def upleft(lines,x,y):
  if y == 0 or x == 0:
    return False
  if lines[y-1][x-1].isnumeric():
    
    print(lines[y-1][x-1])
    return True
  else:
    return False
    
def up(lines,x,y):
  if y == 0:
    return False
  if lines[y-1][x].isnumeric():
    print(lines[y-1][x])
    return True
  else:
    return False
    
def upright(lines,x,y):
  if y == 0 or x == 139:
    return False
  if lines[y-1][x+1].isnumeric():
    print(lines[y-1][x+1])
    return True
  else:
    return False
    
def left(lines,x,y):
  if x == 0:
    return False
  if lines[y][x-1].isnumeric():
    print(lines[y][x-1])
    return True
  else:
    return False
    
def right(lines,x,y):
  if x == 139:
    return False
  if lines[y][x+1].isnumeric():
    print(lines[y][x+1])
    return True
  else:
    return False
    
def downleft(lines,x,y):
  if y == 139 or x == 0:
    return False
  if lines[y+1][x-1].isnumeric():
    print(lines[y+1][x-1])
    return True
  else:
    return False
    
def down(lines,x,y):
  if y == 139:
    return False
  if lines[y+1][x].isnumeric():
    print(lines[y+1][x])
    return True
  else:
    return False
    
def downright(lines,x,y):
  if y == 139 or x == 139:
    return False
  if lines[y+1][x+1].isnumeric():
    print(lines[y+1][x+1])
    findrange(lines[y], x+1)
    return True
  else:
    return False

def findrange(line, x):
  if x == 0:
    for i in range(0, 2):
      print(i)
  elif x == 1:
    for i in range(-1, 2):
      print(i)
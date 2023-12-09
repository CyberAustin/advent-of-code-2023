nonos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

def upleft(lines,x,y):
  if y == 0 or x == 0:
    return False
  if lines[y-1][x-1] not in nonos:
    print(lines[y-1][x-1])
    return True
  else:
    return False
    
def up(lines,x,y):
  if y == 0:
    return False
  if lines[y-1][x] not in nonos:
    print(lines[y-1][x])
    return True
  else:
    return False
    
def upright(lines,x,y):
  if y == 0 or x == 139:
    return False
  if lines[y-1][x+1] not in nonos:
    print(lines[y-1][x+1])
    return True
  else:
    return False
    
def left(lines,x,y):
  if x == 0:
    return False
  if lines[y][x-1] not in nonos:
    print(lines[y][x-1])
    return True
  else:
    return False
    
def right(lines,x,y):
  if x == 139:
    return False
  if lines[y][x+1] not in nonos:
    print(lines[y][x+1])
    return True
  else:
    return False
    
def downleft(lines,x,y):
  if y == 139 or x == 0:
    return False
  if lines[y+1][x-1] not in nonos:
    print(lines[y+1][x-1])
    return True
  else:
    return False
    
def down(lines,x,y):
  if y == 139:
    return False
  if lines[y+1][x] not in nonos:
    print(lines[y+1][x])
    return True
  else:
    return False
    
def downright(lines,x,y):
  if y == 139 or x == 139:
    return False
  if lines[y+1][x+1] not in nonos:
    print(lines[y+1][x+1])
    return True
  else:
    return False
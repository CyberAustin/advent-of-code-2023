import re
from check2 import *

regex = re.compile("\d+")

def part1():
  total = 0
  
  with open("day3.txt", "r") as f:
  
    lines = f.readlines()

    for y in range(0,len(lines)):
      results = re.finditer(regex, lines[y])
      
      for result in results:
       
        try:
          for x in range(result.start(), result.end()):
            if upleft(lines,x,y) or up(lines,x,y) or upright(lines,x,y) or left(lines,x,y) or right(lines,x,y) or downleft(lines,x,y) or down(lines,x,y) or downright(lines,x,y):
              print(f"line: {str(y+1)}  off: {str(x)} s,f:{result.start()}, {result.end()} match: {result.group()}")
              with open("d3out.txt", "a") as out:
                out.write(f"line: {str(y+1)}  off: {str(x)} s,f:{result.start()}, {result.end()} match: {result.group()}\n")
              total += int(result.group())
              break
        except Exception as e:
          print(e)

  print(total)        

def part2():
  total = 0
  pairs = []
  with open("day3.txt", "r") as f:
    lines = f.readlines()
  
    for y in range(0,len(lines)):
      results = re.finditer(regex, lines[y])
  
      for result in results:
        for x in range(result.start(), result.end()):
          if upleft(lines,x,y) or up(lines,x,y) or upright(lines,x,y) or left(lines,x,y) or right(lines,x,y) or downleft(lines,x,y) or down(lines,x,y) or downright(lines,x,y):
            print(f"line: {str(y+1)}  off: {str(x)} s,f:{result.start()}, {result.end()} match: {result.group()}")
            total += int(result.group())
            break

  
  print(total)    
def part2():
  input = []

  with open("d1.txt", "r") as f:
    input = f.readlines()

  sum = 0
  a = 0
  b = 0
  for line in input:
      print(line)
      charcnt = 0
      #debuggin count, used to check the number of num-words matched in the statements below
      count = 0
      #iterates each line placing an int version of the number word before theword
      #maintains the order of the numbers in cases such as "twone", Twonine",etc
      for c in line:
          if line[charcnt: charcnt +3] == "one":
              line = line[:charcnt] + '1' + line[charcnt:]
              count += 1
              charcnt +=1
          if line[charcnt: charcnt +3] == "two":
              line = line[:charcnt] + '2' + line[charcnt:]
              count += 1
              charcnt +=1
          if line[charcnt: charcnt +5] == "three":
              line = line[:charcnt] + '3' + line[charcnt:]
              count += 1
              charcnt +=1
          if line[charcnt: charcnt +4] == "four":
              line = line[:charcnt] + '4' + line[charcnt:]
              count += 1
              charcnt +=1
          if line[charcnt: charcnt +4] == "five":
              line = line[:charcnt] + '5' + line[charcnt:]
              count += 1
              charcnt +=1
          if line[charcnt: charcnt +3] == "six":
              line = line[:charcnt] + '6' + line[charcnt:]
              count += 1
              charcnt +=1
          if line[charcnt: charcnt +5] == "seven":
              line = line[:charcnt] + '7' + line[charcnt:]
              count += 1
              charcnt +=1
          if line[charcnt: charcnt +5] == "eight":
              line = line[:charcnt] + '8' + line[charcnt:]
              count += 1
              charcnt +=1
          if line[charcnt: charcnt +4] == "nine":
              line = line[:charcnt] + '9' + line[charcnt:]
              count += 1
              charcnt +=1            
          charcnt += 1
  
      for c in line:
          if c.isdigit():
              a = c
              break
      for c in reversed(line):
          if c.isdigit():
              b = c
              break
      d = a + b
      #debugging line, shows first num, last num, concatenated num, and thenumber of words replaced
      print(a + "  " + b + "  " + d + "  " + str(count))
      print(line)
      sum += int(d)
  print(input)
  print(sum)
  
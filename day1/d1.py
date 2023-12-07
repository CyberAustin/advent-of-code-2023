import re

reg1 = "(?=(one)\d)"
reg2 = "(?=(two)\d)"
reg3 = "(?=(three)\d)"
reg4 = "(?=(four)\d)"
reg5 = "(?=(five)\d)"
reg6 = "(?=(six)\d)"
reg7 = "(?=(seven)\d)"
reg8 = "(?=(eight)\d)"
reg9 = "(?=(nine)\d)"
reg0 = "(?=(zero)\d)"
reg83 = "(eighthree)"
reg79 = "(sevenine)"
reg18 = "(oneight)"
reg21 = "(twone)"
reg82 = "(eightwo)"

def part1():
  sum = 0
  with open("d1.txt", "r") as f:
    for line in f.readlines():
      tempnum = "00"
      iter = 0
      for char in line:
        if char in "0123456789":
          if iter == 0:
            tempnum = char + char
            iter += 1
          else:
            tempnum = tempnum[0] + char
            iter += 1
      print(tempnum)
      sum += int(tempnum)
  print(sum)

def swap(line):

  #print(line)
  line = re.sub(re.compile(reg83, re.IGNORECASE|re.ASCII), "83", line)
  line = re.sub(re.compile(reg82, re.IGNORECASE|re.ASCII), "82", line)
  line = re.sub(re.compile(reg79, re.IGNORECASE|re.ASCII), "79", line)
  line = re.sub(re.compile(reg21, re.IGNORECASE|re.ASCII), "21", line)
  line = re.sub(re.compile(reg18, re.IGNORECASE|re.ASCII), "18", line)
  line = re.sub(re.compile(reg1, re.IGNORECASE|re.ASCII), "1", line)
  line = re.sub(re.compile(reg2, re.IGNORECASE|re.ASCII), "2", line)
  line = re.sub(re.compile(reg3, re.IGNORECASE|re.ASCII), "3", line)
  line = re.sub(re.compile(reg4, re.IGNORECASE|re.ASCII), "4", line)
  line = re.sub(re.compile(reg5, re.IGNORECASE|re.ASCII), "5", line)
  line = re.sub(re.compile(reg6, re.IGNORECASE|re.ASCII), "6", line)
  line = re.sub(re.compile(reg7, re.IGNORECASE|re.ASCII), "7", line)
  line = re.sub(re.compile(reg8, re.IGNORECASE|re.ASCII), "8", line)
  line = re.sub(re.compile(reg9, re.IGNORECASE|re.ASCII), "9", line)
  line = re.sub(re.compile(reg0, re.IGNORECASE|re.ASCII), "0", line)
  return line
numlist = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def part2():
  of = open("d1out.txt","w")
  sum = 0
  with open("d1.txt", "r") as f:
    for line in f.readlines():
      of.writelines(line)
      line = swap(line)
      of.writelines(line)
      print(line)
      tempnum = "00"
      iter = 0
      for char in line:
        if char in numlist:
          if iter == 0:
            tempnum = char + char
            iter += 1
          else:
            tempnum = tempnum[0] + char
            iter += 1
      print(tempnum)
      sum += int(tempnum)
  print(sum)

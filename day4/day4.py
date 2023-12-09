input = []

with open("day4.txt", "r") as f:
  input = f.readlines()

def part1():
  total = 0
  for line in input:
    linetotal = 0
    card, numbers = line.split(":")
    winning, have = numbers.split("|")
    print(f"{card} {winning} {have}")
    winning = winning.split()
    have = have.split()
    for number in have:
      if number in winning:
        if linetotal == 0:
          linetotal +=1
        else:
          linetotal *=2
    total += linetotal
  print(total)

def part2():
  cards = dict()
  total = 0
  for i in range(1, len(input)+1):
    cards[i] = 1
  for i in range(1, len(input)+1):
    #cards[i] = 1
    print(cards)
    linetotal = 0
    card, numbers = input[i-1].split(":")
    winning, have = numbers.split("|")
    #print(f"{card} {winning} {have}")
    winning = winning.split()
    have = have.split()
    for number in have:
      if number in winning:
        #print(number)
        linetotal +=1
    print(linetotal)
    for j in range(1,linetotal+1):
      #print(f"j:{j} i+j:{i+j}")
      cards[i+j] += cards[i] 
    #print(cards)
    
  #print(cards)
  for v in cards.values():
    total+=v
  print(total)
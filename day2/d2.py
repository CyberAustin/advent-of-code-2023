def part1():
  red_limit = 12
  green_limit = 13
  blue_limit = 14
  sum = 0
  with open("d2.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
      day, games = line.split(':')
      failed = False
      for game in games.split(';'):
        
        for cube in game.split(','):
          count, color = cube.split()
          count = int(count)
          
          if (color == 'red' and count > red_limit) or (color == 'green' and count > green_limit) or (color == 'blue' and count > blue_limit):
            failed = True
        
      if not failed:
        word, num = day.split()
        sum += int(num)
    print(sum)

def part2():
  power = 0
  with open("d2.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
      day, games = line.split(':')
      cubes = {"red":0, "blue":0, "green":0}
      for game in games.split(';'):
        
        for cube in game.split(','):
          count, color = cube.split()
          count = int(count)
          if cubes[color] < count:
            cubes[color] = count
      power += (cubes["red"] * cubes["green"] * cubes["blue"])
  print(power)
      
def day2part1(numRed: int, numGreen: int, numBlue: int) -> int:
  filename = '/Users/sungwoolee/Desktop/aoc/input2.txt'
  with open(filename, 'r') as f:
    raw = f.read()
    games = raw.split('\n')
    ans = 0
    gameNum = 1

    for game in games:
      game = game.replace(';', '')
      game = game.replace(',', '')
      tokens = game.split(" ")[2:]
      num = 0
      isValid = True
      for t in tokens:
        # print(t)
        if t.isnumeric():
          num = int(t)
        elif (t == "red" and num > numRed) or (t == "green" and num > numGreen) or (t == "blue" and num > numBlue):
          isValid = False
          break
      if isValid:
        print(gameNum, tokens)
        ans += gameNum
      gameNum += 1
  return ans



def day2part2() -> int:
  filename = '/Users/sungwoolee/Desktop/aoc/input2.txt'
  with open(filename, 'r') as f:
    raw = f.read()
    games = raw.split('\n')
    ans = 0
    
    for game in games:
      game = game.replace(';', '')
      game = game.replace(',', '')
      tokens = game.split(" ")[2:]
      maxRed, maxGreen, maxBlue = 0, 0, 0
      for t in tokens:
        if t.isnumeric():
          num = int(t)
        elif t == "red":
          maxRed = max(num, maxRed)
        elif t == "green":
          maxGreen = max(num, maxGreen)
        elif t == "blue":
          maxBlue = max(num, maxBlue)
      ans += maxRed * maxGreen * maxBlue
  return ans
print(day2part2())
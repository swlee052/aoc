def day4part1() -> int:
  filename = '/Users/sungwoolee/Desktop/aoc/input4.txt'
  with open(filename, 'r') as f:
    raw = f.read()
    lines = raw.split('\n')
    ans = 0
    
    for line in lines:
      line = line.split()[2:]
      winNums = set()
      isWinNums = True
      score = 0
      for t in line: 
        if t == "|":
          isWinNums = False
        elif isWinNums:
          winNums.add(t)
        elif t in winNums:
          if not score:
            score = 1
          else:
            score *= 2
      ans += score
  return ans

def day4part2() -> int:
  filename = '/Users/sungwoolee/Desktop/aoc/input4.txt'
  with open(filename, 'r') as f:
    raw = f.read()
    lines = raw.split('\n')[:-1]
    numCards = [1] * len(lines)
    sz = len(lines)

    for i in range(sz):
      line = lines[i].split()[2:]
      winNums = set()
      isWinNums = True
      winNumsFound = 0
      
      for t in line: 
        if t == "|":
          isWinNums = False
        elif isWinNums:
          winNums.add(t)
        elif t in winNums:
          winNumsFound += 1
    
      for j in range(i+1, min(sz, i+winNumsFound+1)):
        numCards[j] += numCards[i]
  return sum(numCards)
print(day4part2())
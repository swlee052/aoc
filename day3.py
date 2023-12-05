def day3part1() -> int:
  filename = '/Users/sungwoolee/Desktop/aoc/input3.txt'
  with open(filename, 'r') as f:
    raw = f.read()
    lines = raw.split()
    m, n = len(lines), len(lines[0])
    board = [[c for c in line] for line in lines]
    ans = [0]

    def checkAndAddNum(row: int, col: int) -> None:
      if board[row][col].isnumeric():
        num = board[row][col]
        board[row][col] = '.'
      
        # left
        i = col-1
        while i >= 0 and board[row][i].isnumeric():
          num = board[row][i] + num
          board[row][i] = '.'
          i -=1

        # right
        i = col+1
        while i < n and board[row][i].isnumeric():
          num += board[row][i]
          board[row][i] = '.'
          i += 1

        ans[0] += int(num)
      

    def addAdjNums(row: int, col: int) -> None:
      # up
      if row > 0:
        checkAndAddNum(row-1, col)

      # down
      if row < m-1:
        checkAndAddNum(row+1, col)
      
      # left
      if col > 0:
        checkAndAddNum(row, col-1)
      
      # right
      if col < n-1:
        checkAndAddNum(row, col+1)

      # upleft
      if row > 0 and col > 0:
        checkAndAddNum(row-1, col-1)

      # upright
      if row > 0 and col < n-1:
        checkAndAddNum(row-1, col+1)

      # downleft
      if row < m-1 and col > 0:
        checkAndAddNum(row+1, col-1)

      # downright
      if row < m-1 and col < n-1:
        checkAndAddNum(row+1, col+1)
      

    # add adjacent numbers
    for i in range(m):
      for j in range(n):
        if board[i][j] != '.' and not board[i][j].isnumeric():
          addAdjNums(i, j)

  return ans[0]

def day3part2() -> int:
  filename = '/Users/sungwoolee/Desktop/aoc/input3.txt'
  with open(filename, 'r') as f:
    raw = f.read()
    lines = raw.split()
    m, n = len(lines), len(lines[0])
    board = [[c for c in line] for line in lines]
    ans = [0]

    def addIfGear(row: int, col: int) -> None:
      nums = []
      startPosSet = set()

      def checkAndAddNum(row: int, col: int) -> None:
        if len(nums) <= 2 and board[row][col].isnumeric():
          num = board[row][col]
          startPos = (row, col)
        
          # left
          i = col-1
          while i >= 0 and board[row][i].isnumeric():
            num = board[row][i] + num
            startPos = (row, i)
            i -=1

          # right
          i = col+1
          while i < n and board[row][i].isnumeric():
            num += board[row][i]
            i += 1

          if startPos not in startPosSet:
            startPosSet.add(startPos)
            nums.append(int(num))

      # up
      if row > 0:
        checkAndAddNum(row-1, col)

      # down
      if row < m-1:
        checkAndAddNum(row+1, col)
      
      # left
      if col > 0:
        checkAndAddNum(row, col-1)
      
      # right
      if col < n-1:
        checkAndAddNum(row, col+1)

      # upleft
      if row > 0 and col > 0:
        checkAndAddNum(row-1, col-1)

      # upright
      if row > 0 and col < n-1:
        checkAndAddNum(row-1, col+1)

      # downleft
      if row < m-1 and col > 0:
        checkAndAddNum(row+1, col-1)

      # downright
      if row < m-1 and col < n-1:
        checkAndAddNum(row+1, col+1)

      if len(nums) == 2:
        ans[0] += nums[0] * nums[1]

    # add gear ratios
    for i in range(m):
      for j in range(n):
        if board[i][j] == '*':
          addIfGear(i, j)
    return ans[0]

print(day3part2())

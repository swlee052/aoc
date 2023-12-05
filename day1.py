import re

def aoc():
  digit_strs = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9",
  }

  digit_strs_rev = {
    "eno" : "1",
    "owt" : "2",
    "eerht" : "3",
    "ruof" : "4",
    "evif" : "5",
    "xis" : "6",
    "neves" : "7",
    "thgie" : "8",
    "enin" : "9",
  }

  filename = '/Users/sungwoolee/Desktop/aoc/input1.txt'
  with open(filename, 'r') as f:
    raw = f.read()
    lines = raw.split('\n')
    ans = 0
    cnt = 1
    for line in lines:
      # Combine the digit strings into a regular expression pattern
      
      num = ""

      pattern = '(' + '|'.join(list(digit_strs.keys()) + [str(i) for i in range(1, 10)]) +')'
      li = re.split(pattern, line)
      li = list(filter(None, li))
      sz = len(li)
      print(line, li)
      for i in range(sz):
        s = li[i]
        if s.isnumeric():
          num += s
          break
        elif s in digit_strs:
          num += digit_strs[s]
          break

      pattern = '(' + '|'.join(list(digit_strs_rev.keys()) + [str(i) for i in range(1, 10)]) +')'
      li = re.split(pattern, line[::-1])
      li = list(filter(None, li))
      sz = len(li)
      print(line, li)
      for i in range(sz):
        s = li[i]
        if s.isnumeric():
          num += s
          break
        elif s in digit_strs_rev:
          num += digit_strs_rev[s]
          break

      ans += int(num)
      print(num, ans)
      cnt += 1
  return ans
aoc()
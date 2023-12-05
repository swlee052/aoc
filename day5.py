import math


def main():
    print(part1())
    # print(part2())

def get_lines() -> [str]:
  filename = '/Users/sungwoolee/Desktop/aoc/input5.txt'
  with open(filename, 'r') as f:
    lines = f.readlines()
  return list(filter(None, [l.strip() for l in lines]))


def get_seeds_and_maps():
  lines = get_lines()
  seeds = [int(s) for s in lines[0].split()[1:]]
  maps = []
  m = []

  for line in lines[1:]:
    tokens = line.split()
    interval = []
    for t in tokens:
      if t.isnumeric():
        interval.append(int(t))
      elif t == "map:":
        if m:
          maps.append(m)
        m = []
    if interval:
      m.append(interval)
  maps.append(m)
  return seeds, maps

def part1():
  seeds, maps = get_seeds_and_maps()
  numSeeds = len(seeds)
  locations = seeds
  
  for m in maps:
    for i in range(numSeeds):
      for itvl in m:
        s = locations[i]
        if itvl[1] <= s and s <= itvl[1] + itvl[2]-1:
          locations[i] += itvl[0] - itvl[1]
          break
  return min(locations)

def part2():
  seeds, maps = get_seeds_and_maps()
  numSeeds = len(seeds)
  locations = seeds
  
  for m in maps:
    for i in range(numSeeds):
      for itvl in m:
        s = locations[i]
        if itvl[1] <= s and s <= itvl[1] + itvl[2]-1:
          locations[i] += itvl[0] - itvl[1]
          break
  return min(locations)


main()
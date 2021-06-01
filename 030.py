def dfp(n):
  temp = str(n)
  tot = 0
  for x in temp:
    tot += int(x)**5
  return n == tot


total = 0
for x in range(2,6*(9**5)):
  if dfp(x):
    total += x
    print(x)

print(total)
d = 11
numfigs = 13
# loop over denominators
for x in range(1, d):
  a = 1
  num = []
  for y in range(0, numfigs):
    num.append(a // x)
    a = 10 * (a % x)
  print(num)

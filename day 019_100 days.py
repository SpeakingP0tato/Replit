total = 1000
APR = 0.05
for counter in range (10):
  total += (total*APR)
  print("year", counter+1, "is", round(total,2))

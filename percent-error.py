def percent-errror(actual, experimental):
  ans = (actual/abs((experimental-actual)))*100
  return ans
print(percent-errror(11.6,11.9))

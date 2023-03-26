def front_times(str, n):
  fn = 3
  if fn > len(str):
    fn = len(str)
  front = str[:fn]
  
  res = ""
  for i in range(n):
    res = res + front
  return res
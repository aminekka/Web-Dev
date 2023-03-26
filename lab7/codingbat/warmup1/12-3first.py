def front3(str):

  n = 3
  if len(str) < n:
    n = len(str)
  front = str[:n]
  return front + front + front 
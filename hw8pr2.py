def count_evens(nums):
  evens = 0
  for c in nums:
    if c%2 == 0:
      evens += 1
  return evens


def big_diff(nums):
  smallest = nums[0]
  largest = 0
  for c in nums:
    smallest = min(c, smallest)
    largest = max(c , largest)
  return largest - smallest


def sum13(nums):
  total = 0
  skip = 0
  if nums == []:
    return 0
  else:
    for n in nums:
      if skip == 1:
        skip = 0
        total += 0
      elif n == 13:
        skip = 1
        total += 0
      elif n != 13:
        total += n
  return total

def sum67(nums):
  total = 0
  skip = 0
  if nums == []:
    return 0
  else:
    for n in nums:
      if n == 6:
        skip = 1
        total += 0
      elif skip == 1 and n == 7:
        skip = 0 
        total += 0
      elif skip == 0:
        total += n
       
  return total

def has22(nums):
  twos = 0
  for n in nums:
    if n == 2 and twos == 1:
      return True      
    elif n !=2:
      twos = 0      
    elif n == 2 and twos == 0:
      twos = 1      
  return False

def count_hi(str):
  h = False
  cnt = 0
  for w in str:
    if w == "h":
      h = True
    elif w == "i" and h == True:
      cnt += 1
    elif h == True and w != "i":
      h = False
  return cnt
    

def cat_dog(str):
  cats = 0
  dogs = 0
  for anis in range(len(str)-1):
    if str[anis:anis+3] == "cat":
      cats += 1
    if str[anis:anis+3] == "dog":
      dogs += 1
  if cats == dogs:
    return True
  else:
    return False


def count_code(str):
  cnt = 0
  for c in range(len(str)-1):
    if str[c:c+2] == "co" and (len(str)-1)-c > 2:
      if str[c+3] == "e":
        cnt += 1
  return cnt


def end_other(a, b):
  max_range = (min((len(a)-1), (len(b)-1)))+1   # LOL - I forgot about endswith
  for c in range(max_range):
    return a[-max_range:].lower() == b[-max_range:].lower()

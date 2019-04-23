# Takes a string "hand" ie ("AS 4H 3S AC KS") and returns a list of the numbers from it. T - A = 10 - 14
def getNumbers(hand):
  numbers = []
  finalNumbers = []
  for i in range(len(hand)):
    if i % 3 == 0:
      numbers.append(hand[i])
  for num in numbers:
    try:
      finalNumbers.append(int(num)) 
    except:
      if num == 'T':
        finalNumbers.append(10)
      elif num == 'J':
        finalNumbers.append(11)
      elif num == 'Q':
        finalNumbers.append(12)
      elif num == 'K':
        finalNumbers.append(13)
      elif num == 'A':
        finalNumbers.append(14)
  return finalNumbers

# gets a string hand and returns list of suits
def getSuits(hand):
  suits = []
  finalSuits = []
  for i in range(len(hand)):
    if i % 3 == 1:
      suits.append(hand[i])
  for suit in suits:
    if suit == 'C':
      finalSuits.append(0)
    elif suit == 'D':
      finalSuits.append(1)
    elif suit == 'H':
      finalSuits.append(2)
    elif suit == 'S':
      finalSuits.append(3) 
  return finalSuits

# flush check
def samesuit(suits):
  if len(set(suits)) == 1:
    return True
  return False

# straight check
def consecutive(numbers):
  if sorted(numbers) == list(range(min(numbers), max(numbers)+1)):
    return True
  return False

# This function "Explains" returns the hand type back 1 - 10 with 1 being high card and 10 being royal flush
def explain(hand):
  # Step 1: Get the Numbers and Suits
  numbers = getNumbers(hand)
  suits = getSuits(hand)
  # Step 2: Check for straight, straight flush, and royal flush
  if consecutive(numbers):
    if samesuit(suits):
      if 14 in numbers: # Royal Flush, the straight has an Ace
        return 10
      return 9 # Straight Flush
    return 5 # Straight
  # Step 3: Check for 4 or 3 of a kind and fullhouse
  for num in numbers:
    count = numbers.count(num)
    if count == 4:
      return 8 # a number was counted 4 times
    if count == 3: 
      # fullhouse check
      numbers2 = numbers
      for i in range(5):
        try: numbers2.remove(num)
        except: pass
      if len(set(numbers2)) == 1: # if the remaining two numbers are the same its the set() will make it 1
        return 7 
      else:
        return 4
  # Step 4: check for flush
  if samesuit(suits):
    return 6
  # Step 5: check for 2 or 1 pair
  for num in numbers:
    count = numbers.count(num)
    if count == 2:
      # check for another pair
      numbers2 = numbers
      for i in range(5):
        try: numbers2.remove(num)
        except: pass
      if len(set(numbers2)) == 2: # if it removed a number there was another pair
        return 3
      else:
        return 2
  return 1 # the last possibility  


# This function looks at the individual numbers of each hand and determines a winner
def tiebreaker(hand1, hand2, handtype):
  h1nums = getNumbers(hand1)
  h2nums = getNumbers(hand2)
  if handtype == 1 or handtype == 6:
    for i in range(5):
      if max(h1nums) == max(h2nums):
        h1nums.remove(max(h1nums))
        h2nums.remove(max(h2nums))
        continue
      if max(h1nums) > max(h2nums):
        return 1
      return 2
  if handtype == 9 or handtype == 5: # tie straights
    if max(h1nums) > max(h2nums):
      return 1
    return 2
  if handtype == 8 or handtype == 7: # 4okind and full house
    h1 = list(set(h1nums))
    h2 = list(set(h2nums))
    h1high = 0
    h2high = 0
    h1low = 0
    h2low = 0
    if h1nums.count(h1[0]) == 4 or h1nums.count(h1[0]) == 3:
      h1high = h1[0]
      h1low = h1[1]
    else:
      h1high = h1[1]
      h1low = h1[0]
    if h2nums.count(h2[0]) == 4 or h2nums.count(h2[0]) == 3:
      h2high = h2[0]
      h2low = h2[1]
    else:
      h2high = h2[1]
      h2low = h2[0]
    if h1high == h2high:
      if h1low > h2low:
        return 1
      else:
        return 2
    else:
      if h1high > h2high:
        return 1
      else:
        return 2
  if handtype == 2 or handtype == 4: # 1 pair and 3 of a kind
    x = list(set([z for z in h1nums if h1nums.count(z) > 1]))
    y = list(set([z for z in h2nums if h2nums.count(z) > 1]))
    leftover = 3 if handtype == 2 else 2
    if x[0] == y[0]:
      h1nums.remove(x[0])
      h1nums.remove(x[0])
      h2nums.remove(y[0])
      h2nums.remove(y[0])
      for z in range(leftover):
        if max(h1nums) == max(h2nums):
          h1nums.remove(max(h1nums))
          h2nums.remove(max(h2nums))
          continue
        if max(h1nums) > max(h2nums):
          return 1
        return 2
    if x[0] > y[0]:
      return 1
    return 2
  if handtype == 3:
    x = list(set([z for z in h1nums if h1nums.count(z) > 1]))
    y = list(set([z for z in h2nums if h2nums.count(z) > 1]))
    tempx = x[:]
    tempy = y[:]
    if max(x) == max(y):
      x.remove(max(x))
      y.remove(max(y))
      if max(x) == max(y):
        h1nums.remove(tempx[1])
        h1nums.remove(tempx[1])
        h1nums.remove(tempx[0])
        h1nums.remove(tempx[0])
        h2nums.remove(tempy[1])
        h2nums.remove(tempy[1])
        h2nums.remove(tempy[0])
        h2nums.remove(tempy[0])
        if h1nums[0] > h2nums[0]:
          return 1
        return 2
      elif max(x) > max(y):
        return 1
      return 2
    elif max(x) > max(y):
      return 1
    return 2

# Hand this function the hands it will call the important hands and return a 1 or 2
def compareHands(hand1, hand2):
  hand1type = explain(hand1)
  hand2type = explain(hand2)
  if hand1type == hand2type:
    if tiebreaker(hand1, hand2, hand1type) == 1:
      return True
    return False
  elif hand1type > hand2type:
    return True
  return False

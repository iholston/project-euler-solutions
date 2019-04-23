import handsHandler, time
start = time.time()

# Returns list of hands in string format
def get_cards():
  masterhands = []
  hands = open('poker.txt', 'r') 
  for line in hands:
    masterhands.append(line[:14])
    masterhands.append(line[15:len(line)-1])
  hands.close()
  return masterhands

# Driver
hands = get_cards()
h1total = 0
for i, hand in enumerate(hands):
  if i % 2 == 1: continue
  if handsHandler.compareHands(hand, hands[i+1]):
      h1total += 1
print(h1total)
print(time.time() - start)

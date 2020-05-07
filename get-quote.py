import random

def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes)-1 #if we want to add or remove quotes in the future (updates automatically)
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  primary()

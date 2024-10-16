#drawcard function takes the first number of the lists and checks if they are bigger, smaller or equal
#pop removes can remove last item in a list
#P1 hand and p2 hand is a variable

import random

class game: #class for easier action between rounds
  def __init__(self):
    self.mainDeck = []
    self.deck1 = []
    self.deck2 = []
    self.warpile = []
    self.p1hand = 0
    self.p2hand = 0 
    self.roundCounter = 0
    
    
    for i in range(13):
      for p in range(4):
        self.mainDeck.append(i+1)
    random.shuffle(self.mainDeck)
    
   
    for i in range(51):
      if(i % 2 == 0):
        self.deck1.append(self.mainDeck[i])
      else:
        self.deck2.append(self.mainDeck[i])
        
    while len(self.deck1) < 49 and len(self.deck2) < 49:

      
      if self.roundCounter >= 256:
        break
      
    if len(self.deck1) > (self.deck2): 
      print("YOU LOSE Just kidding :-)")  
      
    elif len(self.deck1) < (self.deck2):
      print("YOU LOSE Just kidding :-)")
      
    else:
      print("YOU TIED yay")
        
    def drawCard(self):
      self.p1hand = self.deck1[0]
      self.p2hand = self.deck2[0] 
      self.deck1.pop()
      self.deck2.pop()
      
      self.judge() 
      self.roundCounter += 1
            
    def War(self):
      self.warpile.extend([self.p1hand, self.p2hand])
      self.warpile.append(self.deck1.pop(0))
      self.warpile.append(self.deck2.pop(0))
  
      self.War()
      self.drawCard()
      
    def judge(self):
      if self.p1hand>self.p2hand: #if player1 wins the wins the round
        print("p1 had " , self.p1hand , "p2 had " , self.p2hand)
        
        
        if len(self.warpile) > 1:
          self.deck1.extend(self.warpile)
          self.warpile.clear()
        self.deck1.extend(self.p1hand, self.p2hand)
        print("player 1's deck is currently at " , len(self.deck1))
        
      elif self.p1hand<self.p2hand:
        print("p1 had " , self.p1hand , "p2 had " , self.p2hand)

        if len(self.warpile) > 1:
          self.deck2.extend(self.warpile)
          self.warpile.clear()
        self.deck2.extend(self.warpile)
        print("player 2's deck is currently at " , len(self.deck2))


      else:
        print("A tie has occured")
        print("p1 has " , self.p2hand , "p2 had " , self.p2hand)
        self.war()

obj = game()
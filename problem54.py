class Game:

	def __init__(self, cards):
		self.playerOneScore = 0
		self.playerTwoScore = 0
		self.result = 0
		cards = cards.split()
		self.playerOnesHand = Hand(cards[0:5])
		self.playerTwosHand = Hand(cards[5:10])

		self.play();

	def play(self):
		self.playerOneScore = self.playerOnesHand.getScore();
		self.playerTwosCore = self.playerTwosHand.getScore();

		if(self.playerOneScore == self.playerTwoScore):
			val = self.handleTie();
			if val == 1:
				self.playerOneScore += 1
			elif val == 2:
				self.playerTwoScore += 1
			else:
				self.result == 0
				return
		if (self.playerOneScore > self.playerTwoScore):
			self.result = 1
		else: 
			self.result = 2

	def handleTie(self):
		if (self.playerOnesHand.values[4] > self.playerTwosHand.values[4]):
			return 1
		if (self.playerOnesHand.values[4] < self.playerTwosHand.values[4]):
			return 2
		if (self.playerOnesHand.values[3] > self.playerTwosHand.values[3]):
			return 1
		if (self.playerOnesHand.values[3] < self.playerTwosHand.values[3]):
			return 2
		if (self.playerOnesHand.values[2] > self.playerTwosHand.values[2]):
			return 1
		if (self.playerOnesHand.values[2] < self.playerTwosHand.values[2]):
			return 2
		if (self.playerOnesHand.values[1] > self.playerTwosHand.values[1]):
			return 1
		if (self.playerOnesHand.values[1] < self.playerTwosHand.values[1]):
			return 2
		if (self.playerOnesHand.values[0] > self.playerTwosHand.values[0]):
			return 1
		if (self.playerOnesHand.values[0] < self.playerTwosHand.values[0]):
			return 2
class Hand: 
	def setValues(self):
		for card in self.cards:
			self.values.append(card.value)
		self.values.sort()

	def isFlush(self):
		currentSuit = self.cards[0].suit
		for card in self.cards:
			if card.suit != currentSuit:
				return False
			currentSuit = card.suit
		return True

	def isRoyalFlush(self):
		low = min(self.values)

		if low == 10 and (low + 1 in self.values) and (low + 2 in self.values) and (low + 3 in self.values) and (low + 4 in self.values):
			return True
		else:
			return False

	def isFourOfAKind(self):
		cardOneCount = self.values.count(self.values[0])
		cardTwoCount = self.values.count(self.values[4])

		if cardOneCount == 4 or cardTwoCount == 4:
			return True
		else: 
			return False

	def isThreeOfAKind(self):
		cardOneCount = self.values.count(self.values[0])
		cardTwoCount = self.values.count(self.values[4])
		cardThreeCount  = self.values.count(self.values[2])
		if cardOneCount == 3 or cardTwoCount == 3 or cardThreeCount == 3:
			return True
		else: 
			return False

	def isStraight(self):
		low = min(self.values)

		if (low + 1 in self.values) and (low + 2 in self.values) and (low + 3 in self.values) and (low + 4 in self.values):
			return True;
		else:
			return False

	def isFullHouse(self):
		
		cardOneCount = self.values.count(self.values[0])
		cardTwoCount = self.values.count(self.values[4])

		if (cardOneCount == 2 and cardTwoCount == 3 ) or (cardOneCount == 3 and cardTwoCount == 2):
			return True
		else: 
			return False

	def isTwoPair(self):
		cardOneCount = self.values.count(self.values[0])
		cardTwoCount = self.values.count(self.values[4])
		cardThreeCount = self.values.count(self.values[2])

		if(cardOneCount == 2 and cardTwoCount == 2) or (cardOneCount == 2 and cardThreeCount == 2) or (cardTwoCount == 2 and cardThreeCount == 2):
			return True;
		return False;

	def isPair(self):
		cardOneCount = self.values.count(self.values[0])
		cardTwoCount = self.values.count(self.values[4])
		cardThreeCount = self.values.count(self.values[2])

		if(cardOneCount == 2 or cardTwoCount == 2 or cardTwoCount == 3):
			return True;
		else:
			return False;

	def __init__(self, cards):
		self.cards = []
		self.values = []
		for c in cards:
			self.cards.append(Card(c))

		self.setValues()

	def getScore(self):
		score = 0
		if self.isRoyalFlush(): score = 140000; 
		elif self.isFlush() and self.isStraight(): score = 130000; 
		elif self.isFourOfAKind(): score = 120000; 
		elif self.isFullHouse(): score = 110000;
		elif self.isFlush(): score = 100000; 
		elif self.isStraight(): score = 90000; 
		elif self.isThreeOfAKind(): score = 80000; 
		elif self.isTwoPair(): score = 70000; 
		elif self.isPair(): score = 60000; 
		else: score = 0  

		return score

class Card:
	def __init__(self, card):
		self.value = self.determineValue(card[0])
		self.suit = card[1]

	def determineValue(x,y):
		return {
			'2':2,
			'3':3,
			'4':4,
			'5':5,
			'6':6,
			'7':7,
			'8':8,
			'9':9,
			'T':10,
			'J':11,
			'Q':12,
			'K':13,
			'A':14
		}.get(y)

def playGames():
	player1Score = 0;
	player2Score = 0;
	file = open("poker.txt")
	
	for line in file:
		game = Game(line)
		if game.result == 1:
			player1Score += 1
		else:
			player2Score += 1

	print "Player one has won " + str(player1Score) + " games! "
	print "Player two has won " + str(player2Score) + " games! "
	if (player1Score > player2Score):
		print "Player 1 wins!"
	else:
		print "Player 2 wins!"
 
def main():
	playGames();

if __name__ == "__main__":
	main()
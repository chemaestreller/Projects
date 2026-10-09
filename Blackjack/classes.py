class Card:
    def __init__(self, suit: str, value: str):
        self.suit = suit
        self.value = value
        
    def display(self):
        print(f"{self.value}{self.suit}")

    def discard(self):
        # TODO
        pass
        # push card to bottom of deck

class Hand:
    def __init__(self):
        self.cards=[]
        # self.chips=chips TODO

    def get(self, card):
        self.cards.append(card)

    def display(self, show_cards=True):
        print(f"There are {len(self.cards)} cards in your hand: ") 
        for card in self.cards:
            card.display()
            # print(card.value)
            pass

    def view(self):
        # method for showing initial dealer draw
        print("The dealer's visible card is: ")
        self.cards[0].display()

    def value(self):
        # self.cards.sort(key=lambda card: card.value == "A")
        sort = sorted(self.cards, key=lambda card: card.value == "A")
        # makes sure aces are evaluated last, but still displayed in random order
        total = 0
        for card in sort:
            try:
                if int(card.value):
                    # if value is numerical, this is evaluated as an int and added to hand total
                    total += int(card.value)
            except:
                if (card.value == "A"):
                    if total + 11 > 21:
                        # if ace would bust, it is worth 1
                        total += 1
                    else:
                        total += 11
                else:
                    # evaluates for J, K, Q
                    total += 10
        print(f"Hand value: {total}") 
        self.value = total
        # return total
            
class Deck:
    def __init__(self):
        self.cards=[]
        suits = ["♡⁠", "♤", "♢", "♧"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def display(self, show_cards=True):
        if show_cards:
            for card in self.cards:
                card.display()
            print(f"{len(self.cards)} cards in the deck.")
        else:
            print(f"{len(self.cards)} cards in the deck.")

    def deal(self, num_cards: int, player_hand: Hand):
        # deal x amounts of cards to a specified hand object
        for _ in range(num_cards):
            player_hand.get(self.cards.pop())
        pass


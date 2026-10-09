from classes import Card, Deck, Hand

deck = Deck()
# deck.display()
deck.shuffle()


hand1=Hand()
dealer= Hand()
deck.deal(2, hand1)
deck.deal(2, dealer)

print("\n")

# hand1.display()
# hand1.value()
# dealer.display()
# dealer.value()

def game():
    while hand1.value() < 21:
        hand1.display()
        hand1.value()
        print(f"Value: {hand1.value()}")
        # try:
        action = input("Would you like to hit or stand? (H/S) ").upper()
        print(f"action: {action}")
        if action == "H":
            deck.deal(1, hand1)
        elif action == "S":
            print("You stood with a final hand of: ")
            hand1.display()
            print(f"Value: {hand1.value()}")
            break
        else: 
            action = input("Please choose to hit or stand (H/S): ").upper()
        # except:
        #     print("inputted not a str")
        #     action = input("Please choose to hit or stand (H/S): ").upper()

    if hand1.value() == 21:
        print(f"You got 21!")
        hand1.display()

    if hand1.value() > 21:
        print(f"You busted with {hand1.value()}!")
        hand1.display()

    # TODO: add code for dealer to hit or stand after player, show dealer hand if player busts, betting, 
    # TODO: comparisons of player vs dealer to see who wins
 
# !debugging
# ace = Card("h", "A")
# card=Card("s", "10")
# c2 = Card("d", "2")
# hand2 = Hand()
# hand2.get(card)
# hand2.get(ace)
# hand2.get(c2)

# hand2.display()
# hand2.value()
# !debugging
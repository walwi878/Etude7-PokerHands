import re

"""
@author William Wallace
@date 22/05/2020

This programm capitalises, sorts in ascending order of value, and prints the cards in a 
hand of poker from stdin, if the hand is in the valid format. 
"""

# numToInt returns the number of the card if it is a digit and converts it to type int. 
def numToInt(handString):
    if handString.isdigit():
        return int(handString)
    else:
        return handString

# cardInts is a key for the sort comparison. It turns double digit numbers from cards into type int.
def cardInts(handString):
    return [numToInt(c) for c in re.split(r'(\d+)', handString)]

# validSeparators returns the seperator of the hand based on what character is present after the first card. 
# Input is invalid if none of the acceptable seperators are present after the first card.   
def validSeparators(handString):
    if handString[2] == '-' or handString[2] == '/' or handString[2] == ' ':
        return handString[2]
    elif handString[3] == '-' or handString[3] == '/' or handString[3] == ' ':
        return handString[3]
    else:
        return -1

# If hand is valid by matching regex, cards in hand are capitalised, reformatted to
# contain face cards, and sorted in ascending order. 
# If hand is invalid, hand is declared invalid and moves on. 
if __name__ == '__main__':
    try:
        while True:
            hand = input()
            handUpper = hand.upper()
            pattern = '^([1-9]|10|11|12|13|[ATJQK])([CDHS])$'            # Sorts cards into suit order when hand contains cards with same number
            parsedCards = []

            # Hand is categorised as invalid if it doesn't meet requirements.            
            if len(hand) < 4:
                print("Invalid:", hand)                                 # Hand is too short
            else:
                seperator = validSeparators(handUpper)
                if seperator == -1:
                    print("Invalid:", hand)                             # Hand contains no valid seperator
                else:
                    cards = re.split(seperator, handUpper)
                    if len(cards) != 5:
                        print("Invalid:", hand)                         # Hand doesn't contain exactly 5 cards sepearated by 4 identical seperators 
                    else:
                        isValid = True
                        for card in cards:
                            if not re.match(pattern, card):
                                isValid = False
                                break
                        if isValid == False:
                            print("Invalid:", hand)                     # Hand doesn't match regex pattern. 
                        
                        # Iterates over each card in the hand, replaces number cards with face cards, and changes value of Ace card to 14.
                        else:
                            for i in range(len(cards)):
                                
                                # Ensures that the change of value in Ace doesn't affect the 1's in the face cards.
                                cards[i] = cards[i].replace('10', 'T')
                                cards[i] = cards[i].replace('11', 'J')
                                cards[i] = cards[i].replace('12', 'Q')
                                cards[i] = cards[i].replace('13', 'K')

                                # Increases value of Ace card for ascending sort.
                                cards[i] = cards[i].replace('1', '14')

                                # Allows new card values to be sorted.
                                cards[i] = cards[i].replace('A', '14')
                                cards[i] = cards[i].replace('T', '10')
                                cards[i] = cards[i].replace('J', '11')
                                cards[i] = cards[i].replace('Q', '12')
                                cards[i] = cards[i].replace('K', '13')
                                
                                # Sorts hand in ascending order based on card's numeric values
                            cards.sort(key = cardInts)

                            # Renames numeric value for face cards to corrsponding face value. 
                            for i in range(len(cards)):
                                cards[i] = cards[i].replace('11', 'J')
                                cards[i] = cards[i].replace('12', 'Q')
                                cards[i] = cards[i].replace('13', 'K')
                                cards[i] = cards[i].replace('14', 'A')                               

                            # Outputs final valid hand as valid cards seperated by spaces. 
                            # Parsed is a list containing unique cards in hand. It doesn't accept duplicates.  
                            for card in cards:
                                if card in parsedCards:
                                    isValid = False
                                    break
                                else:
                                    parsedCards.append(card)

                            # If one of the cards is a duplicate, hand is invalid. 
                            if isValid == False:
                                print("Invalid:", hand)                 # Hand contains duplicate cards 

                            else:
                                outputHand = " ".join(cards)
                                print(outputHand)
    except EOFError:
            pass
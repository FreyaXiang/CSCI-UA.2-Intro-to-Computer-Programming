# Xin Xiang N12021000
# Nov.20
# Section 008
# XinXiang_assign8_part4

names=['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts', \
        '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts', \
        'King of Hearts', 'Queen of Hearts', 'Jack of Hearts', \
        '10 of Diamonds', '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', \
        '5 of Diamonds', '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 'Ace of Diamonds', \
        'King of Diamonds', 'Queen of Diamonds', 'Jack of Diamonds', \
        '10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs', '6 of Clubs', \
        '5 of Clubs', '4 of Clubs', '3 of Clubs', '2 of Clubs', 'Ace of Clubs', \
        'King of Clubs', 'Queen of Clubs', 'Jack of Clubs', \
        '10 of Spades', '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', \
        '5 of Spades', '4 of Spades', '3 of Spades', '2 of Spades', 'Ace of Spades', \
        'King of Spades', 'Queen of Spades', 'Jack of Spades']
values=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, \
        10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, \
        10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, \
        10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10]


#dealing two cards at random to the player
#player card1
player_card1=cards[random.randint(0,len(cards)-1)]
player_index1=cards.index(player_card1)
player_value1=values[player_index1]
#player card2
player_card2=cards[random.randint(0,len(cards)-1)]
player_index2=cards.index(player_card2)
player_value2=values[player_index2]

#store these cards and the associated values in separate lists
cards_player=[player_card1,player_card2]
values_player=[player_value1,player_value2]

#remove the two cards from the deck
del cards[player_index1]
del cards[player_index2]
del values[player_index1]
del values[player_index2]

while True:
    #report the player's hand & value of their hand
    print("Player hand:",cards_player,"is worth",sum(values_player))
    if sum(values_player)==21:
        print("You got 21! Blackjack! You win!")
        break
    elif sum(values_player)>21:
        print("Bust!")
        print("Computer wins!")
        break
    else:
        #"hit" or "stand"?
        answer=input("(h)it or (s)tand? ")
        #validate answer
        while not answer in ["h","s"]:
            print("Invalid option, please try again.")
            answer=input("(h)it or (s)tand? ")
            
        #hit
        if answer=="h":
            #deal the player another card
            new_card=cards[random.randint(0,len(cards)-1)]
            new_index=cards.index(new_card)
            new_value=values[new_index]
            #store the new card and its value in seperate lists
            cards_player+=[new_card]
            values_player+=[new_value]
            #remove the new card from the deck
            del cards[new_index]
            del values[new_index]
            #print
            print("You drew",new_card)
    
        else:
            #redefine the lists of cards and values for computer
            cards=['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts', '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts', 'King of Hearts', 'Queen of Hearts', 'Jack of Hearts', '10 of Diamonds', '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', '5 of Diamonds', '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 'Ace of Diamonds', 'King of Diamonds', 'Queen of Diamonds', 'Jack of Diamonds', '10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs', '6 of Clubs', '5 of Clubs', '4 of Clubs', '3 of Clubs', '2 of Clubs', 'Ace of Clubs', 'King of Clubs', 'Queen of Clubs', 'Jack of Clubs', '10 of Spades', '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', '5 of Spades', '4 of Spades', '3 of Spades', '2 of Spades', 'Ace of Spades', 'King of Spades', 'Queen of Spades', 'Jack of Spades']
            values=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10]
            print()
            #dealing two cards to the computer
            #computer card1
            computer_card1=cards[random.randint(0,len(cards)-1)]
            computer_index1=cards.index(computer_card1)
            computer_value1=values[computer_index1]
            #computer card2
            computer_card2=cards[random.randint(0,len(cards)-1)]
            computer_index2=cards.index(computer_card2)
            computer_value2=values[computer_index2]

            #store these cards and the associated values in separate lists
            cards_computer=[computer_card1,computer_card2]
            values_computer=[computer_value1,computer_value2]

            #remove the two cards from the deck
            del cards[computer_index1]
            del cards[computer_index2]
            del values[computer_index1]
            del values[computer_index2]

            while True:
                #report the computer's hand & value of its hand
                print("Computer hand:",cards_computer,"is worth",sum(values_computer))

              
                if sum(values_computer)>21:
                    print("Bust!")
                    print("Player wins!")
                    break

                elif sum(values_computer)==21:
                    print("Computer got 21!  Blackjack!")
                    print("Computer wins!")
                    break
                
                elif sum(values_computer)>sum(values_player):
                    print("Computer wins!")
                    break
                
                else:
                
                    #deal the computer another card
                    new_card_comp=cards[random.randint(0,len(cards)-1)]
                    new_index_comp=cards.index(new_card_comp)
                    new_value_comp=values[new_index_comp]
                    #store the new card and its value in seperate lists
                    cards_computer+=[new_card_comp]
                    values_computer+=[new_value_comp]
                    #remove the new card from the deck
                    del cards[new_index_comp]
                    del values[new_index_comp]
                    #print
                    print("Computer drew",new_card_comp)
                    
                    
            break
      

                
                        
                    




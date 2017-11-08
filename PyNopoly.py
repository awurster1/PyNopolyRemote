#PyNopoly for Python 3.6  Copyright (C) 2017  Andrew James Wurster
#   This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions as stated in the creative commons copyleft license;

#Note: The developer of PyNopoly is not associated with Monopoly, colorama or the developers of Creative Commons.
#import colorama as color
import random
import chance
import comm_chest
num_players = 0

def main_menu():
    global player1
    global player2
    global player3
    global player4
    global player5
    print("Welcome to PyNopoly!")
    #deal money ($1500/ea)
    #shuffle comm. chest
    #shuffle chance cards
    #python program will automate banker
    num_players = int(input("How many human players?"))
    print("num of players after input is" + str(num_players));
    if num_players == 1:
        print("PyNopoly only supports players 2-5");
        main_menu()
    elif num_players == 2:
        print("if 2");
        num_players = 2
        player1 = {'name':'player1', 'money':'1500'}
        player1['name'] = str(input("What is your name?"))
        player2 = {'name':'player2', 'money':'1500'}
        player2['name'] = str(input("What is your name?"))
	elif num_players == 3:
        num_players = 3
        player1 = {'name':'player1', 'money':'1500'}
        player1['name'] = str(input("What is your name?"))
        player2 = {'name':'player2', 'money':'1500'}
        player2['name'] = str(input("What is your name?"))
        player3 = {'name':'player3', 'money':'1500'}
        player3['name'] = str(input("What is your name?"))
		decide_player_order()
        print(player1['name'] + " " + player2['name'] + " " + player3['name'])
    elif num_players == 4:
        print("if 4");
        num_players = 4
        player1 = {'name':'player1', 'money':'1500'}
        player1['name'] = str(input("What is your name?"))
        player2 = {'name':'player2', 'money':'1500'}
        player2['name'] = str(input("What is your name?"))
        player3 = {'name':'player3', 'money':'1500'}
        player3['name'] = str(input("What is your name?"))
        player4 = {'name':'player4', 'money':'1500'}
        player4['name'] = str(input("What is your name?"))
    elif num_players == 5:
        print("if 5");
        num_players = 5
        player1 = {'name':'player1', 'money':'1500'}
        player2 = {'name':'player2', 'money':'1500'}
        player3 = {'name':'player3', 'money':'1500'}
        player4 = {'name':'player4', 'money':'1500'}
        player5 = {'name':'player5', 'money':'1500'}
    else:
        print("Not a proper input, try again.");
        main_menu()
main_menu()
def decide_player_order():
    print("decide player_order entered");
	while player2 < player1 and player2 < player3 and player2 < player4 and player2 < player5:
		player2 = random.randint(1, 12)
	while player3 < player1 and player3 < player2 and player3 < player4 and player3 < player5:
		player3 = random.randint(1, 12)
	while player4 < player1 and player4 < player2 and player4 < player3 and player4 < player5:
		player4 = random.randint(1, 12)
	while player5 < player1 and player5 < player2 and player5 < player3 and player5 < player4:
		player5 = random.randint(1, 12)
    #decided by python
def buy_property():
    print("buy property entered");
    #When landed on, you can choose to buy property
    #if you do not want it, then it is auctioned off (programmed later)
    #if the bank runs out of houses then players must wait to build houses/hotels
def sell_property():
    print("sell property entered");
    #houses/hotels sold back for half price
def mortgage():
    print("mortgage entered");
    #unimproved properties can be mortgaged
    #mortgage value is printed on the title card
    #no rent can be collected on mortgaged
    #to lift mortgage, pay mortgage + 10% interest
def pay_rent():
    print("pay rent entered");
    #Owner collects based on what is on title card
    #If mortgaged, no rent can be collected (variable for mortgaged)

    #If all properties are owned AND not upgraded, then rent is doubled.
    #However rent is much higher on upgraded properties
def chance():
    print("chance & comm chest entered");
    #take the top card, follow instructions, then return card to bottom of deck
    #get out of jail free is held until used, then returned to bottom of deck
    #jail free card may be sold to another player
def jail():
    print("jail entered");
    #token lands on go to jail
    #draw card go to jail
    #doubles 3 times in a row
    #Do not collect $200

    #Get out by:
    #Thowing doubles on any next turn (move the amount of spaces you roll)
    #Get out of jail free card
    #purchase jail free card from another player
    #pay a fine of $50 before rolling dice on next two turns
    #if doubles are not rolled by the third turn, $50 must be paid
    #property can still be bought and sold
def free_parking():
    print("free space, no money");
def change_player():
    print("change player entered");
def bankrupt():
    print("bankrupt entered");

			
			
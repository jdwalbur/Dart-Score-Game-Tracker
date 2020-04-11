def main():

    phrase = ''
    #start the game or get the instructions
    while phrase != 'start':
        phrase = input(
            'Excited to play some darts. Are you sure you know how. If you need help knowing the rules or how to '
            'use this program just type in help. When you are ready to play type in start: ')
        if phrase == 'help':
            print('*instructions*')
        elif phrase != 'start':
            print('Please enter start or help')
        else:
            #call game
            game(True)
            
def game(runGame):
    gameType = 0;

    #Select 301 game or 501 game
    while gameType == 0:
        try:
            gameType = int(input("Would you like to play a game of 301 or 501? "))
            if gameType != 301 and gameType != 501:
                gameType = 0
        except ValueError:
            print("Please enter 301 or 501")
            gameType = 0

    #select the number of players 1-4
    numPlayers = 0
    while numPlayers == 0:
        try:
            numPlayers = int(input("How many people are playing (1-4)"))
            if not(1<=numPlayers<=4):
                numPlayers = 0
        except ValueError:
            print("Enter a number between 1 and 4")
            numPlayers = 0

    #Dictionary to keep track of player name and score
    players = {}

    # Creates player names and a starting score of gameType for each player
    for i in range(numPlayers):
        name = input("Enter player" + str(i + 1) + " name: ")
        #Check to see if the name already exsists
        for key in players:
            if name == key:
                while name == key:
                    print("That name already exsists please enter a different one.")
                    name = input("Enter player" + str(i + 1) + " name: ")

        #Creating the player name, score, darts used.
        players[name] = [gameType,0]

    #runGame = True
    winner = False
    while runGame:

        for key in players:
            if not(winner):
                #take the key value (its a list) and place it into the variable playerStats
                playerStats = players[key]
                playerScore = playerStats[0]
                dartCount = playerStats[1]

                handScore = -1
                #get the hand score (shot score) from the user (score entered must be between 0-180)
                while handScore == -1:
                    try:
                        handScore = int(input("What was your hand score " + str(key) + ": "))
                        if not(0<=handScore<=180):
                            print("Your hand score can't be below 0 or above 180")
                            handScore = -1
                    except ValueError:
                        print("Your hand score can't be below 0 or above 180")
                        handScore = -1

                    playerScore = playerScore - handScore

                #check if the player busted
                if playerScore < 0 or playerScore == 1:
                    print("Bust!")
                    playerScore = playerScore + handScore
                    dartCount = dartCount + 3
                
                else:
                    if playerScore + handScore < 170:
                        dartsUsed = 0
                        while dartsUsed == 0:
                            try:
                                #ask the user for the number of darts they used
                                dartsUsed = int(input("How many darts did you use (1-3): "))
                                if not(1<=dartsUsed<=3):
                                    print("Enter a number between 1 and 3")
                                    dartsUsed = 0
                            except ValueError:
                                print("Enter a number between 1 and 3")
                            else:
                                dartCount = dartCount + dartsUsed
                                if playerScore == 0:
                                    print("\n", key, " is the winner!", sep="")
                                    winner = True
                                    runGame = False
                    else:
                        dartCount = dartCount + 3


                #update values and dictionary
                playerStats[0] = playerScore
                playerStats[1] = dartCount

                players[key] = playerStats

        #list out the current hand score for all players
        print("Scores:")
        for key in players:
                playerStats = players[key]
                print(key, ": ", playerStats[0], sep="")

    #ask the user if they want to see their stats for the game
    prompt = ""
    while prompt == "":
        prompt = input("Would you like to see your stats for the game?(yes/no): ")
        if prompt!="yes" and prompt !="no":
            prompt = ""
            print("Please enter yes or no")
        elif prompt == "yes":
            #call stats if they user entered yes
            stats(players, gameType)




def stats(players, gameType):
    print("Here are the player states for the game:")
    for key in players:
        playerStats = players[key]
        dartsUsed = playerStats[1]

        threeDartAvg = gameType/(dartsUsed/3)
        singleDartAvg = gameType/dartsUsed

        print("\nName: ", key, sep="")
        print("Darts Used: ", dartsUsed, sep="")
        print("Three Dart Avg: ", format(threeDartAvg, ".1f"), sep="")
        print("Single Dart Avg: ", format(singleDartAvg, ".1f"), "\n", sep="")


main()
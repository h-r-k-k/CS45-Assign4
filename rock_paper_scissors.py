import random

# this is the experimental no-ties version of rock-paper-scissors!!

def get_winner(input):
    """
    given a user's input selection of either rock/paper/scissor, let the computer pick a thing, print out the computer's selection,
    and return the name of the winner.
    """
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print("Computer's choice: " + computer_choice)
    winner = "none"
    if input == 'rock':
        if computer_choice == 'paper':
            winner = "computer"
        elif computer_choice == 'scissors':
            winner = "player"
    elif input == 'paper':
        if computer_choice == 'scissors':
            winner = "computer"
        elif computer_choice == 'rock':
            winner = "player"
    else:                                   # input == 'scissors'
        if computer_choice == 'rock':
            winner = "computer"
        elif computer_choice == 'paper':
            winner = "player"
    return winner


def main():
    # greet the user when it starts
    print('Greetings! \n')
    # explain the rules
    print('Let me explain the rules to you! You will play a rock-paper-scissors game with our computer.\nBoth player can choose one from the three things, and the winner is decided base on: \nrock==>scissors, scissors==>paper, paper==>rock! \n')
    print('now, your pick! (remember to type lower-case letters): ')
    # get the user input (assume the user will type in rock/paper/scissors (lower-case))
    x = input()
    y = get_winner(x)
    # declare a winner or a tie
    # if y == "none":
    #     print('There is a tie... \n')
    # else:
    #     print('~~~~The winner is: ' + y + '~~~~\n')
    while y == "none":
        # if there is a tie, keep matching until the tie breaks
        print('now, your pick again! (remember to type lower-case letters): ')
        x = input()
        y = get_winner(x)
    # after the tie breaks, declare the winner
    print('~~~~The winner is: ' + y + '~~~~\n')




if __name__ == '__main__':
    main()

import random
print('**** Welcome to the Rock / Paper / Scisosors ****')
computer_choise = random.randint(0, 2)
choise_player = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n'))
if choise_player > 2:
    print('Type a number 0, 1 or 2')
    rock = ("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)


    paper = ("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)


    scissors = ("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)
    game_images = [rock, paper, scissors]
    print(game_images[choise_player])
    print('Choise computer:')
    print(game_images[computer_choise])


    if choise_player == computer_choise:
        print('It`s a draw')
    elif choise_player == 0 and computer_choise == 2:
        print('You win!')
    elif choise_player == 2 and computer_choise == 1:
        print('You win!')
    elif choise_player == 1 and computer_choise == 0:
        print('You win!')

    else:
        print('You lose')
else:
    print('You lose')
    
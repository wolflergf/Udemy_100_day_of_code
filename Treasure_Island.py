print('Welcome to Treasure Island.\nYou mission is to find the treasure.')
print('You are in front a cave, there are two entrances, one a left another to right.')
entrance = input('Wich entry do you choose? Type Left or Right:'"\n").lower()
if entrance == 'left':
    print('You enter the very dark cave, but you find a torch, the torch you carry lights the way, you see a light at '
          'the end of the tunnel and find a lake.')
    print('''
    ___ __ 
   (_  ( . ) )__                  '.    \   :   /    .'
     '(___(_____)      __           '.   \  :  /   .'
                     /. _\            '.  \ : /  .'
                .--.|/_/__      -----____   _  _____-----
_______________''.--o/___  \_______________(_)___________
       ~        /.'o|_o  '.|  ~                   ~   ~
  ~            |/    |_|  ~'         ~
               '  ~  |_|        ~       ~     ~     ~
      ~    ~          |_|O  ~                       ~
             ~     ___|_||_____     ~       ~    ~
   ~    ~      .'':. .|_|A:. ..::''.
             /:.  .:::|_|.\ .:.  :.:\   ~
  ~         :..:. .:. .::..:  .:  ..:.       ~   ~    ~
             \.: .:  :. .: ..:: .lcf/
    ~      ~      ~    ~    ~         ~
               ~           ~    ~   ~             ~
        ~         ~            ~   ~                 ~
   ~                  ~    ~ ~                 ~

''')
    print('There is a island in the middle of the lake.')
    choise1 = input('Type "wait" for a boat or "swim" to across:'"\n").lower()
    if choise1 == 'wait':
        print('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.')
        print('''

                               ____
                  _           |---||            _
                  ||__________|SSt||___________||
                 /_ _ _ _ _ _ |:._|'_ _ _ _ _ _ _\`.
                /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\:`.
               /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\::`.
              /:.___________________________________\:::`-._
          _.-'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _`::::::`-.._
      _.-' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ `:::::::::`-._
    ,'_:._________________________________________________`:_.::::-';`
     `.'/ || |:::::`.'/::::::::`.'/::::::::`.'/::::::|.`.'/.|     :|
      ||  || |::::::||::::::::::||::::::::::||:::::::|..||..|     ||
      ||  || |  __  || ::  ___  || ::  __   || ::    |..||;||     ||
      ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_____||__
      ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_|_|_||,(
      ||_.|| | |::| || :: |:::| || :: |::|  || ::    |.'||..|    _||,|
   .-'::_.:'.:-.--.-::--.-:.--:-::--.--.--.-::--.--.-:.-::,'.--.'_|| |
    );||_|__||_|__|_||__|_||::|_||__|__|__|_||__|__|_|;-'|__|_(,' || '-
    ||||  || |. . . ||. . . . . ||. . . . . ||. . . .|::||;''||   ||:'
    ||||.;  _|._._._||._._._._._||._._._._._||._._._.|:'||,, ||,,
    '''''           ''         ''         ''         '''  ''



''')
        choise2 = input('Wich colour do you choose. Type the color above.'"\n").lower()
        if choise2 == 'red':
            print('''
               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

''')
            print('Burned by FIRE!')
        elif choise2 == 'yellow':
            print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
            print('You WIN!')
        elif choise2 == 'blue':
            print('game over blue')
        else:
            print('fim!')
    else:
        print('''                     _.---._     .---.
            __...---' .---. `---'-.   `.
        .-''__.--' _.'( | )`.  `.  `._ :
      .'__-'_ .--'' ._`---'_.-.  `.   `-`.
             ~ -._ -._``---. -.    `-._   `.
                  ~ -.._ _ _ _ ..-_ `.  `-._``--.._
                               -~ -._  `-.  -. `-._``--.._.--''.
                                    ~ ~-.__     -._  `-.__   `. `.
                                      jgs ~~ ~---...__ _    ._ .` `.
                                                      ~  ~--.....--~`''')
        print('Crocodile,eaten')
else:
    print('''
                                     _.-'
                                 _.-'
                 _____________.-'________________
                /         _.-' O                /|
               /  i====_======O      __________/ /
              /  / _.-'      O      /     _   /|/
             /  / | p       o      /     (   / /
            /  /           O      /_________/ /
           /  L===========O                /|/
          /______________O________________/ /
     aos |________________________________|/''')
    print('You enter the very dark cave, but you fell into a trap.')
    print('GAME OVER')

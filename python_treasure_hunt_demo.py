print('''
   _,---,_
 /'_______`\
(/'       `\|___________----------"""""""------,
 \#########||______                          /'
  ^^^^^^^^^||      """"""-----_____        /'
            \                      """--_/'
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
wallet = 50

print('''  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
''')

first = input("You find an old map with a red cross. It looks like an old fashion treasure map. What do you want to do?(ignore/search)\n").lower()
if first == "search":
  
  print('''
          ,  ,.~"""""~~..                                           ___
  )\,)\`-,       `~._                                     .'   ``._
  \  \ | )           `~._                   .-"""""-._   /         \
 _/ ('  ( _(\            `~~,__________..-"'          `-<           \
 )   )   `   )/)   )        \                            \           |
') /)`      \` \,-')/\      (                             \          |
(_(\ /7      |.   /'  )'  _(`                              |         |
    \\      (  `.     ')_/`                                |         /
     \       \   \                                         |        (
      \ )  /\/   /                                         |         `~._
       `-._)     |                                        /.            `~,
                 |                          |           .'  `~.          (`
                  \                       _,\          /       \        (``
                   `/      /       __..-i"   \         |        \      (``
                  .'     _/`-..--""      `.   `.        \        ) _.~<``
                .'    _.j     /            `-.  `.       \      '=< `
              .'   _.'   \    |               `.  `.      \
             |   .'       ;   ;               .'  .'`.     \
             \_  `.       |   \             .'  .'   /    .'
               `.  `-, __ \   /           .'  .'     |   (
                 `.  `'` \|  |           /  .-`     /   .'
                   `-._.--t  ;          |_.-)      /  .'
                          ; /           \  /      / .'
                         / /             `'     .' /
                        /,_\                  .',_(
                       /___(                 /___(   
        ''')
  
  second = input(f"You want to buy a horse but you only have ${wallet} for transport and food, as well as some kind of weapon. Do you want to buy or steal?(buy/steal)\n").lower()
  if second == "buy":
    print('''                     '
                    .      '      .
              .      .     :     .      .
               '.        ______       .'
                 '  _.-"`      `"-._ '
                  .'                '.
           `'--. /                    \ .--'`
                /                      \
               ;                        ;
          - -- |                        | -- -
               |     _.                 |
               ;    /__`A   ,_          ;
           .-'  \   |= |;._.}{__       /  '-.
              _.-""-|.' # '. `  `.-"{}<._
                    / 1938  \     \  x   `"
               ----/         \_.-'|--X----
               -=_ |         |    |- X.  =_
              - __ |_________|_.-'|_X-X##
              jgs `'-._|_|;:;_.-'` '::.  `"-
               .:;.      .:.   ::.     '::.
    ''')
    third = input("You visit a farmer and tell him you wish to enter the mountains in search for something and you need a horse. He offers you a choice between two horses. The best one is $50 and the other is older and slower but only $25. Which one do you want to buy? (fast/slow)\n").lower()
    if third == "fast":
      wallet -= 50
      print("Great! You now have a fast horse, but no money for food or a weapon. After a week you die in a struggle over a loaf of bread. Game over.")
    if third == "slow":
      wallet -= 25
      print('''
                o--o--=g=--o--o     
               /      .'       \
               o      '.       o
                \             /
                 o           o
                  \         /
                   o       o
                    \     /
                     o   o
                      \_/
                       =
                      .^.
                     '   '
                     '. .'
                       ! 
            ''')
      fourth = input("The farmer offers you a deal. He's missing a family necklace lost on the path you're headed. He offers you the horse for free as well as a full bag of food and water, if you promise to search for the necklace. Nice!\n You accept and head to the weapon shop to buy yourself some protection. The shop owner offers you a sword and a shield for $25 or a bow and arrows for the same amount. Which do you choose?(sword/bow)\n").lower()
      if fourth == "sword":
        print('''
                                .-.
                               {{@}}
               <>               8@8
             .::::.             888
         @\\/W\/\/W\//@         8@8
          \\/^\/\/^\//     _    )8(    _
           \_O_<>_O_/     (@)__/8@8\__(@)
      ____________________ `~"-=):(=-"~`
     |<><><>  |  |  <><><>|     |.|
     |<>      |  |      <>|     |S|
     |<>      |  |      <>|     |'|
     |<>   .--------.   <>|     |.|
     |     |   ()   |     |     |P|
     |_____| (O\/O) |_____|     |'|
     |     \   /\   /     |     |.|
     |------\  \/  /------|     |U|
     |       '.__.'       |     |'|
     |        |  |        |     |.|
     :        |  |        :     |N|
      \<>     |  |     <>/      |'|
       \<>    |  |    <>/       |.|
        \<>   |  |   <>/        |K|
         `\<> |  | <>/'         |'|
           `-.|  |.-`           \ /
              '--'               ^
              ''')
        print("Cool. You win!")
      if fourth == "bow":
        print("You suck. Game over.")
  else:
    print("You get caught stealing, the map is taken from you and you're put in jail. Game over.")
else:
  print("Game over.")
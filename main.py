print("\033[1;33mWelcome to the Top Trumps 'Most Handsome Computing Teachers' Simulator")
print()
dict = {}

import time, os
def part1():
  print()
  print("\033[34mYou will input details for Two fighters which you'll use for this game")
  time.sleep(2)
  x = 0
  while x <= 1:
    print()
    ask1 = input('\033[0mEnter The name of your Card: ')
    ask2 = input('Enter Stat for Intelligence: ')
    ask3 = input('Enter Stat for Handsomeness: ')
    ask4 = input('Enter Stat for Coding skills: ')
    ask5 = input('Enter Stat for Baldness level: ')

    dict[ask1] = {'Intelligence': ask2, 'Handsomeness': ask3, 'Coding Skills': ask4, 'Baldness': ask5}
    x += 1


def part2():
  os.system('clear')
  m = list(dict.keys())
  while True:
    print()
    time.sleep(1.5)
    ask = input(f'''Choose your Card
    1: Mr. {m[0]}
    2: Mr. {m[1]}
    >> ''')
    print()
    if ask == '1' or ask == '2':
      b = input('''Choose your Stat:
      1: Intelligence
      2: Handsomeness
      3: Coding Skills
      4: Baldness Level
      >> ''')
      print()
      if b == '1':
        e = dict[m[0]]['Intelligence']
        f = dict[m[1]]['Intelligence']
        if e > f:
          print(f'''\033[32m
          Mr. {m[0]} has an Intelligence Stat of {e}
          Mr. {m[1]} has an Intelligence Stat of {f}
          
          ************ Mr {m[0]} wins!!!***********''')
        elif e < f:
          print(f'''\033[32m
          Mr. {m[0]} has an Intelligence Stat of {e}
          Mr. {m[1]} has an Intelligence Stat of {f}
          
          ************ Mr {m[1]} wins!!!***********''')
        else:
          print(f'''\033[32m
          Mr. {m[0]} has an Intelligence Stat of {e}
          Mr. {m[1]} has an Intelligence Stat of {f}
          
          ************ No winner, No vanquished wins!!!***********''')
    
      elif b == '2':
        e = dict[m[0]]['Handsomeness']
        f = dict[m[1]]['Handsomeness']
        if e > f:
          print(f'''\033[32m
          Mr. {m[0]} has a Handsomeness Stat of {e}
          Mr. {m[1]} has a Handsomeness Stat of {f}
          
          ************ Mr {m[0]} wins!!!***********''')
        elif e < f:
          print(f'''\033[32m
          Mr. {m[0]} has a Handsomeness Stat of {e}
          Mr. {m[1]} has a Handsomeness Stat of {f}
          
          ************ Mr {m[1]} wins!!!***********''')
        else:
          print(f'''\033[32m
          Mr. {m[0]} has a Handsomeness Stat of {e}
          Mr. {m[1]} has a Handsomeness Stat of {f}
          
          ************ No winner, No vanquished wins!!!***********''')
    
      elif b == '3': 
        e = dict[m[0]]['Coding Skills']
        f = dict[m[1]]['Coding Skills']
        if e > f:
          print(f'''\033[32m
          Mr. {m[0]} has a Coding Skills Stat of {e}
          Mr. {m[1]} has a Coding Skills Stat of {f}
          
          ************ Mr {m[0]} wins!!!***********''')
        elif e < f:
          print(f'''\033[32m
          Mr. {m[0]} has a Coding Skills Stat of {e}
          Mr. {m[1]} has a Coding Skills Stat of {f}
          
          ************ Mr {m[1]} wins!!!***********''')
        else:
          print(f'''\033[32m
          Mr. {m[0]} has a Coding Skills Stat of {e}
          Mr. {m[1]} has a Coding Skills Stat of {f}
          
          ************ No winner, No vanquished wins!!!***********''')
    
      elif b == '4':
        e = dict[m[0]]['Baldness']
        f = dict[m[1]]['Baldness']
        if e > f:
          print(f'''\033[32m
          Mr. {m[0]} has a Baldness Stat of {e}
          Mr. {m[1]} has a Baldness Stat of {f}
          
          ************ Mr {m[0]} wins!!!***********''')
        elif e < f:
          print(f'''\033[32m
          Mr. {m[0]} has a Baldness Stat of {e}
          Mr. {m[1]} has a Baldness Stat of {f}
          
          ************ Mr {m[1]} wins!!!***********''')
        else:
          print(f'''\033[32m
          Mr. {m[0]} has a Baldness Stat of {e}
          Mr. {m[1]} has a Baldness Stat of {f}
          
          ************ No winner, No vanquished wins!!!***********''')
    
      else:
        print('\033[31mPlease select 1, 2, 3 or 4 to proceed!')
        continue
        
      print()    
      response = input('\033[0mYou want to play again? y/n: ')
      if response == 'y':
        os.system('clear')
        continue
      else:
        break

    else:
      print()
      print('Please, select 1 or 2')
      continue
  print('Goodbye!')
    

part1()
part2()
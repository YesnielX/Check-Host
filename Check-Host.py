#Check host
from os import sys, system
import os  
import time


#def check-host
def check_host():
  host = input('Enter de Host: ')
  print('')
  response = os.system("ping -c 1 " + host + " > /dev/null 2>&1")
  if response == 0:
    print('Waiting host . . . ')
    time.sleep(3)
    print ("%s The host works perfectly" % host)
    time.sleep(3)
    backmenu = input('Do you want to return to the start menu? [y/n].')
  else:
    print ("%s The host does not work (Does not respond)" % host)
    
  if backmenu == 'y':
    system('clear')
    system('cls')
    options()
    input('Check-Host> ')
    selected()
  else:
    system('clear')
    system('cls')
    print('''
  ======================================
   THANKS for using Check Host

      follow on github @jojosamass
  ======================================
    ''')
    time.sleep(5)
    system('clear')
    sys.exit()


def options():
  print('')
  print('''

 ========================================

  WELCOME TO CHEK HOST

              by @Jojosamass
       github.com/jojosamass

========================================

  ''')
  print('')
  print('1 = Check-Host')
  print('2 = Check-Update')
  print('3 = Exit')
  print('')

options() #print options
input_user = input('Check Host> ')


def selected():
  #option 1
  if input_user == '1': 
    system('clear')
    print ("Starting . ")
    time.sleep(1)
    system('clear')
    print ("Starting . . ")
    time.sleep(1)
    system('clear')
    print ("Starting . . .")
    time.sleep(1)
    system('clear')
    print(check_host())


#option 2
  if input_user == '2': 
    system('clear')
    print('')
    print('Checking Update . . . ')
    print('')
    print('')
    system('git clone https://github.com/jojosamass/Check-host')
    system('clear')
    print('update successful')
    time.sleep(2)
    input('Press Enter You Continue')
    system('clear')
    sys.exit()
#option 3
  if input_user == '3': 
    print('''
    ======================================
    THANKS for using Check Host

      follow on github @jojosamass
    ======================================
    ''')
    time.sleep(5)
    system('clear')
    system('cls')
    sys.exit()
    
selected()

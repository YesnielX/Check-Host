#Check host
import socket # import socket
from os import sys, system  
import time


#def check-host
def check_host():
  # default port for socket 
  port = 80
  host = input('Enter de Host: ')
  print('')
  try: 
    host_ip = socket.gethostbyname(host) 
  except socket.gaierror: 
  
    # this means could not resolve the host 
    print ("There was an error verifying the host")
    sys.exit() 
    print('')
  #  connecting to the server 
  s.connect((host_ip, port)) 

  
  print ("the host is working perfectly, connected to on port %s" %(host_ip) )
  time.sleep(3)
  print('')
  backmenu = input('Do you want to return to the start menu? [y/n].')
  if backmenu == 'y':
    system('clear')
    options()
    input('Check-Host>')
    selected()
  else:
    system('clear')
    sys.exit()


def options():
  print('')
  print('''

 ========================================

  WELCOME TO CHEK-HOST

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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

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

  else:
    sys.exit()

#option 2
  if input_user == '2': 
    system('clear')
    system('git clone https://github.com/jojosamass/Check-host')

  else:
    sys.exit()

#option 1
  if input_user == '3': 
    system('clear')
    sys.exit()
    
selected()

import random

x=0

available_nums=[1,2,3,4,5,6,7,8,9]
gameBoard= [[1,2,3],[4,5,6],[7,8,9]]
rows=3
cols=3

def buildGameBoard():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(cols):
            print("", gameBoard[x][y], "|", end="")
    print("\n+---+---+---+")

def modifyGameBoard(num, turn):
    num-=1
    if (num==1):
        gameBoard[0][0]=turn
    elif (num==2):
        gameBoard[0][1]=turn
    elif (num==3):
        gameBoard[0][2]=turn
    elif (num==4):
        gameBoard[1][0]=turn
    elif (num==5):
        gameBoard[1][1]=turn
    elif (num==6):
        gameBoard[1][2]=turn
    elif (num==7):
        gameBoard[2][0]=turn
    elif (num==8):
        gameBoard[2][1]=turn
    elif (num==9):
        gameBoard[2][2]=turn

def checkForWinner(gameBoard):
  if(gameBoard[0][0] == 'X' and gameBoard[0][1] == 'X' and gameBoard[0][2] == 'X'):
    print("X has won!")
    return "X"
  elif(gameBoard[0][0] == 'O' and gameBoard[0][1] == 'O' and gameBoard[0][2] == 'O'):
    print("O has won!")
    return "O"
  elif(gameBoard[1][0] == 'X' and gameBoard[1][1] == 'X' and gameBoard[1][2] == 'X'):
    print("X has won!")
    return "X"
  elif(gameBoard[1][0] == 'O' and gameBoard[1][1] == 'O' and gameBoard[1][2] == 'O'):
    print("O has won!")
    return "O"
  elif(gameBoard[2][0] == 'X' and gameBoard[2][1] == 'X' and gameBoard[2][2] == 'X'):
    print("X has won!")
    return "X"
  elif(gameBoard[2][0] == 'O' and gameBoard[2][1] == 'O' and gameBoard[2][2] == 'O'):
    print("O has won!")
    return "O"
  if(gameBoard[0][0] == 'X' and gameBoard[1][0] == 'X' and gameBoard[2][0] == 'X'):
    print("X has won!")
    return "X"
  elif(gameBoard[0][0] == 'O' and gameBoard[1][0] == 'O' and gameBoard[2][0] == 'O'):
    print("O has won!")
    return "O"
  elif(gameBoard[0][1] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][1] == 'X'):
    print("X has won!")
    return "X"
  elif(gameBoard[0][1] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][1] == 'O'):
    print("O has won!")
    return "O"
  elif(gameBoard[0][2] == 'X' and gameBoard[1][2] == 'X' and gameBoard[2][2] == 'X'):
    print("X has won!")
    return "X"
  elif(gameBoard[0][2] == 'O' and gameBoard[1][2] == 'O' and gameBoard[2][2] == 'O'):
    print("O has won!")
    return "O"
  elif(gameBoard[0][0] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][2] == 'X'):
    print("X has won!")
    return "X"
  elif(gameBoard[0][0] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][2] == 'O'):
    print("O has won!")  
    return "O"
  elif(gameBoard[0][2] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][0] == 'X'):
    print("X has won!")  
    return "X"
  elif(gameBoard[0][2] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][0] == 'O'):
    print("O has won!") 
    return "O" 
  else:
    return "N"
  
#main

leaveloop=False
turncount=0
print("hi")
while leaveloop==False:
    if (turncount % 2==0):
        buildGameBoard()
        numberPicked=int(input("Pick your play(Numbers 1-9)"))
        if numberPicked <= 9 or numberPicked >= 1:
            modifyGameBoard(numberPicked,"X")
            available_nums.remove(numberPicked)
        else:
            print("Invalid number entered, please pick again")
        turncount= turncount+1
    else:
        while(True):
            cpuChoice = random.choice(available_nums)
            if(cpuChoice in available_nums):
                modifyGameBoard(cpuChoice, 'O')
                available_nums.remove(cpuChoice)
                turncount += 1
                break

    winner = checkForWinner(gameBoard)
    if(winner != "N"):
        print("\nGame over! Thank you for playing :)")
        break

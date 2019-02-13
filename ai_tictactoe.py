# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 20:51:43 2019

@author: Blume
"""
#Initialize the board with ' ' in the range between 0-9
board=[' ' for x in range(10)]
def insertLetter(letter,pos):
    #Assigns the board with the letter('X' or 'O') at particular position
    board[pos]=letter
def spaceIsFree(pos):
    #Checks if the board is empty at that position or not
    return board[pos]==' '
def printBoard(board):
    #Prints the board
    print('   |   |')
    print(' '+ board[1]+' | '+board[2]+' | '+board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+ board[4]+' | '+board[5]+' | '+board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+ board[7]+' | '+board[8]+' | '+board[9])
    print('   |   |')
def isWinner(brd,letter):
    #Checks the winner or not
    return ((brd[1]==letter and brd[2]==letter and brd[3]==letter) or (brd[4]==letter and brd[5]==letter and brd[6]==letter) or (brd[7]==letter and brd[8]==letter and brd[9]==letter) or (brd[1]==letter and brd[4]==letter and brd[7]==letter) or (brd[2]==letter and brd[5]==letter and brd[8]==letter) or (brd[3]==letter and brd[6]==letter and brd[9]==letter) or (brd[1]==letter and brd[5]==letter and brd[9]==letter) or (brd[3]==letter and brd[5]==letter and brd[7]==letter))
def playerMove():
    run=True
    while run:
        move=input('Please select a position to place X from 0-9:\t')
        try:
            move=int(move)
            if(move>0 and move<10):
                if(spaceIsFree(move)):
                    run=False
                    insertLetter('X',move)
                else:
                    print('Sorry, This place is Occupied')
            else:
                print('Please type a number within the range of 0-9')
        except:
            print('Please type a integer number')
def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
   
    #Check for possible winning move to take or to block opponents winning move
    for let in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
 
 
    #Try to take one of the corners
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
   
    #Try to take the center
    if 5 in possibleMoves:
        move = 5
        return move
 
    #Take any edge
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
 
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
 
    return move
def selectRandom(li):
    import random
    ln=len(li)
    r=random.randrange(0,ln)
    return li[r]
def BoardFull(board):
    if board.count(' ')>1:
        return False
    else:
        return True
def main():
    print('\t\t\t Welcome to Tic Tac Toe!')
    ct=0  
    printBoard(board)
    while not(BoardFull(board)):
        if not(isWinner(board,'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry Computer won this time!')
            ct=ct+1
            break
        if not(isWinner(board,'X')):
            move=compMove()
            insertLetter('O',move)
            print('Computer placed an O in position :',move)
            printBoard(board)
        else:
            print('You won this time. Good Job!')
            ct=ct+1
            break
    if BoardFull(board) and ct==0:
        print('\t\t Tie Game!')
main()
 
while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('\t\t-----------------------------------------------')
        main()
    else:
        break
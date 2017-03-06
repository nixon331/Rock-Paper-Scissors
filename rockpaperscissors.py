'''
Created on 27 Feb 2017

@author: James.Nixon
'''
import sys

Player1 = input("Player 1 please insert name: ")
Player2 = input("Player 2 please insert name: ")
Answer1 = input("%s please pick Rock, Paper or Scissor " % Player1)
if(Answer1 != "Rock" and Answer1 != "Paper" and Answer1 != "Scissor"):
    print("you must enter a valid option")
Answer2 = input("%s please pick Rock, Paper or Scissor " % Player2)
if(Answer2 != "Rock" and Answer2 != "Paper" and Answer2 != "Scissor"):
    print("you must enter a valid option")
        
def compare(Answer1, Answer2):        
    if Answer1 == Answer2:
        return("It's a tie!")
    elif Answer1 == 'Rock':
        if Answer2 == 'Scissor':
            return("%s wins!" % Player1)
        else:
            return("%s wins!" % Player2)
    elif Answer1 == 'Scissor':
        if Answer2 == 'Paper':
            return("%s wins!" % Player1)
        else:
            return("%s wins!" % Player2)
    elif Answer1 == 'Paper':
        if Answer2 == 'Rock':
            return("%s wins!" % Player1)
        else:
            return("%s wins!" % Player2)
        
print(compare(Answer1, Answer2))
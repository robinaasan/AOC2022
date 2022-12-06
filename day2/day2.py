
#win -> hand + 6
#draw -> hand + 3 
#loss -> hand + 0

# rock -> 1
# paper -> 2
# scissor -> 3 
from aenum import MultiValueEnum
from enum import Enum

class Action(MultiValueEnum):
    ROCK = "A", "X"
    PAPER = "B", "Y"
    SCISSOR = "C", "Z"
    
class ActionRigged(Enum):
    WIN = "Z"
    DRAW = "Y"
    LOSE = "X"

class Outcome(Enum):
    WIN = 6
    LOSS = 0
    DRAW = 3
    
def valueHand(our_hand: Action):
    match our_hand:
        case Action.ROCK:
            return 1
        case Action.PAPER:
            return 2
        case Action.SCISSOR:
            return 3
        case _:
            raise ValueError("Actions only allowed!")
    
def determineWinner(his_hand: Action, our_hand: Action):
    points = valueHand(our_hand)
    
    if his_hand == our_hand:
        points += Outcome.DRAW.value
    elif our_hand == Action.ROCK:
        if his_hand == Action.PAPER:
            points += Outcome.LOSS.value
        elif his_hand == Action.SCISSOR:
            points += Outcome.WIN.value
            
    elif our_hand == Action.PAPER:
        if his_hand == Action.SCISSOR:
            points += Outcome.LOSS.value
        elif his_hand == Action.ROCK:
            points += Outcome.WIN.value
            
    elif our_hand == Action.SCISSOR:
        if his_hand == Action.ROCK:
            points += Outcome.LOSS.value
        elif his_hand == Action.PAPER:
            points += Outcome.WIN.value
    return points
            
def readGames():
    points = 0
    with open('input.txt', 'r', encoding='UTF8') as elf_file:
        #print(int(calories))
        for line in elf_file:
            line = line.strip()
            hands = line.split(" ")

            hisHandAction = Action(hands[0])
            ourHandAction = Action(hands[1])
            
            points += determineWinner(hisHandAction, ourHandAction)
        return points
        
def determineWinner2(his_hand: Action, rigged_outcome: ActionRigged):
    if rigged_outcome == ActionRigged.DRAW:
        if his_hand == Action.ROCK:
            return Outcome.DRAW.value + valueHand(Action.ROCK)
        elif his_hand == Action.PAPER:
            return Outcome.DRAW.value + valueHand(Action.PAPER)    
        if his_hand == Action.SCISSOR:
            return Outcome.DRAW.value + valueHand(Action.SCISSOR)
            
    elif rigged_outcome == ActionRigged.WIN:
        if his_hand == Action.ROCK:
            return Outcome.WIN.value + valueHand(Action.PAPER)
        elif his_hand == Action.PAPER:
            return Outcome.WIN.value + valueHand(Action.SCISSOR)
        elif his_hand == Action.SCISSOR:
            return Outcome.WIN.value + valueHand(Action.ROCK)
            
    elif rigged_outcome == ActionRigged.LOSE:
        if his_hand == Action.ROCK:
            return Outcome.LOSS.value + valueHand(Action.SCISSOR)
        elif his_hand == Action.PAPER:
            return Outcome.LOSS.value + valueHand(Action.ROCK)
        elif his_hand == Action.SCISSOR:
            return Outcome.LOSS.value + valueHand(Action.PAPER)        

def getGames2():
    points = 0
    with open('input.txt', 'r', encoding='UTF8') as elf_file:
        #print(int(calories))
        for line in elf_file:
            line = line.strip()
            hands = line.split(" ")

            hisHandAction = Action(hands[0])
            ourHandAction = ActionRigged(hands[1])
            
            points += determineWinner2(hisHandAction, ourHandAction)
        return points
        
if __name__ == "__main__":
    points = readGames()
    print(f"1) We got: {points} points\n")
    
    pointsRigged = getGames2()
    print(f"2) We got: {pointsRigged} points\n")
    
"""
Game of Sticks
COMP.CS.100
Riia Hiironniemi
A code for a game called "Game of Sticks". There are first 21 sticks and two players remove 1-3 sticks at a time. One who
removes the last stick is the loser.
"""
def main():
        print("Game of sticks")
        sticks=21
        while sticks>0:
                p1 = int(input("Player 1 enter how many sticks to remove: "))
                while p1>3 or p1<=0:
                        print("Must remove between 1-3 sticks!")
                        p1 = int(input("Player 1 enter how many sticks to remove: "))
                sticks=sticks-p1
                if sticks<=0:
                        loser="1"
                        pass
                else:
                        print("There are", sticks, "sticks left")
                if sticks>0:
                        p2 = int(input("Player 2 enter how many sticks to remove: "))
                        while p2>3 or p2<=0:
                                print("Must remove between 1-3 sticks!")
                                p2 = int(input("Player 2 enter how many sticks to remove: "))
                        sticks = sticks - p2
                        if sticks <= 0:
                                loser="2"
                                pass
                        else:
                                print("There are", sticks, "sticks left")
        print("Player",loser,"lost the game!")
if __name__ == "__main__":
        main()

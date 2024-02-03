import os

clear = lambda : os.system("cls||clear")

class TicTacToe:

    def __init__(self) -> None:
        self.table_game = Table_game()

    def start(self):
        print(self.table_game.verify_winner())
        while not self.table_game.verify_winner():
            clear()
            self.table_game.table()
            player1 = int(input("Digite um posição P1: "))
            while not self.table_game.play(player1, "X"):
                player1 = int(input("Digite um posição P1: "))
            clear()
            self.table_game.table()
            if self.table_game.verify_winner():
                break
            player2 = int(input("Digite uma posição P2: "))
            while not self.table_game.play(player2, "O"):
                player2 = int(input("Digite um posição P1: "))
            clear()
            self.table_game.table()
            
            

                                       
        
        
class Table_game:

    def __init__(self) -> None:
        self.__a1 = ""
        self.__a2 = ""
        self.__a3 = ""
        self.__b1 = ""
        self.__b2 = ""
        self.__b3 = ""
        self.__c1 = ""
        self.__c2 = ""
        self.__c3 = ""
    
    def table(self) -> None:
        
        print(f"{"":^7}" +"|" + f"{"":^7}" + "|" + f"{"":^7}")
        print(f"{self.__a1:^7}"+ "|" + f"{self.__a2:^7}" + "|" + f"{self.__a3:^7}")
        print( "-"*7 + "|" + "-"*7 + "|" + "-"*7) 
        print(f"{"":^7}" +"|" + f"{"":^7}" + "|" + f"{"":^7}")
        print(f"{self.__b1:^7}"+ "|" + f"{self.__b2:^7}" + "|" + f"{self.__b3:^7}")
        print( "-"*7 + "|" + "-"*7 + "|" + "-"*7) 
        print(f"{"":^7}" +"|" + f"{"":^7}" + "|" + f"{"":^7}")
        print(f"{self.__c1:^7}"+ "|" + f"{self.__c2:^7}" + "|" + f"{self.__c3:^7}")

        
    def verify_winner(self) -> bool:
        if ((self.__a1 == self.__a2 == self.__a3) and (self.__a1!= ""and self.__a2 != "" and self.__a3 != "")):
            return True
        elif((self.__a1 == self.__b2 == self.__c3) and (self.__a1!= ""and self.__b2 != "" and self.__c3 != "")):
            return True
        elif((self.__a1 == self.__b1 == self.__c1) and (self.__a1!= ""and self.__b1 != "" and self.__c1 != "")):
            return True
        elif((self.__b1 == self.__b2 == self.__b3) and (self.__b1!= ""and self.__b2 != "" and self.__b3 != "")):
            return True
        elif((self.__a2 == self.__b2 == self.__c2) and (self.__a2!= ""and self.__b2 != "" and self.__c2 != "")):
            return True
        elif((self.__a3 == self.__b3 == self.__c3) and (self.__a3!= ""and self.__b3 != "" and self.__c3 != "")):
            return True
        elif((self.__c1 == self.__c2 == self.__c3) and (self.__c1!= ""and self.__c2 != "" and self.__c3 != "")):
            return True
        else:
            return False
        
    def play(self, position: int, character: str) -> None:
            if position == 1 and self.__a1 == "":
                self.__a1 = character
                return True
            elif position == 2 and self.__a2 == "":
                self.__a2 = character
                return True
            elif position == 3 and self.__a3 == "":
                self.__a3 = character
                return True
            elif position == 4 and self.__b1 == "":
                self.__b1 = character
                return True
            elif position == 5 and self.__b2 == "":
                self.__b2 = character
                return True
            elif position == 6 and self.__b3 == "":
                self.__b3 = character
                return True
            elif position == 7 and self.__c1 == "":
                self.__c1 = character
                return True
            elif position == 8 and self.__c2 == "":
                self.__c2 = character
                return True
            elif position == 9 and self.__c3 == "":
                self.__c3 = character
                return True
            else:
                print("Erro! Posição inválida!")
                return False

game1 = TicTacToe()
game1.start()

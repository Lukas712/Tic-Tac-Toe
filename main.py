import os
from typing import Type
clear = lambda : os.system("cls||clear")

class TicTacToe:

    def __init__(self) -> None:
        self.table_game = Table_game()
        self.__player1 = Player("X")
        self.__player2 = Player("O")

    def __verificar_partida(self) -> bool:
        matriz = self.table_game.get_table()
        contador = 0
        for i in range(9):
            if matriz.get_element_by_id(i) != "":
                contador+=1
        if contador == 9:
            return True
        if matriz.get_element_by_id(0) == matriz.get_element_by_id(1) == matriz.get_element_by_id(2) and matriz.get_element_by_id(0) != "" and matriz.get_element_by_id(1) != "" and matriz.get_element_by_id(2) != "":
            return True
        elif matriz.get_element_by_id(0) == matriz.get_element_by_id(3) == matriz.get_element_by_id(6) and matriz.get_element_by_id(0) != "" and matriz.get_element_by_id(3) != "" and matriz.get_element_by_id(6) != "":
            return True
        elif matriz.get_element_by_id(0) == matriz.get_element_by_id(4) == matriz.get_element_by_id(8) and matriz.get_element_by_id(0) != "" and matriz.get_element_by_id(4) != "" and matriz.get_element_by_id(8) != "":
            return True
        elif matriz.get_element_by_id(1) == matriz.get_element_by_id(4) == matriz.get_element_by_id(7) and matriz.get_element_by_id(1) != "" and matriz.get_element_by_id(4) != "" and matriz.get_element_by_id(7) != "":
            return True
        elif matriz.get_element_by_id(2) == matriz.get_element_by_id(5) == matriz.get_element_by_id(8) and matriz.get_element_by_id(2) != "" and matriz.get_element_by_id(5) != "" and matriz.get_element_by_id(8) != "":
            return True
        elif matriz.get_element_by_id(3) == matriz.get_element_by_id(4) == matriz.get_element_by_id(5) and matriz.get_element_by_id(3) != "" and matriz.get_element_by_id(4) != "" and matriz.get_element_by_id(5) != "":
            return True
        elif matriz.get_element_by_id(6) == matriz.get_element_by_id(7) == matriz.get_element_by_id(8) and matriz.get_element_by_id(6) != "" and matriz.get_element_by_id(7) != "" and matriz.get_element_by_id(8) != "":
            return True
        elif matriz.get_element_by_id(2) == matriz.get_element_by_id(4) == matriz.get_element_by_id(6) and matriz.get_element_by_id(2) != "" and matriz.get_element_by_id(4) != "" and matriz.get_element_by_id(6) != "":
            return True
        else:
            return False
    
    def start(self):
        self.table_game.print_table()
        matriz = self.table_game.get_table()
        
        while not self.__verificar_partida():
            try:
                position_player1 = int(input("Player 1 - Digite a posição: "))
            except:
                print("Erro!")
            while matriz.get_element_by_id(position_player1) != "":
                try:
                    position_player1 = int(input("Player 1 - Digite a posição: "))
                except:
                    print("Erro!")
            self.__player1.jogar(matriz.get_celula(position_player1))

            self.table_game.print_table()
            if self.__verificar_partida():
                break
            try:
                position_player2 = int(input("Player 2 - Digite a posição: "))
            except:
                print("Erro!")
            while matriz.get_element_by_id(position_player2) != "":
                try:
                    position_player2 = int(input("Player 2 - Digite a posição: "))
                except:
                    print("Erro!")
            self.__player2.jogar(matriz.get_celula(position_player2))
            self.table_game.print_table()




            

            
            

class Table_game:

    def __init__(self) -> None:
        self.__values = Matriz()

    def print_table(self) -> None:
        print(f"{"":^7}" +"|" + f"{"":^7}" + "|" + f"{"":^7}")
        print(f"{self.__values.get_element_by_id(0):^7}"+ "|" + f"{self.__values.get_element_by_id(1):^7}" + "|" + f"{self.__values.get_element_by_id(2):^7}")
        print( "-"*7 + "|" + "-"*7 + "|" + "-"*7) 
        print(f"{"":^7}" +"|" + f"{"":^7}" + "|" + f"{""}")
        print(f"{self.__values.get_element_by_id(3):^7}"+ "|" + f"{self.__values.get_element_by_id(4):^7}" + "|" + f"{self.__values.get_element_by_id(5):^7}")
        print( "-"*7 + "|" + "-"*7 + "|" + "-"*7) 
        print(f"{"":^7}" +"|" + f"{"":^7}" + "|" + f"{"":^7}")
        print(f"{self.__values.get_element_by_id(6):^7}"+ "|" + f"{self.__values.get_element_by_id(7):^7}" + "|" + f"{self.__values.get_element_by_id(8):^7}")

    def get_table(self) -> any:
        return self.__values
    
class ValorCelula:

    def __init__(self):
        self.__charactere = ""
        self.__position = 0

    def set_charactere(self, charactere: str) -> None:
        if self.__verifica_caractere():
            self.__charactere = charactere
        else:
            self.__erro_caractere()

    def __verifica_caractere(self) -> bool:
        return self.__charactere == ""
    
    def __erro_caractere(self) -> None:
        print("Erro, posição já ocupada")

    def get_charactere(self) -> str:
        return self.__charactere

    def avanca_posicao(self) -> None:
        if self.__verifica_posicao(self.__position + 1):
            self.__position+=1
        else:
            self.__erro_posicao()

    def volta_posicao(self) -> None:
        if self.__verifica_posicao(self.__position-1):
            self.__position-=1
        else:
            self.__erro_posicao()

    def __verifica_posicao(self, position: int) -> bool:
        return 9 > position >= 0
    
    def __erro_posicao(self) -> None:
        print("Posição Inválida!")

    def get_position(self) -> int:
        return self.__position

class Matriz:

    def __init__(self) -> None:
        self.__elementos = []
        self.__elements()

    def __elements(self):
        for i in range(9):
            self.__elementos.append(ValorCelula())
    
    def get_element_by_id(self, id: int):
        if self.__verifica_id(id):
            charactere = self.__elementos[id]
            return charactere.get_charactere()
        else:
            self.__erro_id()

    def __verifica_id(self, id: int) -> bool:
        return type(id) == int and (9 > id >= 0)

    def __erro_id(self) -> None:
        print("Indíce inválido")

    def get_celula(self, id: int):
        if self.__verifica_id(id):
            celula = self.__elementos[id]
            return celula
        else:
            self.__erro_id()
class Player:

    def __init__(self, charactere:str) -> None:
        self.__charactere = charactere

    def get_charactere(self) -> str:
        if self.__verifica_charactere():
            return self.__charactere
        else:
            self.__erro_charactere()

    
    def __verifica_charactere(self) -> bool:
        return type(self.__charactere) == str

    def __erro_charactere(self) -> bool:
        print("Caractere inválido!")

    def jogar(self, position: Type[ValorCelula]) -> None:
        if self.__verifica_charactere():
                if isinstance(position, ValorCelula):
                    position.set_charactere(self.__charactere)
        else:
            self.__erro_charactere()
            return False
    

    
game1 = TicTacToe()
game1.start()
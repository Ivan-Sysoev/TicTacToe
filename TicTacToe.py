from time import sleep

class Game:
    playing_feild = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    x_database = []
    o_database = []
    x_moves_number = 0
    o_moves_number = 0
    steps_history = []

    indexes_database = {"A1": 0, "A2": 1, "A3": 2, "B1": 3, "B2": 4, "B3": 5, "C1": 6, "C2": 7, "C3": 8}
    winning_combinations = (["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"], ["A1", "B1", "C1"] , ["A2", "B2", "C2"], ["A3", "B3", "C3"], ["A1", "B2", "C3"], ["C1", "B2", "A3"])

    def printer(cls, b):
        print(f'\n"1" "2" "3"\n {b[0]} | {b[1]} | {b[2]} "A"\n-----------\n {b[3]} | {b[4]} | {b[5]} "B"\n-----------\n {b[6]} | {b[7]} | {b[8]} "C"\n')


    def x_step(cls):
        try:
            step = input("Выберете поле: ").upper()
            if step in cls.steps_history:  
                print("Выберите свободное поле")
                cls.x_step()
            cls.steps_history.append(step)
            index = cls.indexes_database[step]
            cls.x_moves_number = cls.x_moves_number + 1
            cls.playing_feild[index] = "x"
            cls.x_database.append(step)
            cls.printer(cls.playing_feild)
        except:
            print("Неверный ввод")
            cls.x_step()
    def o_step(cls):
        try:
            step = input("Выберете поле: ").upper()
            if step in cls.steps_history:  
                print("Выберите свободное поле")
                cls.o_step()
            cls.steps_history.append(step)
            index = cls.indexes_database[step]
            cls.o_moves_number = cls.o_moves_number + 1
            cls.playing_feild[index] = "o"
            cls.o_database.append(step)
            cls.printer(cls.playing_feild)
        except:
            print("Неверный ввод")
            cls.o_step()

    def x_winner(cls):
        for comb in cls.winning_combinations:
            if set(cls.x_database + comb) == set(cls.x_database):
                return True
        return False

    def o_winner(cls):
        for comb in cls.winning_combinations:
            if set(cls.o_database + comb) == set(cls.o_database):
                return True
        return False

    def check_winner(cls):
        """Проверка может ли продолжаться игра или кто-то уже выйграл"""
        if cls.x_winner():
            print(f"Победили крестики!\nЧисло ходов: {cls.x_moves_number - 1}")
            return False
        elif cls.o_winner():
            print(f"Победили нолики!\nЧисло ходов: {cls.o_moves_number - 1}")
            return False
        elif len([elem for elem in cls.playing_feild if elem != " "]) == 9:
            print("Ничья!")
            return False
        else:
            return True

    def run(cls):
        cls.x_step()
        cls.o_step()
        cls.x_step()
        cls.o_step()
        cls.x_step()
        while True:
            if cls.check_winner():
                cls.o_step()
                if cls.check_winner():
                    cls.x_step()
                else:
                    break
            else:
                break

Game().run()
sleep(5)
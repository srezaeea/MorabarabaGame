BOT_CHAR = '#'
USER_CHAR = '&'
WIN_STATES = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11), (12, 13, 14), (15, 16, 17), (18, 19, 20), (21, 22, 23),
              # horizontal
              (0, 9, 21), (3, 10, 18), (6, 11, 15), (1, 4, 7), (16, 19, 22), (8, 12, 17), (5, 13, 20), (2, 14, 23),
              # vertical
              (0, 3, 6), (2, 5, 8), (17, 20, 23), (15, 18, 21)
              # diagonal
              ]

GAME_LEVEL = 5  # you can change level of gam's robot by changing this number


class Board:
    def __init__(self, turn_is_user):
        self.robot_grade = 0
        self.user_grade = 0
        self.turn_is_user = turn_is_user

        self.indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

        self.states = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            , ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def showBoard(self):
        grade = f"{self.robot_grade}:{self.user_grade}"
        print(f"""
                    {self.states[0]}-------------{self.states[1]}-------------{self.states[2]}
                    |  .          |          .  |                                          
                    |    {self.states[3]}--------{self.states[4]}--------{self.states[5]}    |
                    |    |  .     |      . |    |                               
                    |    |   {self.states[6]}----{self.states[7]}----{self.states[8]}   |    |
                    |    |   |         |   |    |
                    {self.states[9]}----{self.states[10]}---{self.states[11]}   {grade}   {self.states[12]}---{self.states[13]}----{self.states[14]}
                    |    |   |         |   |    |                                          
                    |    |   {self.states[15]}----{self.states[16]}----{self.states[17]}   |    |
                    |    | .      |      . |    |                                          
                    |    {self.states[18]}--------{self.states[19]}--------{self.states[20]}    |
                    |  .          |           . |
                    {self.states[21]}-------------{self.states[22]}-------------{self.states[23]}
                    """)

    def add_point(self, index, is_user: bool):
        if is_user:
            if index in self.indexes:
                self.states[index] = self.states[index] = USER_CHAR
                self.indexes.remove(index)
                self.calculate_grade()
                self.showBoard()
                return True
            else:
                return False
        else:
            self.states[index] = self.states[index] = BOT_CHAR
            self.indexes.remove(index)

        self.calculate_grade()
        self.showBoard()

        return index

    def board_is_full(self):
        if len(self.indexes) == 0:
            return True
        return False

    def calculate_grade(self):
        grade = 0
        for item in WIN_STATES:
            if self.states[item[0]] == BOT_CHAR and self.states[item[1]] == BOT_CHAR and self.states[
                item[2]] == BOT_CHAR:
                grade += 1
            elif self.states[item[0]] == USER_CHAR and self.states[item[1]] == USER_CHAR and self.states[
                item[2]] == USER_CHAR:
                grade -= 1

            self.robot_grade = grade
            self.user_grade = -1 * grade

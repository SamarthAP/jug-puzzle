class Jug:
    """
    Jug class represents and manipulates amount of liquid in a jug with a certain capacity
    """
    def __init__(self, amount, cap):
        """
        Create a new Jug with a certain amount of liquid and capacity
        :param amount: amount of liquid
        :param cap: capacity of Jug

        >>> jug1 = Jug(0,8)
        >>> print(jug1)
        (0/8)
        >>> jug2 = Jug(5,5)
        >>> print(jug2)
        (5/5)
        >>> jug3 = Jug(2,4)
        >>> print(jug3)
        (2/4)
        >>> jug4 = Jug(5,2)
        Amount has to be less than capacity AND equal to 0 or more
        >>> jug5 = Jug(-1,2)
        Amount has to be less than capacity AND equal to 0 or more
        """
        if 0 <= amount <= cap:  # if statement used so amount can't be more than capacity or less than 0
            self.amount = amount
            """
            Amount of liquid
            0 <= amount <= cap
            """
            self.cap = cap
            """
            Capacity of the Jug
            0 < cap >= amount
            """
            self.space = self.cap - self.amount
            """
            The space remaining in a Jug
            0 <= space <= cap
            """
        else:
            print('Amount has to be less than capacity AND equal to 0 or more')

    def calculate_space(self):
        """
        Calculates the space remaining in a jug

        >>> jug1 = Jug(3, 5)
        >>> jug1.space
        2
        >>> jug2 = Jug(0, 5)
        >>> jug2.space
        5
        >>> jug3 = Jug(8, 8)
        >>> jug3.space
        0
        """
        self.space = self.cap - self.amount

    def __str__(self):
        """
            none -> String
        Returns a string representation of a Jug
        :return: amount and cap of Jug

        >>> jug1 = Jug(0,8)
        >>> print(jug1)
        (0/8)
        >>> jug2 = Jug(5,5)
        >>> print(jug2)
        (5/5)
        >>> jug3 = Jug(2,4)
        >>> print(jug3)
        (2/4)
        """
        return '({0}/{1})'.format(self.amount, self.cap)

    def spillinto(self, jug):
        """
            (Jug) ->, None
        Spill liquid from one jug to another
        :param jug: jug that is being spilled into

        >>> jug1 = Jug(3, 5)
        >>> jug2 = Jug(0, 8)
        >>> jug1.spillinto(jug2)
        >>> print(jug1)
        (0/5)
        >>> print(jug2)
        (3/8)

        >>> jug3 = Jug(8, 8)
        >>> jug4 = Jug(5, 5)
        >>> jug3.spillinto(jug4)
        >>> print(jug3)
        (8/8)
        >>> print(jug4)
        (5/5)

        >>> jug5 = Jug(9, 9)
        >>> jug6 = Jug(2, 5)
        >>> jug5.spillinto(jug6)
        >>> print(jug5)
        (6/9)
        >>> print(jug6)
        (5/5)

        >>> jug7 = Jug(0, 3)
        >>> jug8 = Jug(4, 5)
        >>> jug7.spillinto(jug8)
        >>> print(jug7)
        (0/3)
        >>> print(jug8)
        (4/5)

        >>> jug9 = Jug(0, 9)
        >>> jug10 = Jug(0, 10)
        >>> jug9.spillinto(jug10)
        >>> print(jug9)
        (0/9)
        >>> print(jug10)
        (0/10)
        """
        if jug.space > self.amount:
            jug.amount += self.amount
            self.amount = 0
            self.calculate_space()
            jug.calculate_space()
        elif jug.space < self.amount:
            self.amount -= jug.space
            jug.amount += jug.space
            self.calculate_space()
            jug.calculate_space()
        elif jug.space == self.amount:
            jug.amount += self.amount
            self.amount = 0
            self.calculate_space()
            jug.calculate_space()


class JugPuzzleClass:
    """
    JugPuzzleClass creates and manipulates Jugs based on user input to solve a puzzle
    """
    def __init__(self):
        """
        Creates a new JugPuzzleClass with 0 moves and a set list of Jugs

        >>> game1 = JugPuzzleClass()
        >>> game1.moves
        0
        >>> print(*game1.jugs)
        (8/8) (0/5) (0/3)

        >>> game2 = JugPuzzleClass()
        >>> game2.moves
        0
        >>> print(*game2.jugs)
        (8/8) (0/5) (0/3)

        >>> game3 = JugPuzzleClass()
        >>> game3.moves
        0
        >>> print(*game3.jugs)
        (8/8) (0/5) (0/3)
        """
        self.moves = 0
        """
        The number of moves a player has made
        moves >= 0
        """
        self.jugs = [Jug(8, 8), Jug(0, 5), Jug(0, 3)]
        """
        List of the 3 Jugs the player uses
        jugs[0].amount + jugs[1].amount + jugs[2].amount = 8
        """

    def spilling(self):
        """
        Spills between Jugs based on user input
        """
        from_jug = int(input('spill from jug: '))
        """
        Jug that is being spilled from
        0 <= from_jug <= 2
        """
        to_jug = int(input('into jug: '))
        """
        Jug that is being spilled into
        0 <= to_jug <= 2
        """

        if from_jug != to_jug:  # if statement used so user can't spill from a jug to the same jug
            self.jugs[from_jug].spillinto(self.jugs[to_jug])
            self.moves += 1

    def game_complete(self):
        """
            None -> Boolean
        Returns True if puzzle is solved
        :return: True or None

        >>> game1 = JugPuzzleClass()
        >>> print(*game1.jugs)
        (8/8) (0/5) (0/3)
        >>> game1.game_complete() is True
        False
        >>> game2 = JugPuzzleClass()
        >>> game2.jugs = [Jug(3,8), Jug(5,5), Jug(0,3)]
        >>> print(*game2.jugs)
        (3/8) (5/5) (0/3)
        >>> game2.game_complete() is True
        False
        >>> game3 = JugPuzzleClass()
        >>> game3.jugs = [Jug(4,8), Jug(4,5), Jug(0,3)]
        >>> print(*game3.jugs)
        (4/8) (4/5) (0/3)
        >>> game3.game_complete() is True
        True
        """
        if self.jugs[0].amount == 4 and self.jugs[1].amount == 4:
            return True

    def run(self):
        """
        Starts the game
        """
        while not self.game_complete():
            try:
                print(str(self.moves) + ' ' + '0:{0} 1:{1} 2:{2}'.format(self.jugs[0], self.jugs[1], self.jugs[2]))
                self.spilling()
            except ValueError:  # restarts loop if input is anything other than a number
                continue
            except IndexError:  # restarts loop if number isn't referencing an available jug
                continue

        print('Congrats you solved it in {} moves!!'.format(self.moves))

if __name__ == '__main__':
    game = JugPuzzleClass()
    game.run()

__author__ = 'Alistair Broomhead'

class Board(object):
    def __init__(self, solution=None):
        if solution is None:
            self.generate_solution()
        else:
            assert len(solution) == 4
            for peg in solution: assert peg in range(6)
            self.solution = solution
        self.guesses = []
    def generate_solution(self):
        # TODO - Randomise
        self.solution = list(range(4))
    def guess(self, solution):
        for peg in solution: assert peg in range(6)
        self.guesses.append(solution)
        if self.solved():
            self.guesses[-1].extend(['+']*4)
            return True
        returnValue = {'match':0, 'there':0}
        unmatchedguess = []
        unmatchedreal = []
        for pegnum in range(len(solution)):
            guesspeg = solution[pegnum]
            realpeg = self.solution[pegnum]
            if guesspeg == realpeg:
                returnValue['match'] += 1
                self.guesses[-1].append('+')
            else:
                unmatchedguess.append(guesspeg)
                unmatchedreal.append(realpeg)
        for peg in unmatchedguess:
            if peg in unmatchedreal:
                returnValue['there'] += 1
                self.guesses[-1].append('?')
        if len(self.guesses) >= 12: return False
        return returnValue
    def solved(self):
        return self.guesses[-1] == self.solution
    def __str__(self):
        str_out = ''
        if (len(self.guesses) >= 12
            or
            self.guesses[-1] == self.solution):
            str_out += ' '.join(self.solution)
        else:
            str_out += ' '.join(['X']*4)
        str_out += '\n'
        for guess in self.guesses:
            str_out += ' '.join([`x` for x in guess]) + "\n"
        return str_out


BOARD = Board()
in_ = [int(x) for x in raw_input("Guess?").split()]
r = BOARD.guess(in_)
while r not in [True, False]:
    print BOARD
    in_ = [int(x) for x in raw_input("Guess?").split()]
    r = BOARD.guess(in_)
if r:
    print 'You win'
else:
    print "You lose"
print BOARD
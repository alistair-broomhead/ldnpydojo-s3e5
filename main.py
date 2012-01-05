import random

__author__ = 'Alistair Broomhead, Mohammed Abdulrazeg, Carles Pina, John C'

class Board(object):
    def __init__(self, solution=None):
        self.solution = []
        if solution is None:
            self.generate_solution()
        else:
            assert len(solution) == 4
            for peg in solution: assert peg in range(6)
            self.solution = solution
       # print self.solution
        self.guesses = []
    def generate_solution(self):
        [self.solution.append(random.choice(range(6))) for i in range(4)]
    def get_input(self):
        while True:
            try:
                in_ = raw_input("Guess?")
                in_ = in_.split()
                in_ = [int(x) for x in in_]
                assert len(in_) == 4
                for peg in in_:
                    assert peg in range(6)
                return self.guess(in_)
            except (TypeError, ValueError, AssertionError):
                pass
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
                unmatchedreal.remove(peg)
                self.guesses[-1].append('?')
        if len(self.guesses) >= 12: return False
        return returnValue
    def solved(self):
        if not self.guesses: return False
        return self.guesses[-1] == self.solution
    def __str__(self):
        str_out = ''
        if (len(self.guesses) >= 12
            or
            (self.guesses and
             self.guesses[-1] == self.solution)):
            str_out += ' '.join([ `x` for x in self.solution])
        else:
            str_out += ' '.join(['X']*4)
        str_out += '\n' + '-'*19 +'\n'
        for guess in self.guesses:
            str_out += ' '.join([`x` for x in guess]) + "\n"
        return str_out


BOARD = Board()
r = {}
while r not in [True, False]:
    print BOARD
    r = BOARD.get_input()
if r:
    print 'You win'
else:
    print "You lose"
print BOARD
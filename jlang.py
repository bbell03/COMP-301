import sys
from enum import Enum


#J0 Object Language, Implemented in Python3
class JNum:
    def __init__(self, n):
        self.n = n
    def pp(self):
        return str(self.n)
    def sexp(self):
        return self.n
    def interp(self):
        return self.n

class JPlus:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    def pp(self):
        return ("(+ " + self.lhs.pp() + " " + self.rhs.pp() + ")")
    def sexp(self):
        return ['+', self.lhs.sexp(), self.rhs.sexp()]
    def interp(self):
        return self.lhs.interp() + self.rhs.interp()

class JMult:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    def pp(self):
        return ("(* "+ self.lhs.pp() + " " + self.rhs.pp() + ")")
    def sexp(self):
        return ['*', self.lhs.sexp(), self.rhs.sexp()]

    def interp(self):
        return self.lhs.interp() * self.rhs.interp()



def check_assert(jexp, output_case): 
    if (jexp == output_case):
        print("TEST PASSED " + str(jexp) + " == " + str(output_case))
        return True
    else:
        print("TEST FAILED " + str(jexp) + " != " + str(output_case))
        return False
    return

  

def j0_tests():
    check_assert((JNum(4).sexp()), 4)
    check_assert((JNum(8).sexp()), 8)
    check_assert((JNum(6).sexp()), 6)
    check_assert((JNum(234).sexp()), 234)
    check_assert((JNum(8).sexp()),8)
    check_assert((JNum(10).sexp()), 10)
    check_assert((JMult(JNum(8), JNum(9)).sexp()), ['*', 8, 9])
    check_assert((JMult(JNum(3), JPlus(JNum(7), JNum(3))).sexp()), ['*', 3, ['+', 7, 3]])
    check_assert((JMult(JNum(2), JPlus(JNum(9), JNum(123))).sexp()), ['*', 2, ['+', 9, 123]])
    check_assert((JPlus(JNum(2),(JPlus(JNum(3), JNum(4)))).sexp()), ['+', 2, ['+', 3, 4]])
    check_assert((JMult(JNum(2), JNum(3)).sexp()), ['*', 2, 3])
    check_assert((JMult(JPlus(JNum(8), JNum(2)), JPlus(JNum(9),
    JNum(10))).sexp()), ['*', ['+', 8, 2], ['+', 9, 10]])
    check_assert((JPlus(JMult(JNum(8), JNum(2)), JMult(JNum(9),
    JNum(10))).sexp()), ['+', ['*', 8, 2], ['*', 9, 10]])

    print(JMult(JNum(2), JPlus(JNum(9), JNum(123))).sexp())

def main():
    j0_tests()


main()

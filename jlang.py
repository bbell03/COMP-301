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
    check_assert((JNum(4).pp()), "4")
    check_assert((JNum(8).pp()), "8")
    check_assert((JNum(6).pp()), "6")
    check_assert((JNum(234).pp()),"234")
    check_assert((JNum(8).interp()), 8)
    check_assert((JNum(10).pp()), "10")
    check_assert((JMult(JNum(8), JNum(9)).interp()), 72)
    check_assert((JMult(JNum(3), JPlus(JNum(7), JNum(3))).interp()), 30)
    check_assert((JMult(JNum(2), JPlus(JNum(9), JNum(123))).pp()), "(* 2 (+ 9 123))")
    check_assert((JPlus(JNum(2),(JPlus(JNum(3), JNum(4)))).pp()), "(+ 2 (+ 3 4))")
    check_assert((JMult(JNum(2), JNum(3)).pp()), "(* 2 3)")
    check_assert((JMult(JPlus(JNum(8), JNum(2)), JPlus(JNum(9),
    JNum(10))).pp()), "(* (+ 8 2) (+ 9 10))")
    check_assert((JPlus(JMult(JNum(8), JNum(2)), JMult(JNum(9),
    JNum(10))).interp()), 106)

    print(JMult(JNum(2), JPlus(JNum(9), JNum(123))).sexp())

def main():
    j0_tests()


main()

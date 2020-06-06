import sys
import operator
from enum import Enum

#J1 Object Language, Implemented in Python3

hole = None

class JNum:
    def __init__(self, n):
        self.n = n
    def pp(self):
        return str(self.n)
    def sexp(self):
        return self.n
    def interp(self):
        return self.n

class JBool:
    def __init__(self, n):
        self.n = n
    def pp(self):
        return str(self.n)
    def sexp(self):
        return self.n
    def interp(self):
        return self.n

class JApp:
    def __init__ (self, list):
        #Op case
        self.prim = list[0]
        self.varg = [list[1],list[2]]
        #If Case
    def pp(self):
        return delta(self.prim, self.varg).pp()
    def sexp(self):
        return delta(self.prim, self.varg).sexp()
    def interp(self):
        return delta(self.prim, self.varg).interp()
         
class JPrim:
    def __init__(self, prim):
        self.prim = prim
    def pp(self):
        if (self.prim == "Plus"):
            return ('+')
        elif (self.prim == "Sub"):
            return ('-')
        elif (self.prim == "Mult"):
            return ('*')
        elif (self.prim == "Div"):
            return ('/')
        elif (self.prim == "Equal"):
            return ('=')
        elif (self.prim == "Less"):
            return ('<')
        elif (self.prim == 'Leq'):
            return ('<=')
        elif (self.prim == 'Great'):
            return ('>')
        elif (self.prim == 'Geq'):
            return ('>=')
    def sexp(self):
        if (self.prim == "Plus"):
            return ('+')
        elif (self.prim == "Sub"):
            return ('-')
        elif (self.prim == "Mult"):
            return ('*')
        elif (self.prim == "Div"):
            return ('/')
        elif (self.prim == "Equal"):
            return ('=')
        elif (self.prim == "Less"):
            return ('<')
        elif (self.prim == 'Leq'):
            return ('<=')
        elif (self.prim == 'Great'):
            return ('>')
        elif (self.prim == 'Geq'):
            return ('>=')
    def interp(self):
        if (self.prim == "Plus"):
            return ('+')
        elif (self.prim == "Sub"):
            return ('-')
        elif (self.prim == "Equal"):
            return ('=')
        elif (self.prim == "Less"):
            return ('<')
        elif (self.prim == 'Leq'):
            return ('<=')
        elif (self.prim == 'Great'):
            return ('>')
        elif (self.prim == 'Geq'):
            return ('>=')

class delta:
    def __init__(self, prim, varg):
        self.prim = prim
        self.varg = varg
        #print(self.prim.pp())
        #print(self.varg[0].pp())
        #print(self.varg[1].pp())
    def pp(self):
        #print('delta-pp')
        return ("(" + self.prim.pp() + " " + self.varg[0].pp() + " " + self.varg[1].pp() + ")")
    def sexp(self):
        return [self.prim.sexp(), self.varg[0].sexp(), self.varg[1].sexp()]
    def interp(self):
        return eval(self.varg[0].interp(), self.prim.interp(), self.varg[1].interp())

class JIf:
    def __init__(self, ec, et, ef):
        self.ec = ec
        self.et = et
        self.ef = ef
    def pp(self):
        return "(if " + self.ec.pp() + " " + self.et.pp() + " " + self.ef.pp() + ")"
    def sexp(self):
        return ['if', self.ec.sexp(), self.et.sexp(), self.ef.sexp()]
    def interp(self):
        if (self.ec.interp() == False):
            return self.ef.interp()
        else:
            return self.et.interp()
            
def whatIf(ob):


def step(ob):
    if (isinstance(ob, JIf)):
        if (ob.ec != False):
            return ob.et

        elif (ob.ec == False):
            return ob.ef
        
        elif (isinstance(ob.ec, JApp)):
            return (JIf(step(ob.ec), et, ef))

    elif (isinstance(ob, JApp)):
        return delta(ob.prim, ob.varg)




#Takes contexts and plugs their redexes with expressions
def plug(context, exp):

    return 

#Contexts -- how to define
# - Describes a program where part of a program is missing
#Application context

#def find_redex():


#https://stackoverflow.com/questions/18591778/how-to-pass-an-operator-to-a-python-function
def eval(inp, relate, cut):
    ops = {'+': operator.add,
           '*': operator.mul,
           '/': operator.floordiv,
           '>': operator.gt,
           '<': operator.lt,
           '>=': operator.ge,
           '<=': operator.le,
           '=': operator.eq}
    return ops[relate](inp, cut)

#def interp(ef, earg):
    #return delta(ef, earg)

def desugar(sexp):
    if (type(sexp) == int):
        return JNum(sexp)
    if (type(sexp) == bool):
        return JBool(sexp)
    elif(len(sexp) == 3 and sexp[0] == '*'):
        return JApp([JPrim('Mult'), desugar(sexp[1]), desugar(sexp[2])])
    elif(len(sexp) == 3 and sexp[0] == '+'):
        return JApp([JPrim('Plus'), desugar(sexp[1]), desugar(sexp[2])])
    elif(len(sexp) == 3 and sexp[0] == '-'):
        return JApp([JPrim('Sub'), desugar(sexp[1]), desugar(sexp[2])])
    elif(len(sexp) == 3 and sexp[0] == '/'):
        return JApp([JPrim('Div'), desugar(sexp[1]), desugar(sexp[2])])
    elif(len(sexp) == 3 and sexp[0] == '<'):
        return JApp([JPrim('Less'), desugar(sexp[1]), desugar(sexp[2])])
    elif(len(sexp) == 3 and sexp[0] == '<='):
        return JApp([JPrim('Leq'), desugar(sexp[1]), desugar(sexp[2])])
    elif(len(sexp) == 3 and sexp[0] == '>'):
        return JApp([JPrim('Great'), desugar(sexp[1]), desugar(sexp[2])])
    elif(len(sexp) == 3 and sexp[0] == '>='):
        return JApp([JPrim('Geq'), desugar(sexp[1]), desugar(sexp[2])])
    elif(len(sexp) == 3 and sexp[0] == '='):
        return JApp([JPrim('Equal'), desugar(sexp[1]), desugar(sexp[2])])
    elif(len(sexp) == 4 and sexp[0] == 'if'):
        return JIf(desugar(sexp[1]), desugar(sexp[2]), desugar(sexp[3]))

def check_assert(jexp, output_case): 
    if (jexp == output_case):
        print("TEST PASSED " + str(jexp) + " == " + str(output_case))
        return True
    else:
        print("TEST FAILED " + str(jexp) + " != " + str(output_case))
        return False
    return

def j1_tests():
    check_assert(JPrim('Plus').pp(), '+')
    check_assert(JPrim('Geq').pp(), '>=')
    check_assert(JBool(True).sexp(), True)
    check_assert(JApp([JPrim('Plus'), JNum(1), JNum(2)]).pp(), "(+ 1 2)")
    check_assert(JApp([JPrim('Plus'), JNum(1), JNum(2)]).sexp(), ['+', 1, 2])
    check_assert(desugar(JApp([JPrim('Div'), JNum(1), JNum(2)]).sexp()).pp(), "(/ 1 2)")
    check_assert(JApp([JPrim('Plus'), JNum(1), JNum(2)]).interp(), 3)
    check_assert((JApp([JPrim('Mult'), JNum(3), JApp([JPrim('Plus'), JNum(7), JNum(3)])]).sexp()), ['*', 3, ['+', 7, 3]])
    check_assert(JIf(JBool(True), JNum(5), JNum(4)).pp(), "(if True 5 4)")
    check_assert(desugar(JIf(JBool(True), JNum(5), JNum(4)).sexp()).pp(), "(if True 5 4)")
    check_assert((JIf(JBool(True), JNum(8), JNum(9)).sexp()), ['if', True, 8, 9])
    check_assert(
        desugar(
            JIf(
                JApp(
                    [JPrim('Equal'), JNum(8), (JApp([JPrim('Plus'), JNum(3), JNum(27)]))]
                    ), 
                JNum(8), 
                JApp(
                    [JPrim('Plus'), JNum(8), JNum(8)]
                    )
                ).sexp()).pp(), "(if (= 8 (+ 3 27)) 8 (+ 8 8))" ),  
    return

#def j0_tests():
    #check_assert((JNum(4).sexp()), 4)
    #check_assert((JIf(JBool(True), JNum(8), JNum(9)).sexp()), ['if', True, 8, 9])
    #check_assert((JNum(6).sexp()), 6)
    #check_assert((JNum(234).sexp()), 234)
    #check_assert((JBool(True).sexp()),True)
    #check_assert((JNum(10).sexp()), 10)
    #check_assert((JLeq(JNum(8), JNum(9)).sexp()), ['<=', 8, 9])
    #check_assert((JMult(JNum(3), JPlus(JNum(7), JNum(3))).sexp()), ['*', 3, ['+', 7, 3]])
    #check_assert((JMult(JNum(2), JPlus(JNum(9), JNum(123))).sexp()), ['*', 2, ['+', 9, 123]])
    #check_assert((JSub(JNum(2),(JPlus(JNum(3), JNum(4)))).sexp()), ['-', 2, ['+', 3, 4]])
    #check_assert((JDiv(JNum(2), JNum(3)).sexp()), ['/', 2, 3])
    #check_assert((JMult(JPlus(JNum(8), JNum(2)), JPlus(JNum(9),
    #JNum(10))).sexp()), ['*', ['+', 8, 2], ['+', 9, 10]])
    #check_assert((JPlus(JMult(JNum(8), JNum(2)), JMult(JNum(9),
    #JNum(10))).sexp()), ['+', ['*', 8, 2], ['*', 9, 10]])

    #print(JMult(JNum(2), JPlus(JNum(9), JNum(123))).pp())
    #print(JMult(JNum(2), JPlus(JNum(9), JNum(123))).sexp())

    #print(JMult(JNum(8), JNum(9)).sexp())
    #test = desugar(JMult(JNum(8), JNum(9)).sexp()).pp()
    #print(test)
    #print(['*', ['+', 8, 2], ['+', 9, 10]])
    #print(desugar(['*', ['+', 8, 2], ['+', 9, 10]]).pp())

def main():
    #j0_tests()
    j1_tests()
    return

main()

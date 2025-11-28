'''
Problem-1:
Create a small calculator which performs operations such as Addition, Subtraction, Multiplication 
and Division using class.
Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string
'''
double = float
class Calculator:
    def __init__(self,a:double,b:double,operation:str):
        self.a = a
        self.b = b
        self.op = operation
        
    def calculate(self):
        if self.op == "addition":
            return self.a+self.b
        elif self.op == "subtraction":
            return self.a-self.b
        elif self.op == "multiplication":
            return self.a*self.b
        elif self.op == "division":
            if self.b == 0:
                return "Can't divide with Zero"
            return self.a/self.b
        else:
            return 'invalid operation'
        
obj1 = Calculator(10,20.5,'addition')
res = obj1.calculate()
print('Addition :',res)

obj1 = Calculator(10,500,'subtraction')
res = obj1.calculate()
print('Subtraction :',res)

obj1 = Calculator(10,100,'multiplication')
res = obj1.calculate()
print('Multiplication :',res)

obj1 = Calculator(10,2,'division')
res = obj1.calculate()
print('Division :',res)
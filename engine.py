import math

class Engine:
    def __init__(self):
        self.memory = 0
        self.expression = ""
        self.result = "0"
    
    def evaluate(self):
        expr = self.expression

        try:
            expr = expr.replace("x", "*")
            expr = expr.replace("÷", "/")
            expr = expr.replace("^", "**")

            self.result = eval(expr)
            return self.result
        except ZeroDivisionError:
            self.result = "Diviseur par 0 "
            return self.result
        except Exception:
            self.result = "Erreur"
            return self.result
        
    def square_root(self, num):
        try:
            self.result = math.sqrt(num)
            return self.result
        except:
            self.result = "Erreur"
            return self.result
        
        
import math
from settings import *
from num_converter import Converter

class Engine:
    def __init__(self):
        self.memory = 0
        self.expression = ""
        self.result = "0"
        self.converter = Converter()
    
    def set_expression(self, expr):
        """Set the expression to be evaluated"""
        self.expression = expr
    
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
        
    def sine(self, num):
        try:
            return math.sin(math.radians(num))
        except:
            return "Error"
    
    def cosine(self, num):
        try:
            return math.cos(math.radians(num))
        except:
            return "Error"
    
    def tangent(self, num):
        try:
            return math.tan(math.radians(num))
        except:
            return "Error"
    
    def logarithm(self, num):
        try:
            return math.log10(num)
        except:
            return "Error"
    
    def natural_log(self, num):
        try:
            return math.log(num)
        except:
            return "Error"
    
    def power(self, base, exponent):
        try:
            return base ** exponent
        except:
            return "Error"
    
    def square(self, num):
        try:
            return num ** 2
        except:
            return "Error"
    
    def percentage(self, num):
        try:
            return num / 100
        except:
            return "Error"
        

    # calcul scientifique
    def process_scientific(self, operation, current_value):
        operations = {
            "x²": self.square,
            "√": self.square_root,
            "%": self.percentage,
            "sin": self.sine,
            "cos": self.cosine,
            "tan": self.tangent,
            "log": self.logarithm,
            "ln": self.natural_log,
            "π": lambda x: PI,
            "e": lambda x: E
        }
        
        if operation in operations:
            try:
                if current_value == "":
                    num = 0
                else:
                    num = float(current_value)
                
                result = operations[operation](num)
                
                if result == "Error":
                    return "Error"
                return self.converter.int_converter(result)
            except:
                return "Error"
        
        return None
    def add_constant(self, constant_name):
        constants = {
            "π": PI,
            "e": E
        }
        return constants.get(constant_name, "")     
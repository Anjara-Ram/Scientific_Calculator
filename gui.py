import tkinter as tk

from settings import *
from num_converter import Converter
from engine import Engine

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.engine = Engine()
        self.converter = Converter()
        self.expression = ""

        self.create_display()
        self.create_buttons()

    def create_display(self):
        self.display = tk.Entry(self.root)
        self.display.grid(row=0, column=0, columnspan=6, 
                  sticky="nsew", padx=10, pady=10)

    
    def create_buttons(self):
        # bouton scientifique (ligne 1)
        sci_buttons = [
            ("sin", 1, 0), ("cos", 1, 1), ("tan", 1, 2), ("log", 1, 3), ("ln", 1, 4)
        ]
        for text, row , col in sci_buttons:
            self.create_button(text, row, col, "#5856d6", "white")
        
        # bouton scientifique (ligne 2)
        sci_buttons2 = [
            ("√", 2, 0), ("x²", 2, 1), ("xʸ", 2, 2), ("π", 2, 3), ("e", 2, 4) 
        ]
        for text, row , col in sci_buttons2:
            self.create_button(text, row, col, "#5856d6", "white")

        utils_buttons = [
            ("(", 3, 0), (")", 3, 1), ("%", 3, 2), ("DEL", 3, 3), ("AC", 3, 4) 
        ]
        for text, row, col in utils_buttons:
            if text in ["DEL", "AC"]:
                self.create_button(text, row, col, "#ff3b30", "white")
            else:
                self.create_button(text, row, col, "#5856d6", "white")
        
        row4_buttons = [
            ("7", 4, 0), ("8", 4, 1), ("9", 4, 2), ("÷", 4, 3)
        ]

        for text, row, col in row4_buttons:
            if text == "÷":
                    self.create_button(text, row, col, "#ff9500", "white")
            else:
                self.create_button(text, row, col, "#3d3d3d", "white")
        
        row5_buttons = [
            ("4", 5, 0), ("5", 5, 1), ("6", 5, 2), ("x", 5, 3)
        ]

        for text, row, col in row5_buttons:
            if text == "x":
                    self.create_button(text, row, col, "#ff9500", "white")
            else:
                self.create_button(text, row, col, "#3d3d3d", "white")

        row6_buttons = [
            ("1", 6, 0), ("2", 6, 1), ("3", 6, 2), ("-", 6, 3)
        ]

        for text, row, col in row6_buttons:
            if text == "-":
                    self.create_button(text, row, col, "#ff9500", "white")
            else:
                self.create_button(text, row, col, "#3d3d3d", "white")
        
        row7_buttons = [
            ("1", 7, 0), ("2", 7, 1), ("3", 7, 2), ("+", 7, 3), ("n!", 7, 4)
        ]

        for text, row, col in row7_buttons:
            if text == "+":
                    self.create_button(text, row, col, "#ff9500", "white")
            else:
                self.create_button(text, row, col, "#3d3d3d", "white")

        
        equal_btn = tk.Button(
            self.root,
            text="=",
            bg="#34c759",
            fg="white",
            command=lambda: self.button_click("=")
        )
        equal_btn.grid(row=4, column=4, rowspan=3, pady=5, sticky="ns")

    def create_button(self, text, row, col, bg_color, fg_color):
        # Creation des bouton un par un
        btn = tk.Button(
             self.root,
             text=text,
             font=FONT_BUTTONS,
             bg=bg_color,
             fg=fg_color,
             width=BTN_WIDTH,
             height=BTN_HEIGHT,
             command=lambda t=text: self.button_click(t)
        )
        btn.grid(row=row, column=col, padx=5, pady=5)
    

    # Quand l utilisateur clique sur un bouton
    def button_click(self, value):
        """Handle all button clicks - SIMPLIFIED"""
        
        # Clear all
        if value == "AC":
            self.expression = ""
            self.update_display()
        
        # Clear last character
        elif value == "DEL":
            self.expression = self.expression[:-1]
            self.update_display()
        
        # Calculate result
        elif value == "=":
            self.calculate()
        
        # Power operator (needs special handling)
        elif value == "xʸ":
            self.expression += "^"
            self.update_display()
        
        # Parentheses
        elif value in ["(", ")"]:
            self.expression += value
            self.update_display()
        
        # Scientific operations (sin, cos, tan, log, ln, √, x², %, π, e)
        elif value in ["sin", "cos", "tan", "log", "ln", "√", "x²", "%", "π", "e"]:
            result = self.engine.process_scientific(value, self.expression)
            if result == "Error":
                self.expression = "Error"
                self.update_display()
                self.expression = ""
            elif result is not None:
                self.expression = result
                self.update_display()
        
        # Numbers and basic operators
        else:
            self.expression += value
            self.update_display()
    
    def calculate(self):
        """Send expression to engine and show result"""
        self.engine.set_expression(self.expression)
        result = self.engine.evaluate()
        
        if result == "Error":
            self.expression = "Error"
            self.update_display()
            self.expression = ""
        else:
            self.expression = self.converter.int_converter(result)
            self.update_display()
    
    # Afficher l expression
    def update_display(self):
        """Refresh the display screen"""
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)
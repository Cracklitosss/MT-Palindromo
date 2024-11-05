import tkinter as tk
from tkinter import ttk
import re

class TuringMachine:
    def __init__(self):
        self.tape = []
        self.head = 0
        self.state = 'q0'
        
    def clean_string(self, text):
        text = re.sub(r'[.,!¡?¿\s]', '', text)
        text = text.lower()
        replacements = {
            'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
            'ü': 'u', 'ñ': 'n'
        }
        for old, new in replacements.items():
            text = text.replace(old, new)
        return text
    
    def check_palindrome(self, input_string):
        clean_text = self.clean_string(input_string)
        self.tape = list(clean_text)
        self.head = 0
        self.state = 'q0'
        
        while self.state != 'qaccept' and self.state != 'qreject':
            if self.state == 'q0':
                if self.head >= len(self.tape) // 2:
                    self.state = 'qaccept'
                else:
                    if self.tape[self.head] == self.tape[len(self.tape) - 1 - self.head]:
                        self.head += 1
                    else:
                        self.state = 'qreject'
        
        return self.state == 'qaccept'

class PalindromeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Máquina de Turing - Verificador de Palíndromos")
        self.turing = TuringMachine()
        
        self.create_widgets()
        
    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Label(main_frame, text="Ingrese el texto:").grid(row=0, column=0, sticky=tk.W)
        self.text_input = tk.Text(main_frame, height=3, width=50)
        self.text_input.grid(row=1, column=0, columnspan=2, pady=5)
        
        ttk.Button(main_frame, text="Verificar", command=self.check_text).grid(row=2, column=0, pady=10)

        self.result_var = tk.StringVar()
        ttk.Label(main_frame, textvariable=self.result_var).grid(row=3, column=0, sticky=tk.W)
        
    def check_text(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if text:
            is_palindrome = self.turing.check_palindrome(text)
            if is_palindrome:
                self.result_var.set("¡Es un palíndromo!")
            else:
                self.result_var.set("No es un palíndromo")
        else:
            self.result_var.set("Por favor, ingrese un texto")

if __name__ == "__main__":
    root = tk.Tk()
    app = PalindromeGUI(root)
    root.mainloop()

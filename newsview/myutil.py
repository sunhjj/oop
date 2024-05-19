import os

def where(control:bool, true_val, false_val):
  return (control and [true_val] or [false_val])[0]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
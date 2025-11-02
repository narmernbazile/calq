#! /usr/bin/env python3
# calq.py: a calculator

def main():
  repl()

def repl():
  stack = list()
  while True:
    expression = input("calq> ")
    calculate(stack, expression)
    print(stack)

def calculate(stack, expression):
  tokens = expression.split()

  for token in tokens:
    if token.isnumeric(): stack.append(int(token))
    if is_operation(token):
      match token:
        case "*": 
          p = stack.pop()
          q = stack.pop()
          stack.append(multiply(p, q))
        case "/": 
          p = stack.pop()
          q = stack.pop()
          stack.append(divide(p, q))
        case "+": 
          p = stack.pop()
          q = stack.pop()
          stack.append(add(p, q))
        case "-": 
          p = stack.pop()
          q = stack.pop()
          stack.append(subtract(p, q))
      
def multiply(p: str, q: str):
  return int(p) * int(q)

def divide(p, q):
  return int(p) / int(q)

def add(p, q):
  return int(p) + int(q)

def subtract(p, q):
  return int(p) - int(q)

def is_operation(input):
  return input == '*' or input == '/' or input == '+' or input == '-'

if __name__ == '__main__': 
  main()

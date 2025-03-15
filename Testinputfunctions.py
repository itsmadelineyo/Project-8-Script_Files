>>> def inputFloat(prompt="Please enter an integer or a float: "):
...     while True:
...         user_input = input(prompt)
...
>>> def inputFloat(prompt="Please enter an integer or a float: "):
...     while True:
...         user_input = input(prompt)
...         if user_input.count('.') > 1:
...             print("Error: the input cannot have more than one '.'")
...             elif not user_input.replace('.', '', 1).isdigit():
...                 print("Error: the input must consist only of digits.")
...                 else:
...                     return float(user_input)
...
  File "<python-input-1>", line 6
    elif not user_input.replace('.', '', 1).isdigit():
    ^^^^
SyntaxError: invalid syntax
>>> if __name__ == "__main__":
...     value = inputFloat()
...     print(value)
...
Please enter an integer or a float: 10
Please enter an integer or a float: 20
Please enter an integer or a float: 30
Please enter an integer or a float:

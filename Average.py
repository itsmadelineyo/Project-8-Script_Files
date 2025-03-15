>>> def read_numbers(filename):
...      with open(filename, 'r') as file:
...           return [float(line.strip()) for line in file]
...
>>> def calculate_average(numbers):
...      if len(numbers) == 0:
...           return 0
...            return sum(numbers) / len(numbers)
...
  File "<python-input-1>", line 4
    return sum(numbers) / len(numbers)
IndentationError: unexpected indent
>>> def calculate_average(numbers):
...      if len(numbers) == 0:
...           return 0
...           return sum(numbers) / len(numbers)
...
>>> def main():
...      file_name = input("Enter the file name: ")
...      numbers = read_numbers(file_name)
...      average = calculate_average(numbers)
...      print(f"The average of the numbers in {file_name} is: {average}")
...
>>> if __name__ == "__main__":
...      main()
...
Enter the file name: yo mama
Traceback (most recent call last):
  File "<python-input-4>", line 2, in <module>
    main()
    ~~~~^^
  File "<python-input-3>", line 3, in main
    numbers = read_numbers(file_name)
  File "<python-input-0>", line 2, in read_numbers
    with open(filename, 'r') as file:
         ~~~~^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'yo mama'
>>>

# input() will always take an input as a string
num1 = input('Enter the num1:\n')
print('Value of num1 is:',num1, 'Data Type of num1 is:', type(num1))
num2 = int(input('Enter the num2:\n'))
print('Value of num2 is:',num2, 'Data Type of num1 is:', type(num2))
num3 = int(input('Enter the num3:\n'))
print('Value of num3 is:',num3, 'Data Type of num3 is:', type(num3))
print(f'Addition of {num2} and {num3} is {num2+num3}')
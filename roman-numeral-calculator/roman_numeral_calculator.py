#!/usr/bin/env python3

"""
Roman Numeral calculator
"""

romans = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
  }

def value(numeral):
  '''
  numeral = string
  
  Returns base 10 value of roman numeral
  if found else returns None
  '''
  return romans.get(numeral)
  

def substract(numerals):
  '''
  numerals = list of roman numerals (string)
  
  Checks if last numeral in numerals is the biggest number
  Meaning we need to substract from it
  
  Returns True or False
  '''
  return value(numerals[0]) < value(numerals[len(numerals) - 1])


def validate(input_numerals):
  '''
  input_numerals = string
  
  Returns list of numerals or False
  '''
  try:
      numerals = list(input_numerals)
  except TypeError:
      return False
  
  if all(value(i) for i in numerals):
    return numerals
  
  return False
  
  
def calculate(numerals):
  '''
  numerals = list of roman numerals (string)
  returns int total value of roman numerals
  '''
  total = 0
  
  nums = validate(numerals)
  
  if nums:
    substraction = substract(nums)
  else:
    return "Please enter a valid roman numeral"

  if substraction:
    # take last value in list
    # to substract from
    total = value(nums.pop())
    
    for n in nums:
      total -= value(n)
    return total
  
  for n in nums:
    total += value(n)
  
  return total
 
 
def main():
    values = list(input('Enter the roman numerals you want to calculate.\nVald numerals are: M, C, D, L, X, V, I --> '))
    for i in values:
        if i not in list(romans.keys()):
             print('Seems you entered an invalid roman number. Please try again...')
             exit()
             
    numerals = ''.join(numerals)
    print(calculate(numerals))


if __name__ == '__main__':
    main()

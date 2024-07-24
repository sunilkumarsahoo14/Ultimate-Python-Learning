""" 
Write a program to fill in a letter template given below with name and date.
letter = ''' 
Dear <|Name|>,
You are selected!
<|Date|>
'''
"""

letter = '''Dear <|Name|>, You are selected! <|Date|> '''

# Using replace string function with chaining to do the task
print(letter.replace("<|Name|>", "Sunil").replace("<|Date|>", "24 SEP"))

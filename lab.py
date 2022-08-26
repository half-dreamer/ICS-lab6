##input part
from convert import *
one_line = ''
all_inputs = ''
user_defined_variables_statements = ''  # to store .FILL instruction
result = ''
while True:
    if '.END' in one_line:
        break
    one_line = input()
    if '.FILL' in one_line:
        user_defined_variables_statements += one_line 
    result += convert_to_machine_lang(one_line)
    all_inputs += one_line+'\n' 
result = result [:len(result)-1]
print(result)    
# now have get all inputs in all_inputs string
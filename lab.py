##input part
from convert import *
one_line = ''
all_inputs = ''
result = ''
while True:
    if '.END' in one_line:
        break
    one_line = input()
    result += convert_to_machine_lang(one_line)
    all_inputs += one_line+'\n' 
result = result [:len(result)-1]
print(result)    
# now have get all inputs in all_inputs string
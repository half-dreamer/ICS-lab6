##input part
from convert import *
one_line = ''
all_inputs = ''
result = ''
single_instruction = ''
temp = ''
while True:
    if '.END' in one_line:
        break
    one_line = input()
    all_inputs += one_line+'\n'
# first loop to inspect all labels
all_inputs_first = str(all_inputs)
all_inputs_second = str(all_inputs)
newline_index = all_inputs.find('\n')
single_instruction = all_inputs[:newline_index+1]
start_position_str,cur_position = convert_to_machine_lang(single_instruction,'None')
start_position     = int (start_position_str,16) 
cur_position       = start_position
#store start position of the instructions (in decimal format)
while  all_inputs_first.find('\n')!= all_inputs_first.rfind('\n'):
    newline_index      = all_inputs_first.find('\n')
    single_instruction = all_inputs_first[:newline_index+1]
    cur_position = get_label(single_instruction,cur_position)
    all_inputs_first   = all_inputs_first[newline_index+1:]
    cur_position       += 1
newline_index = all_inputs_first.find('\n')
single_instruction = all_inputs_first[:newline_index]#the last instruction ,i.e. .END

#second loop,to get converted instruction and print them
result = ''
cur_position = start_position# cur_position has refreshed
while  all_inputs_second.find('\n')!= all_inputs_second.rfind('\n'):
    newline_index      = all_inputs_second.find('\n')
    single_instruction = all_inputs_second[:newline_index+1]
#single instruction includes '\n' ending ;process instruction to get labels
    temp ,cur_position    = convert_to_machine_lang(single_instruction,cur_position)
    result += temp
    all_inputs_second   = all_inputs_second[newline_index+1:]
    cur_position   +=  1
newline_index = all_inputs_second.find('\n')
single_instruction = all_inputs_second[:]#the last instruction ,i.e. .END
temp , cur_position=convert_to_machine_lang(single_instruction,cur_position)
result += temp
print(result[:-1])

    
# now have get all inputs in all_inputs string
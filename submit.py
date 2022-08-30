


operators = ['ADD','AND','NOT','LD','LDR','LDI','LEA','ST','STR','STI',"TRAP",'BR'
,'JMP','JSR','RET','.ORIG','.FILL','.BLKW','.STRINGZ','.END','HALT','GETC','OUT','PUTS'
'IN','PUTSP','RIT','JSRR','BRn','BRz','BRp','BRnz','BRzp','BRnp','BRnzp']


one_register_instructions = ['LD','LEA','STI','ST','LDI']

def hex_trans_to_bin_somenum_digits(somenum):
    """
    >>> hex_trans_to_bin_three_digits = hex_trans_to_bin_somenum_digits(3)
    >>> hex_trans_to_bin_three_digits('2')
    '010'
    """
    def transform_func(single_hex_digit):
        deci_num  = int(single_hex_digit,16)
        bin_num   = bin(deci_num)
        bin_num   = bin_num[2:]
        return bin_num.zfill(somenum)
    return transform_func
hex_trans_to_bin_four_digits = hex_trans_to_bin_somenum_digits(4)
hex_trans_to_bin_three_digits = hex_trans_to_bin_somenum_digits(3)    

def hex_trans_to_imm_with_somenum_digits(somenum):
    """
    create an high order function classifying similar function 
    >>> hex_trans_to_imm_with_five_digits = hex_trans_to_imm_with_somenum_digits(5)
    >>> hex_trans_to_imm_with_five_digits('3')
    '00011'
    >>> hex_trans_to_imm_with_six_digits = hex_trans_to_imm_with_somenum_digits(6)
    >>> hex_trans_to_imm_with_six_digits('-1')
    '111111'
    """
    def transform_func(num):
        return (bin(((1 << somenum) - 1)& int(num,16))[2:]).zfill(somenum)
    return transform_func        
hex_trans_to_imm_with_five_digits = hex_trans_to_imm_with_somenum_digits(5)
hex_trans_to_imm_with_six_digits = hex_trans_to_imm_with_somenum_digits(6)
hex_trans_to_imm_with_eight_digits = hex_trans_to_imm_with_somenum_digits(8)
hex_trans_to_imm_with_sixteen_digits = hex_trans_to_imm_with_somenum_digits(16)


def deci_trans_to_imm_with_somenum_digits(somenum):
    """
    >>> deci_trans_to_imm_with_five_digits = deci_trans_to_imm_with_somenum_digits(5)
    >>> deci_trans_to_imm_with_five_digits(1)
    '00001'
    >>> deci_trans_to_imm_with_five_digits(-1)
    '11111'
    """
    def transform_func(num):
        return (bin(((1 << somenum) - 1) & num)[2:]).zfill(somenum)
    return transform_func    
deci_trans_to_imm_with_five_digits = deci_trans_to_imm_with_somenum_digits(5)
deci_trans_to_imm_with_six_digits  = deci_trans_to_imm_with_somenum_digits(6)
deci_trans_to_imm_with_nine_digits = deci_trans_to_imm_with_somenum_digits(9)
deci_trans_to_imm_with_eleven_digits = deci_trans_to_imm_with_somenum_digits(11)
deci_trans_to_imm_with_sixteen_digits = deci_trans_to_imm_with_somenum_digits(16)

def JSRR_search_for_register(instruction):
    R_index = instruction.find('R') 
    instruction = instruction[R_index:]
    register = instruction[1]
    register_bin = hex_trans_to_bin_three_digits(register)
    return register_bin

def search_for_1_register(instruction):
    """
    return the binary form of the first register
    """        
    instruction = instruction.strip()
    whitespace_index = instruction.find(' ')
    first_word    =  instruction[:whitespace_index]
    if first_word not in one_register_instructions:
        instruction = instruction[whitespace_index:]
    first_reg_index = instruction.find('R')
    instruction = instruction[first_reg_index:]
    register_1 = instruction[1]
    register_1_bin = hex_trans_to_bin_three_digits(register_1)
    return register_1_bin

def search_for_1_2_register(instruction):
    """
    get an instruction containing two register
    return the binary number of the first and second register
    output will not affect input 'instruction'
    """
    first_reg_index = instruction.find('R')
    instruction = instruction[first_reg_index:]
    register_1 = instruction[1]
    register_1_bin = hex_trans_to_bin_three_digits(register_1)
    instruction = instruction[2:]
    register_2_index = instruction.find('R')
    register_2 = instruction[register_2_index+1]
    register_2_bin = hex_trans_to_bin_three_digits(register_2)  
    return register_1_bin,register_2_bin  

def search_for_deci_num(instruction):
            """
    return the  decimal number in the instruction
    the decimal number in the instruction starts with "#"
            """
            num_prefix = instruction.find('#') 
            instruction = instruction[(num_prefix+1):]
            instruction = instruction.rstrip()
            num = 0
            is_minus = False
            if instruction[0] =='-':
                is_minus = True
                instruction = instruction[1:]
            for digit in instruction:
                num = num *10 +int(digit)
            if is_minus:
                num = -num     
            return num        

def search_for_hexa_num(instruction):
    """
    return a string(important!) of hexadecimal number in the instruction
    """            
    num_prefix = instruction.find('x')
    instruction = instruction.rstrip()
    return instruction[num_prefix+1:]

def search_for_label_with_one_register(instruction):
    """
    get an instruction which has a register,return the label name(string)
    """
    instruction = instruction.strip()
    whitespace_index = instruction.find(' ')
    first_word    =  instruction[:whitespace_index]
    if first_word  not in one_register_instructions:
        instruction = instruction[whitespace_index:]
    register_index = instruction.find('R')
    instruction = instruction[register_index+3:]
    label = instruction.strip()  #remove all whitespaces
    return  label

def get_sign_bits(instruction):
    """
    get an BR instruction and return the sign bits 
    """    
    instruction = instruction.strip()
    B_index = instruction.find('BR')
    instruction = instruction[B_index:]
    whitespace_index = instruction.find(' ')
    operator  = instruction[:whitespace_index]#whitespace excluded
    neg_bit,zero_bit,posi_bit = '0','0','0'
    if operator == 'BR':
        return '111'
    else:
        if 'n' in operator:
            neg_bit = '1'
        if 'z' in operator:
            zero_bit = '1'
        if 'p' in operator:
            posi_bit = '1'
        return neg_bit+zero_bit+posi_bit   

def some_operator_get_label(some_operator):
    def get_label_func(instruction):
        instruction = instruction.strip()
        if is_labeled(instruction):
            whitespace_index = instruction.find(' ')
            instruction = instruction[whitespace_index:]
        B_index     = instruction.find(some_operator)
        instruction = instruction[B_index:]
        space_index = instruction.find(' ')
        instruction = instruction[space_index:]
        label = instruction.strip()
        return label
    return get_label_func    
BR_get_label = some_operator_get_label('BR')    
JSR_get_label = some_operator_get_label('JSR')

def STRINGZ_get_string(instruction):
    """
    get an STRINGZ instruction and return the string
    included in the instruction 
    """
    dot_index = instruction.find(".STRINGZ")
    instruction = instruction[dot_index+8:]
    instruction = instruction.strip()
    string = instruction[1:-1]
    return string

def is_labeled(instruction):
    instruction = instruction.strip()
    if instruction.find(' ')>0:
        whitespace_index = instruction.find(' ')
        first_word  = instruction[:whitespace_index]
        if first_word not in operators:
            return True
        return False   
    else:
        return False     

 

label_dict = {}   # store labels and according position;keys are labels,values are positions
operators = ['ADD','AND','NOT','LD','LDR','LDI','LEA','ST','STR','STI',"TRAP",'BR'
,'JMP','JSR','RET','.ORIG','.FILL','.BLKW','.STRINGZ','.END','HALT','GETC','OUT','PUTS'
'IN','PUTSP','RIT','JSRR','BRn','BRz','BRp','BRnz','BRzp','BRnp','BRnzp']
BR_collection = ['BR','BRn','BRz','BRp','BRnz','BRzp','BRnp','BRnzp']
one_register_instruction = ['LD','LEA','STI','ST','LDI']


#labels processing function 
#single instruction includes '\n' ending ;process instruction to get labels
def  get_label(single_instruction,cur_position):
    single_instruction = single_instruction.strip()#remove left and right whitespaces
    first_whitespace_index = single_instruction.find(' ')
    first_word = single_instruction[:first_whitespace_index]
    if '.BLKW' in single_instruction:
        #.BLKW has label condition
        if single_instruction[:5] != '.BLKW':
            first_word = single_instruction[:first_whitespace_index]
            if first_word not in operators:
                label_dict[first_word] = cur_position
        if single_instruction.find('#')>0:
            num = search_for_deci_num(single_instruction)
            cur_position -= 1
            while num>0:
                num -= 1
                cur_position = cur_position+1
            return cur_position  
    elif '.ORIG' in single_instruction:
        return cur_position           
    elif '.STRINGZ' in single_instruction:
        # .STRINGZ may have label
        if single_instruction[:8] != '.STRINGZ':
            first_word = single_instruction[:first_whitespace_index]
            if first_word not in operators:
                label_dict[first_word] = cur_position
        string = STRINGZ_get_string(single_instruction) 
        for i in range(len(string)):
            cur_position += 1     
        return cur_position
    elif single_instruction == '':
        return cur_position - 1   
    elif first_word in BR_collection:
        return cur_position    
    elif ' ' not in single_instruction:
        return cur_position             #single word a line (special case)
    else:
        first_word = single_instruction[:first_whitespace_index]
        if first_word not in operators:
            label_dict[first_word] = cur_position
        return cur_position    


def convert_to_machine_lang(one_instruction,cur_position):
    assert type(one_instruction)==str ,'one_insruction must be string'
    if is_labeled(one_instruction):
        one_instruction = one_instruction.strip()
        whitespace_index = one_instruction.find(' ')
        one_instruction = one_instruction[whitespace_index:]
    if '.ORIG' in one_instruction:
        x_index = one_instruction.rfind('x')
        first  = hex_trans_to_bin_four_digits(one_instruction[x_index+1])
        second = hex_trans_to_bin_four_digits(one_instruction[x_index+2])
        third  = hex_trans_to_bin_four_digits(one_instruction[x_index+3])
        fourth = hex_trans_to_bin_four_digits(one_instruction[x_index+4])
        result = first+second+third+fourth
        return result+'\n',cur_position
    elif '.END' in one_instruction:
        return  '',cur_position
    elif 'NOT' in one_instruction:
        operator_bin = '1001'
        whitespace_index = one_instruction.find(' ')
        one_instruction = one_instruction[whitespace_index:]
        register_1_bin,register_2_bin = search_for_1_2_register(one_instruction)
        return operator_bin+register_1_bin+register_2_bin+'111111\n',cur_position
    elif ('LD'  in one_instruction and 'LDR' not in one_instruction) or \
        'LEA' in one_instruction or 'STI' in one_instruction or ('ST' in one_instruction \
         and 'STR' not in one_instruction) or 'LDI' in one_instruction  :
        if 'LDI' in one_instruction:
            operator_bin = '1010'
        elif 'LEA' in one_instruction:
            operator_bin = '1110'
        elif 'LD' in one_instruction and 'LDI' not in one_instruction:
            operator_bin = '0010'
        elif 'STI' in one_instruction:
            operator_bin = '1011' 
        elif 'ST' in one_instruction:
            operator_bin = '0011'               
        register_1_bin = search_for_1_register(one_instruction)
        #number condition
        if one_instruction.find('#')>0:
            number = search_for_deci_num(one_instruction)
            num_bin = deci_trans_to_imm_with_nine_digits(number)  
        #label condition
        else:
            label = search_for_label_with_one_register(one_instruction)
            assert label in label_dict,  "label cannot be found in dictionary"
            position_moves = label_dict[label]-cur_position-1
            num_bin = deci_trans_to_imm_with_nine_digits(position_moves)
        return operator_bin+register_1_bin+num_bin+'\n',cur_position   
    elif 'LDR' in one_instruction or 'STR' in one_instruction and '.STRINGZ' not in one_instruction:
        if 'LDR' in one_instruction:
            operator_bin = '0110'
        elif 'STR' in one_instruction:
            operator_bin = '0111'    
        new_index = one_instruction.find('R')
        one_instruction = one_instruction[(new_index+1):]
        #to remove the 'R' in the 'LDR' to avoid interrupt later execution
        register_1_bin,register_2_bin = search_for_1_2_register(one_instruction)
        #decimal number condition 
        if one_instruction.find('#')>0:
            num = search_for_deci_num(one_instruction)
            imm_bin = deci_trans_to_imm_with_six_digits(num)
        if one_instruction.find('x')>0:  
            hexa_num_str = search_for_hexa_num(one_instruction)
            imm_bin      = hex_trans_to_imm_with_six_digits(hexa_num_str) 
        return operator_bin+register_1_bin+register_2_bin+imm_bin+'\n',cur_position                      
    elif 'ADD'  in one_instruction or 'AND' in one_instruction:
        if 'ADD' in one_instruction:
            operator_bin = '0001'
        elif 'AND' in one_instruction:
            operator_bin = '0101'    
        whitespace_index = one_instruction.find(' ')
        one_instruction = one_instruction[whitespace_index:]    
        register_occurence = one_instruction.count('R')
        if register_occurence ==3: #e.g. ADD/AND R2,R0,R0    
            register_1_bin,register_2_bin = search_for_1_2_register(one_instruction)
            register_3_index = one_instruction.rfind('R')
            register_3 = one_instruction[register_3_index+1]
            register_3_bin = hex_trans_to_bin_three_digits(register_3)
            return operator_bin+register_1_bin+register_2_bin+'000'+register_3_bin+'\n',cur_position
        else:   #e.g. ADD/AND R1,R3,#3    
            register_1_bin,register_2_bin = search_for_1_2_register(one_instruction)
            if one_instruction.find('#')>0:
                num     = search_for_deci_num(one_instruction)
                imm_bin = deci_trans_to_imm_with_five_digits(num)
            if one_instruction.find('x')>0:
                hexa_num_str = search_for_hexa_num(one_instruction)
                imm_bin      = hex_trans_to_imm_with_five_digits(hexa_num_str)                
        return operator_bin+register_1_bin+register_2_bin+'1'+imm_bin+'\n',cur_position

    elif 'TRAP' in one_instruction:
        operator_bin = '1111'
        hexa_num_str = search_for_hexa_num(one_instruction)
        num_bin      = hex_trans_to_imm_with_eight_digits(hexa_num_str)
        return operator_bin+'0000'+num_bin+'\n',cur_position
    elif 'BR' in one_instruction:
        operator_bin = '0000'
        sign_bin = get_sign_bits(one_instruction)
        #number condition
        if one_instruction.find('#')>0:
            number = search_for_deci_num(one_instruction)
            num_bin = deci_trans_to_imm_with_nine_digits(number)  
        #label condition
        else:
            label = BR_get_label(one_instruction)
            assert label in label_dict,  "label cannot be found in dictionary"
            position_moves = label_dict[label]-cur_position-1
            num_bin = deci_trans_to_imm_with_nine_digits(position_moves)
        return operator_bin+sign_bin+num_bin+'\n',cur_position
        
    elif "JMP" in one_instruction:
        operator_bin = '1100'
        register_1_bin = search_for_1_register(one_instruction)
        return operator_bin+'000'+register_1_bin+'000000'+'\n',cur_position
    elif 'RET' in one_instruction:
        return '1100000111000000'+'\n',cur_position
    elif 'JSR' in one_instruction and 'JSRR' not in one_instruction:
        operator_bin = '0100'  
        #number condition
        if one_instruction.find('#')>0:
            number = search_for_deci_num(one_instruction)
            num_bin = deci_trans_to_imm_with_eleven_digits(number)  
        #label condition
        else:
            label = JSR_get_label(one_instruction)
            assert label in label_dict,  "label cannot be found in dictionary"
            position_moves = label_dict[label]-cur_position-1
            num_bin = deci_trans_to_imm_with_eleven_digits(position_moves)
        return operator_bin+'1'+num_bin+'\n',cur_position

    elif 'JSRR' in one_instruction:   
        operator_bin = '0100'
        new_index    = one_instruction.find('R')
        one_instruction = one_instruction[(new_index+2):]
        register_1_bin = JSRR_search_for_register(one_instruction)
        return operator_bin+'000'+register_1_bin+'000000'+'\n',cur_position
    elif 'RTI' in one_instruction:
        return '1000000000000000'+'\n',cur_position  
    elif '.FILL' in one_instruction:
        if one_instruction.find('#')>0:
            num = search_for_deci_num(one_instruction)
            num_bin = deci_trans_to_imm_with_sixteen_digits(num)
        elif one_instruction.find('x')>0:
            num = search_for_hexa_num(one_instruction)
            num_bin = hex_trans_to_imm_with_sixteen_digits(num)
        return num_bin+'\n',cur_position  
    elif '.BLKW' in one_instruction:
        if one_instruction.find('#')>0:
            num = search_for_deci_num(one_instruction)
            result = ''
            cur_position -= 1
            while num>0:
                result += '0111011101110111'+'\n'
                num -= 1
                cur_position = cur_position+1
            return result,cur_position  
    elif '.STRINGZ' in one_instruction:
        string = STRINGZ_get_string(one_instruction) 
        result = ''
        for i in range(len(string)):
            char = string[i]
            char_ASCII = ord(char)
            single_char_bin = deci_trans_to_imm_with_sixteen_digits(char_ASCII)+'\n'
            result += single_char_bin
            cur_position += 1
        result += '0000000000000000'+'\n'     
        return result,cur_position
#trap condition(special form)
    elif 'GETC' in one_instruction:
        return '1111000000100000'+'\n',cur_position
    elif 'OUT'  in one_instruction:
        return '1111000000100001'+'\n',cur_position
    elif 'IN'   in one_instruction and '.STRINGZ' not in one_instruction:
        return '1111000000100011'+'\n',cur_position
    elif 'PUTSP' in one_instruction:
        return '1111000000100100'+'\n',cur_position  
    elif 'PUTS' in one_instruction:
        return '1111000000100010'+'\n',cur_position    
    elif 'HALT' in one_instruction:
        return '1111000000100101'+'\n',cur_position         
    else :
        return '',cur_position-1   # empty line
    
##input part

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
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


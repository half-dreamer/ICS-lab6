from string import whitespace


one_register_instructions = ['LD','LEA','STI','ST','LDI']

def  hex_trans_to_bin_four_digits(single_hex_digit):
    """transform a single hexadecimal digit (string type) to
        a four-digit-long binary number

    >>> hex_trans_to_bin_four_digits('a')
    '1010'
    >>> hex_trans_to_bin_four_digits('2')
    '0010'
    """        
    deci_num  = int(single_hex_digit,16)
    bin_num   = bin(deci_num)
    bin_num   = bin_num[2:]
    return bin_num.zfill(4)
def hex_trans_to_bin_three_digits(single_hex_digit):
    '''transform a single hexadecimal digit to 
        a three-digit-long binary number        
    '''
    return hex_trans_to_bin_four_digits(single_hex_digit)[1:]

def hex_trans_to_imm_with_five_digits(num):
    """
    transform a hexadecimal number(string!!!) into a binary immediate number(int)
    >>> hex_trans_to_imm_with_five_digits('3')
    '00011'
    >>> hex_trans_to_imm_with_five_digits('-1')
    '11111'
    """  
    return  (bin(((1 << 5) - 1)& int(num,16))[2:]).zfill(5)


def hex_trans_to_imm_with_six_digits(num):
    """
    transform a hexadecimal number(string!!!) into a binary immediate number(int)
    >>> hex_trans_to_imm_with_six_digits('3')
    '000011'
    >>> hex_trans_to_imm_with_six_digits('-1')
    '111111'
    """  
    return  (bin(((1 << 6) - 1)& int(num,16))[2:]).zfill(6)    

def hex_trans_to_imm_with_eight_digits(num):
    """
    transform a hexadecimal number(string!!!) into a binary immediate number(int)
    >>> hex_trans_to_imm_with_eight_digits('3')
    '00000011'
    """  
    return  (bin(((1 << 8) - 1)& int(num,16))[2:]).zfill(8)

def hex_trans_to_imm_with_sixteen_digits(num):
    """
    transform a hexadecimal number(string!!!) into a binary immediate number(int)
    >>> hex_trans_to_imm_with_sixteen_digits('3')
    '0000000000000011'
    """  
    return  (bin(((1 << 16) - 1)& int(num,16))[2:]).zfill(16)       

def deci_trans_to_imm_with_five_digits(num):
    """
    transform a decimal number(int) into a binary immediate number(string)(five digits)
    >>> deci_trans_to_imm_with_five_digits(1)
    '00001'
    >>> deci_trans_to_imm_with_five_digits(-1)
    '11111'
    """    
# this function is to mask the last five digit of num's bianry form 
# and then fill the positive num with 0 to five digits
# negative num needn't to zfill    
    return (bin(((1 << 5) - 1) & num)[2:]).zfill(5)

def deci_trans_to_imm_with_six_digits(num):
    """
    transform a decimal number(int) into a binary immediate number(string)(six digits)
    >>> deci_trans_to_imm_with_six_digits(1)
    '000001'
    >>> deci_trans_to_imm_with_six_digits(-1)
    '111111'
    """        
    return (bin(((1 << 6) - 1) & num)[2:]).zfill(6)


def deci_trans_to_imm_with_nine_digits(num):
    """
    transform a decimal number(int) into a binary immediate number(string)(nine digits)
    >>> deci_trans_to_imm_with_nine_digits(1)
    '000000001'
    >>> deci_trans_to_imm_with_nine_digits(-1)
    '111111111'
    """        
    return (bin(((1 << 9) - 1) & num)[2:]).zfill(9)

def deci_trans_to_imm_with_eleven_digits(num):
    """
    transform a decimal number(int) into a binary immediate number(string)(eleven digits)
    >>> deci_trans_to_imm_with_eleven_digits(1)
    '00000000001'
    >>> deci_trans_to_imm_with_eleven_digits(-1)
    '11111111111'
    """        
    return (bin(((1 << 11) - 1) & num)[2:]).zfill(11)    

def deci_trans_to_imm_with_sixteen_digits(num):
    """
    transform a decimal number(int) into a binary immediate number(string)(sixteen digits)
    >>> deci_trans_to_imm_with_sixteen_digits(1)
    '0000000000000001'
    >>> deci_trans_to_imm_with_sixteen_digits(-1)
    '1111111111111111'
    """        
    return (bin(((1 << 16) - 1) & num)[2:]).zfill(16)

def search_for_1_register(instruction):
    """
    return the binary form of the first register
    """        
    instruction = instruction.strip()
    whitespace_index = instruction.find(' ')
    first_word    =  instruction[:whitespace_index]
    if first_word in one_register_instructions:
        first_reg_index = instruction.find('R')
        instruction = instruction[first_reg_index:]
        register_1 = instruction[1]
        register_1_bin = hex_trans_to_bin_three_digits(register_1)
    else:
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
    if first_word in one_register_instructions:
        register_index = instruction.find('R')
        instruction = instruction[register_index+3:]
        label = instruction.strip()  #remove all whitespaces
        return label
    else:
        instruction = instruction[whitespace_index:]
        register_index = instruction.find('R')
        instruction = instruction[register_index+3:]
        label = instruction.strip()  #remove all whitespaces
        return     label

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
def BR_get_label(instruction):
    """
    get an BR instruction and return its label(offset)(string)
    """             
    instruction = instruction.strip()
    B_index     = instruction.find('BR')
    instruction = instruction[B_index:]
    space_index = instruction.find(' ')
    instruction = instruction[space_index:]
    label = instruction.strip()
    return label

def JSR_get_label(instruction):
    instruction = instruction.strip()
    J_index     = instruction.find('JSR')
    instruction = instruction[J_index:]
    space_index = instruction.find(' ')
    instruction = instruction[space_index:]
    label = instruction.strip()
    return label

def STRINGZ_get_string(instruction):
    """
    get an STRINGZ instruction and return the string
    included in the instruction 
    """
    first_quote_index = instruction.find("\"")
    instruction = instruction[first_quote_index:]
    instruction = instruction.strip()
    string = instruction[1:-1]
    return string


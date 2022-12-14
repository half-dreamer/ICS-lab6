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
    >>> deci_trans_to_imm_with_five_digits(1)
    '000001'
    >>> deci_trans_to_imm_with_five_digits(-1)
    '111111'
    """        
    return (bin(((1 << 6) - 1) & num)[2:]).zfill(6)


def deci_trans_to_imm_with_nine_digits(num):
    """
    transform a decimal number(int) into a binary immediate number(string)(nine digits)
    >>> deci_trans_to_imm_with_five_digits(1)
    '000000001'
    >>> deci_trans_to_imm_with_five_digits(-1)
    '111111111'
    """        
    return (bin(((1 << 9) - 1) & num)[2:]).zfill(9)

def search_for_1_register(instruction):
    """
    return the binary form of the first register
    """        
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

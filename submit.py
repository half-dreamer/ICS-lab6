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

def deci_trans_to_imm_with_sixteen_digits(num):
    """
    transform a decimal number(int) into a binary immediate number(string)(nine digits)
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
# transforming functions
#
from assist_func import *
def convert_to_machine_lang(one_instruction):
    assert type(one_instruction)==str ,'one_insruction must be string'
    if '.ORIG' in one_instruction:
        x_index = one_instruction.rfind('x')
        first  = hex_trans_to_bin_four_digits(one_instruction[x_index+1])
        second = hex_trans_to_bin_four_digits(one_instruction[x_index+2])
        third  = hex_trans_to_bin_four_digits(one_instruction[x_index+3])
        fourth = hex_trans_to_bin_four_digits(one_instruction[x_index+4])
        result = first+second+third+fourth
        return result+'\n'
    elif '.END' in one_instruction:
        return  ''
    elif 'NOT' in one_instruction:
        operator_bin = '1001'
        register_1_bin,register_2_bin = search_for_1_2_register(one_instruction)
        return operator_bin+register_1_bin+register_2_bin+'111111\n'
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
            return operator_bin+register_1_bin+num_bin+'\n'  
#TODO:label condition   
       
    elif 'LDR' in one_instruction or 'STR' in one_instruction:
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
        return operator_bin+register_1_bin+register_2_bin+imm_bin+'\n'                   
    elif 'LDI' in one_instruction:
        operator_bin = '1010'

    
    
    
    
    elif 'ADD'  in one_instruction or 'AND' in one_instruction:
        if 'ADD' in one_instruction:
            operator_bin = '0001'
        elif 'AND' in one_instruction:
            operator_bin = '0101'    
        register_occurence = one_instruction.count('R')
        if register_occurence ==3: #e.g. ADD/AND R2,R0,R0    
            register_1_bin,register_2_bin = search_for_1_2_register(one_instruction)
            register_3_index = one_instruction.rfind('R')
            register_3 = one_instruction[register_3_index+1]
            register_3_bin = hex_trans_to_bin_three_digits(register_3)
            return operator_bin+register_1_bin+register_2_bin+'000'+register_3_bin+'\n'
        else:   #e.g. ADD/AND R1,R3,#3    
            register_1_bin,register_2_bin = search_for_1_2_register(one_instruction)
            if one_instruction.find('#')>0:
                num     = search_for_deci_num(one_instruction)
                imm_bin = deci_trans_to_imm_with_five_digits(num)
            if one_instruction.find('x')>0:
                hexa_num_str = search_for_hexa_num(one_instruction)
                imm_bin      = hex_trans_to_imm_with_five_digits(hexa_num_str)                
        return operator_bin+register_1_bin+register_2_bin+'1'+imm_bin+'\n' 

    elif 'TRAP' in one_instruction:
        operator_bin = '1111'
        hexa_num_str = search_for_hexa_num(one_instruction)
        num_bin      = hex_trans_to_imm_with_eight_digits(hexa_num_str)
        return operator_bin+'0000'+num_bin+'\n'
#trap condition(special form)
    elif 'GETC' in one_instruction:
        return '1111000000100000'+'\n'
    elif 'OUT'  in one_instruction:
        return '1111000000100001'+'\n'
    elif 'PUTS' in one_instruction:
        return '1111000000100010'+'\n'
    elif 'IN'   in one_instruction:
        return '1111000000100011'+'\n'
    elif 'PUTSP' in one_instruction:
        return '1111000000100100'+'\n'  
    elif 'HALT' in one_instruction:
        return '1111000000100101'+'\n'  
#TODO: BR
    elif "JMP" in one_instruction:
        operator_bin = '1100'
        register_1_bin = search_for_1_register(one_instruction)
        return operator_bin+'000'+register_1_bin+'000000'+'\n'
    elif 'RET' in one_instruction:
        return '1100000111000000'+'\n'
#TODO: JSR remeber to distinguish between 'JSR' and 'JSRR'        
    elif 'JSRR' in one_instruction:   
        operator_bin = '0100'
        new_index    = one_instruction.find('R')
        one_instruction = one_instruction[(new_index+2):]
        register_1_bin = search_for_1_register(one_instruction)
        return operator_bin+'000'+register_1_bin+'000000'+'\n'
    elif 'RTI' in one_instruction:
        return '1000000000000000'+'\n'  
    elif '.FILL' in one_instruction:
        if one_instruction.find('#')>0:
            num = search_for_deci_num(one_instruction)
            num_bin = deci_trans_to_imm_with_sixteen_digits(num)
        elif one_instruction.find('x')>0:
            num = search_for_hexa_num(one_instruction)
            num_bin = hex_trans_to_imm_with_sixteen_digits(num)
        return num_bin+'\n' 
    elif '.BLKW' in one_instruction:
        if one_instruction.find('#')>0:
            num = search_for_deci_num(one_instruction)
            result = ''
            while num>0:
                result += '0111011101110111'+'\n'
                num -= 1
            return result    
#TODO:.STRING            
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
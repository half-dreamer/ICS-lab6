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


# transforming functions
#
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
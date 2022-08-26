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
    elif 'HALT' in one_instruction:
        return '1111000000100101'+'\n'
    elif '.END' in one_instruction:
        return  ''
    elif 'NOT' in one_instruction:
        operator_bin = '1001'
        one_instruction,register_1_bin,register_2_bin = search_for_1_2_register(one_instruction)
        return operator_bin+register_1_bin+register_2_bin+'111111\n'
    elif 'LD'  in one_instruction and 'LDR' not in one_instruction and 'LDI' not in one_instruction:
        operator_bin = '0010'
        register_1_bin = search_for_1_register(one_instruction)
        #number condition
        if one_instruction.find('#'):
            number = search_for_deci_num(one_instruction)
            num_bin = deci_trans_to_imm_with_nine_digits(number)
            return operator_bin+register_1_bin+num_bin+'\n'  
#TODO:label condition   
       
    elif 'LDR' in one_instruction:
        operator_bin = '0110'
        register_1_bin,register_2_bin = search_for_1_2_register(one_instruction)
        #decimal number condition 
        if one_instruction.find('#'):
            num = search_for_deci_num(one_instruction)
            num_bin = deci_trans_to_imm_with_six_digits(num)
            return operator_bin+register_1_bin+register_2_bin+num_bin+'\n'
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
            num_prefix = one_instruction.find('#') or one_instruction.find('x')
            if one_instruction.find('#'):
                num     = search_for_deci_num(one_instruction)
                imm_bin = deci_trans_to_imm_with_five_digits(num)
#TODO: to deal with 'x' condition                 
        return operator_bin+register_1_bin+register_2_bin+'1'+imm_bin+'\n' 
    

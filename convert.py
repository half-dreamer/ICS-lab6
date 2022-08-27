# transforming functions
from assist_func import *

label_dict = {}   # store labels and according position
#keys are labels,values are positions
operators = ['ADD','AND','NOT','LD','LDR','LDI','LEA','ST','STR','STI',"TRAP",'BR'
,'JMP','JSR','RET','.ORIG','.FILL','BLKW','.STRINGZ','.END','HALT','GETC','OUT','PUTS'
'IN','PUTSP','RIT','JSRR']
#Note:in operators,'.STRINGZ' may be wrong


#labels processing function 
#single instruction includes '\n' ending ;process instruction to get labels
def  get_label(single_instruction,cur_position):
    single_instruction = single_instruction.strip()#remove left and right whitespaces
    first_whitespace_index = single_instruction.find(' ')
    first_word = single_instruction[:first_whitespace_index]
    if first_word not in operators:
        label_dict[first_word] = cur_position


def convert_to_machine_lang(one_instruction,cur_position):
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
        #label condition
        else:
            label = search_for_label_with_one_register(one_instruction)
            assert label in label_dict,  "label cannot be found in dictionary"
            position_moves = label_dict[label]-cur_position-1
            num_bin = deci_trans_to_imm_with_nine_digits(position_moves)
        return operator_bin+register_1_bin+num_bin+'\n'    
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
        return operator_bin+sign_bin+num_bin+'\n'
        
    elif "JMP" in one_instruction:
        operator_bin = '1100'
        register_1_bin = search_for_1_register(one_instruction)
        return operator_bin+'000'+register_1_bin+'000000'+'\n'
    elif 'RET' in one_instruction:
        return '1100000111000000'+'\n' 
    elif 'JSR' in one_instruction and 'JSRR' not in one_instruction:
        operator_bin = '0100'  
        #number condition
        if one_instruction.find('#')>0:
            number = search_for_deci_num(one_instruction)
            num_bin = deci_trans_to_imm_with_eleven_digits(number)  
        #label condition
        else:
            label = search_for_label_with_one_register(one_instruction)
            assert label in label_dict,  "label cannot be found in dictionary"
            position_moves = label_dict[label]-cur_position-1
            num_bin = deci_trans_to_imm_with_eleven_digits(position_moves)
        return operator_bin+'1'+num_bin+'\n'

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
#TODO:.BLKW cur_position is different from others    
    elif '.BLKW' in one_instruction:
        if one_instruction.find('#')>0:
            num = search_for_deci_num(one_instruction)
            result = ''
            while num>0:
                result += '0111011101110111'+'\n'
                num -= 1
            return result    
#TODO:.STRING            

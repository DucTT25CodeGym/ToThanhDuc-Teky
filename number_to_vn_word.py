VN_NUMBER_CALL_LIST  = {'0':'không'
                        ,'1':'một'
                        ,'2':'hai'
                        ,'3':'ba'
                        ,'4':'bốn'
                        ,'5':'năm'
                        ,'6':'sáu'
                        ,'7':'bảy'
                        ,'8':'tám'
                        ,'9':'chín'}

def get_num_1000_units(str_num, len_str_num):
    """
    Split a numeric string into groups of three digits for thousands unit separation.

    Args:
        str_num (str): The numeric string to be split.
        len_str_num (int): The length of the numeric string.

    Returns:
        list: A list of strings containing groups of three digits each.
    """
    if len_str_num % 3 == 0:
        return [str_num[-(i*3):][:3] for i in range(1, len_str_num//3)]
    else:
        return [str_num[-(i*3):][:3] for i in range(1, len_str_num//3 + 1)]

def get_head_nums(str_num, len_str_num):
    """
    Get the leading digits of a numeric string after thousands unit separation.

    Args:
        str_num (str): The numeric string.
        len_str_num (int): The length of the numeric string.

    Returns:
        str: The leading digits of the numeric string after thousands unit separation.
    """
    return str_num[:len_str_num-len(get_num_1000_units(str_num, len_str_num))*3]

def get_vn_call_3_nums(str_3_nums):
    """
    Convert a string representing a 3-digit number to its Vietnamese call representation.

    Args:
        str_3_nums (str): A string representing a 3-digit number.

    Returns:
        str: The Vietnamese call representation of the input 3-digit number.
    """
    if str_3_nums[1] == '0':
        if str_3_nums[2] == '0':
            vn_num_call = VN_NUMBER_CALL_LIST[str_3_nums[0]] + ' trăm'
        else:
            vn_num_call = (VN_NUMBER_CALL_LIST[str_3_nums[0]] + ' trăm lẻ ' \
                           + VN_NUMBER_CALL_LIST[str_3_nums[2]])
    elif str_3_nums[1] == '1':
        if str_3_nums[2] == '5':
            vn_num_call = (VN_NUMBER_CALL_LIST[str_3_nums[0]] + ' trăm mười lăm')
        elif str_3_nums[2] == '0':
            vn_num_call = (VN_NUMBER_CALL_LIST[str_3_nums[0]] + ' trăm mười')
        else:
            vn_num_call = (VN_NUMBER_CALL_LIST[str_3_nums[0]] + ' trăm mười ' \
                           + VN_NUMBER_CALL_LIST[str_3_nums[2]])
    else:
        if str_3_nums[2] == '5':
            vn_num_call = (VN_NUMBER_CALL_LIST[str_3_nums[0]] + ' trăm ' \
                       + VN_NUMBER_CALL_LIST[str_3_nums[1]] + ' mươi lăm')
        elif str_3_nums[2] == '0':
            vn_num_call = (VN_NUMBER_CALL_LIST[str_3_nums[0]] + ' trăm ' \
                       + VN_NUMBER_CALL_LIST[str_3_nums[1]] + ' mươi')
        elif str_3_nums[2] == '1':
            vn_num_call = (VN_NUMBER_CALL_LIST[str_3_nums[0]] + ' trăm ' \
                       + VN_NUMBER_CALL_LIST[str_3_nums[1]] + ' mươi mốt')
        else:
            vn_num_call = (VN_NUMBER_CALL_LIST[str_3_nums[0]] + ' trăm ' \
                           + VN_NUMBER_CALL_LIST[str_3_nums[1]] + ' mươi ' \
                           + VN_NUMBER_CALL_LIST[str_3_nums[2]])
    return vn_num_call

def get_vn_call_2_nums(str_2_nums):
    """
    Convert a string representing a 2-digit number to its Vietnamese call representation.

    Args:
        str_2_nums (str): A string representing a 2-digit number.

    Returns:
        str: The Vietnamese call representation of the input 2-digit number.
    """
    if str_2_nums[0] == '1':
        if str_2_nums[1] == '5':
            return 'mười lăm'
        elif str_2_nums[1] == '0':
            return 'mười'
        else:
            return 'mười ' + VN_NUMBER_CALL_LIST[str_2_nums[1]]
    else:
        if str_2_nums[1] == '5':
            return VN_NUMBER_CALL_LIST[str_2_nums[0]] + ' mươi lăm'
        elif str_2_nums[1] == '0':
            return VN_NUMBER_CALL_LIST[str_2_nums[0]] + ' mươi'
        elif str_2_nums[1] == '1':
            return VN_NUMBER_CALL_LIST[str_2_nums[0]] + ' mươi mốt'
        else:
            return VN_NUMBER_CALL_LIST[str_2_nums[0]] + ' mươi ' + VN_NUMBER_CALL_LIST[str_2_nums[1]]
        
def head_num_call(head_num):
    """
    Convert the leading digits of a numeric string into their Vietnamese call representation.

    Args:
        head_num (str): The leading digits of a numeric string.

    Returns:
        str: The Vietnamese call representation of the input leading digits.
    """
    if len(head_num) == 1:
        vn_call_heads = VN_NUMBER_CALL_LIST[head_num]
    elif len(head_num) == 2:
        vn_call_heads = get_vn_call_2_nums(str_2_nums = head_num)
    elif len(head_num) == 3:
        vn_call_heads = get_vn_call_3_nums(str_3_nums = head_num)
    return vn_call_heads

def vn_call_components(head_num, tail_num_list):
    """
    Convert the components of a numeric string into their Vietnamese call representation.

    Args:
        head_num (str): The leading digits of the numeric string.
        tail_num_list (list): A list of strings representing the tail components of the numeric string.

    Returns:
        str: The Vietnamese call representation of the input numeric string components.
    """
    if len(tail_num_list) == 1:
        vn_call_tail = get_vn_call_3_nums(str_3_nums = tail_num_list[0])
        vn_call = (head_num + ' nghìn, ' + vn_call_tail)

    elif len(tail_num_list) == 2:
        vn_call_tail_1 = get_vn_call_3_nums(str_3_nums = tail_num_list[1])
        vn_call_tail_2 = get_vn_call_3_nums(str_3_nums = tail_num_list[0])
        vn_call = (head_num + ' triệu, '\
                   + vn_call_tail_1 + ' nghìn, '\
                   + vn_call_tail_2)
    return vn_call

def call_by_vietnamese(num):
    """
    Convert a numeric value into its Vietnamese call representation.

    Args:
        num (int or float): The numeric value to be converted.

    Returns:
        str: The Vietnamese call representation of the input numeric value.
    """
    str_num = str(num)
    len_str_num = len(str(num))
    if len_str_num == 1:
        return VN_NUMBER_CALL_LIST[str_num]
    if len_str_num == 2:
        return get_vn_call_2_nums(str_num)
    if len_str_num == 3:
        return get_vn_call_3_nums(str_num)
    else:
        head_nums = get_head_nums(str_num, len_str_num)   
        head_num_vn_call = head_num_call(head_nums)
        tail_num_list = get_num_1000_units(str_num, len_str_num)

        return (vn_call_components(head_num_vn_call, tail_num_list))
    
def large_number_vietnamese_call(num):
    """
    Convert a large numeric value into its Vietnamese call representation.

    Args:
        num (int or float): The large numeric value to be converted.

    Returns:
        str: The Vietnamese call representation of the input large numeric value.
    """
    str_num = str(num)
    len_str_num = len(str(num))
    
    list_9_nums_bin = []
    for i in range(1, len_str_num//9 + 2):
        list_9_nums_bin += [str_num[-(i*9):][:9]]
        list_9_nums_bin[-1] = list_9_nums_bin[-1][:len_str_num - len(''.join(list_9_nums_bin[:-1]))]

    vn_call_list = []
    for num_comp in list_9_nums_bin[::-1]:
        if num_comp == '':
            continue
        vn_call_list += [call_by_vietnamese(num_comp)]
        
    if len(list_9_nums_bin) == 1:
        call_ = (vn_call_list[0].capitalize())
    else:
        call_ = (' tỷ, '.join(vn_call_list).capitalize())
        
    call_ = call_.replace(', không trăm triệu, không trăm nghìn, không trăm','')
    call_ = call_.replace(', không trăm triệu, không trăm nghìn','')
    call_ = call_.replace(', không trăm triệu','')
    call_ = call_.replace(' không trăm nghìn,','')
    if call_.endswith(', không trăm nghìn, không trăm'):
        call_ = call_.replace(', không trăm nghìn, không trăm','')
    elif call_.endswith(', không trăm'):
        call_ = call_.replace(', không trăm','')
    
    return call_

def input_nature_number():
    """
    Prompt the user to input a non-negative integer.

    Returns:
        int: The non-negative integer entered by the user.
    """
    while True:
        try:
            nature_number = int(input("""
Nhập vào 1 số nguyên: """))
            break
        except:
            print("    Bạn đã nhập sai, vui lòng nhập lại 1 số nguyên.")
    return nature_number

def text_to_speech(text):
    import pyttsx3
    engine = pyttsx3.init()
    voice_id_vn_male = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'

    engine.setProperty("voice", voice_id_vn_male)
    engine.setProperty("rate", 120)
    engine.say(f"{text}")
    engine.runAndWait()

def main():
    num = input_nature_number()
    if num >= 0:
        text = large_number_vietnamese_call(num)
        print('''
----Số bạn vừa nhập vào:   {:,}
----Đọc như sau:           {}
    '''.format(num, text))
        text_to_speech(text)
    else:
        adj_num = num * (-1)
        text = 'Âm ' + large_number_vietnamese_call(adj_num)
        print('''
----Số bạn vừa nhập vào:   {:,}
----Đọc như sau:           {}
    '''.format(num, text.capitalize())
         )
        text_to_speech(text)
    
if __name__ == '__main__':
    main()
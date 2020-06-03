import string

def urlify(input_str, real_length):
    input_list = list(input_str)
    gap = 0
    for i in range(real_length -1, -1, -1):
        if input_list[i] in string.whitespace:
            input_list[len(input_list) - 1 - (real_length - 1 - i) - gap] = '0'
            input_list[len(input_list) - 1 - (real_length - 1 - i) - 1 - gap] = '2'
            input_list[len(input_list) - 1 - (real_length - 1 - i) - 2 - gap] = '%'
            gap += 2
        else:
            input_list[len(input_list) - 1 - (real_length - 1 - i) - gap] = input_list[i]
    return ''.join(input_list)


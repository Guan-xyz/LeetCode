# 709. To Lower Case


def to_lower_case(strings):
    result = ''
    for i in strings:
        if 65 <= ord(i) <= 90:
            result += chr(ord(i)+32)
        else:
            result += i
    return result

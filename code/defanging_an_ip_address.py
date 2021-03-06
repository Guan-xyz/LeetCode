# 1108. Defanging an IP Address


def defang_ip_addr(address):
    result = ''
    for i in address:
        if i != '.':
            result += i
        else:
            result += '[.]'
    return result

print(defang_ip_addr('1.1.1.1'))

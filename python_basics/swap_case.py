def swap_case(s):
    swapStr = ""
    
    for char in s:
        if char.isupper():
            swapStr += char.lower()
        else:
            swapStr += char.upper()
    return swapStr

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
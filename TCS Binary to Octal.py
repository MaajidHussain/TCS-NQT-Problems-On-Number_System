def binary_to_octal(binary_str):
    if not isinstance(binary_str,str):
        raise ValueError("Input must be a string.")
    if binary_str=="":
        return "0"
    for char in binary_str:
        if char not in '01':
            raise ValueError("Input must be a binary string containing only 0's and 1's.")
    Decimal_Value=0
    for i in range(len(binary_str)):
        bit=int(binary_str[len(binary_str) -1 -i])
        Decimal_Value+=bit * (2**i)
    
    Octal_Value=""
    if Decimal_Value==0:
        return "0"
    while Decimal_Value>0:
        Octal_Value=str(Decimal_Value%8) + Octal_Value
        Decimal_Value//=8
    return Octal_Value
    
try:
    print(binary_to_octal("1100110"))
    print(binary_to_octal('011'))
    print(binary_to_octal(''))
    print(binary_to_octal(20))
    print(binary_to_octal('20'))
except ValueError as e:
    print(e)
def binary_to_decimal(binary_str):
    if not isinstance(binary_str,str):
        raise ValueError("Input must be a string.")
    for char in binary_str:
        if char not in '01':
            raise ValueError("Input must be a binary string containing only 0's and 1's.")
    Decimal_Value=0
    for i in range(len(binary_str)):
        bit=l=int(binary_str[len(binary_str)-1-i])
        Decimal_Value+=bit*(2**i)
    return Decimal_Value
try:
    print(binary_to_decimal('1011'))
    print(binary_to_decimal('011'))
    print(binary_to_decimal(''))
    print(binary_to_decimal(20))
    print(binary_to_decimal('20'))
except ValueError as e:
    print(e)
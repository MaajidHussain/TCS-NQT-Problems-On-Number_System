def Decimal_to_Binary(Number):
    if not isinstance(Number,int):
        raise ValueError("Input must be an Integer.")
    if Number<0:
        raise ValueError("Input must be a non-negative integer.")
    if Number==0:
        return "0"
    
    Binary_value=""
    while Number>0:
        Binary_value=str(Number%2)+Binary_value
        Number//=2
    return Binary_value
try:
    print(Decimal_to_Binary(15))
    print(Decimal_to_Binary(18))
    print(Decimal_to_Binary(0))
    print(Decimal_to_Binary(-5))
    print(Decimal_to_Binary(15.5))
except ValueError as e:
    print(e)
    
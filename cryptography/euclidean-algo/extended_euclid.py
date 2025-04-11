"""Extended Eculidean algorithm"""

def extended_eculid(a:int, b:int) -> tuple[int, int, int]:
    """
    Extended euclidean algorithm to calculate gcd and
    bezouts coefficient

    inputs: 
    2 integers whose gcd to calculate

    outputs:
    (d, x, y) where d = gcd, x, y are bezouts coefficients
    """
    if b == 0:
        return (a, 1, 0)

    (d1, x1, y1) = extended_eculid(b, a % b)
    (d, x, y ) = (d1, y1, x1 - (a // b) * y1)
    return (d, x, y)

print(extended_eculid(161, 28))

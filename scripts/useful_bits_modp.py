"""
has a statistical distance from uniformly random given by:

p is provided on stdin in any format that python can eval. For example,

$ python3 scripts/useful_bits_modp.py <<< 0x1a0111ea397fe69a4b1ba7b6434bacd764774b84f38512bf6730d2a0f6b0f6241eabfffeb153ffffb9feffffffffaaab
"""


def useful_bits(p):
    return max(
        n for n in range(p.bit_length() - 1, 0, -1)
        if n + 1 + p.bit_length() - (alpha := p % 2 ** n).bit_length() -
        (2 ** n - alpha).bit_length() >= 128
    )


if __name__ == '__main__':
    print(useful_bits(eval(input())))
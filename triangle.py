def is_valid_triangle(a, b, c) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False

    return a + b > c and a + c > b and b + c > a
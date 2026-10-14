from triangle import classify_triangle
import math

# Test that a triangle with a zero-length side, such as (0, 2, 2),
# is classified as "Invalid" according to the specification.

def test_zero_side_is_invalid():
    assert classify_triangle(0, 2, 2) == "Invalid"

# Test that a triangle with a negative side (-1, 2, 2)
# is classified as "Invalid".

def test_negative_side_is_invalid():
    assert classify_triangle(-1, 2, 2) == "Invalid"

# Test that sides (1, 2, 4) are invalid because
# the sum of the two shorter sides is less than the longest side.

def test_triangle_inequality_failure_is_invalid():
    assert classify_triangle(1, 2, 4) == "Invalid"
  
# Test that (1, 2, 3) is invalid because the sum
# of two sides equals the third side.

def test_degenerate_triangle_is_invalid():
    assert classify_triangle(1, 2, 3) == "Invalid"

# Test that a triangle with three equal sides (4, 4, 4)
# is classified as "Equilateral".

def test_equilateral_triangle():
    assert classify_triangle(4, 4, 4) == "Equilateral"

# Test that a triangle with two equal sides (3, 3, 5)
# is classified as "Isosceles".

def test_isosceles_triangle():
    assert classify_triangle(3, 3, 5) == "Isosceles"

# Test that a triangle with all different sides (4, 5, 6)
# is classified as "Scalene".

def test_scalene_triangle():
    assert classify_triangle(4, 5, 6) == "Scalene"

# Test that a right triangle is identified correctly
# even when the longest side appears first (5, 3, 4).

def test_reordered_right_triangle():
    assert classify_triangle(5, 3, 4) == "Right Scalene"

# Test that a right isosceles triangle with non-integer sides
# (5, 5, 5*sqrt(2)) is correctly classified using floating-point tolerance.

def test_floating_point_right_isosceles_triangle():
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"


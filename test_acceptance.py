from triangle import classify_triangle

def test_stained_glass_acceptance():
    # Test Case 1: Scalene triangle
    assert classify_triangle(2, 3 , 4) == "Scalene"

    # Test Case 2: Invalid triangle
    assert classify_triangle(5, 3, 8) == "Invalid"

    # Test Case 3: Right Scalene triangle
    assert classify_triangle(3, 4, 5) == "Right Scalene"

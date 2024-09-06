import pytest

# Function to test square
def square(n):
    return n ** 2

# Function to test cube
def cube(n):
    return n ** 3

# Function to test fifth power
def fifth_power(n):
    return n ** 5

# Testing the square function
def test_square():
    assert square(2) == 4, "Test Failed: Square of 2 should be 4"
    assert square(3) == 9, "Test Failed: Square of 3 should be 9"

# Testing the cube function
def test_cube():
    assert cube(2) == 8, "Test Failed: Cube of 2 should be 8"
    assert cube(3) == 27, "Test Failed: Cube of 3 should be 27"

# Testing the fifth power function
def test_fifth_power():
    assert fifth_power(2) == 32, "Test Failed: Fifth power of 2 should be 32"
    assert fifth_power(3) == 243, "Test Failed: Fifth power of 3 should be 243"

# Test for invalid input
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")

import pytest
from my_example.my_example_code import my_example_addition_function


def test_my_example_addition_function_good():

    assert my_example_addition_function(1, 2) == 3
    assert my_example_addition_function(0, 0) == 0

def test_my_example_addition_function_type_error_string():

    with pytest.raises(TypeError):
        my_example_addition_function("bob", "lorraine")
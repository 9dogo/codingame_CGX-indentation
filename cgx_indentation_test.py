""" 
Provide tests for the CgxIndentation module
"""

from typing import List
from cgx_indentation import CgxIndentation

def get_input_output_expected(test_dir : str) -> List[str]:
    """
    Get the input, output and expected files names for the test directory in parameter

    Parameters
    ----------
    test_dir : str
        the test directory

    Returns
    -------
    the input file name, the output file name, the expected file name
    """
    return test_dir + "input.txt", test_dir + "output.txt", test_dir + "expected.txt"

def test_boolean_value_with_spaces_and_tab() -> None:
    """
    Test : only one boolean value
    """
    input_fname, output_fname, expected_fname = get_input_output_expected("tests/test1/")
    with (open(input_fname, 'r', encoding="utf8") as input_file,
        open(output_fname, 'w', encoding="utf8") as output_file) :
        cgx_indentation = CgxIndentation()
        cgx_indentation.generate_cgx(input_file, output_file)
    with (open(expected_fname, 'r', encoding="utf8") as expected_file,
        open(output_fname, 'r', encoding="utf8") as output_file) :
        assert(output_file.read() == expected_file.read())


def test_simple_string() -> None:
    """
    Test : only one string
    """
    input_fname, output_fname, expected_fname = get_input_output_expected("tests/test2/")
    with (open(input_fname, 'r', encoding="utf8") as input_file,
        open(output_fname, 'w', encoding="utf8") as output_file) :
        cgx_indentation = CgxIndentation()
        cgx_indentation.generate_cgx(input_file, output_file)
    with (open(expected_fname, 'r', encoding="utf8") as expected_file,
        open(output_fname, 'r', encoding="utf8") as output_file) :
        assert(output_file.read() == expected_file.read())

def test_bloc_with_one_value() -> None:
    """
    Test : a bloc with one value
    """
    input_fname, output_fname, expected_fname = get_input_output_expected("tests/test3/")
    with (open(input_fname, 'r', encoding="utf8") as input_file,
        open(output_fname, 'w', encoding="utf8") as output_file) :
        cgx_indentation = CgxIndentation()
        cgx_indentation.generate_cgx(input_file, output_file)
    with (open(expected_fname, 'r', encoding="utf8") as expected_file,
        open(output_fname, 'r', encoding="utf8") as output_file) :
        assert(output_file.read() == expected_file.read())

def test_bloc_with_several_values() -> None:
    """
    Test : a bloc with several values
    """
    input_fname, output_fname, expected_fname = get_input_output_expected("tests/test4/")
    with (open(input_fname, 'r', encoding="utf8") as input_file,
        open(output_fname, 'w', encoding="utf8") as output_file) :
        cgx_indentation = CgxIndentation()
        cgx_indentation.generate_cgx(input_file, output_file)
    with (open(expected_fname, 'r', encoding="utf8") as expected_file,
        open(output_fname, 'r', encoding="utf8") as output_file) :
        assert(output_file.read() == expected_file.read())

def test_nested_blocs() -> None:
    """
    Test : nested blocs
    """
    input_fname, output_fname, expected_fname = get_input_output_expected("tests/test5/")
    with (open(input_fname, 'r', encoding="utf8") as input_file,
        open(output_fname, 'w', encoding="utf8") as output_file) :
        cgx_indentation = CgxIndentation()
        cgx_indentation.generate_cgx(input_file, output_file)
    with (open(expected_fname, 'r', encoding="utf8") as expected_file,
        open(output_fname, 'r', encoding="utf8") as output_file) :
        assert(output_file.read() == expected_file.read())

def test_empty_bloc() -> None:
    """
    Test : an empty bloc
    """
    input_fname, output_fname, expected_fname = get_input_output_expected("tests/test6/")
    with (open(input_fname, 'r', encoding="utf8") as input_file,
        open(output_fname, 'w', encoding="utf8") as output_file) :
        cgx_indentation = CgxIndentation()
        cgx_indentation.generate_cgx(input_file, output_file)
    with (open(expected_fname, 'r', encoding="utf8") as expected_file,
        open(output_fname, 'r', encoding="utf8") as output_file) :
        assert(output_file.read() == expected_file.read())

def test_several_blocs() -> None:
    """
    Test : several blocs
    """
    input_fname, output_fname, expected_fname = get_input_output_expected("tests/test7/")
    with (open(input_fname, 'r', encoding="utf8") as input_file,
        open(output_fname, 'w', encoding="utf8") as output_file) :
        cgx_indentation = CgxIndentation()
        cgx_indentation.generate_cgx(input_file, output_file)
    with (open(expected_fname, 'r', encoding="utf8") as expected_file,
        open(output_fname, 'r', encoding="utf8") as output_file) :
        assert(output_file.read() == expected_file.read())

def test_several_key_value() -> None:
    """
    Test : several key/values in the same bloc
    """
    input_fname, output_fname, expected_fname = get_input_output_expected("tests/test9/")
    with (open(input_fname, 'r', encoding="utf8") as input_file,
        open(output_fname, 'w', encoding="utf8") as output_file) :
        cgx_indentation = CgxIndentation()
        cgx_indentation.generate_cgx(input_file, output_file)
    with (open(expected_fname, 'r', encoding="utf8") as expected_file,
        open(output_fname, 'r', encoding="utf8") as output_file) :
        assert(output_file.read() == expected_file.read())

def test_full_example() -> None:
    """
    Test : full example : nested blocs, strings, keys and values
    """
    input_fname, output_fname, expected_fname = get_input_output_expected("tests/test11/")
    with (open(input_fname, 'r', encoding="utf8") as input_file,
        open(output_fname, 'w', encoding="utf8") as output_file) :
        cgx_indentation = CgxIndentation()
        cgx_indentation.generate_cgx(input_file, output_file)
    with (open(expected_fname, 'r', encoding="utf8") as expected_file,
        open(output_fname, 'r', encoding="utf8") as output_file) :
        assert(output_file.read() == expected_file.read())

def test_single_bloc_one_value() -> None:
    """
    Test : one bloc, one value
    """
    input_fname, output_fname, expected_fname = get_input_output_expected("tests"
        +"/additional_tests/single_bloc_one_value")
    with (open(input_fname, 'r', encoding="utf8") as input_file,
        open(output_fname, 'w', encoding="utf8") as output_file) :
        cgx_indentation = CgxIndentation()
        cgx_indentation.generate_cgx(input_file, output_file)
    with (open(expected_fname, 'r', encoding="utf8") as expected_file,
        open(output_fname, 'r', encoding="utf8") as output_file) :
        assert(output_file.read() == expected_file.read())

def test_regex_equal() -> None:
    """
    Test : test substitution of the equal character
    """
    input_fname, output_fname, expected_fname = get_input_output_expected("tests"
        +"/additional_tests/equal/")
    with (open(input_fname, 'r', encoding="utf8") as input_file,
        open(output_fname, 'w', encoding="utf8") as output_file) :
        cgx_indentation = CgxIndentation()
        cgx_indentation.generate_cgx(input_file, output_file)
    with (open(expected_fname, 'r', encoding="utf8") as expected_file,
        open(output_fname, 'r', encoding="utf8") as output_file) :
        assert(output_file.read() == expected_file.read())

def test_simple_key_value_with_spaces() -> None:
    """
    Test : one key/value with spaces and tabs around the key and the value
    """
    input_fname, output_fname, expected_fname = get_input_output_expected("tests"
        +"/additional_tests/simple_key_value_with_spaces/")
    with (open(input_fname, 'r', encoding="utf8") as input_file,
        open(output_fname, 'w', encoding="utf8") as output_file) :
        cgx_indentation = CgxIndentation()
        cgx_indentation.generate_cgx(input_file, output_file)
    with (open(expected_fname, 'r', encoding="utf8") as expected_file,
        open(output_fname, 'r', encoding="utf8") as output_file) :
        assert(output_file.read() == expected_file.read())

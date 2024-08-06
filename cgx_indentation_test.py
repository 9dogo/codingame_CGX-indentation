import pytest
from cgx_indentation import Cgx_indentation

def test_boolean_value_with_spaces_and_tab():
    cgx_indentation = Cgx_indentation("tests/test1")
    cgx_indentation.generate_cgx()
    cgx_indentation.close_files()
    with (open(cgx_indentation.output_file_name, 'r', encoding="utf8") as output,
        open(cgx_indentation.expected_file_name, 'r', encoding="utf8") as expected) :
        assert(output.read() == expected.read())


def test_simple_string():
    cgx_indentation = Cgx_indentation("tests/test2")
    cgx_indentation.generate_cgx()
    cgx_indentation.close_files()
    with (open(cgx_indentation.output_file_name, 'r', encoding="utf8") as output,
        open(cgx_indentation.expected_file_name, 'r', encoding="utf8") as expected) :
        assert(output.read() == expected.read())

def test_bloc_with_one_value():
    cgx_indentation = Cgx_indentation("tests/test3")
    cgx_indentation.generate_cgx()
    cgx_indentation.close_files()
    with (open(cgx_indentation.output_file_name, 'r', encoding="utf8") as output,
        open(cgx_indentation.expected_file_name, 'r', encoding="utf8") as expected) :
        assert(output.read() == expected.read())

def test_bloc_with_several_values():
    cgx_indentation = Cgx_indentation("tests/test4")
    cgx_indentation.generate_cgx()
    cgx_indentation.close_files()
    with (open(cgx_indentation.output_file_name, 'r', encoding="utf8") as output,
        open(cgx_indentation.expected_file_name, 'r', encoding="utf8") as expected) :
        assert(output.read() == expected.read())

def test_nested_blocs():
    cgx_indentation = Cgx_indentation("tests/test5")
    cgx_indentation.generate_cgx()
    cgx_indentation.close_files()
    with (open(cgx_indentation.output_file_name, 'r', encoding="utf8") as output,
        open(cgx_indentation.expected_file_name, 'r', encoding="utf8") as expected) :
        assert(output.read() == expected.read())

def test_empty_bloc():
    cgx_indentation = Cgx_indentation("tests/test6")
    cgx_indentation.generate_cgx()
    cgx_indentation.close_files()
    with (open(cgx_indentation.output_file_name, 'r', encoding="utf8") as output,
        open(cgx_indentation.expected_file_name, 'r', encoding="utf8") as expected) :
        assert(output.read() == expected.read())

def test_several_blocs():
    cgx_indentation = Cgx_indentation("tests/test7")
    cgx_indentation.generate_cgx()
    cgx_indentation.close_files()
    with (open(cgx_indentation.output_file_name, 'r', encoding="utf8") as output,
        open(cgx_indentation.expected_file_name, 'r', encoding="utf8") as expected) :
        assert(output.read() == expected.read())

def test_several_key_value():
    cgx_indentation = Cgx_indentation("tests/test9")
    cgx_indentation.generate_cgx()
    cgx_indentation.close_files()
    with (open(cgx_indentation.output_file_name, 'r', encoding="utf8") as output,
        open(cgx_indentation.expected_file_name, 'r', encoding="utf8") as expected) :
        assert(output.read() == expected.read())

def test_full_example():
    cgx_indentation = Cgx_indentation("tests/test11")
    cgx_indentation.generate_cgx()
    cgx_indentation.close_files()
    with (open(cgx_indentation.output_file_name, 'r', encoding="utf8") as output,
        open(cgx_indentation.expected_file_name, 'r', encoding="utf8") as expected) :
        assert(output.read() == expected.read())

def test_single_bloc_one_value():
    cgx_indentation = Cgx_indentation("tests/additional_tests/single_bloc_one_value")
    cgx_indentation.generate_cgx()
    cgx_indentation.close_files()
    with (open(cgx_indentation.output_file_name, 'r', encoding="utf8") as output,
        open(cgx_indentation.expected_file_name, 'r', encoding="utf8") as expected) :
        assert(output.read() == expected.read())

def test_regex_equal():
    cgx_indentation = Cgx_indentation("tests/additional_tests/equal")
    cgx_indentation.generate_cgx()
    cgx_indentation.close_files()
    with (open(cgx_indentation.output_file_name, 'r', encoding="utf8") as output,
        open(cgx_indentation.expected_file_name, 'r', encoding="utf8") as expected) :
        assert(output.read() == expected.read())


def test_simple_key_value_with_spaces():
    cgx_indentation = Cgx_indentation("tests/additional_tests/simple_key_value_with_spaces")
    cgx_indentation.generate_cgx()
    cgx_indentation.close_files()
    with (open(cgx_indentation.output_file_name, 'r', encoding="utf8") as output,
        open(cgx_indentation.expected_file_name, 'r', encoding="utf8") as expected) :
        assert(output.read() == expected.read())

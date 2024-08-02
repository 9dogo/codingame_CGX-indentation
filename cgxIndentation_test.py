import pytest
from cgxIndentation import CgxIndentation

def test_boolean_value_with_spaces_and_tab():
    cgxIndentation = CgxIndentation("tests/test1")
    cgxIndentation.generateCgx()
    cgxIndentation.closeFiles()
    assert(open(cgxIndentation.output_file_name, 'r').read() == open(cgxIndentation.expected_file_name, 'r').read())


def test_simple_string():
    cgxIndentation = CgxIndentation("tests/test2")
    cgxIndentation.generateCgx()
    cgxIndentation.closeFiles()
    assert(open(cgxIndentation.output_file_name, 'r').read() == open(cgxIndentation.expected_file_name, 'r').read())

def test_bloc_with_one_value():
    cgxIndentation = CgxIndentation("tests/test3")
    cgxIndentation.generateCgx()
    cgxIndentation.closeFiles()
    assert(open(cgxIndentation.output_file_name, 'r').read() == open(cgxIndentation.expected_file_name, 'r').read())

def test_bloc_with_several_values():
    cgxIndentation = CgxIndentation("tests/test4")
    cgxIndentation.generateCgx()
    cgxIndentation.closeFiles()
    assert(open(cgxIndentation.output_file_name, 'r').read() == open(cgxIndentation.expected_file_name, 'r').read())

def test_nested_blocs():
    cgxIndentation = CgxIndentation("tests/test5")
    cgxIndentation.generateCgx()
    cgxIndentation.closeFiles()
    assert(open(cgxIndentation.output_file_name, 'r').read() == open(cgxIndentation.expected_file_name, 'r').read())

def test_empty_bloc():
    cgxIndentation = CgxIndentation("tests/test6")
    cgxIndentation.generateCgx()
    cgxIndentation.closeFiles()
    assert(open(cgxIndentation.output_file_name, 'r').read() == open(cgxIndentation.expected_file_name, 'r').read())

def test_full_example():
    cgxIndentation = CgxIndentation("tests/test11")
    cgxIndentation.generateCgx()
    cgxIndentation.closeFiles()
    assert(open(cgxIndentation.output_file_name, 'r').read() == open(cgxIndentation.expected_file_name, 'r').read())

def test_single_bloc_one_value():
    cgxIndentation = CgxIndentation("tests/additional_tests/single_bloc_one_value")
    cgxIndentation.generateCgx()
    cgxIndentation.closeFiles()
    assert(open(cgxIndentation.output_file_name, 'r').read() == open(cgxIndentation.expected_file_name, 'r').read())

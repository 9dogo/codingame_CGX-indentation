import pytest
from cgxIndentation import CgxIndentation

def test_boolean_value_with_spaces_and_tab():
    cgxIndentation = CgxIndentation("tests/test1")
    cgxIndentation.generateCgx()
    cgxIndentation.closeFiles()
    assert(open(cgxIndentation.output_file_name, 'r').read() == open(cgxIndentation.expected_file_name, 'r').read())

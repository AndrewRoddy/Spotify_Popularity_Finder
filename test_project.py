import pytest
from project import length_limit
from project import yes_or_no
from project import ms_to_m


def test_length_limit():
    # Makes sure that regular values work
    assert length_limit("hello everyone how is it going?", 5) == "hello..."
    assert length_limit("hello everyone how is it going?", 10) == "hello ever..."
    assert length_limit("hello", 1) == "h..."

    # Tests 0 length
    assert length_limit("hello", 0) == "..."

    # Tests only inputting spaces
    assert length_limit("     .", 5) == "     ..."


def test_yes_or_no():
    # Tests yes inputs
    assert yes_or_no("1") == 1
    assert yes_or_no("y") == 1
    assert yes_or_no("yes") == 1

    # Tests no inputs
    assert yes_or_no("0") == 0
    assert yes_or_no("n") == 0
    assert yes_or_no("no") == 0

    # Test invalid inputs
    assert yes_or_no("z") == -1
    assert yes_or_no("") == -1


def test_ms_to_m():
    # Tests one second
    assert ms_to_m(1000) == "0:01"
    assert ms_to_m(10000) == "0:10"

    # Tests minutes
    assert ms_to_m(60000) == "1:00"
    assert ms_to_m(120000) == "2:00"

    # Tests minutes and seconds
    assert ms_to_m(121000) == "2:01"

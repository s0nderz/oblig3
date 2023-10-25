import pytest

from main import isLeapYear, random_year


def test_is_leap_year_divisble_by_4_and_not_100():
    assert isLeapYear()

def test_is_leap_year_divisble_by_400():
    assert isLeapYear()

def test_is_leap_year_divisible_by_4000():
    assert isLeapYear() == False

def test_is_not_leap_year_divisble_by_100_not_4_and_not_400():
    assert isLeapYear() == False
    assert isLeapYear() == False
    assert isLeapYear() == False
    assert isLeapYear() == False


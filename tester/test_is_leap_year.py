import pytest

from oblig3.main import isLeapYear


def test_is_leap_year_divisble_by_4_and_not_100():
    assert isLeapYear(2000)

def test_is_leap_year_divisble_by_400():
    assert isLeapYear(2024)

def test_is_leap_year_divisible_by_4000():
    assert isLeapYear(4000) == False

def test_is_not_leap_year_divisble_by_100_not_4_and_not_400():
    assert isLeapYear(1700) == False
    assert isLeapYear(1800) == False
    assert isLeapYear(1900) == False
    assert isLeapYear(2100) == False


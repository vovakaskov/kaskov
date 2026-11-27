import string
import operator


def _is_not_punctuation(ch):
    return ch not in string.punctuation


def remove_punctuation(s):
    return "".join(filter(_is_not_punctuation, s))


import pytest


@pytest.mark.parametrize("s, expected", [
    ("Hi, world!", "Hi world"),
    ("", ""),
    ("a.b,c;d", "abcd"),
    ("...", ""),
])
def test_remove_punctuation_removes_punctuation(s, expected):
    assert remove_punctuation(s) == expected


def test_remove_punctuation_does_not_mutate_input():
    s = "Hi, world!"
    original = s
    remove_punctuation(s)
    assert s == original

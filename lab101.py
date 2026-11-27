import operator


def _validate(intervals):
    for start, end in intervals:
        if start > end:
            raise ValueError(f"Invalid interval: [{start}, {end}]")


def merge_intervals(intervals):
    _validate(intervals)

    merged = []
    for start, end in sorted(intervals, key=operator.itemgetter(0)):
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged


import pytest


def test_merge_intervals_overlapping_merges():
    assert merge_intervals([[1, 3], [2, 6], [8, 10]]) == [[1, 6], [8, 10]]


@pytest.mark.parametrize("intervals, expected", [
    ([[1, 2], [2, 3]], [[1, 3]]),
    ([[1, 10], [2, 3]], [[1, 10]]),
    ([], []),
])
def test_merge_intervals_various_cases(intervals, expected):
    assert merge_intervals(intervals) == expected


def test_merge_intervals_invalid_raises_value_error():
    with pytest.raises(ValueError):
        merge_intervals([[5, 1]])


def test_merge_intervals_does_not_mutate_input():
    intervals = [[1, 3], [2, 6], [8, 10]]
    original = [pair[:] for pair in intervals]
    merge_intervals(intervals)
    assert intervals == original

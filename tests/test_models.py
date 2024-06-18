"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
from inflammation.models import daily_mean, daily_max, daily_min
import pytest


# def test_daily_mean_zeros():
#     """Test that mean function works for an array of zeros."""
#
#     test_input = np.array([[0, 0],
#                            [0, 0],
#                            [0, 0]])
#     test_result = np.array([0, 0])
#
#     # Need to use Numpy testing functions to compare arrays
#     npt.assert_array_equal(daily_mean(test_input), test_result)
#
#
# def test_daily_mean_integers():
#     """Test that mean function works for an array of positive integers."""
#
#     test_input = np.array([[1, 2],
#                            [3, 4],
#                            [5, 6]])
#     test_result = np.array([3, 4])
#
#     # Need to use Numpy testing functions to compare arrays
#     npt.assert_array_equal(daily_mean(test_input), test_result)

# To parametrise our above 2 tests we can write the above 2 tests as:
# This means we can use the same test code with different inputs instead
# of writing a separate function for each different test
@pytest.mark.parametrize(
    'test, expected',
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),  # Note: input in last square brackets is the expected result
        ([[1, 2], [3, 4], [5, 6]], [3, 4]),
    ])
def test_daily_mean(test, expected):
    """Test mean function works for array of zeros and positive integers."""
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))


# def test_daily_max_integers():
#     """Test that max function works for an array of positive integers."""
#     test_input = np.array([[1, 2],
#                            [3, 4],
#                            [5, 6]])
#     test_result = np.array([5, 6])
#
#     npt.assert_array_equal(daily_max(test_input), test_result)


@pytest.mark.parametrize(
    'test, expected',
    [
        ([[-5, 0], [3, 6], [0, 1]], [3, 6]),  # Note: input in last square brackets is the expected result
        ([[-1, -2], [-3, -4], [-5, -6]], [-1, -2]),
        ([[4, 2, 5], [1, 6, 2], [4, 1, 9]], [4, 6, 9]),
        ([[4, -2, 5], [1, -6, 2], [-4, -1, 9]], [4, -1, 9])
    ])
def test_daily_max(test, expected):
    """Test max function works for arrays of negative and positive numbers."""
    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))


# def test_daily_min():
#     """Test that min function works for an array of positive and integers."""
#     test_input = np.array([[1, 2, -7],
#                            [3, 4, -2],
#                            [5, 6, -3]])
#     test_result = np.array([1, 2, -7])
#
#     npt.assert_array_equal(daily_min(test_input), test_result)

@pytest.mark.parametrize(
    'test, expected',
    [
        ([[1, 2, -7], [3, 4, -2], [5, 6, -3]], [1, 2, -7]),
        ([[1, 2], [3, 4], [5, 6]], [1, 2]),
        ([[4, 2, 5], [1, 6, 2], [4, 1, 9]], [1, 1, 2]),
        ([[4, -2, 5], [1, -6, 2], [-4, -1, 9]], [-4, -6, 2])
    ])
def test_daily_min(test, expected):
    """Test min function works for array of mixed negative and positive numbers."""
    npt.assert_array_equal(daily_min(np.array(test)), np.array(expected))


def test_daily_min_string():
    """Test for TypeError when passing strings"""
    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 3], ['General', 'kenobi']])

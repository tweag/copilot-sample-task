import pandas as pd
import unittest

# Possible values for 'cut', in increasing order of quality
CUT = ["Fair", "Good", "Very Good", "Premium", "Ideal"]

# Possible values for 'color', in increasing order of quality
COLOR = ["J", "I", "H", "G", "F", "E", "D"]

# Possible values for 'clarity', in increasing order of quality
CLARITY = ["I1", "SI2", "ST1", "VS2", "VS1", "VVS2", "VVS1", "IF"]

def load():
    """Returns a pandas dataframe with the data from diamonds.csv.
    """

    pass

def aggregate(data, weight_range, group_key):
    pass

def filter_range(data, key, range):
    """Returns subtable in which the key column belongs to the specified range.

    `key` can be "cut", "color", or "clarity", and `range` is a pair of strings
    representing a range that includes both endpoints.

    For example, if `key` is "cut" and `range` is ("Good", "Premium") then the
    return value is a data frame consisting of all the diamonds whose cut is
    "Good", "Very Good", or "Premium".
    """
    col_to_order = {
        "cut": CUT,
        "color": COLOR,
        "clarity": CLARITY
    }

    low, high = range
    ordered_values = col_to_order[key]
    low_index = ordered_values.index(low)
    high_index = ordered_values.index(high)
    values = ordered_values[low_index: high_index + 1]
    return data[data[key].isin(values)]


######################################
# Unit tests
######################################

class TestAggregate(unittest.TestCase):

    def test_load(self):
        data = load()
        self.assertEqual(
            list(data.columns), ["carat", "cut", "color", "clarity", "price"])
        self.assertEqual(data.shape, (53940, 5))

    def test_small_by_color(self):
        data = load()
        small_by_color = aggregate(data, (0, 1), "color")
        self.assertEqual(
            small_by_color,
            [
                1547.0363321799307,
                1596.311451495259,
                1696.0653524748232,
                1721.8043047669353,
                1919.747154588676,
                1807.5567362428842,
                1903.0045837917125,
            ])

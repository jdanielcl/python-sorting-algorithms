from unittest import TestCase
from main import Sorting

def dataset_one(func):
    def wrapper(self, *args, **kwargs):
        data = [5, 4, 3, 2, 1]
        self.sorting = Sorting(data)
        func(self, *args, **kwargs)
    return wrapper

class SortingTest(TestCase):

    @dataset_one
    def test_selection_sort(self):
        pass
import unittest
import selectionsort


# test arrays
test_arrs = [
    [-2, 7, 15, -14, 0, 15, 0, 7, -7, -4, -13 ],
    [10, 6, 2, 4, -2, 0, 23, 65, 1, 1 , -1 , 0],
    [-23, 2, 8, 6, 2, -10, 23, 64, 96, 45, 73 ],
    [232, 324, -234, 765, 784, 647, 403, 324, 0],
    [-2342, 8324, -4534, 3445, -7455, 2343, 9934]
]


class TestTimSort(unittest.TestCase):
    def test_one(self):
        for arr in test_arrs:
            print(f"Array: {arr}")
            self.assertEqual(selectionsort.selection_sort(arr), sorted(arr))
            print(f"Sorted Array: {arr}")

if __name__ == "__main__":
    unittest.main()
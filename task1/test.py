import unittest
from solution import strict

class StrictTestCase(unittest.TestCase):
    @strict
    def typed_only(self, a: int, b: int) -> int:
        return a + b

    @strict
    def mixed_typing(self, a: int, b, c: int) -> int:
        return a + c

    @strict
    def empty(self):
        return 'good'

    def test_matching_types(self):
        self.assertEqual(self.typed_only(1, 2), 3)
        self.assertEqual(self.empty(), 'good')
        self.assertEqual(self.mixed_typing(1, "hello", 2), 3)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            self.typed_only(1, 2.4)

    def test_differing_args_count(self):
        with self.assertRaises(TypeError):
            self.typed_only(1, 2, 3)
            self.typed_only(1)
            self.typed_only()
            self.empty(1)


if __name__ == '__main__':
    unittest.main()
import unittest


def Do() -> bool:
    return True


if __name__ == "__main__":
    print(Do())


class TestDo(unittest.TestCase):
    def testBasic(self):
        self.assertTrue(Do())

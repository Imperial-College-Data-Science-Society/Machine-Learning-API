import unittest


class TestSetup(unittest.TestCase):
    """Test Dependencies from `requirements.txt`."""

    def test__sys(self):
        import sys
        return self.assertIsNotNone(sys)


if __name__ == '__main__':
    unittest.main()

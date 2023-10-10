import unittest
import luhns

class LuhnsTest(unittest.TestCase):
  def test_valid_card(self):
    self.assertTrue(luhns.validate(123))

if __name__ == '__main__':
  unittest.main()

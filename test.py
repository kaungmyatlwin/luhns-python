import unittest
import luhns

class LuhnsTest(unittest.TestCase):
  def test_valid_card(self):
    self.assertTrue(luhns.validate(79927398713))
    # self.assertFalse(luhns.validate(123456789))

if __name__ == '__main__':
  unittest.main()

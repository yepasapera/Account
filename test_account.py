import unittest
from account import *


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.acc = Account("Alice")

    def tearDown(self):
        del self.acc

    def test_init(self):
        self.assertEqual(self.acc._Account__account_name, "Alice")
        self.assertEqual(self.acc._Account__account_balance, 0)

    def test_deposit(self):
        self.assertTrue(self.acc.deposit(100))
        self.assertEqual(self.acc._Account__account_balance, 100)
        # depositing 0
        self.assertFalse(self.acc.deposit(0))
        self.assertEqual(self.acc._Account__account_balance,100)
        #depositing negative
        self.assertFalse(self.acc.deposit(-100))
        self.assertEqual(self.acc._Account__account_balance, 100)


    def test_withdraw(self):
        self.assertTrue(self.acc.deposit(100))
        #withdrawing 0
        self.assertFalse(self.acc.withdraw(0))
        self.assertEqual(self.acc._Account__account_balance, 100)
        #overdrawing
        self.assertFalse(self.acc.withdraw(-200))
        self.assertEqual(self.acc._Account__account_balance, 100)
        #withdrwaing within the limit
        self.assertFalse(self.acc.withdraw(-20))
        self.assertEqual(self.acc._Account__account_balance, 100)


if __name__ == '__main__':
    unittest.main()


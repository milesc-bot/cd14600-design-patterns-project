import unittest
from balance.budget_strategy import (
    BudgetStrategy,
    FiftyThirtyTwentyStrategy,
    ZeroBasedBudgetStrategy,
)


class TestFiftyThirtyTwentyStrategy(unittest.TestCase):

    def setUp(self):
        self.strategy = FiftyThirtyTwentyStrategy()

    def test_strategy_name(self):
        self.assertEqual(self.strategy.get_name(), "50/30/20 Rule")

    def test_positive_balance_allocation(self):
        allocation = self.strategy.analyze(1000)
        self.assertEqual(allocation["Needs"], 500.0)
        self.assertEqual(allocation["Wants"], 300.0)
        self.assertEqual(allocation["Savings"], 200.0)

    def test_zero_balance_allocation(self):
        allocation = self.strategy.analyze(0)
        self.assertEqual(allocation["Needs"], 0.0)
        self.assertEqual(allocation["Wants"], 0.0)
        self.assertEqual(allocation["Savings"], 0.0)

    def test_negative_balance_allocation(self):
        allocation = self.strategy.analyze(-100)
        self.assertEqual(allocation["Needs"], 0.0)
        self.assertEqual(allocation["Wants"], 0.0)
        self.assertEqual(allocation["Savings"], 0.0)

    def test_allocation_keys(self):
        allocation = self.strategy.analyze(500)
        self.assertIn("Needs", allocation)
        self.assertIn("Wants", allocation)
        self.assertIn("Savings", allocation)
        self.assertEqual(len(allocation), 3)


class TestZeroBasedBudgetStrategy(unittest.TestCase):

    def setUp(self):
        self.strategy = ZeroBasedBudgetStrategy()

    def test_strategy_name(self):
        self.assertEqual(self.strategy.get_name(), "Zero-Based Budgeting")

    def test_positive_balance_allocation(self):
        allocation = self.strategy.analyze(1000)
        self.assertEqual(allocation["Housing"], 350.0)
        self.assertEqual(allocation["Living Expenses"], 250.0)
        self.assertEqual(allocation["Transportation"], 150.0)
        self.assertEqual(allocation["Savings"], 100.0)
        self.assertEqual(allocation["Debt Repayment"], 100.0)
        self.assertEqual(allocation["Personal"], 50.0)

    def test_zero_balance_allocation(self):
        allocation = self.strategy.analyze(0)
        for value in allocation.values():
            self.assertEqual(value, 0.0)

    def test_negative_balance_allocation(self):
        allocation = self.strategy.analyze(-50)
        for value in allocation.values():
            self.assertEqual(value, 0.0)

    def test_allocation_keys(self):
        allocation = self.strategy.analyze(200)
        expected_keys = [
            "Housing", "Living Expenses", "Transportation",
            "Savings", "Debt Repayment", "Personal",
        ]
        for key in expected_keys:
            self.assertIn(key, allocation)
        self.assertEqual(len(allocation), 6)

    def test_allocations_sum_to_balance(self):
        balance = 1000
        allocation = self.strategy.analyze(balance)
        total = sum(allocation.values())
        self.assertAlmostEqual(total, balance, places=2)


class TestStrategySwapping(unittest.TestCase):

    def test_can_swap_strategies_at_runtime(self):
        strategies = [
            FiftyThirtyTwentyStrategy(),
            ZeroBasedBudgetStrategy(),
        ]
        balance = 1000
        for strategy in strategies:
            allocation = strategy.analyze(balance)
            self.assertIsInstance(allocation, dict)
            self.assertTrue(len(allocation) > 0)

    def test_cannot_instantiate_abstract_class(self):
        with self.assertRaises(TypeError):
            BudgetStrategy()


if __name__ == "__main__":
    unittest.main()

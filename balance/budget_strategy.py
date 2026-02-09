from abc import ABC, abstractmethod


class BudgetStrategy(ABC):
    """Abstract base class for budget planning strategies (Strategy Pattern).

    This pattern allows users to switch between different budgeting
    approaches at runtime without modifying the core Balance logic.
    """

    @abstractmethod
    def analyze(self, balance) -> dict:
        """Analyze the current balance and return budget allocation.

        Args:
            balance (float): The current available balance.

        Returns:
            dict: A dictionary with category names as keys and
                  allocated amounts as values.
        """
        pass

    @abstractmethod
    def get_name(self) -> str:
        """Return the name of this budgeting strategy.

        Returns:
            str: The strategy name.
        """
        pass


class FiftyThirtyTwentyStrategy(BudgetStrategy):
    """Implements the 50/30/20 budgeting rule.

    Allocates income as follows:
    - 50% for Needs (rent, groceries, utilities)
    - 30% for Wants (dining, entertainment, hobbies)
    - 20% for Savings (emergency fund, investments)
    """

    def analyze(self, balance):
        """Allocate balance using 50/30/20 rule."""
        if balance <= 0:
            return {"Needs": 0.0, "Wants": 0.0, "Savings": 0.0}
        return {
            "Needs": round(balance * 0.50, 2),
            "Wants": round(balance * 0.30, 2),
            "Savings": round(balance * 0.20, 2),
        }

    def get_name(self):
        return "50/30/20 Rule"


class ZeroBasedBudgetStrategy(BudgetStrategy):
    """Implements zero-based budgeting.

    Every dollar is assigned a purpose. Allocates income as:
    - 35% for Housing
    - 25% for Living Expenses
    - 15% for Transportation
    - 10% for Savings
    - 10% for Debt Repayment
    - 5% for Personal
    """

    def analyze(self, balance):
        """Allocate every dollar to a specific category."""
        if balance <= 0:
            return {
                "Housing": 0.0,
                "Living Expenses": 0.0,
                "Transportation": 0.0,
                "Savings": 0.0,
                "Debt Repayment": 0.0,
                "Personal": 0.0,
            }
        return {
            "Housing": round(balance * 0.35, 2),
            "Living Expenses": round(balance * 0.25, 2),
            "Transportation": round(balance * 0.15, 2),
            "Savings": round(balance * 0.10, 2),
            "Debt Repayment": round(balance * 0.10, 2),
            "Personal": round(balance * 0.05, 2),
        }

    def get_name(self):
        return "Zero-Based Budgeting"

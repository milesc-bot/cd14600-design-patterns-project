"""This module serves as the entry point for the program."""
from balance.balance import Balance
from balance.balance_observer import LowBalanceAlertObserver
from balance.balance_observer import PrintObserver
from balance.budget_strategy import (
    FiftyThirtyTwentyStrategy,
    ZeroBasedBudgetStrategy,
)
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory
from transaction.transaction_adapter import TransactionAdapter
from transaction.external_income_transaction import ExternalFreelanceIncome


def main():
    print("=" * 60)
    print("  Personal Finance Manager — Design Patterns Demo")
    print("=" * 60)

    print("\n--- Setting up Balance (Singleton Pattern) ---")
    balance = Balance.get_instance()
    balance.reset()
    print(f"Balance instance created: {balance.summary()}")

    balance2 = Balance.get_instance()
    print(
        f"Same instance? {balance is balance2} "
        f"(Singleton verified)"
    )

    print("\n--- Registering Observers (Observer Pattern) ---")
    print_observer = PrintObserver()
    low_balance_observer = LowBalanceAlertObserver(threshold=100)
    balance.register_observer(print_observer)
    balance.register_observer(low_balance_observer)
    print("PrintObserver registered.")
    print("LowBalanceAlertObserver registered (threshold: $100.00).")

    print("\n--- Adding Standard Transactions ---")
    transactions = [
        Transaction(100, TransactionCategory.INCOME),
        Transaction(50, TransactionCategory.EXPENSE),
        Transaction(200, TransactionCategory.INCOME),
        Transaction(75, TransactionCategory.EXPENSE),
    ]

    for t in transactions:
        print(f"\nApplying: {t}")
        balance.apply_transaction(t)

    print(f"\n{balance.summary()}")

    print("\n--- External Freelance Income (Adapter Pattern) ---")
    freelance_income = ExternalFreelanceIncome(
        1200, "INV-98765", "Mobile App Project"
    )
    print(
        f"External income: ${freelance_income.amount}, "
        f"Invoice: {freelance_income.invoice_id}, "
        f"Project: {freelance_income.description}"
    )
    adapter = TransactionAdapter(freelance_income)
    adapted_transaction = adapter.to_transaction()
    print(f"Adapted to: {adapted_transaction}")

    print(f"\nApplying adapted transaction:")
    balance.apply_transaction(adapted_transaction)
    print(f"\n{balance.summary()}")

    print("\n--- Budget Planning (Strategy Pattern) ---")

    current_balance = balance.get_balance()

    print(f"\nUsing 50/30/20 Rule Strategy:")
    strategy_50_30_20 = FiftyThirtyTwentyStrategy()
    allocation = strategy_50_30_20.analyze(current_balance)
    print(f"Strategy: {strategy_50_30_20.get_name()}")
    for category, amount in allocation.items():
        print(f"  {category}: ${amount:.2f}")

    print(f"\nSwitching to Zero-Based Budgeting Strategy:")
    strategy_zero = ZeroBasedBudgetStrategy()
    allocation = strategy_zero.analyze(current_balance)
    print(f"Strategy: {strategy_zero.get_name()}")
    for category, amount in allocation.items():
        print(f"  {category}: ${amount:.2f}")

    print("\n--- Triggering Low Balance Alert ---")
    large_expense = Transaction(1300, TransactionCategory.EXPENSE)
    print(f"\nApplying large expense: {large_expense}")
    balance.apply_transaction(large_expense)
    print(f"\n{balance.summary()}")

    print("\n" + "=" * 60)
    print("  Demo Complete")
    print("=" * 60)


if __name__ == "__main__":
    main()

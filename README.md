# Personal Finance Manager — Design Patterns Project

A hands-on Python application demonstrating four classic Object-Oriented Design Patterns applied to a simplified personal finance manager. The application tracks transactions, adapts external data, observes balance changes, and supports dynamic budgeting strategies.

## Getting Started

### Dependencies

- Python >= 3.10.x

### Installation

1. Clone the repo:

```bash
git clone <your-repo-url>
cd cd14600-project-starter/starter
```

2. Run the Program:

```bash
python main.py
```

## Testing

This project uses Python's built-in `unittest` framework.

To run all tests:

```bash
python -m unittest discover -v
```

To run a single test file:

```bash
python -m unittest balance.test_balance -v
```

### Test Breakdown

- `balance/test_balance.py` — Verifies correct implementation of the Singleton Balance class.
- `balance/test_balance_observer.py` — Validates that low-balance alerts are triggered at the correct threshold and that PrintObserver outputs correctly.
- `balance/test_budget_strategy.py` — Tests both budget strategies (50/30/20 and Zero-Based) including edge cases.
- `transaction/test_transaction.py` — Confirms Transaction creation, string representation, and equality.
- `transaction/test_transaction_adapter.py` — Ensures external freelance income is correctly adapted into Transaction objects.

## Design Patterns Implemented

### 1. Singleton Pattern — `Balance` class (`balance/balance.py`)

**Why this pattern was chosen:**
The Balance class manages the application's financial state. Having multiple Balance instances could lead to inconsistent or duplicated financial data. The Singleton pattern guarantees a single, globally accessible instance of the balance manager.

**How it improves the design:**
- Ensures data consistency across the entire application — every component references the same balance.
- Prevents accidental creation of multiple balance trackers.
- Provides a clear `get_instance()` access point so all modules share the same state.

**Trade-offs:**
- Makes unit testing slightly more complex since state persists between tests (mitigated with the `reset()` method).
- Tight coupling to a global instance can reduce flexibility if multiple balances were ever needed.

### 2. Adapter Pattern — `TransactionAdapter` class (`transaction/transaction_adapter.py`)

**Why this pattern was chosen:**
The application needs to process income from external freelance platforms that use a different data format (with invoice IDs and project descriptions). The Adapter pattern bridges this incompatibility by converting `ExternalFreelanceIncome` objects into standard `Transaction` objects.

**How it improves the design:**
- Allows the application to integrate with external data sources without modifying the core `Transaction` class.
- Follows the Open/Closed Principle — new external formats can be supported by writing new adapters rather than changing existing code.
- Keeps the internal transaction model clean and focused.

**Trade-offs:**
- Adds an extra layer of abstraction for each external data format.
- Some external data (like `invoice_id` and `description`) is not preserved in the adapted Transaction, which could be a limitation if that information is needed later.

### 3. Observer Pattern — `LowBalanceAlertObserver` and `PrintObserver` (`balance/balance_observer.py`)

**Why this pattern was chosen:**
Multiple components need to react to balance changes (printing updates, triggering alerts). The Observer pattern decouples the Balance from its dependents, allowing any number of observers to be registered and notified automatically when a transaction is applied.

**How it improves the design:**
- Decouples the Balance class from notification logic — it does not need to know what happens after a transaction.
- New observers can be added without modifying Balance (e.g., an email notification observer, a logging observer).
- `LowBalanceAlertObserver` monitors the balance against a configurable threshold and triggers an alert when the balance drops too low.
- `PrintObserver` provides real-time visibility into every transaction and the resulting balance.

**Trade-offs:**
- Observers are notified in registration order, which could matter if one observer depends on another's side effects.
- Debugging can be harder when many observers are registered since the notification chain is implicit.

### 4. Strategy Pattern (Student's Choice) — Budget Strategies (`balance/budget_strategy.py`)

**Why this pattern was chosen:**
Users have different budgeting preferences. The Strategy pattern allows the application to support multiple budgeting approaches and switch between them at runtime without modifying any core logic. This makes the budgeting feature flexible and extensible.

**Where it fits into the app:**
The Strategy pattern is used for budget planning analysis. After transactions are processed and the balance is known, users can apply different budgeting strategies to see how their funds should be allocated. Two concrete strategies are provided:

- **50/30/20 Rule** (`FiftyThirtyTwentyStrategy`): Allocates 50% to Needs, 30% to Wants, and 20% to Savings.
- **Zero-Based Budgeting** (`ZeroBasedBudgetStrategy`): Assigns every dollar to a specific category (Housing, Living Expenses, Transportation, Savings, Debt Repayment, Personal).

**How it improves flexibility, testability, and scalability:**
- **Flexibility:** New budgeting strategies can be added by simply creating a new class that extends `BudgetStrategy` — no existing code needs to change.
- **Testability:** Each strategy can be tested independently with known inputs and expected outputs.
- **Scalability:** The architecture supports any number of strategies, and users can switch between them dynamically.

**Trade-offs:**
- Introduces additional classes for each new strategy, increasing the number of files.
- For simple applications with only one budgeting approach, this pattern might be over-engineered — but it pays off as requirements grow.

## Project Structure

```
├── balance/
│   ├── balance.py                  # Singleton Balance class
│   ├── balance_observer.py         # Observer interface and implementations
│   ├── budget_strategy.py          # Strategy pattern for budgeting
│   ├── test_balance.py             # Balance unit tests
│   ├── test_balance_observer.py    # Observer unit tests
│   └── test_budget_strategy.py     # Strategy unit tests
├── transaction/
│   ├── transaction.py              # Transaction class with enum
│   ├── transaction_category.py     # TransactionCategory enum
│   ├── transaction_adapter.py      # Adapter for external transactions
│   ├── external_income_transaction.py  # External freelance income model
│   ├── test_transaction.py         # Transaction unit tests
│   └── test_transaction_adapter.py # Adapter unit tests
├── main.py                         # Entry point and demo script
├── README.md                       # This file
└── LICENSE.txt                     # License
```

## Built With

* [Python](https://www.python.org/) — Main programming language
* [unittest](https://docs.python.org/3/library/unittest.html) — Testing framework
* [PEP8](https://peps.python.org/pep-0008/) — Style guide for Python code

## License

[License](LICENSE.txt)

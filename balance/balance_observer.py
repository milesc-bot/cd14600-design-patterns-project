class IBalanceObserver:
    """Interface for balance observers."""

    def update(self, balance, transaction):
        """Handle balance updates."""
        raise NotImplementedError("Subclasses must implement update method.")


class PrintObserver(IBalanceObserver):
    """Observer that prints the current balance after each transaction."""

    def update(self, balance, transaction):
        """Print balance update message."""
        print(
            f"[PrintObserver] Transaction applied: "
            f"{transaction}. Current balance: ${balance:.2f}"
        )


class LowBalanceAlertObserver(IBalanceObserver):
    """Observer that triggers an alert when balance falls below threshold."""

    def __init__(self, threshold):
        self.threshold = threshold
        self.alert_triggered = False

    def update(self, balance, transaction):
        """Alert if balance drops below threshold."""
        if balance < self.threshold:
            self.alert_triggered = True
            print(
                f"[ALERT] Low balance warning! Balance ${balance:.2f} "
                f"is below threshold ${self.threshold:.2f}."
            )
        else:
            self.alert_triggered = False

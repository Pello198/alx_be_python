import sys
from bank_account import BankAccount

def fmt_amount_for_message(a: float) -> str:
    # Format deposit/withdraw messages to remove unnecessary .00 while keeping readability
    # Example: 50.0 -> "50", 50.5 -> "50.50"
    if a == int(a):
        return f"{int(a)}"
    return f"{a:.2f}"

def main():
    # start with $100.00 (float)
    account = BankAccount(100.0)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        try:
            account.deposit(amount)
            print(f"Deposited: ${fmt_amount_for_message(amount)}")
        except ValueError as e:
            print(e)
    elif command == "withdraw" and amount is not None:
        try:
            if account.withdraw(amount):
                print(f"Withdrew: ${fmt_amount_for_message(amount)}")
            else:
                print("Insufficient funds.")
        except ValueError as e:
            print(e)
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()

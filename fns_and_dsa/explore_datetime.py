# explore_datetime.py

from datetime import datetime, timedelta


def display_current_datetime():
    """Display the current date and time in YYYY-MM-DD HH:MM:SS format."""
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date


def calculate_future_date(current_date, days_to_add):
    """Calculate a future date by adding days_to_add to current_date."""
    future_date = current_date + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date


def main():
    # Part 1: Display current datetime
    current_date = display_current_datetime()

    # Part 2: Ask user for number of days to add
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()

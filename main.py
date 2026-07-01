# Business Expense Tracker
# Main file: menu and program flow

from datetime import datetime
from expenses import (
    load_expenses,
    total_by_category,
    total_by_month,
    most_expensive_month,
    monthly_average,
    filter_by_date_range,
    export_summary
)

FILE_NAME = "expenses_data.csv"
OUTPUT_FILE = "summary_report.csv"


def show_menu():
    print("\n===== BUSINESS EXPENSE TRACKER =====")
    print("1. Total spent by category")
    print("2. Total spent by month")
    print("3. Most expensive month")
    print("4. Monthly average")
    print("5. Filter expenses by date range")
    print("6. Export summary report to CSV")
    print("0. Exit")
    print("=====================================")


def ask_for_date(message):
    """Asks the user for a date in YYYY-MM-DD format and returns a datetime object."""
    while True:
        try:
            date_str = input(message).strip()
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD (e.g. 2026-01-15).")


def main():
    expenses = load_expenses(FILE_NAME)

    if not expenses:
        print("No expense data found. Please check the CSV file.")
        return

    print(f"\n{len(expenses)} expense records loaded successfully.")

    while True:
        show_menu()
        option = input("Select an option: ").strip()

        if option == "1":
            print("\n--- TOTAL BY CATEGORY ---")
            for category, total in total_by_category(expenses).items():
                print(f"  {category}: ${total:,.2f}")

        elif option == "2":
            print("\n--- TOTAL BY MONTH ---")
            for month, total in total_by_month(expenses).items():
                print(f"  {month}: ${total:,.2f}")

        elif option == "3":
            month, amount = most_expensive_month(expenses)
            print(f"\n--- MOST EXPENSIVE MONTH ---")
            print(f"  {month} with a total of ${amount:,.2f}")

        elif option == "4":
            avg = monthly_average(expenses)
            print(f"\n--- MONTHLY AVERAGE ---")
            print(f"  ${avg:,.2f} per month")

        elif option == "5":
            print("\n--- FILTER BY DATE RANGE ---")
            start = ask_for_date("Start date (YYYY-MM-DD): ")
            end = ask_for_date("End date (YYYY-MM-DD): ")

            if start > end:
                print("Start date cannot be after end date.")
                continue

            filtered = filter_by_date_range(expenses, start, end)

            if not filtered:
                print("No expenses found in that date range.")
            else:
                print(f"\n{len(filtered)} expense(s) found:")
                for e in filtered:
                    print(f"  {e['date'].strftime('%Y-%m-%d')} | {e['category']} | "
                          f"${e['amount']:,.2f} | {e['description']}")

        elif option == "6":
            export_summary(expenses, OUTPUT_FILE)

        elif option == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

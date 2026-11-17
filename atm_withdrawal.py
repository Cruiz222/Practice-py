
from decimal import Decimal, InvalidOperation
import getpass


def authenticate_customer(valid_pin, max_attempts=3):
    for attempt in range(max_attempts):
        pin = getpass.getpass("Enter your PIN: ")

        if pin == valid_pin:
            print("Authentication successful.")
            return True

        print(f"Incorrect PIN. {max_attempts - attempt - 1} attempts remaining.")

    return False


def validate_withdrawal(amount, balance, atm_cash):
    if amount <= 0:
        return "Invalid withdrawal amount."

    if amount % Decimal("500") != 0:
        return "Amount must be a multiple of ₦500."

    if amount > balance:
        return "Insufficient account balance."

    if amount > atm_cash:
        return "ATM has insufficient cash."

    return None


def dispense_cash(amount, dispenser_success):
    print(f"Attempting to dispense ₦{amount:,.2f}...")
    return dispenser_success


def process_withdrawal(amount, balance, atm_cash,
                       dispenser_success=True,
                       reversal_success=True):

    transaction = {
        "amount": amount,
        "status": "pending",
    }

    error = validate_withdrawal(amount, balance, atm_cash)

    if error:
        transaction["status"] = "failed"
        print(error)
        return balance, atm_cash, transaction

    transaction["status"] = "authorized"

    # Debit customer account
    balance -= amount
    transaction["status"] = "dispensing"

    if dispense_cash(amount, dispenser_success):
        atm_cash -= amount
        transaction["status"] = "successful"
        print("Please collect your cash.")
    else:
        print("Cash dispensing failed.")

        if reversal_success:
            balance += amount
            transaction["status"] = "reversed"
            print("Your account has been refunded.")
        else:
            transaction["status"] = "reversal_pending"
            print("Reversal pending. Please contact your bank.")

    return balance, atm_cash, transaction


def atm_withdrawal(card_inserted, valid_card, balance, valid_pin,
                   dispenser_success=True, reversal_success=True):

    atm_cash = Decimal("100000")
    transaction = None
    card_retained = False

    print("WELCOME DEAR VALUED CUSTOMER")

    if not card_inserted:
        print("Please insert your card.")
        return

    if not valid_card:
        print("Invalid card.")
        print("Please collect your card.")
        return

    if not authenticate_customer(valid_pin):
        card_retained = True
        print("Maximum PIN attempts reached. Card retained.")
        return

    option = input("Select transaction (withdrawal): ").strip().lower()

    if option != "withdrawal":
        print("Unsupported transaction.")
        print("Please collect your card.")
        return

    try:
        amount = Decimal(input("Enter withdrawal amount: ").strip())
    except InvalidOperation:
        print("Invalid amount.")
        print("Please collect your card.")
        return

    balance, atm_cash, transaction = process_withdrawal(
        amount,
        balance,
        atm_cash,
        dispenser_success,
        reversal_success,
    )

    print(f"Transaction status: {transaction['status']}")
    print(f"Account balance: ₦{balance:,.2f}")

    if not card_retained:
        print("Please collect your card.")

    print("Thank you for banking with us.")


# Example simulation
atm_withdrawal(
    card_inserted=True,
    valid_card=True,
    balance=Decimal("100000"),
    valid_pin="1234",
    dispenser_success=True,
    reversal_success=True,
)

import time
from colorama import Style, Fore

class ATM:
    def __init__(self, pin, password):
        self.pin = pin
        self.password = password
        self.balance = 0.0

    def check_credentials(self, entered_pin, entered_password):
        return self.pin == entered_pin and self.password == entered_password

    def check_balance(self):
        print(Fore.YELLOW + f"\n\033[1mLoading...\n")
        time.sleep(1)
        print(Fore.GREEN + f"\n\033[1mBALANCE: {self.balance:.2f}")
        print(Fore.YELLOW + f"\n\033[1mLoading...\n")
        time.sleep(1)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(Fore.YELLOW + f"\n\033[1mLoading...\n")
            time.sleep(1)
            print(Fore.GREEN + f"\n\033[1m{amount:.2f} has been deposited.\n")
            print(Fore.YELLOW + f"\n\033[1mLoading...\n")
            time.sleep(1)
        else:
            print(Fore.YELLOW + f"\n\033[1mLoading...\n")
            time.sleep(1)
            print(Fore.RED + f"\n\033[1mEnter a positive value.\n")
            print(Fore.YELLOW + f"\n\033[1mLoading...\n")
            time.sleep(1)

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(Fore.YELLOW + f"\n\033[1mLoading...\n")
            time.sleep(1)
            print(Fore.GREEN + f"\n\033[1m{amount:.2f} has been withdrawn.\n")
            print(Fore.YELLOW + f"\n\033[1mLoading...\n")
            time.sleep(1)
        elif amount <= 0:
            print(Fore.YELLOW + f"\n\033[1mLoading...\n")
            time.sleep(1)
            print(Fore.RED + f"\n\033[1mEnter a positive value.\n")
            print(Fore.YELLOW + f"\n\033[1mLoading...\n")
            time.sleep(1)
        else:
            print(Fore.YELLOW + f"\n\033[1mLoading...\n")
            time.sleep(1)
            print(Fore.RED + f"\n\033[1mInsufficient balance.\n")
            print(Fore.YELLOW + f"\n\033[1mLoading...\n")
            time.sleep(1)

    def transfer(self, amount, recipient_account):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(Fore.YELLOW + f"\n\033[1mLoading...\n")
            time.sleep(1)
            print(Fore.GREEN + f"\n\033[1m{amount:.2f} has been transferred to account {recipient_account} successfully.\n")
            print(Fore.YELLOW + f"\n\033[1mLoading...\n")
            time.sleep(1)
        elif amount <= 0:
            print(Fore.YELLOW + f"\n\033[1mLoading...\n")
            time.sleep(1)
            print(Fore.RED + "\n\033[1mEnter a positive value.\n")
            print(Fore.YELLOW + f"\n\033[1mLoading...\n")
            time.sleep(1)
        else:
            print(Fore.YELLOW + f"\n\033[1mLoading...\n")
            time.sleep(1)
            print(Fore.RED + "\n\033[1mInsufficient balance.\n")
            print(Fore.YELLOW + f"\n\033[1mLoading...\n")
            time.sleep(1)

def main():
    atm = ATM(pin="1234", password="password")

    entered_pin = input(Fore.BLUE + Style.BRIGHT + "Enter your PIN: ")
    entered_password = input(Fore.BLUE + "\n\033[1mEnter your password: ")

    if not atm.check_credentials(entered_pin, entered_password):
        print(Fore.RED + "\n\033[1mInvalid PIN or password.\n")
        return main()

    while True:
        print(Fore.CYAN + "\033[1m\n....ATM Menu....")
        print(Fore.CYAN + "\033[1m1. Check Balance")
        print(Fore.CYAN + "\033[1m2. Deposit")
        print(Fore.CYAN + "\033[1m3. Withdraw")
        print(Fore.CYAN + "\033[1m4. Transfer")
        print(Fore.CYAN + "\033[1m5. Quit")

        choice = input(Fore.BLUE + "\n\033[1mChoose an option: ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input(Fore.BLUE + "\n\033[1mEnter amount to deposit: "))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input(Fore.BLUE + "\n\033[1mEnter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == '4':
            amount = float(input(Fore.BLUE + "\n\033[1mEnter amount to transfer: "))
            recipient_account = input(Fore.BLUE + "\n\033[1mEnter recipient account number: ")
            atm.transfer(amount, recipient_account)
        elif choice == '5':
            print(Fore.GREEN + "\n\033[1mThank you for using the ATM. :)")
            break
        else:
            print(Fore.RED + "\n\033[1mInvalid option. Please try again.")


main()

print(Style.RESET_ALL)

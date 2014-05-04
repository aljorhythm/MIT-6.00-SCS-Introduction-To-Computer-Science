from pprint import pprint
from bisect import bisect
from builtins import round
import math

# Problem 1
class CreditCardDebt:
    def __init__(self, annualInterestRate, initialBalance, minMonthlyPaymentRate):
        self.annualInterestRate = annualInterestRate
        self.initialBalance = initialBalance
        self.minimumMonthlyPaymentRate = minMonthlyPaymentRate
        return

    def minimumMonthlyPayment(self, balance):
        return self.minimumMonthlyPaymentRateminMonthlyPaymentRate * balance

    def interestPaid(self, balance):
        return self.annualInterestRate / 12 * balance

    def nMonths(self, n):
        balance = self.initialBalance
        months = []
        for nTH in range(n):
            month = {}
            month['month'] = nTH + 1
            month['interestPaid'] = self.interestPaid(balance)
            month['minMonthlyPayment'] = self.minimumMonthlyPayment(balance)
            month['principlePaid'] = month['minMonthlyPayment'] - month['interestPaid']
            balance = balance - month['principlePaid']
            month['balance'] = balance

            months.append(month)
        return months

def problem1():
    balance = float(input('Enter outstanding balance on credit card: '))
    annualInterestRate = float(input('Enter annual credit card interest rate: '))
    minMonthlyPaymentRate = float(input('Enter minimum monthly payment rate: '))

    creditCard = CreditCardDebt(annualInterestRate, balance, minMonthlyPaymentRate)

    while True:
        numberOfMonths = int(input("Enter number of months (0 to exit loop): "))
        if numberOfMonths == 0:
            break
        months = creditCard.nMonths(numberOfMonths)
        for month in months:
            pprint (month)

# Problem 2

class CreditCardPayer:
    def __init__(self, annualInterestRate, initialBalance):
        self.initialBalance = initialBalance
        self.monthlyInterestRate = annualInterestRate / 12

    def updatedBalance(self, balance, monthlyPayment):
        return balance * (1 + self.monthlyInterestRate) - monthlyPayment

    def minimumWithinAYear(self):
        monthly = 10
        while True:
            balance = self.initialBalance
            for month in range(12):
                balance = self.updatedBalance(balance, monthly)
                if balance <= 0:
                    return {"Months taken: " : month + 1, "Balance": balance, "Minimum monthly":monthly}
            monthly = monthly + 10

def problem2():
    balance = float(input("Enter outstanding balance on your credit card: "))
    annualInterestRate = float(input("Enter annual credit card interest rate: "))
    creditCardPayment = CreditCardPayer(annualInterestRate, balance)
    print (creditCardPayment.minimumWithinAYear())

# Problem 3
# Fast and accurate
class FastCreditCardPayer (CreditCardPayer):
    def __init__(self, annualInterestRate, initialBalance):
        CreditCardPayer.__init__(self, annualInterestRate, initialBalance)

    def minimumWithinAYearToCents(self):
        lowerBound = self.initialBalance / 12
        higherBound = (self.initialBalance * (1 + (self.monthlyInterestRate)) ** 12.0) / 12.0
        return self.bisekt(lowerBound, higherBound)

    def bisekt(self, lowerBound, higherBound):
        arr = []
        middleBound = ((higherBound - lowerBound) / 2) + lowerBound

        arr.append (self.afterAyear(higherBound))
        arr.append (self.afterAyear(middleBound))
        arr.append(self.afterAyear(lowerBound))
        index = bisect(arr, 0)

        # exit clause for recursive function
        if (math.ceil(middleBound * 100) / 100) == higherBound:
            return[higherBound, arr[0]]
        else:
            # find out whether balance=0 after 12 months is between lowerBound and middleBound or higherBound and middleBound
            if index == 1:
                lowerBound = middleBound
            elif index == 2:
                higherBound = middleBound
            return self.bisekt(round(lowerBound, 2), round(higherBound, 2))

    def afterAyear(self, monthlyPayment):
        balance = self.initialBalance
        for _ in range(12):
                balance = self.updatedBalance(balance, monthlyPayment)
        return balance

def problem3():
    balance = float(input("Enter outstanding balance on your credit card: "))
    annualInterestRate = float(input("Enter annual credit card interest rate: "))
    creditCardPayment = FastCreditCardPayer(annualInterestRate, balance)
    print (creditCardPayment.minimumWithinAYearToCents())

problem1()
problem2()
problem3()

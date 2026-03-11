from cardisk import Cardisk, ussd

app = Cardisk()

LOANS = []

@app.route("/")
def main_menu():
    ussd.menu("Welcome to Wolke Services", [
        ("Loans", "/loans"),
        ("Savings", "/savings"),
        ("Insurance", "/insurance")
    ])

@app.route("/loans")
def loans():
    ussd.menu("Loans Menu", [
        ("Apply for loan", "/loans/apply"),
        ("Check loan status", "/loans/status"),
        ("Repay loan", "/loans/repay")
    ])

@app.route("/loans/apply")
def loan_apply():
    ussd.screen(f"Enter loan amount for {ussd.msisdn}")
    ussd.next("/loans/confirm")

@app.route("/loans/confirm")
def loan_confirm():
    amount = ussd.input
    ussd.screen(f"Loan of ${amount} submitted successfully for {ussd.msisdn}")
    LOANS.append({ 'msisdn': ussd.msisdn, 'amount': amount, 'paid': False})
    ussd.end()

@app.route("/loans/status")
def ckeck_loans():
    ussd.screen("\n".join([f"{i}. {d['amount']} - {'paid' if d['paid'] else 'unpaid'}" for i, d in enumerate(LOANS, 1)]))
    ussd.end()
    

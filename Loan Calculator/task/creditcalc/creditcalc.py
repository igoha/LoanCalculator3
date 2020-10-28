import math
import argparse


def foo_montly_payment(principal, interest, payment):
    if args.principal < 0 or args.payment < 0 or args.interest < 0:  # test negative arguments
        foo_incorect_parameter()
    i = interest / (12 * 100)
    payment_monts = math.ceil(math.log((payment / (payment - i * principal)), 1 + i))
    years = payment_monts // 12
    monts = payment_monts % 12
    s1 = ("s" if years > 1 else "")
    s2 = ("s" if monts > 1 else "")
    print_monts = (f"and {monts} month{s2} " if monts > 1 else "")
    overpaid = (payment_monts * payment) - principal
    if years > 0:
        print(f"It will take {years} year{s1} {print_monts}to repay this loan!")
    else:
        print(f"It will take {monts} month{s2} to repay this loan!")
    print(f"Overpayment = {overpaid:.0f}!")
    return


def foo_anuity_paiment(principal, periods, interest):
    if args.principal < 0 or args.periods < 0 or args.interest < 0:  # test negative arguments
        foo_incorect_parameter()
    i = interest / (12 * 100)
    anuity = principal * ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))
    print(f"Your monthly payment = {math.ceil(anuity)}!")
    return


def foo_loan_principal(periods, interest, payment):
    if args.periods < 0 or args.payment < 0 or args.interest < 0:  # test negative arguments
        foo_incorect_parameter()
    i = interest / (12 * 100)
    load = (payment / ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))) // 1
    overpaid = (periods * payment) - load
    print(f"Your loan principal = {load:.0f}!")
    print(f"Overpayment = {overpaid:.0f}!")
    return


def foo_differentiated_payment(principal, periods, interest):
    if args.principal < 0 or args.periods < 0 or args.interest < 0:  # test negative arguments
        foo_incorect_parameter()
    payment_sum = 0
    i = interest / (12 * 100)
    for monts in range(1, periods + 1):
        mont_payment = (principal / periods) + i * (principal - ((principal * (monts - 1)) / periods))
        payment_sum += math.ceil(mont_payment)
        print(f"Month {monts}: payment is {math.ceil(mont_payment)}")
    over_payment = payment_sum - principal
    print(f"\nOverpayment = {over_payment}")
    return


def foo_incorect_parameter():
    print("Incorrect parameters")
    exit()


# program
my_parser = argparse.ArgumentParser(description="Loan calculator")
my_parser.add_argument("--type", help="type of calculation")
my_parser.add_argument("--principal", help="loan principal", type=int)
my_parser.add_argument("--periods", help="number of periods", type=int)
my_parser.add_argument("--interest", help="loan interest", type=float)
my_parser.add_argument("--payment", help="montly payment", type=int)
args = my_parser.parse_args()

# convert namespace to dictionary
args_dist = vars(args)
# varst = vars(args)["payment"]

# test number of arguments.   change dictionary to list a count None values
args_value_list = list(args_dist.values())
if args_value_list.count(None) != 1:
    foo_incorect_parameter()

# test type of calculation
if args.type == "diff":
    if args.payment is not None:
        foo_incorect_parameter()
    foo_differentiated_payment(args.principal, args.periods, args.interest)
elif args.type == "annuity":
    if args.principal is None:
        foo_loan_principal(args.periods, args.interest, args.payment)
    elif args.periods is None:
        foo_montly_payment(args.principal, args.interest, args.payment)
    elif args.payment is None:
        foo_anuity_paiment(args.principal, args.periods, args.interest)
else:
    print("Incorrect parameters.")

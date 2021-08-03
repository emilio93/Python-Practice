import argparse

def loan_payment_calculator(rate, present_value, number_of_periods):
  """Calculates the loan payment based on the rate, the present value and the
     mnumber of periods

  Args:
      rate (float): The loan rate.
      present_value (float): The loan present value.
      number_of_periods (int): The loan number of periods.

  Returns:
      float: The loan payment.
  """
  payment = rate * present_value / (1 - (1 + rate)**(-number_of_periods))
  return payment

def cli():
  parser = argparse.ArgumentParser(description='Loan Payment Calculator')
  parser.add_argument('-p',
                      '--present-value',
                      type=float,
                      help='Present value',
                      required=True
                      )
  parser.add_argument('-r',
                      '--rate',
                      type=float,
                      help='The rate of the loan',
                      required=True
                      )
  parser.add_argument('-n',
                      '--number_of_periods',
                      type=int,
                      help='The number of periods of the loan',
                      required=True
                      )
  parser.add_argument('-v',
                      '--verbose',
                      action="store_true",
                      help="Print the formula",
                      required=False
                      )
  args = parser.parse_args()
  return args

def calculate_loan_payment(args):
  return loan_payment_calculator(
    rate=args.rate,
    present_value=args.present_value,
    number_of_periods=args.number_of_periods,
  )

def __main__():
  args = cli()
  loan_payment = calculate_loan_payment(args)
  print(f"Loan payment is {loan_payment}")
  if (args.verbose):
    print('')
    print(f"Payment = rate * present_value / (1 - (1 + rate)**(-number_of_periods))")
    print(f"Payment = {args.rate} * {args.present_value} / (1 - (1 + {args.rate})**(-{args.number_of_periods}))")
    print(f"Payment = {args.rate * args.present_value} / (1 - ({1 + args.rate})**(-{args.number_of_periods}))")
    print(f"Payment = {args.rate * args.present_value} / (1 - {(1 + args.rate)**(-args.number_of_periods)})")
    print(f"Payment = {args.rate * args.present_value} / {(1 - (1 + args.rate)**(-args.number_of_periods))}")
    print(f"Payment = {loan_payment}")

__main__()

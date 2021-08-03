import argparse

def interest_loan_calculator(principal, rate, time_periods):
  """interest = principal * rate * time_periods

  Args:
      principal (float): The principal of the loan.
      rate (float): The rate of the loan.
      time_periods (float): The time periods of the loan.

  Returns:
      float: The interest of the loan.
  """
  return principal * rate * time_periods

def principal_loan_calculator(interest, rate, time_periods):
  """principal = interest / ( rate * time_periods )

  Args:
      interest (float): The interest rate of the loan.
      rate (float): The rate of the loan.
      time_periods (float): The time periods of the loan.

  Returns:
      float: The principal of the loan.
  """
  return interest / (rate * time_periods)

def rate_loan_calculator(interest, principal, time_periods):
  """rate = interest / ( principal * time_periods )

  Args:
      interest (float): [description]
      principal (float): [description]
      time_periods (float): [description]

  Returns:
      float: The rate of the loan.
  """
  return interest / (principal * time_periods)

def time_periods_loan_calculator(interest, principal, rate):
  """time_periods = interest / ( principal * rate )

  Args:
      interest (float): [description]
      principal (float): [description]
      rate (float): [description]

  Returns:
      float: The time periods of the loan.
  """
  return interest / (principal * rate)

def test():
  """Tests the functions in this module."""
  arg_interest = 3200
  arg_principal = 20000
  arg_rate = 0.08
  arg_time_periods = 2

  interest = interest_loan_calculator(
    arg_principal,
    arg_rate,
    arg_time_periods
  )
  principal = principal_loan_calculator(
    arg_interest,
    arg_rate,
    arg_time_periods
  )
  rate = rate_loan_calculator(arg_interest, arg_principal, 2)
  time_periods = time_periods_loan_calculator(
    arg_interest,
    arg_principal,
    arg_rate
  )

  hasError = False
  if interest != arg_interest:
    hasError = True
    print("Error: interest_loan_calculator()")
  if principal != arg_principal:
    hasError = True
    print("Error: principal_loan_calculator()")
  if rate != arg_rate:
    hasError = True
    print("Error: rate_loan_calculator()")
  if time_periods != arg_time_periods:
    hasError = True
    print("Error: time_periods_loan_calculator()")
  if not hasError:
    print("All functions work.")

def cli():
  parser = argparse.ArgumentParser(description='Loan Payment Calculator')
  parser.add_argument('-p',
                      '--principal',
                      type=float,
                      help='Principal of the loan',
                      required=True
                      )
  parser.add_argument('-r',
                      '--rate',
                      type=float,
                      help='Rate of the loan',
                      required=True
                      )
  parser.add_argument('-t',
                      '--time-periods',
                      type=int,
                      help='Time periods of the loan',
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

def calculate_loan_interest(args):
  return interest_loan_calculator(
    principal=args.principal,
    rate=args.rate,
    time_periods=args.time_periods
  )

def __main__():
  args = cli()
  interest = calculate_loan_interest(args)
  print(f"The interest is {interest}")
  if (args.verbose):
    print('')
    print(f"Interest = Principal * Rate * Time Periods")
    print(f"Interest = {args.principal} * {args.rate} * {args.time_periods}")
    print(f"Iterest = {interest}")

__main__()

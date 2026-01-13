NOT_ELIGIBLE = 0
FULL_BENEFITS = 1
DISCOUNTED_BENEFITS = 2

def age_validity():
  while True:
    try:
      age = int(input("Enter Age: "))
      if age <= 0:
        raise ValueError
      return age
    except ValueError:
      print("Invalid input. Enter a valid age\n")

def year_validity():
  while True:
    try:
      year = int(input("Enter Years of Service: "))
      if year <= 0:
        raise ValueError
      return year
    except ValueError:
      print("Invalid input. Enter a valid year.\n")

def eligibility(age, year):
  if age < 50:
    return NOT_ELIGIBLE
  elif age >= 65 or age + year >= 80:
    return FULL_BENEFITS
  else:
    return DISCOUNTED_BENEFITS

def display_result(result):
  if result == NOT_ELIGIBLE:
    print("You are not eligible for retirement\n")
  elif result == FULL_BENEFITS:
    print("You are eligible for retirement with full pension benefits\n")
  else:
    print("You are eligible for retirement with discounted pension benefits\n")

def main():
  print("\nRetirement Eligibility Checker:")
  age = age_validity()
  year = year_validity()
  result = eligibility(age, year)
  display_result(result)

if __name__ == "__main__":
  main()




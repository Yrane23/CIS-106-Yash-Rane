# Initialize variables for total gross pay and employee count
total_gross_pay = 0
employee_count = 0

# start the program
user_input = input("Do you want to do this program (Yes/No)? ").strip().lower()

# Continue with the program if the user answers "Yes"
while user_input == "yes":
    # Collect employee data
    last_name = input("Enter employee's last name: ")
    hours_worked = float(input("Enter hours worked: "))
    rate_of_pay = float(input("Enter rate of pay ($/hr): "))

    # Calculate gross pay, including overtime
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        gross_pay = (40 * rate_of_pay) + (overtime_hours * rate_of_pay * 1.5)
    else:
        gross_pay = hours_worked * rate_of_pay

    # Update totals
    total_gross_pay += gross_pay
    employee_count += 1

    # Display individual employee's gross pay
    print(f"{last_name}: Gross Pay = ${gross_pay:.2f}")

    # Ask the user if they want to process another employee
    user_input = input("Do you want to enter another employee's data (Yes/No)? ").strip().lower()

# exit the loop, calculate and display the total and average pay if employe count is greater than 0
if employee_count > 0:
    average_pay = total_gross_pay / employee_count
    print(f"\nTotal Gross Pay for all employees: ${total_gross_pay:.2f}")
    print(f"Number of employees processed: {employee_count}")
    print(f"Average pay per employee: ${average_pay:.2f}")
else:
    print("No employees were processed.")





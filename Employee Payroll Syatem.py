class Employee:
    def __init__(self,emp_id,name,basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        hrs = 0.20 * self.basic_salary
        da = 0.10 * self.basic_salary
        gross_salary = self.basic_salary + hrs + da 
        return gross_salary

    def display(self):
        print("\nEmployee Details")
        print("\nEmployee ID:",self.emp_id)
        print("\nName:",self.name)
        print("\nBasic Salary:",self.basic_salary)
        print("\nGross Salary",self.calculate_salary)
        print("-" * 30)


class EmployeePayrollSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        emp_id = int(input("Enter Employee ID:"))
        name = input("Enter EMployee Name:")
        basic_salary = float(input("Enter Basic Salary:"))

        employee = Employee(emp_id,name,basic_salary)
        self.Employees.append(employee)

        print("Employee added successfully!")

    def search_employee(self):
        emp_id = int(input("Enter Employee ID to search:"))

        for employee in self.employees:
            if employee.emp_id == emp_id:
                employee.display()
                return

        print("Employee not found.")

    def update_salary(self):
        emp_id = int(input("Enter EMployee ID:"))

        for employee in self.employees:
            if employee.emp_id == emp_id:
                new_salary = float(input("Enter New Basic Salary:"))
                employee.basic_salary = new_salary
                print("Salary updated successfully!")
                return

        print("Employee not found.")

    def delete_employee(self):
        emp_id = int(input("Enter Employee ID to delete:"))

        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                print("Employee deleted successfully!")
                return

        print("Employee not found.")


#Mini Program
eps = EmployeePayrollSystem()

while True:
    print("\n===== EMPLOYEE PAYROLL SYSTEM =====")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        eps.add_employee()

    elif choice == "2":
        eps.display_employee()
        
    elif choice == "3":
        eps.search_employee()

    elif choice == "4":
        eps.udate_salary()

    elif choice == "5":
        eps.delete_employee()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")
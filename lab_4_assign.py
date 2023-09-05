class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def search_by_age(self, target_age):
        results = [emp for emp in self.employees if emp.age == target_age]
        return results

    def search_by_name(self, target_name):
        results = [emp for emp in self.employees if emp.name == target_name]
        return results

    def search_by_salary(self, operator, target_salary):
        if operator == ">":
            results = [emp for emp in self.employees if emp.salary > target_salary]
        elif operator == "<":
            results = [emp for emp in self.employees if emp.salary < target_salary]
        elif operator == ">=":
            results = [emp for emp in self.employees if emp.salary >= target_salary]
        elif operator == "<=":
            results = [emp for emp in self.employees if emp.salary <= target_salary]
        else:
            results = []
        return results

def main():
    emp_db = EmployeeDatabase()

    emp_db.add_employee(Employee("161E90", "Raman", 41, 56000))
    emp_db.add_employee(Employee("161F91", "Himadri", 38, 67500))
    emp_db.add_employee(Employee("161F99", "Jaya", 51, 82100))
    emp_db.add_employee(Employee("171E20", "Tejas", 30, 55000))
    emp_db.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Choose a search parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (> < <= >=)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        target_age = int(input("Enter the target age: "))
        results = emp_db.search_by_age(target_age)
    elif choice == "2":
        target_name = input("Enter the target name: ")
        results = emp_db.search_by_name(target_name)
    elif choice == "3":
        operator = input("Enter the operator (> < <= >=): ")
        target_salary = int(input("Enter the target salary: "))
        results = emp_db.search_by_salary(operator, target_salary)
    else:
        print("Invalid choice")
        return

    if results:
        print("Search Results:")
        for emp in results:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
    else:
        print("No results found")

if __name__ == "__main__":
    main()

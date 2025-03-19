employees = [
    (101, "E001", 50000),
    (102, "E002", 60000),
    (101, "E003", 45000),
    (103, "E004", 75000),
    (102, "E005", 55000),
    (103, "E006", 72000),
    (101, "E007", 52000),
    (102, "E008", 59000)
]

dept_salaries = {}

for dept_no, emp_id, salary in employees:
    if dept_no not in dept_salaries:
        dept_salaries[dept_no] = []
    dept_salaries[dept_no].append(salary)

for dept_no, salaries in dept_salaries.items():
    min_salary = min(salaries)
    max_salary = max(salaries)
    
    print(f"Department {dept_no}: Min Salary = {min_salary}, Max Salary = {max_salary}")
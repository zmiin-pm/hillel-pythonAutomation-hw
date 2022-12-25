from company import Company
from employee import Employee

new_company = Company('Some Comp', 3)
employee_john = Employee('John', 40)
employee_john.add_info('Education - High')
employee_john.add_info('Certificate - 04482')
new_company.add_employee(employee_john)
new_company.view_company_info()

new_employees = Employee.bulk_create(
    [
        ('Anna', 20),
        ('Mark', 32),
        ('Edik', 22),
        ('Bill', 19)
    ]
)
second_company = Company.create_company_from_employees('One more Comp', new_employees)
second_company.view_company_info()

all_employees = Company.get_all_employees([new_company, second_company])
Employee.save_info_to_file(all_employees)

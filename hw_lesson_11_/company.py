
class Company:

    main_company_address = '7675 Albany St. Brooklyn, NY 11201'

    def __init__(self, company_name: str, vacations_number: int):
        self.company_name = company_name
        self.vacations_number = vacations_number
        self.employees_list = []

    def add_employee(self, employee: object):
        """
        Add employee to the company
        :param employee: instance of Employee
        :return: instance of Company with added employee
        """
        if self.vacations_number > 0:
            self.employees_list.append(employee)
            self.vacations_number -= 1
            return self
        raise Exception(f'No free vacations')

    def view_company_info(self):
        """
        Print company info
        :return: null
        """
        print('_______________________________________________')
        print(f'Company name: {self.company_name}')
        print(f'Main company address: {self.main_company_address}')
        print(f'Employees: {len(self.employees_list)}')
        print(f'Free vacations: {self.vacations_number}')
        print('_______________________________________________')

    @classmethod
    def create_company_from_employees(cls, company_name: str, lst: list):
        """
        Create a company from list of employees
        :param company_name: Name of the company
        :param lst: list of employees
        :return: instance of Company
        """
        new_company = cls(company_name, len(lst))
        for employee in lst:
            new_company.add_employee(employee)
        return new_company

    @staticmethod
    def get_all_employees(companies: list) -> list:
        """
        To get all employees from companies list
        :param companies:
        :return: list of instances of Employee
        """
        result = []
        for company in companies:
            result.extend(company.employees_list)
        return result


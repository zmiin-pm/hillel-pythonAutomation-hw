import os
from typing import List, Tuple


class Employee:

    employee_id: int = 1

    def __init__(self, name: str, age: int):
        self.employee_id = Employee.employee_id
        Employee.employee_id += 1
        self.name = name
        self.age = age
        self.additional_info = ''

    @classmethod
    def bulk_create(cls, lst: List[Tuple]) -> list:
        """
        Additional constructor to create multiple employees
        :param lst: list of tuples. Tuple(name, age)
        :return: list of instances of Employee
        """
        return [cls(item[0], item[1]) for item in lst]

    def add_info(self, info: str) -> None:
        """
        Additional info for Employee
        :param info: string of additional info
        :return: None
        """
        self.additional_info += info + '\n'

    def get_info(self):
        """
        Convert attributes of instance to list of strings
        Uses during save to file
        :return: list of strings with attributes and values
        """
        return [f'{item[0]}: {item[1]}\n' for item in self.__dict__.items()]

    @staticmethod
    def save_info_to_file(employees: list):
        """
        Create folder 'employee' (if not exists) and save employees info
        to separate files
        :param employees: list of instances
        :return: None
        """
        folder = 'employees'
        os.makedirs(folder, exist_ok=True)
        for employee in employees:
            file_name = f'{employee.employee_id}_{employee.name}.txt'
            with open('./'+folder+'/'+file_name, 'w') as f:
                f.writelines(
                    employee.get_info()
                )
            print(f'File {file_name} was created')

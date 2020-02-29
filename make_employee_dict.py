class Employee:

  def __init__(self, name, ID_number, salary, email_address):
      self.name = name
      self.ID_number = ID_number
      self.salary = salary
      self.email_address = email_address

  def make_employee_dict(self):
        return {self.name, self.ID_number, self.salary, self.email_address}

emp1 = Employee('Sam Jackson', 456, 50000, 'sj@abcompany')

print(Employee.make_employee_dict())
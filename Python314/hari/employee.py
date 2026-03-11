class Employee:
    def __init__(self,name,employee_id,salary):
        self.name=name
        self.employee_id=employee_id
        self.salary=salary
    def calculate_yearly_bonus(self):
        if self.salary>50000:
            bonus=self.salary*0.1
        else:
            bonus=self.salary*0.5
        return bonus
    def apply_salary_hike(self,percentage):
        self.salary+=self.salary*(percentage/100)
employee1=Employee("Kathir","MC001",50000)
bonus=employee1.calculate_yearly_bonus()
print(f"Yearly bonus for {employee1.name}:{bonus}")
employee1.apply_salary_hike(5)
print(f"Updated salary for {employee1.name}:{employee1.salary}")

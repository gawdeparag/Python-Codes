class Employee:
    #class variable
    dept = 'Sales'
    base_s = 2000

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def base_salary(cls):
        Employee.base_s *= 2
        return Employee.base_s
        
        
    def incr_salary(self, salary):
        salary = self.salary * 10 + Employee.base_salary()
        return salary
        
a = Employee('Intro', 5000)
b = Employee('Extro', 7000)
print(a.name)
print(a.dept)
print(a.incr_salary(a.salary))
#varchya process madhe 'base_s' chya value madhe changes kele hote.
#Te aata khaali 'b' chya calling madhe maintained rahatil
#Mhanje 'a' chya calling mule 'base_s = 4000' jhala
print('---------------')
print(b.name)
print(b.dept)
print(b.incr_salary(b.salary))
#Ani ithe 'base_s = 8000' hoil mhanjech '(base_s = 4000) * 2'
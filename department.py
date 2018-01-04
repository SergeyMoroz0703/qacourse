
class Department():
    def __init__(self, managers_list=None):
        self.managers = managers_list

    def get_manager_list(self):
        managers_name = []
        for i in Manager.all_managers:
            managers_name.append(i.first_name)

        return ('There are {num} managers. {list}'.format(num = Manager.numOfInstances, list = managers_name))

    def salary_msg(self):
        all_employee = Employee.all_employee
        print('\n' + 'There are all salaries:')
        for i in all_employee:
            print (i.first_name, i.second_name, i.salary)

    def manager_team_msg(self):
        print('\n' + 'There are lists of team of every manager')
        for i in Manager.all_managers:
            print(i.first_name, i.second_name, i.team)








class Employee():
    all_employee = []
    def __init__(self, first_name, second_name, salary, exp, manager):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary
        self.exp = exp
        self.manager = manager
        self.all_employee.append(self)
        if self.manager is not None:
            self.manager.add_team(self.first_name)



    def get_salary(self):
        salary = self.salary
        if self.exp >= 2 and self.exp <= 5:
            salary = salary + 200
        elif self.exp > 5:
            salary = (salary*1.2) + 500
        return salary



class Developer(Employee):
    def get_salary(self):
        salary = super().get_salary()
        return salary


class Designer(Employee):
    def __init__(self, first_name, second_name, salary, exp, manager, effictivness=0.0):
        super().__init__(first_name, second_name, salary, exp, manager)
        if effictivness >=0 and effictivness <= 1:
            self.effictivness = effictivness
            self.get_salary()
        else:
            self.err_msg()



    def get_salary(self):
        self.salary = super().get_salary() *  self.effictivness
        return self.salary

    def err_msg(self):
        return 'Effictivness should be in range 0-1'



class Manager(Employee):

    all_managers = []        #list of all Managers object
    numOfInstances = 0

    def countInstances(cls):
        cls.numOfInstances += 1
    countInstances = classmethod(countInstances)


    def __init__(self, first_name, second_name, salary, exp, team):
        super().__init__(first_name, second_name, salary, exp, manager=None)
        self.team = team
        self.countInstances()
        self.manager = [self.first_name, self.second_name, self.salary, self.exp]
        self.all_managers.append(self)

    def add_team(self, member):
        self.team.append(member)

    def get_salary(self):
        devs = self.check_team()[0]
        des = self.check_team()[1]

        if len(self.team) > 5 and len(self.team) <= 10:
            if devs > des:
                self.salary=(super().salary + 200) * 1.1
            else:
                self.salary = super().salary + 200
        elif len(self.team) > 10:
            if devs > des:
                self.salary=(super().salary + 300) * 1.1
            else:
                self.salary = super().salary + 300 * 1.1


    def check_team(self):
        count_dev = 0
        count_des = 0
        for i in self.team:
            if isinstance(i, Designer):
                count_des = count_des + 1
            elif isinstance(i, Developer):
                count_dev = count_dev + 1
        return [count_dev, count_des]




Department = Department()
Manager1 = Manager('ManagerName1', 'ManagerSurname1', 100, 2, [])
Manager2 = Manager('ManagerName2', 'ManagerSurname2', 100, 2, [])
Manager3 = Manager('ManagerName3', 'ManagerSurname3', 100, 2, [])
Manager4 = Manager('ManagerName4', 'ManagerSurname4', 100, 2, [])


Designer1 = Designer('DesName1', 'DesSurname1', 300, 2, Manager1, 0.5)
Designer2 = Designer('DesName2', 'DesSurname2', 300, 2, Manager1, 1)


print(Department.get_manager_list())
Department.salary_msg()
Department.manager_team_msg()
print(Manager.all_managers)



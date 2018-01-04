
class Department():
    def __init__(self, managers_list=None):
        self.managers = managers_list

    def get_manager_list(self):

        return ('There are {num} managers. {list}'.format(num = Manager.numOfInstances, list = Manager.managers_list))








class Employee():
    def __init__(self, first_name, second_name, salary, exp, manager):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary
        self.exp = exp
        self.manager = manager

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
        else:
            self.err_msg()



    def get_salary(self):
        salary = super().get_salary() *  self.effictivness
        return salary

    def err_msg(self):
        return 'Effictivness should be in range 0-1'



class Manager(Employee):
    numOfInstances = 0
    managers_list = []
    def countInstances(cls):
        cls.numOfInstances += 1
    countInstances = classmethod(countInstances)


    def __init__(self, first_name, second_name, salary, exp, team):
        super().__init__(first_name, second_name, salary, exp, manager=None)
        self.team = team
        self.countInstances()
        self.manager = [self.first_name, self.second_name, self.salary, self.exp]
        self.managers_list.append(self.manager)


    def get_team(self):
        return self.team

    def add_team(self, member):
        self.team.append(member)

    def get_salary(self):
        devs = self.check_team()[0]
        des = self.check_team()[1]

        if len(self.team) > 5 and len(self.team) <= 10:
            if devs > des:
                salary=(super().salary + 200) * 1.1
            else:
                salary = super().salary + 200
        elif len(self.team) > 10:
            if devs > des:
                salary=(super().salary + 300) * 1.1
            else:
                salary = super().salary + 300 * 1.1


    def check_team(self):
        count_dev = 0
        count_des = 0
        for i in self.get_team():
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


Designer1 = Designer('DesName1', 'DesSurname1', 100, 2, Manager1, 0.5)
Designer2 = Designer('DesName2', 'DesSurname2', 100, 2, Manager1, 1)

print(Manager1.get_team())

print(Department.get_manager_list())



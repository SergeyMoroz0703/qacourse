
class Department():
    def __init__(self, managers_list):
        self.managers = managers_list

    def give_salary(self):
        pass




class Employee():
    def __init__(self, first_name, second_name, salary, exp, manager):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary
        self.exp = exp
        self.manager = manager
        # if self.manager is not None:
        #     Manager.add_team(self)

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
    def __init__(self, first_name, second_name, salary, exp, team):
        super().__init__(first_name, second_name, salary, exp, manager=None)
        self.team = team

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





Manager1 = Manager('ManagerName1', 'ManagerSurname1', 100, 2, [])


Designer1 = Designer('DesName1', 'DesSurname1', 100, 2, Manager1, 0.5)
Designer2 = Designer('DesName2', 'DesSurname2', 100, 2, Manager1, 1)

Manager1.add_team(Designer1)
Manager1.add_team(Designer2)


print(Manager1.salary)










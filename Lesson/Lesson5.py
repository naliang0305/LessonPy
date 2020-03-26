class Member:
    def __init__(self, new_gender, new_major, new_id):
        self.__gender = new_gender  #__gender是private屬性
        self.major = new_major
        self.id = new_id    #建構子
    def get_gender(self):
        """回傳private屬性"""
        return self.__gender

    def set_gender(self, new_gender):
        if new_gender == 'M' or new_gender == 'F':
            self.__gender = new_gender
        else:
            print('====請傳入"M"或"F"')

    def borrow_resource(self):
        pass
    def check_auth(self):
        pass

class Student(Member):

    def __init__(self, new_gender, new_major, new_id):
        super().__init__(new_gender, new_major, new_id)

    def join_class(self):
        pass
    def quit_class(self):
        pass
    def borrow_resource(self):
        print('student borrow')

class Professor(Member):
    def __init__(self, new_gender, new_major, new_id):
        super().__init__(new_gender, new_major, new_id)

    def join_class(self):
        pass
    def quit_class(self):
        pass
    def borrow_resource(self):
        print('professor borrow')


student1 = Student('M', '工管系', 'D16665165')
student2 = Student('F', '數媒系', 'D16665165')
professor1 = Professor('F', '財金系', 'T1668484')
professor2 = Professor('M', '會計系', 'T4841351')

ls = [student1, student2, professor1, professor2]

for item in ls:
    item.borrow_resource()






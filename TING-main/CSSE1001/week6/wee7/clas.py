class Student(object) :

    def __init__(self,name,student_num,degree):
        self._name = name
        self._student_num = student_num
        self._degree = degree
    def get_name(self):
        return self._name
    
    def get_student_num(self):
        return self._student_num
    
    def get_degree(self):
        return self._degree
    def set_degree(self,new_degree):
        self._degree = new_degree
        return self._degree
    def get_first_name(self):
        first, _, last = self._name.partition(' ')
        return first
    def get_last_name(self):    
        first, _, last = self._name.partition(' ')
        return last


s = Student('John Smith',12345678,'BInfTech')


    
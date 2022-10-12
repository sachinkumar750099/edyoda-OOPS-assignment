class student:

    def __init__(self):
        self.__name = ""

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_rollno(self,rollno):
        self.__rollno = rollno
    
    def get_rollno(self):
        return self.__rollno


obj = student()
obj.set_name("vikrant goswami")
print(obj.get_name())
obj.set_rollno(12)
print(obj.get_rollno())
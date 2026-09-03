class NegativeError(Exception):
    pass
class Person():
    def __init__(self,name,roll_no,marks) -> None:
        self.name = name
        self.roll_no = roll_no
        self.__marks = marks
    def get_marks(self):
        return self.__marks
    def set_marks(self,newMarks):
        try:
            if newMarks<0:
                raise NegativeError("Marks cannot be negative!")
            self.__marks= newMarks
        except NegativeError as e:
            print(f"Error: {e}")
    def ger_average(self):
        return sum(self.__marks)/len(self.__marks)
    @staticmethod
    def grade(avg):
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "D"
s= Person("Ashish",21,[61,72,33,54])
print(f"Student Name is {s.name}")
s.roll_no
avg = s.ger_average()
print(s.grade(avg))
f= open("Student.csv","r+")
f.write("Ashish is a very good Student")
f.seek(0)
print(f.read())
f.close()

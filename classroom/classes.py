# 1a : 
class Person(object):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def fullname(self):
        return self.fname + self.lname
    def __str__(self):
        return "Full name is" %(self.fname, self.lname)

# 1b :
class Student(Person):
    def __init__(self, fname, lname, subject):
        Person.__init__(self, fname, lname)
        self.subject = subject
    def NameSubject(self):
        return self.NameSubject
    def printNameSubject(self):
        print("%s %s studies %s" %(self.fname, self.lname, self.subject))

# 1d :
class Teacher(Person):
    def __init__(self, fname, lname, course):
        super(Teacher, self).__init__(fname, lname)
        self.course = course
    def Course(self):
        return self.course
    def printTeachCourse(self):
        print("%s %s teaches %s" %(self.fname, self.lname, self.course))
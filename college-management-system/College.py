from Department import Department
import pickle

class College:
    def __init__(self,collegeName:str,departments:list):
        self.name=collegeName
        self.departments=departments
    def get_name(self):
        return self.name
    def print_departments(self):
        for department in self.departments:
            print(department)
        return
    def add_department(self):
        deptName=input('Enter Department Name')
        hod=input('Enter HOD Name')
        courses=input('Enter Course List').split()
        newDepartment=Department(deptName,hod,courses)
        self.departments.append(newDepartment)

myFile=open('myfile.pkl','rb')
gkcm=None

if myFile==None:
    dept1=Department('CSE','Surajit Pal',['C programming','Math','Physics'])
    dept2=Department('ME','Abhijit Mal',['Engineering Drawing','Math','Physics'])

    gkcm=College('Greater Kolkata College Of Engineering And Management',[dept1,dept2])
else:
    gkcm=pickle.load(myFile)

gkcm.print_departments()

gkcm.add_department()

gkcm.print_departments()

myFile=open('myfile.pkl','wb')

pickle.dump(gkcm,myFile)

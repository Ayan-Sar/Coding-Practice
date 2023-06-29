class Employee:
    __firstname=""
    __gender=""
    __company=""
    __pay=0 
    def setData(self,firstname,lastname,company,pay):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__company = company
        self.__pay = pay
    def showData(self):
        print("First Name\t:", self.__firstname)
        print("Last name\t:", self.__lastname)
        print("Company\t:", self.__company)
        print("Pay\t:", self.__pay)
        print("Email id is\t:", self.__firstname + "." + self.__lastname + "@" + self.__company + ".com")
def main():
    emp=Employee()
    emp.setData('Mohandas','Gandhi','Microsoft',500000)
    emp.showData()
if __name__=="__main__":
    main()
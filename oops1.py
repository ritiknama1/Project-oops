#initiate a class
class employee:
    def __init__(self):
        self.id = 1000
        self.salary = 50000
        self.wife = "unmarried"
    
        print("bhai ki wife unmarried hai kyoki salary 50k hai")
    
    def travel(self, new_salary):
        print(f"bhai ki wife ab married hai as he has {new_salary}")


Ritik = employee()
Ritik.travel(100000)
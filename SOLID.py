#SOLID: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion
#Single Responsibility Principle: A class should have only one reason to change.
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_user_info(self):
        return f"Name: {self.name}, Email: {self.email}"
    
#Open/Closed Principle: Software entities should be open for extension but closed for modification.
class Shape:
    def area(self):
        pass        

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2  
    
#Liskov Substitution Principle: Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.
class Bird:
    def fly(self):
        return "I can fly!"     
    
class Sparrow(Bird):
    pass        
class Ostrich(Bird):
    def fly(self):
        raise Exception("I can't fly!")
    
    

#Interface Segregation Principle: Clients should not be forced to depend on interfaces they do not use.
class Printer:
    def print_document(self, document):
        pass
class Scanner:
    def scan_document(self, document):
        pass
class MultiFunctionDevice(Printer, Scanner):
    def print_document(self, document):
        return f"Printing: {document}"

    def scan_document(self, document):
        return f"Scanning: {document}"
    
#Dependency Inversion Principle: High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.
class Database:
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        return "Connecting to MySQL Database"

class PostgreSQLDatabase(Database):
    def connect(self):
        return "Connecting to PostgreSQL Database"

class Application:
    def __init__(self, database: Database):
        self.database = database

    def run(self):
        return self.database.connect()
    
# Example usage
if __name__ == "__main__":
    user = User("Alice", "adsdasd")
    print(user.get_user_info()) 
    circle = Circle(5)
    print(f"Area of Circle: {circle.area()}")
    sparrow = Sparrow()
    print(sparrow.fly())
    ostrich = Ostrich()
    try:
        print(ostrich.fly())
    except Exception as e:
        print(e)
    mfd = MultiFunctionDevice()
    print(mfd.print_document("My Document"))
    print(mfd.scan_document("My Document"))
    postgres_db = PostgreSQLDatabase()
    app = Application(postgres_db)
    print(app.run())    

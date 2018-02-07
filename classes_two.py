#classes can inherit from one another! Example:

class Customer(object):
    def __init__(self, customer_name):
        self.customer_name= customer_name
    def display_cart(self):
        print "Here is your cart..."

class ReturningCustomer(Customer):
    def display_previous_purchases(self):
        print "Here are the things you previously bought..."

brian = ReturningCustomer("Brian Akers")
brian.display_cart()

#note that in the above, our second class did not define the initialize or display_cart function! Yet we were still able to call on them


#another example:
class Shape(object):
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3


#you can also override an inherited variable/function:
class Employee(object):
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return self.hours * 12.00
    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)

brian = PartTimeEmployee("Brian")
print brian.calculate_wage(2000)

#however, even if we overwrite a method, we can still access the parent's original method through 'super'
#the syntax for this is:
    # class Derived(Base):
    #     def m(self):
    #         return super(Derived, self).m()

#this is noted on line 44, whereby, instead of calculating $12/hour, we use the full time wage of $20/hour
lumberg = PartTimeEmployee("Bill Lumberg")
print lumberg.full_time_wage(2000)


class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    number_of_sides = 3
    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3) == 180:
            return True
        else:
            return False

my_triangle = Triangle(45, 45, 90)
print my_triangle.number_of_sides
print my_triangle.check_angles()

class Equilateral(Triangle):
    angle = 60
    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle

eq_triangle = Equilateral()
print eq_triangle.number_of_sides
print eq_triangle.check_angles()

#note that in the above, we overwrote the initialize, but we definied angle 1, 2, and 3
#this allowed us to then use the method check_angles, since its three parameters are angle 1, 2, 3

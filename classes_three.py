class Computer(object):
    condition = "new"
    def __init__(self, model, color, ram, storage):
        self.model = model
        self.color = color
        self.ram = ram
        self.storage = storage
    def display_computer(self):
        return "This is a %s %s with %s gb of RAM and %s gb SSD." %(self.color, self.model, str(self.ram), str(self.storage))
    def use_computer(self):
        self.condition = "used"

my_computer = Computer("Macbook Pro", "space grey", 16, 512)
print my_computer.display_computer()
print my_computer.condition

my_computer.use_computer()
print my_computer.condition
#note that in the above we modified condition variable from new to used, via the use_computer method
#if we were to create a new computer variable, it would have the "new" condition

class CellPhone(Computer):
    def __init__(self, model, color, ram, storage, carrier):
        self.model = model
        self.color = color
        self.ram = ram
        self.storage = storage
        self.carrier = carrier
    def use_computer(self):
        self.condition = "almost new"
    def __repr__(self):
        return "(%s, %s, %i, %i, %s)" %(self.model, self.color, self.ram, self.storage, self.carrier)

my_cell = CellPhone("iPhone", "black", 8, 64, "Verizon")
print my_cell.carrier
print my_cell.condition
my_cell.use_computer()
print my_cell.condition
#in the above, we overrode the "use computer" method, to change the condition from new to "almost new"

#OVERRIDING __repr__():
#there is a built in function, __repr__ which stands for representation
#representation is how python will represent an object
#normally, this is returned in a format similar to <__ object at 0x012202>
#however, we can tell python to show us the object however we want
#note the difference between printing my_computer and my_cell below
print my_computer
print my_cell
#since we overwrote the repr method for the CellPhone class, we see the object differently than for the computer class

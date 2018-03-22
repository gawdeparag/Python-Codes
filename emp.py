class Emp:
    def __init__(self, e_id, name):
        self.e_id = e_id
        self.name = name

    def display(self):
        print("{0:5d}, {1:20s}".format(self.e_id, self.name))

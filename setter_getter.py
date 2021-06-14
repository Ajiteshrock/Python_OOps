class settter_getter:
    def __init__(self,first_name,last_name):
         self.first_name  = first_name
         self.last_name   = last_name

    @property
    def email(self):
        return "{}{}".format(self.first_name.lower(),self.last_name.lower())+"24@gmail.com"

    @property
    def name(self):
        return str(self.first_name)+str(self.last_name)

    @name.setter
    def name(self,string):
        first , last = string.split(' ')
        self.first_name = "Yadav"
        self.last_name  = "ji"

    @name.deleter
    def name(self):
        self.first_name = None
        self.last_name  = None
        print("Data Deleted")


aj = settter_getter('Ajitesh','Mishra')
aj.name = "Akash Yadav"
print(aj.email) ; del aj.name ; print(aj.name)

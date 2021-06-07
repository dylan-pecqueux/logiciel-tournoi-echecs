class Player:

    def __init__(self, last_name, first_name, date_of_birth, sex, classment):
        """Has last name, first name, date of birth (dd/mm/aaaa), sex (m or f) 
           and a positive number for classment
        """
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.classment = classment

    def __str__(self):
        """Used for print player in view"""
        return f" {self.first_name} {self.last_name}\n {self.sex}\n né le : {self.date_of_birth}\n classement : {self.classment}"

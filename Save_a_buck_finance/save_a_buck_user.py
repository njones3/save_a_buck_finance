# save_a_buck_user.py

class User:
    def __init__(self, firstname, lastname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def user(self):
        return f"Welcome {self.firstname} {self.lastname}"
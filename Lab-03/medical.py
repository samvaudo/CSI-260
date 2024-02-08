"""
Author: Samuel Vaudo
Class: CSI-260-01
Certification of Authenticity:
I certify that this is entirely my own work, except where I have given fully documented
references to the work of others. I understand the definition and consequences of
plagiarism and acknowledge that the assessor of this assignment may, for the purpose of
assessing this assignment reproduce this assignment and provide a copy to another member
of academic staff and / or communicate a copy of this assignment to a plagiarism
service(which may then retain a copy of this assignment on its database for the purpose
of future plagiarism checking).
"""
class Patient:
    ''''DOCSTRING'''
    __lastID = 0
    _all_patients = {}

    def __init__(self, fname, lname, address, phone, contact_name, contact_phone):
        """first name, last name, address, phone number,and emergency contact"""
        self.firstName = fname
        self.lastName = lname
        self.addr = address
        self.pPhone = phone
        self.cName = contact_name
        self.cPhone = contact_phone
        self.ID = Patient.id(0)
        Patient._all_patients[self.ID] = self
        print(Patient.id())

    @classmethod
    def id(cls, value=1):
        if value == 0:
            cls.__lastID = cls.__lastID + 1
        return cls.__lastID

    def __str__(self):
        pass


class Procedure:
    pass

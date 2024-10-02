class StudentRegistration:
    def __init__(self, registration_number, student_name):
        self.registration_number = registration_number
        self.student_name = student_name
    def display_registration(self):
        print(f"Registration Number: {self.registration_number}")
        print(f"Student Name: {self.student_name}")
    def update_registration(self, new_registration_number):
        self.registration_number = new_registration_number
student1 = StudentRegistration("S23B13/008", "AKURUT JOSELINE")
student1.display_registration()
student1.update_registration("S23B13/010")
student1.display_registration()
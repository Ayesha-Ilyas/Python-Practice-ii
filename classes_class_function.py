class student:
    def __init__(self,bio,gpa,fee):
        self.bio=bio
        self.gpa=gpa
        self.fee=fee
    def hi(self):
            if self.gpa>=3.5:
                return True
            else:
                return False


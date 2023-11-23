from django.db import models


class Entry(models.Model):
    login = models.CharField(max_length=24)
    email = models.EmailField()
    password = models.CharField(max_length=64)  # Password in Sha-256
    creation_date = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, primary_key=True)  # user id
    otp = models.CharField(max_length=100)  # otp: empty - regular state, filled - logging process
    
    def toArray(self):
        return [self.login, self.email, self.password, self.creation_date, self.id, self.otp]
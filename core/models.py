from django.db import models
from django.contrib.auth.models import User

class MemberProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, unique=True)
    national_id = models.CharField(max_length=10, unique=True)
    middle_name = models.CharField(max_length=50, blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    # def_(self):
    #     return f"{self.user.username} - {self.national_id_id}" __str_
    def __str__(self):
        return f"{self.user.first_name} {self.middle_name} {self.user.last_name} - {self.national_id_id} "

class Contribution(models.Model):
    member = models.ForeignKey(MemberProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

class Loan(models.Model):
    STATUS_CHOICES = [('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')]
    member = models.ForeignKey(MemberProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    applied_at = models.DateField(auto_now_add=True)

class Repayment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateField(auto_now_add=True)

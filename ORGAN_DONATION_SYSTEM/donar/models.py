from django.db import models
import datetime
from django.core.validators import MinLengthValidator
class Donar(models.Model):
    first_name =models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=500)


    def register(self):
        self.save()

    @staticmethod
    def get_donar_by_email(email):
        try:
            return Donar.objects.get(email=email)
        except:
            return False


    def isExist(self):
        if Donar.objects.filter(email=self.email):
            return True
        else:
            return False




class Organ(models.Model):
    donar = models.ForeignKey(Donar,
                                 on_delete=models.CASCADE)
    organ_name=models.CharField(max_length=255, default='', blank=True)                            
    quantity = models.IntegerField(default=1)
    hospital_name = models.CharField(max_length=255, default='', blank=True)
    hospital_address = models.CharField(max_length=255, default='', blank=True)
    hospital_phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    

    def donate(self):
        self.save()

    @staticmethod
    def get_donar_by_donar_id(donar_id):
        return Organ.objects.filter(donar=doanr_id).doanted_on('-date')
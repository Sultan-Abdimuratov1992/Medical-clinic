from django.db import models
from service.models import Service




class Doctor(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  phone = models.CharField(max_length=13)
  description = models.TextField(blank=False)
  photo = models.ImageField(upload_to="doctor/%Y/%m/%d/")
  service = models.ManyToManyField(Service, related_name="doctors")

  def __str__(self):
    return self.first_name

class DoctorService(models.Model):
  doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
  service = models.ForeignKey(Service, on_delete=models.CASCADE)
  class Meta:
    unique_together = ('doctor', 'service')

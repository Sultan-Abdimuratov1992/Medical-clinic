from django.db import models
from doctor.models import Doctor
from datetime import date
from service .models import Service
from subService.models import SubService
from status.models import Status
from payment.models import Payment



class Appointment(models.Model):
  first_name = models.CharField(max_length=150, verbose_name="Имя пациента")
  last_name = models.CharField(max_length=150, verbose_name="Фамилия пациента")
  birth_date = models.DateField(default=date.today, verbose_name="Дата рождение")
  phone = models.CharField(max_length=13, verbose_name="Тел.Номер")
  appointment_date = models.DateField(default=date.today, verbose_name='Дата назначение') 
  service = models.ForeignKey(Service, on_delete=models.SET_NULL, blank=True, null=True)
  subService = models.ManyToManyField(SubService, blank=True, related_name='appointments')
  date_start = models.DateTimeField(verbose_name="Начало дата", blank=True, null=True)
  date_end = models.DateTimeField(verbose_name="Дата окончание", blank=True, null=True)
  doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, blank=True, null=True)
  status = models.ForeignKey(Status, on_delete=models.SET_NULL, blank=True, null=True)
  payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)

  def __str__(self):
    return self.first_name

class AppointmentSubService(models.Model):
  appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
  sub_service = models.ForeignKey(SubService, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=1)

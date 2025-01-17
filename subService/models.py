from django.db import models
from service.models import Service
from django.template.defaultfilters import slugify
from django.urls import reverse


def translate_to_eng(s: str) -> str:
  d = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
    'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'к': 'k',
    'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
    'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
    'ш': 'sh', 'щ': 'shch', 'ь': '', 'ы': 'y', 'ъ': '', 'э': 'r', 'ю': 'yu', 'я': 'ya'}
  return "".join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))

class SubService(models.Model):
  name = models.CharField(max_length=150, verbose_name="Название под-услуга")
  price = models.IntegerField(verbose_name="Сумма")
  service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
  slug = models.SlugField(max_length=150, unique=True, db_index=True)

  def __str__(self):
    return self.name
  
  def save(self, *args, **kwargs):
    self.slug = slugify(translate_to_eng(self.name))
    super().save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse('subService:delete_subService_page', kwargs={'subService_id': self.slug})

from django.db import models
from django.template.defaultfilters import slugify




def translate_to_eng(s: str) -> str:
  d = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
    'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'к': 'k',
    'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
    'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
    'ш': 'sh', 'щ': 'shch', 'ь': '', 'ы': 'y', 'ъ': '', 'э': 'r', 'ю': 'yu', 'я': 'ya'}
  return "".join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))

class Payment(models.Model):
  name = models.CharField(max_length=150, verbose_name="Название платежа")
  amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
  create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
  slug = models.SlugField(max_length=150, unique=True, db_index=True)

  def __str__(self):
    return f"{self.name} - {self.amount}"
  
  def save(self, *args, **kwargs):
    self.slug = slugify(translate_to_eng(self.name))
    super().save(*args, **kwargs)

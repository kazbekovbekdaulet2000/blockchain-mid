from django.db import models
from django.contrib.auth import get_user_model
import json
import hashlib

User = get_user_model()

# Create your models here.
class AbstractCreatedAt(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    abstract = True

CURRENCY = (
  ("T", "TENGE"),
  ("RUB", "RUBLE"),
  ("USD", "DOLLAR"),
  ("EUR", "EURO")
)

class CoffeeType(AbstractCreatedAt):
  name = models.CharField(max_length=255)
  description = models.TextField()

  class Meta: 
    ordering = ['created_at']
    verbose_name = 'Тип кофе'
    verbose_name_plural = 'Типы кофе'

  def __str__(self):
    return self.name

class Product_coffee(AbstractCreatedAt):
  name = models.CharField(max_length=255)
  price = models.PositiveBigIntegerField()
  image = models.ImageField(upload_to='products', null=True, blank=True)
  currency = models.CharField(max_length=255, choices=CURRENCY, default="USD")
  weight = models.FloatField(null=True, blank=True)
  entity = models.PositiveBigIntegerField(null=True, blank=True)
  type = models.ForeignKey(CoffeeType, on_delete=models.CASCADE, null=True, blank=True)

  class Meta: 
    ordering = ['created_at']
    verbose_name = 'Кофе'
    verbose_name_plural = 'Кофе'

  def __str__(self):
    return self.name


ORDER_STATUS = (
  (0, "На комплектации"),
  (1, "В пути"),
  (2, "Доставлен"),
)

class Order(AbstractCreatedAt):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True)
  product = models.ForeignKey(Product_coffee, on_delete=models.CASCADE, null = True)
  delivery_start = models.DateTimeField(null=True, blank=True)
  delivery_date = models.DateTimeField(null=True, blank=True)
  entity = models.PositiveBigIntegerField(null=True, blank=True)
  weight = models.FloatField(null=True, blank=True)
  price = models.PositiveBigIntegerField(null=True, blank=True)
  status = models.IntegerField(choices=ORDER_STATUS, default=0)

  class Meta: 
    ordering = ['created_at']
    verbose_name = 'Заказы'
    verbose_name_plural = 'Заказы'

  def __str__(self):
    return f"{self.user.username} - {self.product.name}"

def createHash():
  value = BlockChain.objects.values('id').distinct().last()
  if value is None:
    return 0
  else:
    value = BlockChain.objects.values('hash').distinct().last()
    return  value['hash']

class BlockChain(AbstractCreatedAt):
  data = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
  prev_hash = models.CharField(max_length=64, default=createHash, unique=True)
  hash = models.CharField(max_length=64, unique=True,  default=None, null=True)
  status = models.BooleanField(default=False)
  time = models.DateTimeField(auto_now_add=True)

  def save(self, *args, **kwargs):
    if self.hash is None:
      value = BlockChain.objects.values('id').distinct().last()
      if value is None:
        md5_key = hashlib.md5(str("qwerty").encode())
        self.hash = md5_key.hexdigest()
        super().save(*args, **kwargs)
      else:
        try:
          total_value = str(self.prev_hash + str(self.data.id))
          print(type(total_value), type(self.prev_hash), total_value)
          self.hash = hashlib.md5(total_value.encode()).hexdigest()
          super().save(*args,**kwargs)
        except Exception as err:
          print(err)

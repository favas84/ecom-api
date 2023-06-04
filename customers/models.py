from django.db import models

# Create your models here.


class AbstractDateBase(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Customer(AbstractDateBase):
    name = models.CharField(max_length=100)
    email = models.EmailField('email address', unique=True)

    def __str__(self):
        return self.name


class Product(AbstractDateBase):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=True)
    customer = models.ForeignKey(Customer, related_name='products',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.name

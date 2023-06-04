from django.db import models

# Create your models here.


class AbstractDateBase(models.Model):
    """
    Abstract base model class to track the creation and modification
    timestamps of objects.
    """
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Customer(AbstractDateBase):
    """
    Model representing a customer.

    Fields:
        name (CharField): The name of the customer.
        email (EmailField): The email address of the customer. Should be
        unique.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField('email address', unique=True)

    def __str__(self):
        return self.name


class Product(AbstractDateBase):
    """
    Model representing a product.

    Fields:
        name (CharField): The name of the product.
        description (TextField): The description of the product.
        status (BooleanField): The status of the product (True for active,
        False for inactive).
        customer (ForeignKey): The customer who owns this product.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=True)
    customer = models.ForeignKey(Customer, related_name='products',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.name

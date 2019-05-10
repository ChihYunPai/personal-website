from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    """docstring for Post"""
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=30)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    # print(text.get_prep_value())
    # pause("pause")
    # """for hash number"""
    # encoded_text = text.encode('UTF-8')
    # hash_number = hashlib.blake2b(encoded_text, digest_size=20).hexdigest()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class NewTable(models.Model):
    """docstring for NewTable"""
    bigint_f = models.BigIntegerField()
    bool_f = models.BooleanField()
    date_f = models.DateField()
    char_f = models.CharField(max_length=20, unique=True)
    datetime_f = models.DateTimeField(auto_now_add=True)
    decimal_f = models.DecimalField(max_digits=10, decimal_places=2)
    float_f = models.FloatField(null=True)
    int_f = models.IntegerField(default=2010)
    text_f = models.TextField()


class Product(models.Model):
    """docstring for Product"""
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    sku = models.CharField(max_length=50)
    brand = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1, choices=SIZES)
    qty = models.PositiveIntegerField()

    def __str__(self):
        return '<sku: {}, brand: {}, model: {}, price: {}, size: {}, qty: {}>'.format(self.sku, self.brand, self.name, self.price, self.size, self.qty)


class Maker(models.Model):
    """docstring for Maker"""
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ProductModel(models.Model):
    """docstring for PModel"""
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    url = models.URLField(default='http://i.imgur.com/Ous4iGB.png')

    def __str__(self):
        return self.name


class PhoneProduct(models.Model):
    """docstring for PhoneProduct"""
    product_model = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default='超值二手機')
    description = models.TextField(default='暫無說明')
    year = models.PositiveIntegerField(default=2016)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class ProductPhoto(models.Model):
    """docstring for ProductPhoto"""
    prodcut = models.ForeignKey(PhoneProduct, on_delete=models.CASCADE)
    description = models.CharField(max_length=30, default='產品照片')
    url = models.URLField(default='http://i.imgur.com/Z230eeq.png')

    def __str__(self):
        return self.description
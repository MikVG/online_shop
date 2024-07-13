from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    model = models.CharField(max_length=150, verbose_name='модель')
    release_date = models.DateField(verbose_name='дата выпуска')
    create_date = models.DateField(auto_now_add=True, verbose_name='дата создания')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return f'{self.name} {self.model}'


class SalesNetwork(models.Model):

    LEVEL_CHOICE = [
        (0, 'завод'),
        (1, 'розничная сеть'),
        (2, 'индивидуальный предприниматель'),
    ]

    level = models.CharField(max_length=100, choices=LEVEL_CHOICE, verbose_name='уровень')
    name = models.CharField(max_length=250, verbose_name='название')
    email = models.EmailField(max_length=50, verbose_name='email')
    country = models.CharField(max_length=150, verbose_name='страна', **NULLABLE)
    city = models.CharField(max_length=150, verbose_name='город', **NULLABLE)
    street = models.CharField(max_length=150, verbose_name='улица', **NULLABLE)
    building = models.CharField(max_length=15, verbose_name='номер дома', **NULLABLE)
    product = models.ManyToManyField(Product, verbose_name='продукты')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='поставщик', **NULLABLE)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='задолженность')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    class Meta:
        verbose_name = 'звено'
        verbose_name_plural = 'звенья'

    def __str__(self):
        return f'{self.name} {self.level} {self.country}'

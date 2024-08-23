from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Villa(models.Model):
    address = models.CharField(max_length=223)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    logo = models.ImageField(upload_to='media/villas_logos')
    price = models.DecimalField(decimal_places=2, max_digits=12)
    bedroom = models.PositiveSmallIntegerField()
    bathroom = models.PositiveSmallIntegerField()
    floor = models.PositiveSmallIntegerField()
    area = models.PositiveSmallIntegerField()
    parking = models.PositiveSmallIntegerField()
    room_count = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Вилла'
        verbose_name_plural = 'Виллы'

class Lead(models.Model):
    full_name = models.CharField(max_length=123)
    email = models.EmailField()
    subject = models.CharField(max_length=123)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Лид'
        verbose_name_plural = 'Лиды'
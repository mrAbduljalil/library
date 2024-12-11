from django.db import models

class Books(models.Model):
    FORMAT_CHOICES = [
        ("Standard", "Standard"),
        ("Downloadable", "Downloadable"),
        ("External", "External"),
    ]

    AVAILABILITY_CHOICES = [
        ("In Stock", "In Stock"),
        ("Out of Stock", "Out of Stock"),
        ("On Sale", "On Sale"),
        ("New", "New"),
    ]

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Authors', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField(null=True, blank=True)
    categories = models.ManyToManyField('Categories')
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES)
    format = models.CharField(max_length=20, choices=FORMAT_CHOICES)
    published_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Authors(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Reviews(models.Model):
    book = models.ForeignKey('Books', on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    text = models.TextField(null=False, blank=False)
    rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.book)


class Categories(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

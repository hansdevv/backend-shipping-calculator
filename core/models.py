from django.db import models

class Country(models.Model):
    country_name = models.CharField(max_length=100, unique=True, verbose_name="Country Name")
    country_flag = models.URLField(max_length=200, blank=True, null=True, verbose_name="Country Flag URL")
    country_currency = models.CharField(max_length=10, verbose_name="Country Currency Code (e.g., USD, IDR)")

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ['country_name']

    def __str__(self):
        return self.country_name

class Category(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='categories', verbose_name="Origin Country")
    category_title = models.CharField(max_length=150, verbose_name="Category Title")
    price_per_kilo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price Per Kilo (International)")

    class Meta:
        verbose_name_plural = "Categories"
        # Ensure that a category title is unique per country
        unique_together = ('country', 'category_title')
        ordering = ['country__country_name', 'category_title']

    def __str__(self):
        return f"{self.category_title} ({self.country.country_name})"


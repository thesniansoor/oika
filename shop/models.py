from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Category Name")
    description = models.TextField(verbose_name="Category Description", null=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="sub_categories", null=True, verbose_name="Category")
    name = models.CharField(max_length=200, verbose_name="Sub-Category Name")
    description = models.TextField(verbose_name="Sub-Category Description", null=True, blank=True)

    class Meta:
        verbose_name = "Sub-Category"
        verbose_name_plural = "Sub-Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="products",  null=True, verbose_name="Sub-Category")
    name = models.CharField(max_length=200, verbose_name="Product Name")
    description = models.TextField(verbose_name="Product Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    stock = models.IntegerField(verbose_name="Stock Quantity")
    available = models.BooleanField(default=True, verbose_name="Available for Sale")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    image = models.ImageField(upload_to='product/', null=True, blank=True, verbose_name="Product Image")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

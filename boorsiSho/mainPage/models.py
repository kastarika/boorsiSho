from django.db import models

# Create your models here.

class Industry(models.Model):
    name = models.CharField( max_length=100, default="" )

    def __str__(self):
        return str(self.name)
    
class FinancialYear(models.Model):
    year = models.IntegerField( null=True )

    def __str__(self):
        return str(self.year)

class Category(models.Model):
    name = models.CharField( max_length=100, default="" )
    industry = models.ForeignKey( Industry, on_delete=models.CASCADE, null=True )

    def __str__(self):
        return str(self.name)

class Company(models.Model):
    name = models.CharField( max_length=100, default="" )
    symbol = models.CharField( max_length=100, default="" )
    category = models.ForeignKey( Category, on_delete=models.CASCADE, null=True )
    industry = models.ForeignKey( Industry, on_delete=models.CASCADE, null=True )

    def __str__(self):
        return str(self.name)

class FinancialRatio(models.Model):
    currentRatio = models.IntegerField( null=True )
    quickRatio = models.IntegerField( null=True )
    company = models.ForeignKey( Company, on_delete=models.CASCADE, null=True )
    financialYear = models.ForeignKey( FinancialYear, on_delete=models.CASCADE, null=True )

    dateCreated = models.DateTimeField( auto_now_add=True )

    def __str__(self):
        return str(self.company)
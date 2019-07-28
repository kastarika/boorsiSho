#companyName symbol industryName categoryName currentRatio quickRatio financialYear


import pyexcel as PE
from . import models
fileLocation = "static/mainPage/static/Database.xlsx"
sheetName = "Total"

def fillInDatabase():
    DB = PE.get_book( file_name=fileLocation )[sheetName]

    for row in DB:
        newIndustry = models.Industry.objects.get_or_create( name=row[3] )
        newCategory = models.Category.objects.get_or_create( name=row[4] )
        newFinancialYear = models.FinancialYear.objects.get_or_create( year=row[7] )
        newCompany = models.Company.objects.get_or_create( name=row[1] )
        newFinancialRatio = models.FinancialRatio

        newIndustry.name = row[3]
        newIndustry.save()

        newCategory.name = row[4]
        newCategory.industry = newIndustry
        newCategory.save()

        newCompany.name = row[1]
        newCompany.symbol = row[2]
        newCompany.industry = newIndustry
        newCompany.category = newCategory
        newCompany.save()

        newFinancialYear.year = row[7]
        newFinancialYear.save()

        newFinancialRatio.currentRatio = row[5]
        newFinancialRatio.quickRatio = row[6]
        newFinancialRatio.company = newCompany
        newFinancialRatio.financialYear = newFinancialYear
        newFinancialRatio.save()
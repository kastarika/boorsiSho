#companyName symbol industryName categoryName currentRatio quickRatio financialYear


import django_excel as DE
from mainPage import models

class Import:
    def __init__(self):
        pass

    @staticmethod
    def fillInDatabase( dataSheet ):
        #dataSheet = PE.get_sheet( inputDataFile )

        for row in dataSheet:
            newIndustry = models.Industry.objects.get_or_create( name=row[3] )[0]
            newCategory = models.Category.objects.get_or_create( name=row[4] )[0]
            newFinancialYear = models.FinancialYear.objects.get_or_create( year=row[7] )[0]
            newCompany = models.Company.objects.get_or_create( name=row[1] )[0]
            newFinancialRatio = models.FinancialRatio()
            
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
from django.db import models
from Auth_user.models import * 

class CompanyDetails(models.Model):
    company_details_id = models.AutoField(primary_key=True)
    user_id =models.ForeignKey(CoreUser,on_delete=models.CASCADE,related_name='company_user')
    company_name = models.CharField(max_length=155)
    company_address = models.CharField(max_length=155)
    pincode=models.CharField(max_length=15)
    company_logo=models.ImageField(upload_to='CompanyLogo/')
    bank_name=models.CharField(max_length=155)
    branch_name=models.CharField(max_length=155)
    account_number=models.CharField(max_length=155)
    ifsc_code=models.CharField(max_length=155)
    gst_in=models.CharField(max_length=155)
    digital_seal=models.ImageField(upload_to='CompanyLogo/')
    digital_signature=models.ImageField(upload_to='CompanyLogo/')
    
    DisplayField = ['company_details_id','company_name','company_address','pincode','bank_name']
    
    def __str__(self):
        return self.company_name
    class Meta:
        db_table='company_details'
class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=255)
    email = models.EmailField(null=True,unique=True)
    contact =PhoneNumberField(null=True,unique=True)
    address = models.CharField(max_length=555)
    pincode=models.CharField(max_length=15,null=True)
    
    DisplayField = ['client_id','client_name','email','contact','address']
    
    def __str__(self):
        return self.client_name    
    
    class Meta:
        db_table = 'client'

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=255)
    start_date = models.DateField(null=True)
    duration = models.CharField(max_length=155)

    
    DisplayField = ['project_id','project_name','duration','start_date']

    def __str__(self):
        return self.project_name
    
    class Meta:
        db_table = 'project'

class Invoice_item(models.Model):
    invoice_item_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project,on_delete=models.CASCADE,null=True)
    item_price = models.IntegerField()
    tax_id = models.ForeignKey("Tax",on_delete=models.CASCADE,null=True)
    tax_amount = models.DecimalField(decimal_places=2,max_digits=10,null=True)

    DisplayField = ['invoice_item_id','project_id','item_price','tax_id','tax_amount']

    def __str__(self):
        return f"InvoiceItem {self.project_id.project_name}"
    
    class Meta:
        db_table = 'invoice_item' 

class Item_tax(models.Model):
    item_tax_id = models.AutoField(primary_key=True)
    invoice_item = models.ForeignKey(Invoice_item,on_delete=models.CASCADE,related_name='item')
    tax = models.ForeignKey('Tax',on_delete=models.CASCADE,related_name='tax')
    amount = models.DecimalField(max_digits=10,decimal_places=2,null=True)

    class Meta:
        db_table = 'item_tax'



class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(Client,on_delete=models.CASCADE,null=True,related_name='client_invoice')
    invoice_item_id = models.ManyToManyField("Invoice_item")
    generated_date = models.DateField()
    invoice_pdf = models.FileField(upload_to='Invoice/',null=True) 
    total_amount = models.IntegerField()
    invoice_number=models.CharField(null=True)
    status = models.CharField(max_length=255)
    

    DisplayField = ['invoice_id','client_id','total_amount','status','generated_date','invoice_pdf']

    def __str__(self):
        return self.client_id.client_name    
    class Meta:
        db_table = 'invoice'
        
       




class Technology_option(models.Model):
    option_id = models.AutoField(primary_key=True)
    option = models.CharField(max_length=155)

    DisplayField = ['option_id','option']

    def __str__(self):
        return self.option
    
    class Meta:
        db_table = 'technology_option'


class Technology(models.Model):
    tech_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    option_id = models.ForeignKey(Technology_option,on_delete=models.CASCADE,null=True)

    DisplayField = ['tech_id','name','option_id']

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'technology'
    

class Payment_method(models.Model):
    payment_method_id = models.AutoField(primary_key=True)
    payment_type = models.CharField(max_length=55)

    DisplayField = ['payment_method_id','payment_type']

    def __str__(self):
        return self.payment_type
    
    class Meta:
        db_table = 'payment_method'


class Tax(models.Model):
    tax_id = models.AutoField(primary_key=True)
    tax_name = models.CharField(max_length=155)
    rate = models.DecimalField(decimal_places=2,max_digits=5)

    DisplayField = ['tax_id','tax_name','rate']

    def __str__(self):
        return f'{self.tax_name} - {self.rate}%'
    
    class Meta:
        db_table = 'tax'



class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=150)

    DisplayField = ['team_id','team_name']

    def __str__(self):
        return self.team_name
    
    class Meta:
        db_table = 'team'












class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    invoice_id = models.ForeignKey(Invoice,on_delete=models.CASCADE,null=True)
    method_id = models.ForeignKey(Payment_method,on_delete=models.CASCADE,null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=5)
    payment_date = models.DateField(blank=False)

    DisplayField = ['payment_id','invoice_id','method_id','amount','payment_date']

    def __str__(self):
        return self.payment_id
    
    class Meta:
        db_table = 'payment'
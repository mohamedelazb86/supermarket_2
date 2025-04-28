from django.db import models

class Setting(models.Model):
    name=models.CharField(max_length=120)
    logo=models.ImageField(upload_to='logo')
    subtitle=models.TextField(max_length=2000)
    call_us=models.CharField(max_length=75)
    email_us=models.CharField(max_length=150)
    phones=models.CharField(max_length=100)
    address=models.TextField(max_length=500)
    andriod_apps=models.URLField(null=True,blank=True)
    facebook=models.URLField(null=True,blank=True)
    ios_apps=models.URLField(null=True,blank=True)
    youtube=models.URLField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    

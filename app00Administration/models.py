from django.db import models
import uuid

# Create your models here.
def generate_unique_id():
    return uuid.uuid4().hex[:16]

# Firm Model
class Firm(models.Model):
    firm_id =models.CharField(primary_key=True, default=generate_unique_id, editable=False, max_length=16)
    firm_name = models.CharField(max_length=200, null=False, unique=False)
    firm_domain = models.CharField(max_length=200, null=False, unique=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.firm_name)

    # def get_absolute_url(self):
    #     return reverse('administration:view-firms')
from django.db import models
from datetime import datetime

class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    message_updated_date = models.DateTimeField(null=True, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_contact = Contact.objects.get(pk=self.pk)
                if old_contact.message != self.message:
                    self.message_updated_date = datetime.now()
            except Contact.DoesNotExist:
                pass
        
        super().save(*args, **kwargs)

    @property
    def was_message_updated(self):
        return self.message_updated_date is not None
    
    @property
    def message_status(self):
        if self.message_updated_date:
            return "Updated"
        return "Original"
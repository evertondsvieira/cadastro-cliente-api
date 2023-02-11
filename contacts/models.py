from django.db import models

class Contact(models.Model):
    class Meta:
        ordering = ["id"]
    full_name = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    users = models.ForeignKey(
        "users.User", 
        on_delete=models.CASCADE,
        related_name="contacts",
    )
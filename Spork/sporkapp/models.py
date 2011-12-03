from django.db import models

# Create your models here.

class Provider(models.Model):
    account_name = models.CharField(max_length=20)
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=60)
<<<<<<< HEAD
=======
    def __unicode__(self):
        return self.name
>>>>>>> 44fb5a8f08cbe1f12ffd0622a92e98efff2709f5
    
class Receiver(models.Model):
    account_name = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=60)
    ein = models.CharField(max_length=20)
<<<<<<< HEAD
=======
    def __unicode__(self):
        return self.account_name
>>>>>>> 44fb5a8f08cbe1f12ffd0622a92e98efff2709f5

class Donation(models.Model):
    DONATION_STATUS_CHOICES = (
        (u'available', u'available'),
        (u'claimed', u'claimed'),
        (u'expired', u'expired')
    )

    description = models.CharField(max_length=250)
    num_servings = models.IntegerField()
    expiration_time = models.IntegerField()
    time_created = models.DateTimeField()
    status = models.CharField(max_length=20, choices=DONATION_STATUS_CHOICES)
    donated_by = models.ForeignKey(Provider)
    claimed_by = models.ForeignKey(Receiver)
    time_claimed = models.DateTimeField()
<<<<<<< HEAD
=======
    def __unicode__(self):
        return self.description
>>>>>>> 44fb5a8f08cbe1f12ffd0622a92e98efff2709f5

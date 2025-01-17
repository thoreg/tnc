"""Model definitions of the banking app live here."""
from django.db import models
from django_extensions.db.models import TimeStampedModel


class TransactionFileUpload(TimeStampedModel):
    """Upload of CSV files with detailed information about transactions."""

    processed = models.BooleanField(default=False)
    original_csv = models.FileField(upload_to="banking/csv/")
    file_name = models.CharField(max_length=64, unique=True)

    class Meta:
        """..."""
        managed = False


# Create your models here.
class DKBTransaction(TimeStampedModel):
    """Table to store rows from DKB csv download."""
    booking_date = models.DateTimeField()
    """ Buchungsdatum """
    value_date = models.DateTimeField()
    """ Wertstellung """
    status = models.CharField(max_length=64)
    """ Status """
    sender = models.CharField(max_length=128)
    """ Zahlungspflichtige*r """
    receiver = models.CharField(max_length=128)
    """ Zahlungsempfänger*in """
    purpose = models.TextField()
    """ Verwendungszweck """
    payment_type = models.CharField(max_length=64)
    """ Umsatztyp """
    iban = models.CharField(max_length=64)
    """ IBAN """
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    """ Betrag (€) """

    class Meta:
        """..."""
        verbose_name_plural = "DKB Transaktionen"

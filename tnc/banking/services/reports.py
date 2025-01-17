"""Report related functions live here."""
from decimal import Decimal
import logging
from pprint import pprint
from tnc.lib.csv import read_csv
from banking.models import DKBTransaction
from datetime import datetime

LOG = logging.getLogger(__name__)


def import_dkb_transaction_report(file_path: str) -> None:
    """Import transaction data from DKB."""
    for line in read_csv(file_path):
        pprint(line)

        # Remove thousand dot, repace comma
        amount = Decimal(line['Betrag (€)'].replace(".", "").replace(",", "."))
        booking_date = datetime.strptime(line['\ufeff"Buchungsdatum"'], "%d.%m.%y")
        value_date = datetime.strptime(line['Wertstellung'], "%d.%m.%y")

        entry, created = DKBTransaction.objects.get_or_create(
            booking_date=booking_date,
            value_date=value_date,
            status=line['Status'],
            sender=line['Zahlungspflichtige*r'],
            receiver=line['Zahlungsempfänger*in'],
            purpose=line['Verwendungszweck'],
            payment_type=line['Umsatztyp'],
            iban=line['IBAN'],
            amount=amount,
        )
        if created:
            LOG.info(f"created {entry.iban} {entry.amount} {entry.payment_type}")
        else:
            LOG.info(f"known {entry.iban} {entry.amount} {entry.payment_type}")

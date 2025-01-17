"""Views of the banking app."""
import datetime as dt
import logging
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from tnc.lib.file_upload import handle_uploaded_file

from .forms import UploadFileForm
from .models import TransactionFileUpload
from .services.reports import import_dkb_transaction_report

LOG = logging.getLogger(__name__)


@login_required
def somethingelseindex(request):
    """Zalando Index View."""
    ctx = {
        "title": "welcome to the banking context"
    }
    return render(request, "banking/index.html", ctx)


@login_required
def index(request):
    """Handle for uploaded files."""
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        files = request.FILES.getlist("original_csv")
        if form.is_valid():
            for f in files:
                path = handle_uploaded_file(settings.DKB_FINANCE_CSV_UPLOAD_PATH, f)
                import_dkb_transaction_report(path)

            msg = f"{len(files)} files uploaded successfully"
            messages.success(request, msg)
            return redirect(reverse("banking_index"))

        context = {"msg": "Form is invalid"}
        return render(request, "banking/index.html", context)
    else:
        form = UploadFileForm()

    file_uploads = TransactionFileUpload.objects.all().order_by("-created")[:50]
    LOG.info(f"we have {len(file_uploads)} objects")

    return render(
        request,
        "banking/index.html",
        {"file_uploads": file_uploads, "form": form},
    )

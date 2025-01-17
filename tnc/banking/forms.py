from django import forms

from .models import TransactionFileUpload


class UploadFileForm(forms.ModelForm):
    """Upload Form for Finance CSV Files."""

    original_csv = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"allow_multiple_selected": True})
    )

    class Meta:
        """..."""
        model = TransactionFileUpload
        fields = ["original_csv"]

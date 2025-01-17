"""Base views"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone


def page_not_found_view(request, _exception):
    """..."""
    return render(request, "404.html", status=404)


@login_required
def index(request):
    """..."""
    return render(
        request,
        "tnc/index.html",
        {
            "now": timezone.now()
        },
    )

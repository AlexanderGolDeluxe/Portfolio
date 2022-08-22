from datetime import datetime

from django.shortcuts import render, redirect

from .forms import ContactsForm


def index(request, language=""):
    template_suffix = "_eng" if language else ""
    if request.method == "POST":
        contacts_form = ContactsForm(request.POST)
        if contacts_form.is_valid():
            request.session["contacts_saved"] = True
            request.session.set_expiry(300)
            contacts_form.save()
            return redirect("/#contacts")

    context = dict(
        datetime_now=datetime.now(),
        contacts_form=ContactsForm,
        contacts_saved=request.session.get("contacts_saved")
    )
    return render(request, f"cvmainapp/index{template_suffix}.html", context)


def refresh_form(request, language=""):
    template_suffix = "/eng" if language else ""
    request.session.flush()
    return redirect(template_suffix + "/#contacts")

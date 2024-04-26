from datetime import datetime, date

from django.shortcuts import render, redirect

from .forms import ContactsForm
from .services import years_to_word


def index(request, language=""):
    if request.method == "POST":
        contacts_form = ContactsForm(request.POST)
        if contacts_form.is_valid():
            request.session["contacts_saved"] = True
            request.session.set_expiry(300)
            contacts_form.save()
            return redirect("/#contacts")

    lang_suffix = "_eng" if language else ""
    work_experience = date.today() - date(2021, 2, 1)
    context = dict(
        datetime_now=datetime.now(),
        contacts_form=ContactsForm,
        contacts_saved=request.session.get("contacts_saved"),
        experience_years=years_to_word(
            years=int(work_experience.days / 365.2425),
            lang=lang_suffix.lstrip("_"))
    )
    return render(request, f"cvmainapp/index{lang_suffix}.html", context)


def refresh_form(request, language=""):
    template_suffix = "/eng" if language else ""
    request.session.flush()
    return redirect(template_suffix + "/#contacts")

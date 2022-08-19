from django import forms

from .models import Contacts


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ["user_name", "user_email", "message"]
        labels = {
            "user_name": "Name",
            "user_email": "Email",
            "message": "Message"
        }
        widgets = {
            "user_name": forms.TextInput(attrs = {
                "class": "contacts-form-input",
                "id": "contact_name"
            }),
            "user_email": forms.EmailInput(attrs = {
                "class": "contacts-form-input",
                "id": "contact_email"
            }),
            "message": forms.Textarea(attrs = {
                "class": "contacts-form-textarea",
                "id": "contact_message"
            })
        }
        message_textarea = widgets["message"]
        del message_textarea.attrs["cols"]
        del message_textarea.attrs["rows"]

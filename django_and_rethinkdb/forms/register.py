from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    """
    Form for registering a new account.
    """
    username = forms.EmailField(widget=forms.TextInput,label="Email")
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Password"
    )

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        """
        Verifies that the values entered into the password fields match

        NOTE: Errors here will appear in ``non_field_errors()`` because it applies to more than one field.
        """
        cleaned_data = super(RegistrationForm, self).clean()
        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

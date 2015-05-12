from django import forms

class LoginForm(forms.Form):
    """
    Login form
    """
    username = forms.EmailField(widget=forms.widgets.TextInput)
    password = forms.CharField(widget=forms.widgets.PasswordInput)

    class Meta:
        fields = ['username', 'password']

from django import forms


class LoginForm(forms.Form):
    choices = [("HM", "HeadMaster"), ("ST", "Student"), ("TE", "Teacher")]
    username = forms.CharField(label='Username', empty_value=False,required=True)
    password = forms.CharField(label='Password', empty_value=False,required=True, max_length=8, widget=forms.PasswordInput)
    usertype = forms.ChoiceField(label='LogIn As', choices=choices)
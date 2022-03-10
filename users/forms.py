from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column



class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'email',
            Row(
                Column('password1', css_class='form-group col-md-6'),
                Column('password2', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Submit('submit', 'Submit', css_class="btn-secondary")
        )
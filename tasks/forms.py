from django import forms
from django.forms.widgets import NumberInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class TaskForm(forms.Form):
    name = forms.CharField(label='New task', max_length=100)
    description = forms.CharField(widget=forms.Textarea, required=False)
    # task_list = forms.
    completed = forms.BooleanField(required=False)
    target_date = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    # target_date = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    # target_date = forms.DateTimeInput()
    # Date = forms.DateField(widget = forms.SelectDateWidget)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'description',
            Row(
                Column('completed', css_class='form-group col-md-auto'),
                Column('target_date', css_class='form-group col-md-auto'),
                css_class='form-row'
            ),
            Submit('submit', 'Create new task')
        )


class TaskListForm(forms.Form):
    name = forms.CharField(label='List name', max_length=100)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            Submit('submit', 'Create new list')
        )
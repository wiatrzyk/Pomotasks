from django import forms
from django.forms.widgets import NumberInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

CHOICES = (
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
)

class TaskForm(forms.Form):
    name = forms.CharField(label='Task', max_length=100)
    description = forms.CharField(widget=forms.Textarea, required=False)
    task_list = forms.ChoiceField()
    completed = forms.BooleanField(required=False)
    target_date = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    # target_date = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    # target_date = forms.DateTimeInput()
    # Date = forms.DateField(widget = forms.SelectDateWidget)

    def __init__(self, *args, **kwargs):
        self.choices = kwargs.pop('choices')
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['task_list'].choices = self.choices
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
            Column('name', css_class='form-group col-md-auto'),
            Column('task_list', css_class='form-group col-md-auto'),
            ),
            'description',
            Row(
                Column('completed', css_class='form-group col-md-auto'),
                Column('target_date', css_class='form-group col-md-auto'),
                css_class='form-row'
            ),
            Submit('submit', 'Submit', css_class="btn-secondary")
        )


class TaskListForm(forms.Form):
    name = forms.CharField(label='List name', max_length=100)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            Submit('submit', 'Create new list', css_class="btn-secondary")
        )
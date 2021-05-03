from django.forms import DateInput, ModelForm, NumberInput, TextInput

from .models import Course


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ["title", "description", "start_date", "finish_date", "amount"]
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Course name",
            }),
            "description": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Brief course description",
            }),
            "start_date": DateInput(format='%Y-%m-%d', attrs={"class": "form-control",
                                                               "placeholder": "Start date in format YYYY-MM-DD",
            }),
            "finish_date": DateInput(format='%Y-%m-%d', attrs={"class": "form-control",
                                                               "placeholder": "Finish date in format YYYY-MM-DD",
            }),
            "amount": NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Lectures amount",
            }),
        }

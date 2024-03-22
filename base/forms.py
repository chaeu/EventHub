from django.forms import ModelForm, DateInput, TimeInput
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        widgets = {
            "date": DateInput(attrs={"type": "date"}),
            "time": TimeInput(attrs={"type": "time"})
        }
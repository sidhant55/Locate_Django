from django import forms
from rest_framework import request
import datetime
from .models import Locator
from .serializers import LocatorSerializer
obj  = Locator.objects.all()
serial = LocatorSerializer(obj, many=True)
ar =[]
for i in range(len(serial.data)):
    a=str((serial.data)[i]['scu_id'])
    ar.append((a,a))
ar =set(ar)
ar = tuple(ar)

class dataform(forms.Form):

    scu_id = forms.ChoiceField(choices=ar, label="Vehicle ID")
    startdate = forms.CharField(widget=forms.SelectDateWidget(years=range(2010, datetime.date.today().year+10)), label='Start Date')
    starttime= forms.CharField(widget=forms.TimeInput(attrs={'placeholder':'Optional'}), required=False, label='Start Time' )
    enddate= forms.CharField(widget=forms.SelectDateWidget(years=range(2010, datetime.date.today().year+10)), label='End Date')
    endtime= forms.CharField(widget=forms.TimeInput(attrs={'placeholder':'Optional'}), required=False, label='End Time')
    # end = forms.DateTimeField(label='end')

    def stdate(self):
        return str(self.startdate)
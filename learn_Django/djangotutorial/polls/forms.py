from django import forms
from .models import Poll

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        # Chỉ định các trường bạn muốn người dùng nhập
        fields = ['title', 'message', 'time', 'status']
        
        # (Tùy chọn) Thêm class CSS cho HTML để form đẹp hơn
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-input'}),
            'message' : forms.Textarea(attrs={'class': 'form-textarea'}),
            'time' : forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'status' : forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }

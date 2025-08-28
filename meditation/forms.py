from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    mobile = forms.CharField(max_length=10)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    robot_check = forms.BooleanField(required=True)

    def clean_mobile(self):
        mobile = self.cleaned_data.get("mobile")
        if not mobile.isdigit() or len(mobile) != 10:
            raise forms.ValidationError("Enter a valid 10-digit mobile number.")
        return mobile

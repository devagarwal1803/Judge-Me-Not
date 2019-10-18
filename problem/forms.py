from django import forms

class ans(forms.Form):
    Enrollment=forms.CharField(max_length=20)
    Solution=forms.CharField(widget=forms.Textarea)
    
    def clean_Solution(self):
        Solution=self.cleaned_data.get('Solution')
        return Solution
    
    def clean_Enrollment(self):
        Enrollment=self.cleaned_data.get('Enrollment')
        return Enrollment
    
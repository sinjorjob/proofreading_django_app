from django import forms

CHOICES = (('low', '低',), ('medium', '中',), ('high', '高',))


class UserForm(forms.Form):
     textone = forms.CharField(label='入力文章',max_length=500,
     min_length=1,widget=forms.Textarea(attrs=
     {'id': 'textone','placeholder':'ここにチェックしたい文章を入力してください\n(500文字まで）'}))
     sensitivity = forms.ChoiceField(label='チェックの厳密さ', widget=forms.Select, choices=CHOICES
     )
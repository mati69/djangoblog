from django import forms
from .models import Post

class ImgForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image']

class PostForm(forms.ModelForm):  # jest jednocześnie formularzem modelu ModelForm z biblioteki forms

    title = forms.CharField(help_text='maksymalnie 200 znaków')

    class Meta:
        model = Post # klasa informuje Django jaki model ma być wykorzystany do stworzenia furmularza
        fields = ['title', 'text', 'image'] # jakie mają być pola - nie musi być pola autora i daty,
                                            # czasem aby autorem był bierzący uzytkownik trzeba dodać kod
                                            # przed zapisaniem formularza: form.instance.author = self.request.user

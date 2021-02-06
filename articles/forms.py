
from django import forms 
from tinymce.widgets import TinyMCE
from articles.models import Post

class TinyMCEWidget(TinyMCE): 
    def use_required_attribute(self, *args): 
        return False

class ArticleForm(forms.ModelForm):
    content = forms.CharField( 
        widget=TinyMCEWidget( 
            attrs={'required': False, 'cols': 30, 'rows': 10} 
        ) 
    ) 

    class Meta:
        model = Post
        fields = ('title','content','image','author', 'category','tags')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'slug': forms.TextInput(attrs={'class':'form-control'}),
            'tags': forms.TextInput(attrs={'class':'form-control'}),
        }
        labels = {
            'Title': 'Title',
            'Content': 'Content',
            'Author': 'Author',
            'Image': 'Image',
            'slug': 'slug',
            'Category':'category',
            'Tags':'tags',
        }
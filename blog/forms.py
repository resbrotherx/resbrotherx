from django import forms
from blog.models import Post, Comment
# from tinymce import TinyMCE

# class TinyMCEWidget(TinyMCE):
# 	def use_required_attribute(self, *args):
# 		return False

# class PostForm(forms.ModelForm):
#     content = forms.CharField(
#         widget=TinyMCE(attrs={
#             'required': False,
#             'cols': 30,
#             'rows': 10
#         }))

#     class Meta:
#         model = Post
#         fields = '__all__'


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'your comment.......',
        'name': 'commentText',
        'rows': '1'
    }))
    class Meta:
        model = Comment
        fields = ('comment', )
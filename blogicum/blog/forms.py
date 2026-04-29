from django import forms
from django.contrib.auth import get_user_model

from .models import Post, Comment

User = get_user_model()


def _to_bool(value):
    return str(value).strip().lower() in {'1', 'true', 'yes', 'on'}


class PostForm(forms.ModelForm):
    is_published = forms.TypedChoiceField(
        choices=((True, 'Да'), (False, 'Нет')),
        coerce=_to_bool,
        empty_value=True,
        required=False,
        initial=True,
        label='Опубликовано',
    )

    class Meta:
        model = Post
        fields = (
            'title',
            'text',
            'is_published',
            'pub_date',
            'location',
            'category',
            'image',
        )
        widgets = {
            'pub_date': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={'type': 'datetime-local'},
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

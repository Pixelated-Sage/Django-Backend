from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'Your Username',
                'autocomplete': 'off',
            }
        )
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Your Password',
                'autocomplete': 'off',
                'id': 'password-id',
            }
        )
    )

    show = forms.BooleanField(
        label="Show Password",
        required=False,
        widget=forms.CheckboxInput(\
            attrs={
                'class': 'show-password',
            }
        ),
    )
from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from rest_framework.reverse import reverse_lazy

from .models import User, Profile, Country, Rang
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'nickname', 'is_staff', 'is_active')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'nickname', 'password', 'is_active', 'is_staff')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].help_text = ("Raw passwords are not stored, so there is no way to see "
                                             "this user's password, but you can <a href=\"%s\"> "
                                             "<strong>Change the Password</strong> using this form</a>.") %\
                                            reverse_lazy('admin:auth_user_password_change', args=[self.instance.id])

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('nickname', 'email', )
    fieldsets = (
        (None, {'fields': ('email', 'password', 'nickname', 'is_active', 'is_staff')}),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nickname', 'is_staff', 'is_active', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Country)
admin.site.register(Rang)

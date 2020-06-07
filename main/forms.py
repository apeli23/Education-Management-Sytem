from django import forms
from .models import (Principle, SubCounty, Category, Status, School)


class PrincipleForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }
        )
    )
    first_name = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }
        )
    )
    last_name = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }
        )
    )
    email = forms.EmailField(
        max_length=20,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }
        )
    )
    # forms.
    password = forms.CharField(
        max_length=20,
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'New password'
            }
        )
    )
    password2 = forms.CharField(
        max_length=20,
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'New password'
            }
        )
    )
    telNo = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Tel Number'
            }
        )
    )
    tsc = forms.CharField(
        max_length=20,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Tsc Number'
            }
        )
    )


class CategoryForm(forms.Form):
    name = forms.CharField(
        max_length=10,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Category Name'
            }
        )
    )
    description = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Category description'
            }
        )
    )


class StatusForm(forms.Form):
    name = forms.CharField(
        max_length=10,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Status Name'
            }
        )
    )
    description = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Status description'
            }
        )
    )
    # TODO: Define form fields here


class SubcountyForm(forms.Form):
    name = forms.CharField(
        max_length=10,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Subcounty Name'
            }
        )
    )


class SchoolForm(forms.Form):
    school_types = (
        ('PR', 'Primary'),
        ('SC', 'Secondary'),
    )
    name = forms.CharField(
        max_length=10,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'School Name'
            }
        )
    )

    knecCode = forms.CharField(
        max_length=10,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'SChool knec code'
            }
        )
    )
    principle = forms.ModelChoiceField(
        queryset=Principle.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                # 'placeholder': 'Status Name'
            }
        )
    )
    subCounty = forms.ModelChoiceField(
        queryset=SubCounty.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                # 'placeholder': 'Status Name'
            }
        )
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                # 'placeholder': 'Status Name'
            }
        )
    )
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                # 'placeholder': 'Status Name'
            }
        )
    )
    sType = forms.ChoiceField(
        choices=school_types,
        required=True,
        label='Types',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                # 'placeholder': 'Status Name'
            }
        )
        # max_length=10,
        # label='School type',

    )
    streams = forms.IntegerField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Number of streams'
            }
        )
    )
    enrollment = forms.IntegerField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enrollment'
            }
        )
    )


class CapacityForm(forms.Form):
    gender = (
        ('B', 'Boys'),
        ('G', 'Girls'),
    )
    school = forms.ModelChoiceField(
        queryset=School.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Status Name'
            }
        )
    )
    year = forms.CharField(
        max_length=4,
        min_length=4,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Admission Year'
            }
        )
    )

    gender = forms.ChoiceField(
        # max_length=10,
        label='Gender',
        choices=gender,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Status Name'
            }
        )
    )
    amount = forms.IntegerField(
        # max_length=20,
        # min_length=1,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Number'
            }
        )
    )


class FilesUploads(forms.Form):
    file_types = (
        ('SC', 'Schools'),
        ('PR', 'Principles'),
        ('SB', 'Subcounties'),
        ('CT', 'Categories'),
        ('ST', 'Status'),
        ('CP', 'Capacity')
    )
    Ftype = forms.ChoiceField(
        label='File type',
        choices=file_types,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    file = forms.FileField(
        label='Select file',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control-file',
            }
        )
    )

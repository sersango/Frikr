# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError

from photos.models import Photo
from photos.settings import SWEARWORDS


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        exclude = ['owner']

    def clean(self):

        cleaned_data = super(PhotoForm, self).clean()

        description = cleaned_data.get('description'.lower(), '')

        for swearword in SWEARWORDS:
            if swearword.lower() in description:
                raise ValidationError(u'La palabra "{0}" no está permitida.'.format(swearword))

        return cleaned_data


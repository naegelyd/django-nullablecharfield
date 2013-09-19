from django.db import models
from django.utils.translation import gettext_lazy as _

from nullablecharfield.forms.fields import CharNullField as CharNullFieldForm
from nullablecharfield.widgets import NullableTextWidget

class CharNullField(models.CharField):
    description = _("String (up to %(max_length)s)")

    def get_internal_type(self):
        return "CharField"

    def formfield(self, **kwargs):
        if 'form_class' not in kwargs or kwargs['form_class'] is None:
            kwargs['form_class'] = CharNullFieldForm
        defaults = {'null': self.null}
        defaults.update(kwargs)
        defaults['widget'] = NullableTextWidget
        return super(CharNullField, self).formfield(**defaults)
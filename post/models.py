from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.


class Post(TranslatableModel):
    translations = TranslatedFields(title=models.CharField(_('title'), max_length=300),
                                    description=models.TextField(),
                                    created_at=models.DateTimeField(auto_now=True))

    def __str__(self) -> str:
        return self.title

from django.db.models.signals import post_save, pre_delete
from django.db.models import FileField
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

from .models import MediaUserModel


def media_connection_make(**kwargs):
    instance = kwargs['instance']
    owner_field = getattr(instance, 'OWNER', None)
    relative_instance = instance

    if owner_field:
        for relation in owner_field.split('.'):
            relative_instance = getattr(relative_instance, relation)

        owner = relative_instance

        for field in instance._meta.fields:
            if isinstance(field, FileField):
                value = str(field.value_from_object(instance))
                content_type = ContentType.objects.get_for_model(instance)

                if kwargs['created']:
                    MediaUserModel.objects.create(user=owner, content_type=content_type,
                                                    instance=instance.id, field=field.name, media_path=value)
                else:
                    object = MediaUserModel.objects.get(user=owner, content_type=content_type,
                                                        instance=instance.id, field=field.name)
                    object.media_path = value
                    object.save()


def media_connection_delete(*args, **kwargs):
    instance = kwargs['instance']
    owner_field = getattr(instance, 'OWNER', None)

    if owner_field:
        owner = getattr(instance, owner_field)

        for field in instance._meta.fields:
            if isinstance(field, FileField):
                content_type = ContentType.objects.get_for_model(instance)

                object = MediaUserModel.objects.get(user=owner, content_type=content_type,
                                                    instance=instance.id, field=field.name)
                object.delete()


for sender in settings.MEDIA_SECURITY_MODEL:
    post_save.connect(media_connection_make, sender)
    pre_delete.connect(media_connection_delete, sender)

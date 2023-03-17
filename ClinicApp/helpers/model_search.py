from django.db.models import Model

def get_or_none(model: Model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return None

def filter_or_none(model: Model, *args, **kwargs):
    try:
        return model.objects.filter(*args, **kwargs)
    except model.DoesNotExist:
        return None
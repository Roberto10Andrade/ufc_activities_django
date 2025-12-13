from django.db import migrations


def update_status_values(apps, schema_editor):
    """Atualiza os status antigos para os novos valores"""
    Activity = apps.get_model('activities', 'Activity')
    
    # Mapeia os status antigos para os novos
    status_mapping = {
        'ACTIVE': 'IN_PROGRESS',
        'UPCOMING': 'PENDING',
    }
    
    for old_status, new_status in status_mapping.items():
        Activity.objects.filter(status=old_status).update(status=new_status)


def reverse_status_values(apps, schema_editor):
    """Reverte os status para os valores antigos"""
    Activity = apps.get_model('activities', 'Activity')
    
    status_mapping = {
        'IN_PROGRESS': 'ACTIVE',
        'PENDING': 'UPCOMING',
    }
    
    for old_status, new_status in status_mapping.items():
        Activity.objects.filter(status=old_status).update(status=new_status)


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_activity_image_url_alter_activity_coordinator_and_more'),
    ]

    operations = [
        migrations.RunPython(update_status_values, reverse_status_values),
    ]

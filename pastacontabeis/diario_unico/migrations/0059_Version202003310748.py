# Generated by Django 2.2.5 on 2020-01-06 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diario_unico', '0058_Version202001241148'),
    ]

    operations = [
        migrations.RunSQL("""ALTER TABLE diario_unico ADD rubrica_esocial varchar(36) NULL;""",  ""  # Aqui ficaria o SQL para reverter a migration
                          )



    ]

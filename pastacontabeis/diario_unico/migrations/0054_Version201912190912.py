# Generated by Django 2.2.5 on 2020-01-06 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diario_unico', '0053_Version201912181638'),
    ]

    operations = [
        migrations.RunSQL("""ALTER TABLE info_cobranca DROP COLUMN situacao;""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),
        migrations.RunSQL("""ALTER TABLE info_pagamento DROP COLUMN situacao;""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),
        migrations.RunSQL("""ALTER TABLE info_pagamento ADD situacao varchar(40) NULL;""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),
        migrations.RunSQL("""ALTER TABLE info_cobranca ADD situacao varchar(40) NULL;""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),
    ]

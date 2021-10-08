# Generated by Django 2.2.5 on 2020-01-06 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diario_unico', '0016_Version201907160738'),
    ]

    operations = [
        migrations.RunSQL("""
                alter table documento_fiscal rename to documento;
             """,  ""  # Aqui ficaria o SQL para reverter a migration
                          ),

        migrations.RunSQL("""
                alter table documento add column documento varchar(36) not null default '';
             """,  ""  # Aqui ficaria o SQL para reverter a migration
                          ),

        migrations.RunSQL("""
               update documento set documento=documento_fiscal;
             """,  ""  # Aqui ficaria o SQL para reverter a migration
                          ),


        migrations.RunSQL("""
                alter online table documento modify column documento varchar(36) not null;
             """,  ""  # Aqui ficaria o SQL para reverter a migration
                          ),

        migrations.RunSQL("""
                alter table documento drop column documento_fiscal;
             """,  ""  # Aqui ficaria o SQL para reverter a migration
                          ),
    ]

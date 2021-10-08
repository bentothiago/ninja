# Generated by Django 2.2.5 on 2020-01-06 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diario_unico', '0033_Version201908210847'),
    ]

    operations = [
        migrations.RunSQL("""
        insert into pessoas
        (pessoa, cpf_cnpj, codigo, 
        descricao, nomefantasia, email, 
        tenant, telefone, indice_contabil)
        values ('e226b89e-60f3-402d-b0c0-8074490b604d','40418600082', 'apt_1001', 
                'Apartamento 1001', 'Apartamento 1001', 'joaomachado@com.br',
                47, '22998227981', 1);""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),

        migrations.RunSQL("""
        insert into pessoas
        (pessoa, cpf_cnpj, codigo, 
        descricao, nomefantasia, email, 
        tenant, telefone, indice_contabil)
        values ('7f0f1ba2-56f4-4210-b9b6-219467f07173','18413642078', 'apt_1002', 
                'Apartamento 1002', 'Apartamento 1002', 'sergiosilva@com.br',
                47, '22998227982', 2);""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),

        migrations.RunSQL("""
        insert into pessoas
        (pessoa, cpf_cnpj, codigo, 
        descricao, nomefantasia, email, 
        tenant, telefone, indice_contabil)
        values ('4acecb0c-c867-43ec-bbec-12808dfff231','95392069010', 'apt_1003', 
                'Apartamento 1003', 'Apartamento 1003', 'carlosbenevides@com.br',
                47, '22998227983', 3);""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),


        migrations.RunSQL("""
        insert into pessoas
        (pessoa, cpf_cnpj, codigo, 
        descricao, nomefantasia, email, 
        tenant, telefone, indice_contabil)
        values ('3e5bda63-1b17-47a0-be51-842539357ebe','31942117060', 'apt_1004', 
                'Apartamento 1004', 'Apartamento 1004', 'joaomachado@com.br',
                47, '22998227984', 4);	""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),

        migrations.RunSQL("""
        insert into pessoas
        (pessoa, cpf_cnpj, codigo, 
        descricao, nomefantasia, email, 
        tenant, telefone, indice_contabil)
        values ('e323f2e3-cfe9-47d1-a916-0daa8b28f85b','36637320021', 'apt_1005', 
                'Apartamento 1005', 'Apartamento 1005', 'joaomachado@com.br',
                47, '22998227985', 5);	""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),
    ]

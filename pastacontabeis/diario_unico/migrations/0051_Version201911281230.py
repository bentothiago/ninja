# Generated by Django 2.2.5 on 2020-01-06 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diario_unico', '0050_Version201911251128'),
    ]

    operations = [
        migrations.RunSQL("""insert into conta_contabil (conta_contabil,
            plano_contas,
            conta_contabil_pai,
            codigo,
            nome,
            grupo,
            natureza,
            inicio_vigencia,
            fim_vigencia,
            tenant)
        values (
            'dd3cd049-4ddd-139d-671ed1879c9780b6',
            'CONDOMINIO',
            '9cf11374-59c7-4e26-a4fc-85b533753fda',
            '2.1.2.02.0005',
            'PIS RETIDO A RECOLHER',
            2,
            'C',
            2019,
            null,
            47	
        );""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),


        migrations.RunSQL("""insert into conta_contabil (conta_contabil,
            plano_contas,
            conta_contabil_pai,
            codigo,
            nome,
            grupo,
            natureza,
            inicio_vigencia,
            fim_vigencia,
            tenant)
        values (
            'c6c6d9b8-797f-4610-82ad-ab9110ca4a44',
            'CONDOMINIO',
            '9cf11374-59c7-4e26-a4fc-85b533753fda',
            '2.1.2.02.0006',
            'COFINS RETIDO A RECOLHER',
            2,
            'C',
            2019,
            null,
            47	
        );""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),


        migrations.RunSQL("""insert into conta_contabil (conta_contabil,
            plano_contas,
            conta_contabil_pai,
            codigo,
            nome,
            grupo,
            natureza,
            inicio_vigencia,
            fim_vigencia,
            tenant)
        values (
            'c769fd45-feed-4ef2-9835-9db576c6e7bb',
            'CONDOMINIO',
            '9cf11374-59c7-4e26-a4fc-85b533753fda',
            '2.1.2.02.0007',
            'CSLL RETIDO A RECOLHER',
            2,
            'C',
            2019,
            null,
            47	
        );""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),


        migrations.RunSQL("""insert into conta_contabil (conta_contabil,
            plano_contas,
            conta_contabil_pai,
            codigo,
            nome,
            grupo,
            natureza,
            inicio_vigencia,
            fim_vigencia,
            tenant)
        values (
            '8a03bb6b-c162-4e96-bb5a-1f4f42c3a311',
            'CONDOMINIO',
            '9cf11374-59c7-4e26-a4fc-85b533753fda',
            '2.1.2.02.0008',
            'ISS RETIDO A RECOLHER',
            2,
            'C',
            2019,
            null,
            47	
        );""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),



        migrations.RunSQL("""insert into conta_contabil (conta_contabil,
            plano_contas,
            conta_contabil_pai,
            codigo,
            nome,
            grupo,
            natureza,
            inicio_vigencia,
            fim_vigencia,
            tenant)
        values (
            '82618df2-e28a-4e97-b2d3-115e3c020c13',
            'CONDOMINIO',
            '9cf11374-59c7-4e26-a4fc-85b533753fda',
            '2.1.2.02.0009',
            'ICMS RETIDO A RECOLHER',
            2,
            'C',
            2019,
            null,
            47	
        );""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),



        migrations.RunSQL("""insert into pessoas (pessoa, cpf_cnpj, codigo, descricao, nomefantasia, email, site, tenant, telefone,
        indice_contabil, ativo_fornecedor)        
        values ('0441d0be-2c75-a955-31b0ba704c6de2bd', 'GOVERNO', 
                            'GOVERNO', 'GOVERNO', 'GOVERNO', null, null, 47, null,
        99, 1);""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),
    ]

# Generated by Django 2.2.5 on 2020-01-06 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diario_unico', '0026_Version201908081345'),
    ]

    operations = [
        migrations.RunSQL("""update conta_contabil set tenant=47;""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),
        migrations.RunSQL("""update contas_personalizadas set tenant=47;""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),
        migrations.RunSQL("""update contas_personalizadas_cache set tenant=47;""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),
        migrations.RunSQL("""update definicoes_lancamentos set tenant=47;""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),
        migrations.RunSQL("""update diario_unico set tenant=47;""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),
        migrations.RunSQL("""update documento set tenant=47;""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),
        migrations.RunSQL("""update documento set tenant=47;""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),
        migrations.RunSQL("""update estabelecimentos set tenant=47;""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),
        migrations.RunSQL("""update info_cobranca set tenant=47;""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),
        migrations.RunSQL("""update info_fiscal_mercadoria set tenant=47;""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),
        migrations.RunSQL("""update info_fiscal_mercadoria set tenant=47;""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),
        migrations.RunSQL("""update info_pagamento set tenant=47;""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),
        migrations.RunSQL("""update lancamento_numero set tenant=47;""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),
        migrations.RunSQL("""update lancamento_numero set tenant=47;""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),
        migrations.RunSQL("""update pessoas set tenant=47;""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),
        migrations.RunSQL("""update tenants set tenant=47;""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),

        migrations.RunSQL("""INSERT INTO pessoas (pessoa, cpf_cnpj, codigo, descricao, nomefantasia, email, site, tenant, telefone) VALUES('63f7d155-ce46-492e-9aea-9bf7b5bb42ed', '95987000033', '33352394000104', 'CONDOMINO', 'Condomino de exemplo', 'sergiosilva@com.br', '', 47, '08002821195');""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),

        migrations.RunSQL("""update pessoas set codigo='20' where descricao='HOMOLOGACAO';""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),
    ]

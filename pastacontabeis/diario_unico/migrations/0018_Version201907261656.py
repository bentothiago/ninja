# Generated by Django 2.2.5 on 2020-01-06 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diario_unico', '0017_Version201907191607'),
    ]

    operations = [
        migrations.RunSQL("""
                insert into definicoes_lancamentos(definicao_lancamento,
                                            evento,
                                            numero,
                                            natureza,
                                            ordem,
                                            conta,
                                            historico,
                                            formula,
                                            diario_subtipo,
                                            plano_contas)
                values ('23dcdb37-b66c-47f4-b94d-c2709c3e1028',
                        'APROPRIACAO_COTA_CONDOMINIAL',
                        1,
                        'D',
                        1,
                        '1.1.2.01',
                        'Cotas condominiais a receber',
                        'valor',
                        1,
                        'CONDOMINIO');
                 """,  ""  # Aqui ficaria o SQL para reverter a migration
                          ),


        migrations.RunSQL("""
                insert into definicoes_lancamentos(definicao_lancamento,
                                            evento,
                                            numero,
                                            natureza,
                                            ordem,
                                            conta,
                                            historico,
                                            formula,
                                            diario_subtipo,
                                            plano_contas)
                values ('5161dd41-9153-4c72-8f55-d5021a8f0596',
                        'APROPRIACAO_COTA_CONDOMINIAL',
                        1,
                        'C',
                        2,
                        '3.1.1.01',
                        'Receita de cotas condominiais',
                        'valor',
                        1,
                        'CONDOMINIO');
                 """,  ""  # Aqui ficaria o SQL para reverter a migration
                          ),

    ]

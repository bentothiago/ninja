# Generated by Django 2.2.5 on 2020-01-03 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diario_unico', '0004_Version201907041847'),
    ]

    operations = [

        migrations.RunSQL("""
                CREATE TABLE pessoas
                (
                    pessoa character varying(36),
                    cpf_cnpj character varying(14),
                    codigo character varying(30) NOT NULL,
                    descricao character varying(150),
                    nomefantasia character varying(150),
                    email character varying(100),
                    site character varying(100),
                    tenant bigint,
                    telefone character varying(20)
                );""",  ""  # Aqui ficaria o SQL para reverter a migration
                          ),

        migrations.RunSQL("""
                CREATE TABLE enderecos(
                    cidade character varying(60),
                    bairro character varying(60),
                    cep character varying(8),
                    tipologradouro character varying(10),
                    logradouro character varying(150),
                    numero character varying(10),
                    complemento character varying(60),
                    pessoa character varying(36) not null
                );
            """,  ""  # Aqui ficaria o SQL para reverter a migration
                          ),

        migrations.RunSQL("""
                CREATE TABLE estabelecimentos
                (
                    pessoa character varying(36),
                    inscricaoestadual character varying(20),
                    inscricaomunicipal character varying(20),
                    inicio_atividades date,
                    final_atividades date,
                    cnae character varying(7),
                    empresa character varying(36),
                    codigo_municipio int,
                    tenant int
                );
            """,  ""  # Aqui ficaria o SQL para reverter a migration
                          ),

        migrations.RunSQL("""
                CREATE TABLE tenants
                (
                    tenant int NOT NULL,
                    nome character varying(200),
                    codigo character varying(30)
                );
            """,  ""  # Aqui ficaria o SQL para reverter a migration
                          ),

        migrations.RunSQL("""
                CREATE TABLE usuarios
                (
                    nome character varying(60),
                    email character varying(100),
                    login character varying(100)                                                                                                   
                );
            """,  ""  # Aqui ficaria o SQL para reverter a migration
                          ),

        migrations.RunSQL("""
                insert into pessoas (pessoa ,
                            cpf_cnpj,
                            codigo,
                            descricao,                            
                            nomefantasia,
                            email,
                            site,
                            tenant,
                            telefone)
                values( 'da850bff-b54d-41c9-89f5-91ba9a5752c5',
                '33352394000104',
                '33352394000104',
                'CEDAE',
                'CEDAE',
                'comunicacao@cedae.com.br',
                'www.cedae.com.br',
                10,
                '08002821195');
                            """,  ""  # Aqui ficaria o SQL para reverter a migration
                          ),

        migrations.RunSQL("""
                    insert into pessoas (pessoa ,
                                cpf_cnpj,
                                codigo,
                                descricao,                            
                                nomefantasia,
                                email,
                                site,
                                tenant,
                                telefone)
                    values( 'fa2c2eb2-1506-4f76-b22c-08fa7a4529b0',
                    '07523555000167',
                    '07523555000167',
                    'ENEL',
                    'ENEL',
                    'vmateus@ampla.com',
                    'www.enel.com.br',
                    10,
                    '08002800120');
            """,  ""  # Aqui ficaria o SQL para reverter a migration
                          ),

        migrations.RunSQL("""
                    insert into pessoas (pessoa ,
                                cpf_cnpj,
                                codigo,
                                descricao,                            
                                nomefantasia,
                                email,
                                site,
                                tenant,
                                telefone)
                    values( '9f716268-63a1-4f19-ba66-30b139230203',
                    '60444437000146',
                    '60444437000146',
                    'LIGHT',
                    'LIGHT',
                    'ouvidoria@light.com.br',
                    'www.light.com.br',
                    10,
                    '08002840182');
            """,  ""  # Aqui ficaria o SQL para reverter a migration
                          ),

        migrations.RunSQL("""
                    insert into pessoas (pessoa ,
                                cpf_cnpj,
                                codigo,
                                descricao,                            
                                nomefantasia,
                                email,
                                site,
                                tenant,
                                telefone)
                    values( '8839a39b-14f5-4307-9ff2-893fda7e6822',
                    '33938119000169',
                    '33938119000169',
                    'NATURGY',
                    'NATURGY',
                    'sac@naturgy.com',
                    'www.naturgy.com.br',
                    10,
                    '08000240197');
            """,  ""  # Aqui ficaria o SQL para reverter a migration
                          ),

        migrations.RunSQL("""
                    insert into pessoas (pessoa ,
                                cpf_cnpj,
                                codigo,
                                descricao,                            
                                nomefantasia,  
                                email,
                                site,
                                tenant,
                                telefone)
                    values( '60375e29-5a64-4709-ab64-8435b38bfa6a',
                    '34216873000158',
                    'HOMOLOGACAO',
                    'HOMOLOGACAO',
                    'CEDAE',
                    'sergiosilva@com.br',
                    'www.com.br',
                    10,
                    '226146151864');
            """,  ""  # Aqui ficaria o SQL para reverter a migration
                          ),

        migrations.RunSQL("""
                    insert into estabelecimentos (
                                    pessoa,
                                    inscricaoestadual,
                                    inscricaomunicipal,
                                    inicio_atividades,
                                    final_atividades,
                                    cnae,
                                    empresa,
                                    codigo_municipio,  
                                    tenant)
                    values( 'da850bff-b54d-41c9-89f5-91ba9a5752c5',
                    '00001',
                    '00001',
                    '2000/01/01',
                    null,
                    '05',
                    null,
                    12345,
                    10);
            """,  ""  # Aqui ficaria o SQL para reverter a migration
                          ),

        migrations.RunSQL("""
                insert into tenants (
                                        tenant,
                                            nome ,
                                            codigo)
                values( 10,
                        'HOMOLOGACAO',
                        'HOMOLOGACAO');
            """,  ""  # Aqui ficaria o SQL para reverter a migration
                          ),

        migrations.RunSQL("""
                insert into usuarios (
                                            nome,
                                            email,
                                            login)
                values( 'HOMOLOGACAO',
                        'HOMOLOGACAO',
                        'HOMOLOGACAO');
            """,  ""  # Aqui ficaria o SQL para reverter a migration
                          ),
    ]

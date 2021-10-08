# Generated by Django 2.2.5 on 2020-02-18 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_VersionFaturamento201909041635'),
    ]

    operations = [
        # faturamento.regua_cobranca
        migrations.RunSQL("""
      insert into faturamento.regua_cobranca (
        regua_cobranca,	codigo,
        descricao, tenant, padrao
      ) values (
        'c9e183a9-eaae-42a5-8c15-db3051503a22', 'COBRANCA_COTAS',
        'Controle de inadimpl�ncia para a cobran�a de cotas condominiais.', 47, true
      );
    """, ""),

        # Etapas da r�gua de cobran�a
        migrations.RunSQL("""
      insert into faturamento.regua_cobranca_etapa(
        regua_cobranca_etapa,
        regua_cobranca,
        descricao,
        template_email,
        prazo,
        tenant,
        apos_vencimento
      ) values(
        '99665a5c-da4f-46c2-b7ed-f7fc442e8713',
        'c9e183a9-eaae-42a5-8c15-db3051503a22',
        'Lembrete da cota condominial',
        'Prezado cliente, sua cota condominial, no valor de R$ {valor}, estar� vencendo no dia {vencimento}.<br><br>Por favor, desconsidere esta mensagem, caso j� tenha efetuado o pagamento.',
        7,
        47,
        false
      );
    """, ""),

        migrations.RunSQL("""
      insert into faturamento.regua_cobranca_etapa (
        regua_cobranca_etapa,
        regua_cobranca,
        descricao,
        template_email,
        prazo,
        tenant,
        apos_vencimento
      ) values (
        '09f1191f-6956-4391-a877-c853013364d0',
        'c9e183a9-eaae-42a5-8c15-db3051503a22',
        'Lembrete de atraso da cota condominial',
        'Prezado cliente, sua cota condominial no valor de R$ {valor} venceu no dia {vencimento}. Por favor, entre em contato para regularizar esta pend�ncia.<br><br>Obs.: Favor desconsiderar esta mensagem caso j� tenha efetuado o pagamento.',
        7,
        47,
        true
      );
    """, ""),

        migrations.RunSQL("""
      insert into faturamento.regua_cobranca_etapa(
        regua_cobranca_etapa,
        regua_cobranca,
        descricao,
        template_email,
        prazo,
        tenant,
        apos_vencimento
      ) values(
        '8a70f578-1dae-4382-91f0-ddc1ed26e689',
        'c9e183a9-eaae-42a5-8c15-db3051503a22',
        'Aviso de cobran�a administrativa da cota condominial',
        'Prezado cliente, sua cota condominial est� em aberto h� 15 dias, e estar�o sendo iniciadas tratativas administrativas de cobran�a. Por favor, entre em contato para regularizar esta pend�ncia.<br><br>Obs.: Favor desconsiderar esta mensagem caso j� tenha efetuado o pagamento.',
        15,
        47,
        true
      );
    """, ""),

        migrations.RunSQL("""
      insert into faturamento.regua_cobranca_etapa (
        regua_cobranca_etapa,
        regua_cobranca,
        descricao,
        template_email,
        prazo,
        tenant,
        apos_vencimento
      ) values (
        '5aba0b73-a068-4d28-825b-6ec06c2013d3',
        'c9e183a9-eaae-42a5-8c15-db3051503a22',
        'Aviso de cobran�a judicial da cota condominial',
        'Prezado cliente, sua cota condominial est� em aberto h� 30 dias, e estar�o sendo iniciadas tratativas judiciais de cobran�a. Por favor, entre em contato para regularizar esta pend�ncia.<br><br>Obs.: Favor desconsiderar esta mensagem caso j� tenha efetuado o pagamento.',
        30,
        47,
        true
      );    
    """, ""),
    ]

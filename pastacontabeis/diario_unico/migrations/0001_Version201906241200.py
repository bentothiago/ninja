# Generated by Django 2.2.5 on 2020-01-03 14:42

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE TABLE documento_fiscal (
                documento_fiscal VARCHAR(36) NOT NULL,
                tipo int,
                numero varchar(16),
                ano int,
                sinal int,
                modelo varchar(9),
                data_lancamento date,
                emissao date,
                competencia_inicial date,
                competencia_final date,
                cfop varchar(9),
                situacao int,
                valor numeric(16,4),
                data_entrada date,
                tipo_ligacao int,
                origem int,
                codigo_consumo int,
                serie varchar(9),
                subserie varchar(9),
                grupo_tensao varchar(9),
                estabelecimento VARCHAR(36),
                empresa VARCHAR(36),
                grupo_empresarial VARCHAR(36),
                participante VARCHAR(36),
                usuario VARCHAR(36),
                codigo_barras varchar(100),
                tenant integer not null	
            )
            ENGINE=InnoDB;
            """,
            ""  # Aqui ficaria o SQL para reverter a migration
        ),
        migrations.RunSQL(
            """
            CREATE TABLE info_fiscal_mercadoria (
                info_fiscal_mercadoria VARCHAR(36) NOT NULL,
                valor_unitario NUMERIC(20,6) NULL,
                unidade varchar(6) NULL,
                tiposoma INTEGER NULL,
                classe INTEGER NULL,
                tiporec INTEGER NULL,
                ignorasoma bool NULL,
                vinculoreceita INTEGER NULL,
                semmov BOOL NULL,
                quantidade numeric(20,4) NULL,
                desc_nao_trib numeric(15,2) NULL,
                lote varchar(20) NULL,
                quantidade_lote numeric(15,2) NULL,
                fabricacao DATE NULL,
                validade date NULL,
                preco_max numeric(15,2) NULL,
                remas INTEGER NULL,
                tanque integer NULL,
                bico integer NULL,
                cide numeric(15,2) NULL,
                basecide numeric(15,2) NULL,
                valorcide numeric(15,2) NULL,
                valoriof numeric(15,2) NULL,
                pesoliq numeric(15,2) NULL,
                pesobruto numeric(15,2) NULL,
                capacidade numeric(15,2) NULL,
                volumes integer NULL,
                impexp numeric(15,2) NULL,
                valorimpexp numeric(15,2) NULL,
                acdraw varchar(20) NULL,
                cst_icms varchar(2) NULL,
                cstosn varchar(3) NULL,
                icmsorigem numeric(15,2) NULL,
                icmsdestino numeric(15,2) NULL,
                encargosicms numeric(15,4) NULL,
                reducaoicms numeric(15,4) NULL,
                baseicms numeric(15,2) NULL,
                diferencial numeric(15,2) NULL,
                antecipacao numeric(15,2) NULL,
                icmsdiferido numeric(15,2) NULL,
                abatimentoicms numeric(15,2) NULL,
                valorciap numeric(15,2) NULL,
                mesesciap integer NULL,
                tipoipi integer NULL,
                tiposomaipi integer NULL,
                ipi numeric(15,2) NULL,
                reducaoipi numeric(15,2) NULL,
                encargosipi numeric(15,2) NULL,
                baseipi numeric(15,2) NULL,
                abatimentoipi numeric(15,2) NULL,
                seloipi varchar(20) NULL,
                lacreipi varchar(20) NULL,
                lucro numeric(15,2) NULL,
                tipost integer NULL,
                reducaost numeric(15,4) NULL,
                basestfixa numeric(15,2) NULL,
                basesubst numeric(15,2) NULL,
                substnaoretida numeric(15,2) NULL,
                substobs numeric(15,2) NULL,
                tipo_pc integer NULL,
                pisimp numeric(15,4) NULL,
                cofinsimp numeric(15,4) NULL,
                basepisimp numeric(15,2) NULL,
                basecofinsimp numeric(15,2) NULL,
                basestpis numeric(15,2) NULL,
                basestcofins numeric(15,2) NULL,
                valorstpis numeric(15,2) NULL,
                valorstcofins numeric(15,2) NULL,
                ordem bigint NULL,
                documento varchar(36) NULL,
                item varchar(36) NULL,
                proprietario varchar(36) NULL,
                receptor varchar(36) NULL,
                obra varchar(36) NULL,
                tipo_linha integer NULL,
                linha varchar(36) NULL,
                vendedor varchar(36) NULL,
                ipienquadramentocodigo varchar(10) NULL,
                ipienquadramentodescricao text NULL,
                cest varchar(7) NULL,
                valorpercentualfcpicmsdestino numeric(15,2) NULL,
                valoraliquotainternaicmsdestino numeric(15,2) NULL,
                valorpercentualpartilhaicmsdestino numeric(15,2) NULL,
                valorpercentualicmsinter numeric(15,2) NULL,
                situacaogerencial integer NULL,
                valordebitopis numeric(15,2) NULL,
                valordebitocofins numeric(15,2) NULL,
                local_estoque varchar(36) NULL,
                linha_pendente bool NULL,
                custo_total numeric(15,6) NULL,
                percentualfatorcomissao numeric(15,6) NULL,
                percentualcomissao numeric(15,6) NULL,
                pfcp numeric(15,2) NULL,
                vfcp numeric(15,2) NULL,
                vbcfcp numeric(15,2) NULL,
                vbcfcpst numeric(15,2) NULL,
                pfcpst numeric(15,2) NULL,
                vfcpst numeric(15,2) NULL,
                pfcpstret numeric(15,2) NULL,
                vfcpstret numeric(15,2) NULL,
                vbcfcpufdest numeric(15,2) NULL,
                vbcfcpstret numeric(15,2) NULL,
                pst numeric(15,2) NULL,
                tenant INTEGER not null
            )
            ENGINE=InnoDB;
            """,
            ""  # Aqui ficaria o SQL para reverter a migration
        ),
        migrations.RunSQL(
            """
            CREATE TABLE info_fiscal_servico (
                info_fiscal_servico VARCHAR(36) NOT NULL,
                valor_unitario numeric(15,5) NULL,
                quantidade numeric(15,4) NULL,
                remas integer NULL,
                ordem bigint NULL,
                documento varchar(36) NULL,
                obra varchar(36) NULL,
                valorfcpicmsdestino numeric(15,2) NULL,
                valoricmsdestino numeric(15,2) NULL,
                valoricmsinterestadualorigem numeric(15,2) NULL,
                vakirdebitopis numeric(15,2) NULL,
                valordebitocofins numeric(15,2) NULL,
                incideirrf bool NULL,
                incideinss bool NULL,
                tipo_servico integer NULL,
                rapis integer NULL,
                deducao numeric(15,2) NULL,
                vlrservicos15 numeric(15,2) NULL,
                vlwservicos20 numeric(15,2) NULL,
                vlwservicos25 numeric(15,2) NULL,
                valorinssadicional numeric(15,2) NULL,
                valorinssnaoretido numeric(15,2) NULL,
                nota_deducao varchar(36) NULL,
                servico varchar(36) NULL,
                vencimento datetime NULL,
                inicioreferencia datetime NULL,
                fimreferencia datetime NULL,
                diasvencimento integer NULL,
                titulo_servico varchar(36) NULL,
                item_contrato_servico varchar(36) NULL,
                participante varchar(36) NULL,
                contrato varchar(36) NULL,
                processamentocontrato varchar(36) NULL,
                tipocobranca integer NULL,
                parcela integer NULL,
                totalparcelas integer NULL,
                objetoservico varchar(36) NULL,
                base_iss numeric(15,2) NULL,
                base_inss numeric(15,2) NULL,
                base_irrf numeric(15,2) NULL,
                base_pis numeric(15,2) NULL,
                base_csll numeric(15,2) NULL,
                retem_iss bool NULL,
                retem_inss bool NULL,
                retem_irrf bool NULL,
                retem_cofins bool NULL,
                retem_pis bool NULL,
                retem_csll bool NULL,
                emissao datetime NULL,
                valor_pis numeric(15,2) NULL,
                valor_cofins numeric(15,2) NULL,
                id_origem varchar(36) NULL,
                datareajusteitemcontrato date NULL,
                valortotalocorrenciasitemcontrato numeric(15,2) NULL,
                aliquota_iss numeric(15,2) NULL,
                aliquota_inss numeric(15,2) NULL,
                aliquota_ir numeric(15,2) NULL,
                aliquota_pis numeric(15,2) NULL,
                aliquota_cofins numeric(15,2) NULL,
                aliquota_csll numeric(15,2) NULL,
                percentual_incidencia_inss numeric(15,2) NULL,
                reducao_base_iss numeric(15,2) NULL,
                unitario_variavel numeric(15,8) NULL,
                tenant INTEGER not null
            )
            ENGINE=InnoDB;
            """,
            ""  # Aqui ficaria o SQL para reverter a migration
        ),
        migrations.RunSQL(
            """
            CREATE TABLE diario_universal (
                diario_universal VARCHAR(36) NOT null,
                documento varchar(36) null,
                diario_universal_tipo INTEGER NOT NULL,
                diario_universal_subtipo INTEGER NOT NULL,
                indice_item INTEGER null,
                cancela_linha_diario_universal BOOLEAN null,
                estabelecimento varchar(36) NULL,
                empresa varchar(36) NULL,
                participante varchar(36) NULL,
                grupo_empresarial varchar(36) NULL,
                usuario varchar(36) null,
                modulo INTEGER NULL,
                conta_financeira varchar(36) NULL,
                forma_pagamento varchar(36) NULL,
                projeto varchar(36) NULL,
                renegociacao varchar(36) NULL,
                item varchar(36) NULL,
                pedido varchar(36) NULL,
                tipo_forma_pagamento INTEGER NULL,
                sinal INTEGER NULL,
                origem INTEGER NULL,
                base NUMERIC(15,2) NULL,
                percentagem_sobre_base NUMERIC NULL,
                descricao varchar(200) NULL,
                situacao INTEGER NULL,
                codigo varchar(100) NULL,
                cancelado BOOL NULL,
                valor_total_sem_rateio NUMERIC(15,2) NULL,
                codigo_barras varchar(100) NULL,
                url_documento varchar(300) NULL,
                valor NUMERIC NULL,
                data DATE NULL,
                natureza_lancamento varchar(2) NULL,
                lote_contabil varchar(36) NULL,
                ordem_lancamento BIGINT NULL,
                historico_lancamento TEXT NULL,
                numero_lancamento BIGINT NULL,
                indicador_lancamento_contabil BOOL NULL,
                definicao_lancamento TEXT NULL,
                centro_custo varchar(36) NULL,
                conta_contabil varchar(36) NULL,
                semana INTEGER NULL,
                tipo_calculo varchar(10) NULL,
                avos_ferias INTEGER NULL,
                rubrica varchar(36) NULL,
                movimento varchar(36) NULL,
                trabalhador varchar(36) NULL,
                lotacao varchar(36) NULL,
                departamento varchar(36) NULL,
                tenant INTEGER not null,
                item_documento varchar(36) NULL
            )
            ENGINE=Columnstore;
            """,
            ""  # Aqui ficaria o SQL para reverter a migration
        ),
        migrations.RunSQL(
            """
            CREATE TABLE lancamento_numero (
                estabelecimento varchar(36),
                ano integer,
                numero integer,
                tenant integer not null
            );
            """,
            ""  # Aqui ficaria o SQL para reverter a migration
        )
    ]

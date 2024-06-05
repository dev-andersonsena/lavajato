# Generated by Django 4.2.11 on 2024-06-01 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0043_remove_agendamento_lavagem_adicional_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamento',
            name='lavagem_adicional',
            field=models.CharField(choices=[('LAVAGEM_TECNICA', 'LAVAGEM TÉCNICA'), ('LAVAGEM_TECNICA_M', 'LAVAGEM TÉCNICA MOTO'), ('LIMPEZA_DETALHADA', 'LIMPEZA DETALHADA'), ('LIMPEZA_DETALHADA_PROTECAO', 'LIMPEZA DETALHADA + PROTEÇÃO'), ('POLIMENTO_TECNICO_PROTECAO_6_M', 'POLIMENTO TECNICO + PROTEÇÃO DE 6 MESES'), ('POLIMENTO_TECNICO_M', 'POLIMENTO TECNICO MOTO'), ('LIMPEZA_CHASSI_DETALHADA', 'LIMPEZA CHASSI DETALHADA'), ('HIGIENIZAÇÃO_DE_BANCOS_COURO', 'HIGIENIZAÇÃO DE BANCOS COURO'), ('LIMPEZA_DE_MOTOR_COM_ENVENIZAMENTO', 'LIMPEZA DE MOTOR COM ENVENIZAMENTO'), ('DESCONTAMINAÇÃO', 'DESCONTAMINAÇÃO'), ('CERA_EM_PASTA', 'CERA EM PASTA'), ('REMOÇÃO_DE_CHUVA_ACIDA_E_VITRIFICAÇÃO_DO_PARABRIZA', 'REMOÇÃO DE CHUVA ACIDA E VITRIFICAÇÃO DO PARABRIZA'), ('POLIMENTO_TECNICO_VITRIFICAÇÃO', 'POLIMENTO TECNICO + VITRIFICAÇÃO DE PINTURA ( 1 ANO PROTEÇÃO )'), ('PACOTE_COMPLETO_VITRIFICAÇÃO', 'PACOTE COMPLETO VITRIFICAÇÃO COMPLETA'), ('VITRIFICAÇÃO_M', 'VITRIFICAÇÃO MOTO'), ('HIGIENIZAÇÃO_DE_BANCOS_TÉCNICO_5L', 'HIGIENIZAÇÃO DE BANCOS TÉCNICO'), ('HIGIENIZAÇÃO_DE_BANCOS_TÉCNICO_7L', 'HIGIENIZAÇÃO DE BANCOS TÉCNICO')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='agendamento',
            name='tipo_lavagem',
            field=models.CharField(choices=[('LAVAGEM_TECNICA', 'LAVAGEM TÉCNICA'), ('LAVAGEM_TECNICA_M', 'LAVAGEM TÉCNICA MOTO'), ('LIMPEZA_DETALHADA', 'LIMPEZA DETALHADA'), ('LIMPEZA_DETALHADA_PROTECAO', 'LIMPEZA DETALHADA + PROTEÇÃO'), ('POLIMENTO_TECNICO_PROTECAO_6_M', 'POLIMENTO TECNICO + PROTEÇÃO DE 6 MESES'), ('POLIMENTO_TECNICO_M', 'POLIMENTO TECNICO MOTO'), ('LIMPEZA_CHASSI_DETALHADA', 'LIMPEZA CHASSI DETALHADA'), ('HIGIENIZAÇÃO_DE_BANCOS_COURO', 'HIGIENIZAÇÃO DE BANCOS COURO'), ('LIMPEZA_DE_MOTOR_COM_ENVENIZAMENTO', 'LIMPEZA DE MOTOR COM ENVENIZAMENTO'), ('DESCONTAMINAÇÃO', 'DESCONTAMINAÇÃO'), ('CERA_EM_PASTA', 'CERA EM PASTA'), ('REMOÇÃO_DE_CHUVA_ACIDA_E_VITRIFICAÇÃO_DO_PARABRIZA', 'REMOÇÃO DE CHUVA ACIDA E VITRIFICAÇÃO DO PARABRIZA'), ('POLIMENTO_TECNICO_VITRIFICAÇÃO', 'POLIMENTO TECNICO + VITRIFICAÇÃO DE PINTURA ( 1 ANO PROTEÇÃO )'), ('PACOTE_COMPLETO_VITRIFICAÇÃO', 'PACOTE COMPLETO VITRIFICAÇÃO COMPLETA'), ('VITRIFICAÇÃO_M', 'VITRIFICAÇÃO MOTO'), ('HIGIENIZAÇÃO_DE_BANCOS_TÉCNICO_5L', 'HIGIENIZAÇÃO DE BANCOS TÉCNICO'), ('HIGIENIZAÇÃO_DE_BANCOS_TÉCNICO_7L', 'HIGIENIZAÇÃO DE BANCOS TÉCNICO')], default='', max_length=100),
        ),
    ]

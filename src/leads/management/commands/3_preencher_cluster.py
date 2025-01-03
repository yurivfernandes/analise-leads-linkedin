from django.core.management.base import BaseCommand

from leads.models import (
    Cargo,
    Cluster,
    Lead,
    Localizacao,
    Setor,
    TamanhoEmpresa,
)


class Command(BaseCommand):
    help = "Preenche a tabela Cluster associando IDs das dimensões conforme o nome na tabela Lead."

    def handle(self, *args, **options):
        for lead in Lead.objects.all():
            # Buscar o ID do cargo
            cargo = Cargo.objects.filter(descricao=lead.cargo).first()
            cargo_id = cargo.id if cargo else None

            # Buscar o ID do setor
            setor = Setor.objects.filter(descricao=lead.setor).first()
            setor_id = setor.id if setor else None

            # Buscar o ID da localização
            localizacao = Localizacao.objects.filter(
                descricao=lead.localizacao
            ).first()
            localizacao_id = localizacao.id if localizacao else None

            # Buscar o ID do tamanho da empresa
            tamanho_empresa = TamanhoEmpresa.objects.filter(
                descricao=lead.tamanho_empresa
            ).first()
            tamanho_empresa_id = (
                tamanho_empresa.id if tamanho_empresa else None
            )

            # Verificar se o registro já existe no Cluster
            cluster, created = Cluster.objects.update_or_create(
                lead=lead,
                defaults={
                    "cargo_id": cargo_id,
                    "setor_id": setor_id,
                    "localizacao_id": localizacao_id,
                    "tamanho_empresa_id": tamanho_empresa_id,
                },
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Registro criado para o lead: {lead.nome}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Registro atualizado para o lead: {lead.nome}"
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(
                "Processo de preenchimento da tabela Cluster concluído!"
            )
        )

from django.core.management.base import BaseCommand

from leads.models import Cargo, Lead, Localizacao, Setor, TamanhoEmpresa


class Command(BaseCommand):
    help = "Popula as tabelas de dimensão com base nos dados da tabela Lead"

    def handle(self, *args, **kwargs):
        self.populate_dimensions()

    def populate_dimensions(self):
        # Populating Setor dimension
        setores = Lead.objects.values_list("setor", flat=True).distinct()
        for setor in setores:
            if setor:
                Setor.objects.get_or_create(descricao=setor)

        # Populating Localizacao dimension
        localizacoes = Lead.objects.values_list(
            "localizacao", flat=True
        ).distinct()
        for localizacao in localizacoes:
            if localizacao:
                Localizacao.objects.get_or_create(descricao=localizacao)

        # Populating Cargo dimension
        cargos = Lead.objects.values_list("cargo", flat=True).distinct()
        for cargo in cargos:
            if cargo:
                Cargo.objects.get_or_create(descricao=cargo)

        # Populating TamanhoEmpresa dimension
        tamanhos_empresa = Lead.objects.values_list(
            "tamanho_empresa", flat=True
        ).distinct()
        for tamanho in tamanhos_empresa:
            if tamanho:
                TamanhoEmpresa.objects.get_or_create(descricao=tamanho)

        self.stdout.write(
            self.style.SUCCESS(
                "As tabelas de dimensão foram populadas com sucesso!"
            )
        )

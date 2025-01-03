import random

from django.core.management.base import BaseCommand
from faker import Faker

from leads.models import Lead


class Command(BaseCommand):
    help = "Gera dados fake para o modelo Lead"

    def add_arguments(self, parser):
        parser.add_argument(
            "quantidade",
            type=int,
            help="Quantidade de registros a serem gerados",
        )

    def handle(self, *args, **options):
        quantidade = options["quantidade"]
        faker = Faker("pt_BR")  # Gera dados em português
        tamanhos_empresa = ["Pequena", "Média", "Grande"]
        segmentacoes = ["Quente", "Morno", "Frio"]
        status_opcoes = ["Ativo", "Inativo", "Convertido", "Perdido"]

        leads = []
        for _ in range(quantidade):
            leads.append(
                Lead(
                    nome=faker.name(),
                    email=faker.email(),
                    telefone=faker.phone_number(),
                    cargo=faker.job(),
                    empresa=faker.company(),
                    localizacao=faker.city(),
                    linkedin_url=faker.url(),
                    setor=random.choice(
                        [
                            "Tecnologia",
                            "Saúde",
                            "Educação",
                            "Varejo",
                            "Serviços",
                        ]
                    ),
                    tamanho_empresa=random.choice(tamanhos_empresa),
                    cnae=str(random.randint(1000, 9999))
                    + "-"
                    + str(random.randint(0, 9)),
                    tempo_no_cargo=random.randint(1, 120),
                    habilidades=", ".join(faker.words(nb=5)),
                    origem=random.choice(
                        ["LinkedIn", "Evento", "Landing Page"]
                    ),
                    canal_aquisicao=random.choice(
                        ["E-mail", "Redes Sociais", "Indicação"]
                    ),
                    lead_score=random.randint(0, 100),
                    segmentacao=random.choice(segmentacoes),
                    etapa_funil=random.choice(
                        [
                            "Prospecção",
                            "Qualificação",
                            "Proposta",
                            "Fechamento",
                        ]
                    ),
                    valor_potencial=random.uniform(1000, 50000),
                    produtos_interesse=", ".join(faker.words(nb=3)),
                    status=random.choice(status_opcoes),
                    ultima_interacao=faker.date_between(
                        start_date="-1y", end_date="today"
                    ),
                )
            )

        Lead.objects.bulk_create(leads)

        self.stdout.write(
            self.style.SUCCESS(f"{quantidade} leads criados com sucesso!")
        )

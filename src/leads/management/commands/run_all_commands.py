from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Executa os comandos de geração de leads, popular dimensões e preencher cluster."

    def add_arguments(self, parser):
        parser.add_argument(
            "quantidade",
            nargs="?",
            type=int,
            default=1000,
            help="Quantidade de registros a serem gerados (padrão: 1000)",
        )

    def handle(self, *args, **options):
        quantidade = options["quantidade"]

        # Executa os comandos sequencialmente
        self.stdout.write(self.style.SUCCESS(f"Gerando {quantidade} leads..."))
        call_command("1_gerar_leads", quantidade)

        self.stdout.write(self.style.SUCCESS("Populando dimensões..."))
        call_command("2_popular_dimensoes")

        self.stdout.write(self.style.SUCCESS("Preenchendo cluster..."))
        call_command("3_preencher_cluster")

        self.stdout.write(
            self.style.SUCCESS(
                "Todos os comandos foram executados com sucesso!"
            )
        )

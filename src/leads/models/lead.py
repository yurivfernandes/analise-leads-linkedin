from django.db import models


class Lead(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    empresa = models.CharField(max_length=255, blank=True, null=True)
    localizacao = models.CharField(max_length=100, blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    setor = models.CharField(max_length=100, blank=True, null=True)
    tamanho_empresa = models.CharField(
        max_length=50,
        choices=[
            ("Pequena", "Pequena"),
            ("Média", "Média"),
            ("Grande", "Grande"),
        ],
        blank=True,
        null=True,
    )
    cnae = models.CharField(max_length=20, blank=True, null=True)
    tempo_no_cargo = models.PositiveIntegerField(
        blank=True, null=True, help_text="Em meses"
    )
    habilidades = models.TextField(blank=True, null=True)
    origem = models.CharField(max_length=100, blank=True, null=True)
    data_entrada = models.DateField(auto_now_add=True)
    canal_aquisicao = models.CharField(max_length=50, blank=True, null=True)
    lead_score = models.PositiveIntegerField(default=0)
    segmentacao = models.CharField(
        max_length=50,
        choices=[
            ("Quente", "Quente"),
            ("Morno", "Morno"),
            ("Frio", "Frio"),
        ],
        blank=True,
        null=True,
    )
    etapa_funil = models.CharField(max_length=50, blank=True, null=True)
    valor_potencial = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    produtos_interesse = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=50,
        choices=[
            ("Ativo", "Ativo"),
            ("Inativo", "Inativo"),
            ("Convertido", "Convertido"),
            ("Perdido", "Perdido"),
        ],
        blank=True,
        null=True,
    )
    ultima_interacao = models.DateField(blank=True, null=True)

    class Meta:
        db_table = "leads"
        verbose_name = "LinkedIn Leads"
        verbose_name_plural = "LinkedIn Leads"

    def _str_(self):
        return f"{self.nome} - {self.email}"

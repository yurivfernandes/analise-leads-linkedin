from django.db import models

from .dimensoes import Cargo, Localizacao, Setor, TamanhoEmpresa
from .lead import Lead


class Cluster(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    tamanho_empresa = models.ForeignKey(
        TamanhoEmpresa, on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Cluster"
        verbose_name_plural = "Clusters"

    def __str__(self):
        return f"Cluster: {self.lead.nome} - {self.setor.nome}"

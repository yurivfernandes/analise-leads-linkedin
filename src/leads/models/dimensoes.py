from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Setor(BaseModel):
    class Meta:
        db_table = "setor"
        verbose_name = "Setor"
        verbose_name_plural = "Setores"


class Localizacao(BaseModel):
    class Meta:
        db_table = "localizacao"
        verbose_name = "Localização"
        verbose_name_plural = "Localizações"


class Cargo(BaseModel):
    class Meta:
        db_table = "cargo"
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"


class TamanhoEmpresa(BaseModel):
    class Meta:
        db_table = "tamanho_empresa"
        verbose_name = "Tamanho da Empresa"
        verbose_name_plural = "Tamanhos das Empresas"

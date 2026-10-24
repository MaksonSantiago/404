from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    telefone = models.CharField("telefone", max_length=20, blank=True)

    def __str__(self):
        return self.get_full_name() or self.username


class Evento(models.Model):
    titulo = models.CharField("título", max_length=200)
    descricao = models.TextField("descrição da causa solidária")
    data_evento = models.DateTimeField("data e hora do evento")
    local = models.CharField("local", max_length=255)
    meta_arrecadacao = models.DecimalField(
        "meta de arrecadação", max_digits=12, decimal_places=2
    )
    valor_arrecadado = models.DecimalField(
        "valor arrecadado",
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    class Meta:
        ordering = ["data_evento", "titulo"]
        verbose_name = "evento"
        verbose_name_plural = "eventos"

    def __str__(self):
        return self.titulo


class Doacao(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="doacoes",
        verbose_name="usuário",
    )
    evento = models.ForeignKey(
        Evento,
        on_delete=models.CASCADE,
        related_name="doacoes",
        verbose_name="evento",
    )
    valor = models.DecimalField("valor doado", max_digits=12, decimal_places=2)
    data_doacao = models.DateTimeField("data da doação", auto_now_add=True)

    class Meta:
        ordering = ["-data_doacao"]
        verbose_name = "doação"
        verbose_name_plural = "doações"

    def __str__(self):
        return f"Doação de R$ {self.valor:.2f} para {self.evento} por {self.usuario}"
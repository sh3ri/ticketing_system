from django.db import models


class TicketNumGenerator(models.Model):
    ticket_num = models.IntegerField(default=1010)

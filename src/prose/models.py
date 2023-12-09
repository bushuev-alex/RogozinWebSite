from django.db import models


class ProjitoeNeUgasaet(models.Model):
    text = models.TextField()

    def get_absolute_url(self):
        return f"/prose/lived/{self.pk}"


class ThoughtAboutLived(models.Model):
    text = models.TextField()

    def get_absolute_url(self):
        return f"/prose/thoughts/{self.pk}"


class PagesOfHistory(models.Model):
    text = models.TextField()

    def get_absolute_url(self):
        return f"/prose/pages/{self.pk}"

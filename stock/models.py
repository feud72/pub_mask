from django.db import models


class Store(models.Model):
    region = models.CharField(max_length=30)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name + " # " + self.region


class Stock(models.Model):
    store = models.ForeignKey("Store", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.store.name + " # " + self.created_at.strftime("%m-%d-%H-%M")

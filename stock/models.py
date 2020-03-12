from django.db import models


class Store(models.Model):
    region = models.CharField(max_length=30)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name + " # " + self.region

    @property
    def remain_stat(self):
        obj = self.stock_set.order_by("created_at").last()
        return obj.status


class Stock(models.Model):
    store = models.ForeignKey("Store", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.store.name + " # " + self.created_at.strftime("%m-%d-%H-%M")

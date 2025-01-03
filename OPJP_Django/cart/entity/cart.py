from django.db import models

from kakao_account.entity.account import Account
from books.entity.books import Books
# Create your models here.


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="carts")
    bookName = models.ForeignKey(Books, on_delete=models.CASCADE, related_name="carts")
    bookPrice = models.ForeignKey(Books, on_delete=models.CASCADE, related_name="carts")
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'cart'
        app_table = 'cart'

    def __str__(self):
        return f"Cart(id={self.id}, account={self.account}), bookname={self.bookName}"
    
    def getId(self):
        return self.id
    
    def getAccount(self):
        return self.account
    
    def getBookName(self):
        return self.bookName
    
    def getBookPrice(self):
        return self.bookPrice
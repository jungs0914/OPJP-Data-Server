from django.db import models

from kakao_account.entity.account import Account
from books.entity.books import Books


class BookMark(models.Model):
    bookmarkId = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='bookmark')
    # bookName = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='bookmark')
    # bookImage = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='bookmark')
    books = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='bookmark')
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'bookmark'
        app_label = 'bookmark'

    def __str__(self):
        return f"Bookmark(id={self.bookmarkId}, account={self.account}, bookName={self.bookName})"
    
    def getId(self):
        return self.bookmarkId
    
    def getAccount(self):
        return self.account
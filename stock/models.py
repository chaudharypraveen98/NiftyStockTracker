from django.db import models

class IndexModel(models.Model):
    name  = models.CharField(max_length=40,blank=False,primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.name} : {self.start_date} - {self.end_date}"

class StockModel(models.Model):
    """
    Represents stock data.

    Fields:
    - entry_id (NUMBER): ID for each entry
    - index_name (CharField): Index name of stock.
    - date (DateField): The date of the stock data.
    - open_price (DecimalField): The opening price of the stock.
    - high_price (DecimalField): The highest price of the stock.
    - low_price (DecimalField): The lowest price of the stock.
    - close_price (DecimalField): The closing price of the stock.
    - shares_traded (BigIntegerField): The number of shares traded.
    - turnover (DecimalField): The total turnover of the stock.
    """

    entry_id = models.AutoField(primary_key=True)
    index_name = models.ForeignKey(IndexModel, on_delete=models.CASCADE, related_name='index')
    date = models.DateField()
    open_price = models.DecimalField(max_digits=10, decimal_places=2)
    high_price = models.DecimalField(max_digits=10, decimal_places=2)
    low_price = models.DecimalField(max_digits=10, decimal_places=2)
    close_price = models.DecimalField(max_digits=10, decimal_places=2)
    shares_traded = models.BigIntegerField()
    turnover = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        """
        Returns a string representation of the stock data object.

        Example:
        "2021-01-01 - Open: 100.00, High: 110.00, Low: 90.00, Close: 105.00, Shares Traded: 1000, Turnover: 100000.00"
        """
        return f"{self.date} - Open: {self.open_price}, High: {self.high_price}, Low: {self.low_price}, Close: {self.close_price}, Shares Traded: {self.shares_traded}, Turnover: {self.turnover}"

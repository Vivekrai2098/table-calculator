import backtrader as bt

# Create a custom strategy
class MyStrategy(bt.Strategy):
    params = (
        ("sma_period", 20),
    )

    def __init__(self):
        self.data_close = self.data.close
        self.sma = bt.indicators.SimpleMovingAverage(
            self.data, period=self.params.sma_period
        )

    def next(self):
        if self.data_close[0] > self.sma[0]:
            # Buy signal
            self.buy()
        elif self.data_close[0] < self.sma[0]:
            # Sell signal
            self.sell()

# Create a cerebro engine
cerebro = bt.Cerebro()

# Add data feed
data = bt.feeds.YahooFinanceData(dataname="AAPL", fromdate="2010-01-01", todate="2021-01

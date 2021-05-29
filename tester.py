import backtrader as bt
import datetime
import matplotlib

from backtrader.sizers.fixedsize import FixedSize
from strategies import TestStrategy

cerebro = bt.Cerebro()


#setting the cash
cerebro.broker.set_cash(1000000)


data = bt.feeds.YahooFinanceCSVData(
    dataname = "ADANIGREEN.csv",
  
    # Do not pass values before this date
    fromdate=datetime.datetime(2020, 1, 1),
    # Do not pass values after this date
    todate=datetime.datetime(2021, 1, 1),
    reverse=False)


#setting up the data
cerebro.adddata(data)


 
#adding strategy to cerebro
cerebro.addstrategy(TestStrategy)

#adding sizer
cerebro.addsizer(bt.sizers.SizerFix, stake=1000)


print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())


#plotting the results
cerebro.plot()
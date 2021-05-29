import backtrader as bt


cerebro = bt.Cerebro()


#setting the cash
cerebro.broker.set_cash(1000000)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
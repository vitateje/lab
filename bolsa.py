import bovespa

bf = bovespa.File("/home/vitateje/Desktop/teste")
for rec in bf.query(stock='PETR3'):
    print('<{}, {}, {}>'.format(rec.date, rec.stock_symbol, rec.price_close))


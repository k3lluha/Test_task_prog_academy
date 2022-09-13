price_bitcoin = int(input('What is Bitcoin price today '))
dolars = int(input('How mach $ do you have? '))
print(f'You can buy {"%.7f" % (dolars / price_bitcoin)} BTC')
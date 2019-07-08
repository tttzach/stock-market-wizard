import time
import sys, getopt
import datetime
from poloniex import poloniex

def main(argv):
	period = 10
	pair = "BTC_XML"

	periods = [300, 900, 1800, 7200, 14400, 86400]

	try:
		opts, args = getopt.getopt(argv,"hp:c:",["period=","currency="])
	except getopt.GetoptError:
		print('trading-bot.py -p <period> -c <currency pair>')
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print('trading-bot.py -p <period -c <currency pair>')
			sys.exit()
		elif opt in ("-p", "--period"):
			if (int(arg) in periods):
				period = arg
			else:
				print("Invalid periods")
				sys.exit(2)
		elif opt in ("-c", "--currency"):
			pair = arg

	conn = poloniex('FVXWV9V4-UQ1FTYHP-ZHEKRJNI-DF5JX6H3', '9e1144e9aed52e403ebf44af49a6eeafeab39d81c0c73fcf6919a040456ef7248633d6048b36911319546e26ca702b0681964df8f20a110d6ab551e0ace15148')

	while True:
		currentValues = conn.api_query("returnTicker")
		lastPairPrice = currentValues[pair]["last"]
		print("{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()) + " Period: %ss %s: %s" % (period, Pair, lastPairPrice))
		time.sleep(int(period))

if __name__ == "__main__":
	main(sys.argv[1:])
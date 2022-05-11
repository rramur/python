from nsetools import Nse
from pprint import pprint
import time

nse = Nse()

while 1:
    q = nse.get_quote('sbin')

    print ("Symbol: " + q['symbol'])
    print ("Company: " + q['companyName'])

    print ("Buy List\nPrice \t Quantity")
    print (str(q['buyPrice1']) + "\t" + str(q['buyQuantity1']))
    print (str(q['buyPrice2']) + "\t" + str(q['buyQuantity2']))
    print (str(q['buyPrice3']) + "\t" + str(q['buyQuantity3']))
    print (str(q['buyPrice4']) + "\t" + str(q['buyQuantity4']))

    print ("Sell List\nPrice \t Quantity")
    print (str(q['sellPrice1']) + "\t" + str(q['sellQuantity1']))
    print (str(q['sellPrice2']) + "\t" + str(q['sellQuantity2']))
    print (str(q['sellPrice3']) + "\t" + str(q['sellQuantity3']))
    print (str(q['sellPrice4']) + "\t" + str(q['sellQuantity4']))
    
    time.sleep(5)

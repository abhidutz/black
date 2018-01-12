# Dependencies
import requests as req
from datetime import datetime, date, time
import SendAlert

url = "https://api.iextrading.com/1.0/stock/";

stocks = ['AAC','AAME','AAU','AAV','ABAC','ABCD','ABDC','ABEV','ABIL','ABIO','ABR','ABUS','ACERW','ACFC','ACHN',
                'ACHV','ACMR','ACRX','ACST','ACTG','ADAP','ADES','ADMA','ADMP','ADOM','ADRO','ADVM','ADXS','ADXSW',
                'AEG','AEHR','AEMD','AETI','AEY','AEZS','AFMD','AG','AGC','AGEN','AGFS','AGFSW','AGI','AGLE','AGRX',
                'AGTC','AHC','AHPAW','AHPI','AHT','AINV','AIRG','AIRI','AKER','AKG','AKS','AKTS','AKTX','ALDX','ALIM','ALJJ',
          'ALLT','ALN','ALO','ALQA','ALRN','ALSK','ALT','AMBR','AMCN','AMDA','AMMA','AMPE','AMRC','AMRH','AMRHW','AMRN','AMRS',
          'AMS','AMSC','AMTX','ANDAR','ANDAW','ANFI','ANH','ANTH','ANW','ANY','AOD','APDN','APDNW','APEN','APHB','APOP',
          'APOPW','APPS','APRI','APRN','APT','APTO','APVO','APWC','AQB','AQMS','ARAY','ARC','ARCI','ARCT','ARCW','ARDM',
          'ARDX','AREX','ARGS','ARLZ','ARQL','ARTW','ARTX','ARWR','ASC','ASFI','ASG','ASM','ASNA','ASPN','ASPU','ASRV',
          'AST','ASTC','ASV','ASX','AT','ATAI','ATAX','ATEC','ATEN','ATHX','ATLC','ATNM','ATOM','ATOS','ATRS','ATTO','ATTU',
          'ATXI','AU','AUDC','AUG','AUMN','AUO','AUPH','AUTO','AUY','AVAL','AVDL','AVEO','AVGR','AVH','AVID','AVIR','AVP',
          'AVXL','AWP','AWRE','AWX','AXAS','AXON','AXR','AXSM','AXTI','AXU','AYTU','AZRX','BASI','BBDO','BBG','BBOX','BBRG']


stock_market_open_time = time(hour=8, minute=30, second=0, microsecond=0)
stock_market_close_time = time(hour=23, minute=0, second=0, microsecond=0)

def stockPriceCollectionWithSentiment():
    counter = 0;
    stockTicksMap={};
    time_var = datetime.now()
    for stock in stocks:
        response = req.get(url+stock+"/quote")
        stockTicksMap[stock] = response.json()['latestPrice']
    print(stockTicksMap);
    print(datetime.now()-time_var);

    while ((datetime.now().time() > stock_market_open_time) & ( datetime.now().time() < stock_market_close_time) & counter < 50):
        for stock in stocks:
            response = req.get(url + stock + "/quote")
            priceNow = response.json()['latestPrice']
            priceAtBegining = stockTicksMap[stock]
            if((priceNow - priceAtBegining)/priceAtBegining > 0.03):
                SendAlert.sendAlert(stocks)
                stocks.remove(stock)


try:
    stockPriceCollectionWithSentiment()
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')

from . import Loader

import pandas as pd
import gzip
import json


class SOFRStripRatesLoader(Loader):
    dataset = 'SOFRSR'
    fileglob = 'SOFR-Term-Rate-Fixings_*.JSON'

    names = ['instrument.productCode', 'instrument.productDescription',
            'instrument.securityId', 'pointInTime.businessDate', 'rate',
            'transactionTime']

    dtypes = {'category': ('mdEntryCode', 'mdEntryType', 'mdUpdateAction',
                           'symbol', 'openCloseSettlFlag'),
              'int64': ('rptSeq',),
              'float': ('netChgPrevDay', 'netPctChg', 'mdEntryPx'),
              'date:%Y%m%d_%H:%M:%S.%f': 'mdEntryDateTime'}

    def _load(self, filename):
        result = []
        with open(filename, 'rt', encoding='utf-8') as f:
            for line in f:
                line = json.loads(line)
            result = pd.io.json.json_normalize(line['payload'])
        
        return result


SOFRstripratesLoader = SOFRStripRatesLoader()

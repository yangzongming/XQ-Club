import datetime
import json
import decimal


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(obj, decimal.Decimal):
            return str(decimal.Decimal(obj).quantize(decimal.Decimal('0.00')))
        else:
            return json.JSONEncoder.default(self,obj)
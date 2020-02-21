class Rate:
    def buildRateRequest(self):
        rateReq = {
            "items": [
                {
                    "productId": 3387821,
                    "variantId": 12009212,
                    "weight_unit": "grams",
                    "weight": 2,
                    "quantity": 1
                }
            ]
        }
        return rateReq
    def getRates(self):
        #req = self.buildRateRequest()
        res = {
            "rateHashKey": "zsTUi",
            "shipment_price": 27.00
        }
        return res

class Shipment:
    def buildRequest(self):
        req = {
            "rateHashKey": "zsTUi",
            "packageWt": 23
        }
        return req
    def getShipment(self):
        #req = self.buildRequest()
        res = {
            "shipmentId": 'kjuiujs'
        }
        return res
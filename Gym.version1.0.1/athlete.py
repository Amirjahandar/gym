class Athlete(object):

    def __init__(self, Id, name, family, tell, date, payment = 0):
        self._Id = Id
        self._name = name
        self._family = family
        self._tell = tell
        self._date = date
        self._payment = payment


    def __str__(self):
        return "ID : {}// NAME : {}// FAMILY : {}// TELL : {}// DATE : {} ".format(self._Id, self._name, self._family, self._tell, self._date)

    def _set_payment(self, payment):

        if(isinstance(payment, float) and payment > 0):
            self._payment = payment
        else:
            self._payment = 0
            print("enter your payment in correct way!")


    def _get_payment(self):
        return self._payment


    Payment = property(_get_payment, _set_payment)
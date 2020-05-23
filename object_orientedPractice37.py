# class Ticket:
#     def original(self):
#         self.adult_price = 100
#
#     def weekend_price(self):
#         self.adult_price *= 1.2
#         return self.adult_price
#
#     def child_price(self):
#         return self.adult_price/2
'''
this is a practice about the object-oriented programming, in which we can understand
how to use class.

This practice is from the fishC forum
'''

class Ticket():
    def __init__(self, weekend=False, child = False):
        self.price = 100
        if weekend:
            self.rate = 1.2
        else:
            self.rate = 1
        if child:
            self.discount = 0.5
        else:
            self.discount = 1

    def calcPrice(self, num):
        return self.price*self.rate*self.discount*num

adult = Ticket()
child = Ticket(child=True)

print('two adults and 1 child should pay: %.2f' % (adult.calcPrice(2)+child.calcPrice(1)))

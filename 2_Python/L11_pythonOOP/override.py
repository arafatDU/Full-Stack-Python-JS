class User:

    def __init__(self, user_name, total_purchase):
        self.user_name = user_name
        self.total_purchase = total_purchase

    def get_shipping_cost(self):
        if self.total_purchase >= 1000:
            return 40
        return 60


class PremiumUser(User):

    def get_discount(self):
        if self.total_purchase >= 2000:
            return 100
        return 20

    # override
    def get_shipping_cost(self):
        return 0



premium_user = PremiumUser("Arafat", 2000)
print(premium_user.get_shipping_cost())

user_one = User("Sakib", 900)
print(user_one.get_shipping_cost())

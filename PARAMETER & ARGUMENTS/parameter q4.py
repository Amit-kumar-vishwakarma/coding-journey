"""
write the function called descount_price
that takes original prise and descounted price as parameter and
print the final
price after descount
"""


def descount_price(original_price, discount_percent):
    descount_amount = (discount_percent / 100) * original_price
    final_amount = original_price - descount_amount
    print(f" your finasl amount is rs.{final_amount}")


descount_price(100, 50)

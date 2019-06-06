import redis



def append_product(user_id, product_id):
    """

    :param user_id: unique user as key
    :param product_id: product id in DB
    :return: added product
    """

    r = redis.StrictRedis(host='localhost', port=6379, db=1)

    r.append(user_id, str(product_id)+"_")






def get_product(user_id):
    """

    :param user_id: unique user as key
    :return: user selected items
    """

    r = redis.StrictRedis(host='localhost', port=6379, db=1)
    try:
        value = r.get(user_id)
        return value.decode("utf-8").split("_")
    except AttributeError:
        return []


def empty_cart(user_id):
    """

    :param user_id: unique user id
    :return: True result if everything ok
    """
    r = redis.StrictRedis(host='localhost', port=6379, db=1)
    r.delete(str(user_id))

def get_full_price(products):
    """
    Calculating full price of user cart
    :param products:
    :return:
    """
    full_price = 0
    for product in products:
        full_price += product.price

    return full_price







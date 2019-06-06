import uuid


def tracker(request):
    """
    Creates new user id it it`s not created
    returns id if user created
    :param request:
    :return: user_id
    """

    if user_created(request):
        print(get_id(request))
    else:
        print(create_user(request))



def get_id(request):
    """
    get user unique id
    :param request:
    :return:
    """
    return request.session["user_id"]


def user_created(request):
    """
    check weather user is created
    :param request:
    :return:
    """
    try:
        request.session["user_id"]
        return True
    except KeyError:
        return False

def create_user(request):
    """
    Creates new key for user
    :param request:
    :return:
    """
    request.session["user_id"] = str(uuid.uuid4())
    return request.session["user_id"]
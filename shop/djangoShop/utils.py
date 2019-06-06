import uuid


def tracker(request):
    """
    Create unique id for unauthenticated users
    :param request:
    :return:
    """
    request.session["user_id"] = uuid.uuid4()
    return True

def get_id(request):
    """
    get user unique id
    :param request:
    :return:
    """
    return request.session["user_id"]


def is_user_created(request):
    """
    check weather user is created
    :param request:
    :return:
    """

    if request.session["user_id"]:
        return True
    else:
        return False
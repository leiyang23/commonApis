def resp(code=0, data=None, msg="success"):
    return {
        "code": code,
        "data": data,
        "msg": msg
    }

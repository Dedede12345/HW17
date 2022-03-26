
def recr_base(error):
    if repr(error) == "<class 'BaseException'>":
        return
    temp = error.__base__
    print(temp)
    recr_base(temp)

recr_base(ValueError)
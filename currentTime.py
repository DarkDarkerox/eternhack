import  datetime


def get_time():
    """This function tell us the time"""
    currentDT = datetime.datetime.now()
    return currentDT.strftime("%H:%M:%S")


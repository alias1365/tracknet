import datetime
from persiantools.jdatetime import JalaliDate


def miladi2shamsi(mdate):
    try:
        if isinstance(mdate, str):
            mdate = datetime.datetime.fromisoformat(mdate)
        tmp = JalaliDate(datetime.date(mdate.year, mdate.month, mdate.day))
        return "%s-%s-%s" % (tmp.year, tmp.month, tmp.day)
    except:
        return ''


def miladi2shamsi_hm(mdate):
    try:
        if isinstance(mdate, str):
            mdate = datetime.datetime.fromisoformat(mdate)
        tmp = JalaliDate(datetime.date(mdate.year, mdate.month, mdate.day))
        return "%s/%s/%s - %s:%s" % (tmp.year, tmp.month, tmp.day, mdate.hour, mdate.minute)
    except:
        return ''


def shamsi2miladi(mdate):
    try:
        if isinstance(mdate, str):
            lst = mdate.split('-')
            return JalaliDate(int(lst[0]), int(lst[1]), int(lst[2])).to_gregorian()
        else:
            return JalaliDate(mdate.year, mdate.month, mdate.day).to_gregorian()
    except:
        return ''


def comma_price(price):
    num = int(price)
    return f"{num:,}"


def lite_text(txt, liteNo=25):
    if len(txt) <= liteNo:
        return txt
    return txt[0:liteNo] + '...'

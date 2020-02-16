# -*- coding: utf-8 -*-
# @Time : 2020/2/12 19:12
# @Author : jjh
# @File : Time_Tool.py
# @Software: PyCharm
# @contact: 469672930@qq.com
# -*- 功能说明 -*-
# 时间处理工具
# -*- 功能说明 -*-


# 基本的日期与时间转换
# 你需要执行简单的时间转换，比如天到秒，小时到分钟等的转换
from datetime import timedelta
from datetime import datetime
import pytz
def timeConversion():
    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)
    c = a + b
    print(c.days)
    print(c.seconds)
    print(c.total_seconds())
    print("===========")
    a = datetime(2012, 9, 23)
    print(a + timedelta(days=10))
    b = datetime(2012, 12, 21)
    d = b - a
    print(d.days)
    print("===========")
    now = datetime.today()
    print(now)
    print(now + timedelta(minutes=10))

# 判断输入的年份是否闰年
def isALeapYear(yearNum = None):
    if yearNum is None:
        yearNum = 2020
    a = datetime(yearNum, 3, 1)
    b = datetime(yearNum, 2, 28)
    print((a - b).days)
    return (a - b).days is 2


#计算最后一个周五的日期
#你需要查找这个星期中某一天最后出现的日期，比如星期五
from datetime import datetime, timedelta
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']
def getPreviousByday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date
# print(getPreviousByday('Sunday', datetime(2012, 12, 21)))

# 计算当前月份的日期范围
# 你的代码需要在当前月份中循环每一天，想找到一个计算这个日期范围的高效方法
from datetime import datetime, date, timedelta
import calendar
def getMonthRange(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
        # start_date = date.today().replace(year=2019, month=3, day=1)
        print(start_date)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    print(start_date,"-",end_date)
    return (start_date, end_date)

# 为了在日期范围上循环，要使用到标准的数学和比较操作。 比如，可以利用 timedelta 实例来递增日期，小于号<用来检查一个日期是否在结束日期之前
def dateRange(start, stop, step):
    while start < stop:
        yield start
        start += step

def topTest():
    a_day = timedelta(days=1)
    first_day, last_day = getMonthRange(date(year=2019, month=3, day=1))
    while first_day < last_day:
        print(first_day)
        first_day += a_day
    print("==========")
    for d in dateRange(datetime(2012, 9, 1), datetime(2012, 10, 1),timedelta(hours=6)):
        print(d)
###########################################

# 字符串转换为日期
# 你的应用程序接受字符串格式的输入，但是你想将它们转换为 datetime 对象以便在上面执行非字符串操作
from datetime import datetime
def StrConversionDay(text = None):
    if text is None:
        text = '2020-02-16'
    d = datetime.strptime(text, '%Y-%m-%d')
    print(d) #2020-02-16 00:00:00
    nice_d = datetime.strftime(d, '%A %B %d, %Y') #还有一点需要注意的是， strptime() 的性能要比你想象中的差很多， 因为它是使用纯Python实现
    print(nice_d) #Sunday February 16, 2020
    parse_d = ParseYmd(text)
    print(parse_d)

# 比strptime()效率快7倍的自写函数
# 如果你要在代码中需要解析大量的日期并且已经知道了日期字符串的确切格式，可以自己实现一套解析方案来获取更好的性能
def ParseYmd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))

# 结合时区的日期操作
# 你有一个安排在2012年12月21日早上9:30的电话会议，地点在芝加哥。 而你的朋友在印度的班加罗尔，那么他应该在当地时间几点参加这个会议呢？
from datetime import datetime
from pytz import timezone
from logic.ConfigPathSys import ConfigPathSystem
def TimeZoneOperation(myCountyKey = None,myTime = None,otherCountyKey = None):
    if myCountyKey is None:
        myCountyKey = 'Asia/Shanghai'
    if myTime is None:
        myTime = datetime.today()
    if otherCountyKey is None:
        otherCountyKey = 'US/Central'

    utc_d = datetime.today().astimezone(pytz.utc) #格林尼治时间
    print("utcTime is ",utc_d)

    countryDirt = ConfigPathSystem().getCoutryData()
    countryNameDirt = ConfigPathSystem().getCoutryNameData()
    _timezone = timezone(myCountyKey)
    my_loc_d = _timezone.localize(myTime)
    print("myCountryKey is :",myCountyKey, " time is :",my_loc_d)
    for value in countryDirt:
        break
        valueInfo = countryDirt[value]
        for countryKey in valueInfo:
            #print(countryKey)  #'US/Central'
            #_timezone = timezone(countryKey)
            otherCountry_d = my_loc_d.astimezone(timezone(countryKey))
            countryName = countryNameDirt[countryKey]
            print(countryName, "当地时间是 ", otherCountry_d)
            #print("otherCountryKey is :", countryKey, " astimezone time is :", otherCountry_d)

            # later = _timezone.normalize(loc_d + timedelta(minutes=30))
            # print("later is :", later)

    print(otherCountyKey,"当地时间是 ",my_loc_d.astimezone(timezone(otherCountyKey)))

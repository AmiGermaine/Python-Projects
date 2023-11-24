import datetime
from datetime import timedelta

t1 = timedelta()
# If modified within last 24 hours, then copy to destination folder
modifyDateLimit = modifyDate + datetime.timedelta(days=1)
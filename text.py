import iso8601

def getDuration(t1, t2):
    diff = t2-t1
    days, seconds = diff.days, diff.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    return str(hours)+"H", str(minutes)+"M"
t1 = iso8601.parse_date("2020-08-01T16:20:00")
t2 = iso8601.parse_date("2020-08-01T10:00:00")

print(getDuration(t1, t2))

def dateWords(d):
    return str(d.strftime('%A %d %B %Y')).title()

print(dateWords(t1))
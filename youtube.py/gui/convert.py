def convert_views(views):
    typ = {0: '', 1: 'K', 2: 'M', 3: 'B', 4: 'T'}
    l = (len(str(views))-1) // 3
    return '%.2f' % (views/1000**l) + typ[l]


def convert_duration(duration):
    if duration[:2] == '00':
        return duration[3:] + ' minutes'
    return duration + ' hours'


def convert_likes(likes):
    typ = {0: '', 1: 'K', 2: 'M', 3: 'B', 4: 'T'}
    l = (len(str(likes))-1) // 3
    return str((likes//1000**l)) + typ[l]


def convert_title(title):
    if len(title) > 20:
        return title[:20] + '...'
    return title


def convert_channel(channel):
    if len(channel) > 15:
        return channel[:15] + '..'
    return channel

# def monthly_calendar(month, last_day):
#     cld = []
#     for day in range(1, last_day+1):
#         cld.append(f"{month}月{day}日")
#     return cld

def calendar():
    cld = []
    for m in range(1, 13):
        if m in [1,3,5,7,8,10,12]:
        #     cld.extend(monthly_calendar(m, 31))
            cld.extend(
                [f"{m}月{d}日" for d in range(1, 32)]
            )
        elif m in [4,6,9,11]:
            # cld.extend(monthly_calendar(m, 30))
            cld.extend(
                [f"{m}月{d}日" for d in range(1, 31)]
            )
        else:
            # cld.extend(monthly_calendar(m, 28))
            cld.extend(
                [f"{m}月{d}日" for d in range(1, 29)]
            )
    return cld

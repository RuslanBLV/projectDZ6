def filter_by_state(stats):
    """ Сортировка по ключу "state": "EXECUTED" или "CANCELED" """
    executed = []
    canceled = []
    for stat in stats:
        if stat["state"] == "EXECUTED":
            executed.append(stat)
        elif stat["state"] == "CANCELED":
            canceled.append(stat)
    return (f"""{executed}
{canceled}""")

def sort_by_date(data: str, reverse: bool=True) -> list:
    """Сортировка даты по убыванию"""
    return sorted(data, key= lambda x: x["date"], reverse=reverse)



#print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
#print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
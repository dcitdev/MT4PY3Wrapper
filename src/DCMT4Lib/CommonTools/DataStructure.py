class ParamKeeper:
    def __init__(self):
        self.int_list = list()
        self.double_list = list()
        self.date_list = list()
        self.string_list = list()

    def __str__(self):
        report = list()

        # handle int
        report.append("We have int:")
        for param in self.int_list:
            report.append(f"""{param}""")

        # handle double
        report.append("We have double:")
        for param in self.double_list:
            report.append(f"""{param}""")

        # handle date
        report.append("We have date:")
        for param in self.date_list:
            report.append(f"""{param}""")

        # handle string
        report.append("We have string:")
        for param in self.string_list:
            report.append(f"""{param}""")

        return "\n".join(report)

class MqlDateTime:
    def __init__(self):
        self.year = 0
        self.mon = 0
        self.day = 0
        self.hour = 0
        self.min = 0
        self.sec = 0
        self.day_of_week = 0 # Day of week (0-Sunday, 1-Monday, ... ,6-Saturday)
        self.day_of_year = 0 # Day number of the year (January 1st is assigned the number value of zero)

    def __str__(self):
        return f"""year: {self.year} mon: {self.mon} day: {self.day} hour: {self.hour} min: {self.min} sec: {self.sec} day_of_week: {self.day_of_week} day_of_year: {self.day_of_year}"""

class MqlTick:
    def __init__(self):
        self.time = None
        self.bid = 0.0
        self.ask = 0.0
        self.last = 0.0
        self.volume = 0

    def __str__(self):
        return f"""time: {self.time}, bid: {self.bid}, ask: {self.ask}, last: {self.last}, volume: {self.volume}"""


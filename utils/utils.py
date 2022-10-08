class Constants:
    FALL_TIME = 1
    PART_TIME = 2
    HOURLY = 3


class App_Utils:
    @staticmethod
    def check_value_is_empty(value=str):
        for item in value:
            if item.isspace() or item == "":
                 return True

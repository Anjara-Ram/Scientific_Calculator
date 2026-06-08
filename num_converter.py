class Converter:

    @staticmethod
    def is_number(text):
        try:
            float(text)
            return True
        except:
            return False
    @staticmethod
    def int_converter(num):
        if isinstance(num, float) and num.is_integer():
            return str(int(num))
        return str(round(num, 10))

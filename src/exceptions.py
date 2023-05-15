class InstantiateCSVError(Exception):
    """
    Исключение вызывается, когда файл .csv повреждён.
    К примеру отсутствует одна из колонок данных.

    """
    pass
class InvalidMarksError(Exception):
    pass

def check_marks(marks):
    if not 0 <= marks <= 100:
        raise InvalidMarksError("Marks must be 0-100")
    return "Valid marks"

try:
    print(check_marks(120))
except InvalidMarksError as error:

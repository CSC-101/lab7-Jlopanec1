#1
def str_to_float(s) -> Optional[float]:
    try:
        s = float(s)
        return s
    except ValueError:
        return None
s = "34"
print(str_to_float(s))
print(type(float(s)))

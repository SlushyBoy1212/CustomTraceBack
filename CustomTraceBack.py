import sys
import traceback

#---Actual Code---#
def customtraceback(exc_type, exc_value, exc_tb):
    tbf(name=str(exc_type.__name__), value=str(exc_value), tb=traceback.format_tb(exc_tb)[0].strip())
def default_traceback(name, value, tb):
    if name == "BaseException":
        print(value)
    elif not value.strip():
        print(f"{name}")
    else:
        print(f"{name}: {value}")
def traceBackExample(name, value, tb):
    print(f"{name}: {value}")
    print(tb)
tbf = default_traceback
def setTraceBack(function):
    global tbf
    if not callable(function):
        return
    tbf = function
def help():
    setTraceBack(traceBackExample)
    print(f"\033[91m\033[4mCustomTraceBack\033[0m")
    print(f"\033[91mUSAGE:\033[0m")
    print(f"\033[91mCustomTraceBack.setTraceBack(tracebackfunction)\033[0m")
    print(f"\033[91m(tracebackfunction is a function)\033[0m")
    print(f"EXAMPLE:")
    print(f"def traceBackExample(name, value, tb):")
    print("    print(f\"{name}: {value}\")")
    print("    print(tb)")
    print("CustomTraceBack.setTraceBack(traceBackExample)")
    print("Lets run the example:")
    raise Exception(f"traceback")
sys.excepthook = customtraceback
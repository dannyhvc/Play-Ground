import eel

eel.init("web") #folder that hold gui content

@eel.expose
def my_python_method(param1: str, param2: str) -> None:
    print(param1 + ' ' + param2)

eel.start("main.html", block=False)  # starting page :: already set the root directory

while True:
    eel.sleep(10)
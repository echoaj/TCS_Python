

class Sow:
    content = None

    def __repr__(self):
        return "----"


task = Sow(content="Hello world")

print(task.content)

from models import Task


def init_db():
    task_list = Task.query().fetch(20)
    if len(task_list) <= 0:
        for i in range(20):
            t = Task()
            t.description = "Task #" + str(i)
            t.put()

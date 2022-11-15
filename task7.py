from functools import partial


def create_handlers(callback):
    handlers = []
    for step in range(5):
        handlers.append(partial(callback, step))
    return handlers


def execute_handlers(handlers):
    for handler in handlers:
        handler()


def call(*args, **kwargs):
    print(*args, kwargs)


if __name__ == "__main__":
    handlers = create_handlers(call)
    execute_handlers(handlers)

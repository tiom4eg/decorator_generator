# Pass function (if before is None or after is None)
def passer():
    pass


# Decorator generator (lol)
def generator(before=passer, after=passer):
    def decorator(func):
        def wrapper(*args, **kwargs):
            before()
            func(*args, **kwargs)
            after()
        return wrapper
    return decorator


# Test inputs for our generator
def test_before():
    return f"Look, I'm flying! My speed: 9 mph!"


def test_after():
    return f"Oh no, I falled to ground after 15 seconds..."


# Test of our generator
@generator(test_before, test_after)
def hello_world():
    print("Hello, World!")


hello_world()

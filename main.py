from negilib import negilib

@negilib
def test():
    sum(range(10_000_000))

if __name__ == "__main__":
    test()
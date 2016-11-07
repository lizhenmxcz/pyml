class aa:
    w = 10

    def __init__(self):
        self.x = 11
        self.y = 12

    def add(self):
        return self.x + w

if __name__ == '__main__':
    b = aa()
    print(b.add())

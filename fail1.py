class Peopls():
    def __init__(self, id, name, ):
        self.id = id
        self.name = name

    def info(self):
        print(f'Id is:{self.id}\nName is: {self.name}')


if __name__== "__main__":

    p1 = Peopls(13, "Albert")
    p1.info()

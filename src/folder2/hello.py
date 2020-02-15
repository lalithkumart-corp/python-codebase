class Hello:
    def init(self, msg):
        print('Invoked init method of class HELLO')
        self.message = msg
        print('Message obtained ', self.message)
    def getMsg(self):
        print(self.message)

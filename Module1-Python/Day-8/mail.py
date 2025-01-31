from abc import ABC,abstractmethod
class mail(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def send(self,message):
        pass
    @abstractmethod
    def receive(self,received_msg):
        pass
class email(mail):
    def __init__(self):
        print("Mail created")
    def send(self,message):
        print("sent",message)
    def receive(self, received_msg):
            print(received_msg)

class whatsapp(mail):
    def __init__(self):
          print("whatsapp message recorded")
    def send(self,message):
         print("sent", message)
    def receive(self, received_msg):
         print("received",received_msg)

class msger(mail):
    def __init__(self):
          print("the message is recorded")
    def send(self,message):
        print("sent", message)

    def receive(self, received_message):
         print("received message ", received_message)

whatsapp_message=whatsapp()
whatsapp_message.send("this is whatsapp's message")
whatsapp_message.receive("this is the whatsapp's received message")
msger_message=msger()
msger_message.send("this is the msger's message")
msger_message.receive("this is the msger's received message")
email_message=email()
email_message.send("this is the email's sent message")
email_message.receive("this is the email's received message")
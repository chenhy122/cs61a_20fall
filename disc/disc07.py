class MinList:
    """A list that can only pop the smallest element"""
    def __init__(self):
        self.items = []
        self.size = 0
    def append(self, item):
        """Appends an item to the MinList
    >>> m = MinList()
    >>> m.append(4)
    >>> m.append(2)
    >>> m.size
    2
    """
        self.items.append(item)
        self.size += 1
    
    def pop(self):
        """ Removes and returns the smallest item from the MinList
    >>> m = MinList()
    >>> m.append(4)
    >>> m.append(1)
    >>> m.append(5)
    >>> m.pop()
    1
    >>> m.size
    2
    """
        n = min(self.items)
        self.items.remove(n)
        self.size -= 1
        return n
    
    
    

class Email:
    """Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.message = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name
        
        
        
class Server:
    """Each Server has an instance attribute clients, which
    is a dictionary that associates client names with client objects."""
    def __init__(self):
        self.clients = {}
        
    def send(self, email):
        """Take an email and put it in the inbox of the client
    it is addressed to.
    """
    
    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds them
    to the clients instance attribute.
    """
        self.clients[client_name] = client
    
    
class Client:
    """Every Client has instance attributes name (which is
    used for addressing emails to the client), server
    (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received).
    """
    def __init__(self, server, name):
        self.inbox = []
        
        
    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the
    given recipient client.
    """
    
    def receive(self, email):
        """Take an email and add it to the inbox of this
    client.
    """
class Poll:
    def __init__(self,id,title, message, time,status):
        self.id = id
        self.title = title 
        self.message = message
        self.time = time
        self.status = status
Poll_list = [
      Poll(0,'Polls Dashboard', 'Welcome to the Polls Dashboard!', '2024-06-01 12:00:00', False),
      Poll(1,'Polls User', 'Welcome to the Polls User!', '2024-06-01 12:00:00', True),
      Poll(2,'Polls Login', 'Welcome to the Polls Login!', '2024-06-01 12:00:00', False),
]   
def get_Poll_list():
        return Poll_list
def get_Detail_Poll(id):
       poll_list = get_Poll_list()
       return poll_list[id]
def delete_Poll(id):
    global Poll_list
    Poll_list = [poll for poll in Poll_list if poll.id != id]
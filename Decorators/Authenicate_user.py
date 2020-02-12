#An @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {1:{'name': 'Sorna','valid': True},
2:{ 'name':'Prafull','valid':False}}
 


def authenticated(fn):
  def wrapper(*args, **kwargs):
    if args[0][2]['valid']:
        return fn(*args, **kwargs)
  return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)

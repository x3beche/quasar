from ax45sEngine.algorithms import axen,axde

text='test >< +-*/ crypto'
encrypted=axen(text,237415)

print('This encrypt state : "'+axen(text,237415)+'"')
print('This decrypt state : "'+axde(encrypted,237415)+'"')

from ax45sEngine.algorithms import axen,axde

text="sasasasasasasasasasasasasa"
encrypted=axen(text,1001)

print("This encrypt state : ",axen(text,237415))
print("This decrypt state : ",axde(encrypted,237415))

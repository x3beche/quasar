from ax45sEngine.algorithms import axen,axde

text="AX45-S Crypto Algorithm"
encrypted=axen(text,1001)

print("This encrypt state : ",axen(text,1001))
print("This decrypt state : ",axde(encrypted,1001))

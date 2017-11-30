import aiml
# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("LOAD AIML B")
# Press CTRL-C to break this loop
while True:
 message=raw_input("Enter your message for bot >> ") 
if message == "quit":
        exit()
else:
 bot=kernel.respond(message)
 if bot=="G1 script to be run":
  print("g1")
 else: 
  print("g2")

 

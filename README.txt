PYTHON LEARNING - READ ME

TODO
-









DONE










GAMEPLAN
-synonymizing
-definitions
-abstract relatonships
-6sense RANDOM ASCII art
-flash cards
-looping timer
-2 random 'facts; - how do they relate?

-type/retype notes
-habit log: what worked? what didn't?

Dopamine break...
-take 5 screenshots, point me to a folder
-set timer and I'll remind you



















LEARNED

//GET request on 'server'
app.get("/dreams/:hello", function (request, response) {
  response.send(request.params.hello);
});

//GET request from python
def runMe():
  r = requests.get("https://studypython.gomix.me/dreams/welcome")
  print r.text

//Keep while'ing until EOF
while True:
  enter = raw_input("Run?\n");
  if enter=="EOF":
    break
  if enter == "runRan":
      enter2 = raw_input("vars?\n")
      if enter2 != '':
        runRan(enter2)
      else:
        runRan()
        
  if enter == "runPrintString":
      enter2 = raw_input("vars?\n")
      if enter2 != '':
        runPrintString(enter2)
      else:
        runPrintString()
    
    
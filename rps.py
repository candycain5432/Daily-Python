try: # Adds KeyboardInterrupt Exception

    # Imports librarys
    import random
    
    # Options for the CPU to choose from
    opt = ["rock", "paper", "scissors"] 

    # While loops keep the game going until KeyboardInterrupt
    while True:
        # Takes input
        ply = str(input("Choose Rock Paper or Scissors\n"))
        
        # If error = 1 a issue has occured if error = 0 it continues
        error = 0
        
        # Creates the result variable
        result = None
        
        # Cpu's play
        cpu = random.choice(opt)
        
        # Checks the logic for the game
        if ply.lower() == cpu.lower():
            result = "Tie"
        elif ply.lower() == "rock" and cpu.lower() == "paper":
            result = "CPU Wins!"
        elif ply.lower() == "rock" and cpu.lower() == "scissors":
            result = "Player Wins!"
        elif ply.lower() == "paper" and cpu.lower() == "rock":
            result = "Player Wins!"
        elif ply.lower() == "paper" and cpu.lower() == "scissors":
            result = "CPU Wins"
        elif ply.lower() == "scissors" and cpu.lower() == "rock":
            result = "CPU Wins!"
        elif ply.lower() == "scissors" and cpu.lower() == "paper":
            result = "Player Wins!"
        else:
            print("Something went wrong")
            error = 1
    

        # Checks for error
        if error != 1:
            print(f"Computer plays {cpu}\n") 
        else:
            break
        
        # Checks for errors again
        if result != None:
            print(result, "\n")
        else:
            break

except KeyboardInterrupt:
    print("Exit")

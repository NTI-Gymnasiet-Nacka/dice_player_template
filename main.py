from random import randint

#En spelarklass för ett enkelt tärningsspel med spelare
class Player:

   def __init__(self):
       # Attribut: Name, Score, Wins, Lastroll. Score, Wins och Lastroll ska alltid börja på 0
       """
            Attribut
            Name : str
            Score : int
            Wins : int
            Lastroll: int, default 0
       """
       pass

   def __str__(self):
       # Skriv ut vad spelaren heter och vad dens score är
       return f""

   def add_score(self, points):
       # Lägger till antal points i score
       pass

   def resets_core(self):
       # Nollställer scoren
       pass
   
   def win(self):
       # Ökar antalet wins med 1 för spelaren
       pass
  
   def roll(self):
       # Rullar en tärning och sparar resultatet i attributet Lastroll
       pass
   
def main():
    exampleplayer = Player() # Fyll i Player
    
if __name__ == "__main__":
    main()
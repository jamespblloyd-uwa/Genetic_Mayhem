# Genetic_Mayhem

Pixel art game about a scientist picking up a pipette and trying to fill the tubes and avoid the dangerous plants. Thanks to @Pythondude (YouTube)/ @MouhammadHamsho (Twitter) for their YouTube tutorial (https://www.youtube.com/watch?v=G_LXB5C-r20).
## Setting up the environment and dependencies

I reccommend that you use `conda` or `mamba` to install the dependencies and to do so in their own virtual environment rather than conda/mamba's base environment. To do so please down load the Genetic_Mayhem_env.yml to your computer from this GitHub repo and then create a new `conda` environment using the below command:
```
$ conda env create --file Genetic_Mayhem_env.yml -n "Genetic_Mayhem_env"
$ conda activate Genetic_Mayhem_env
```

Now you have all the dependencies and have loaded the correct environment, you are ready to move to the installation of the game below.

I had assumed that doing the below would be surficent but it was not, so I reccommend recreating my env using the above yml file, even if it is a bit bloated.
```
$ conda create -n "Genetic_Mayhem_env2" python=3.9 pygame=2.4.0
$ conda activate Genetic_Mayhem_env
```

## Installation

In the terminal type the below commands where you want to download the game:
```
$ git clone https://github.com/jamespblloyd-uwa/Genetic_Mayhem.git
$ cd Genetic_Mayhem
```
Now you are ready to play the game. Launch it by being in the Genetic_Mayhem directory and typing:
```
$ python main.py
```

## Gameplay

Use the arrow keys to move the scientist around the screen. You can use Z or SPACEBAR to shoot a drop of liquid from the scientist once they have picked up the pipette.

You need to shoot drops of water at the Eppe tubes to make them go away and win the game. They shoot drops of water back at you. Also, watch out for the dangerous plants running around the lab as if you collide with one, it is game over!

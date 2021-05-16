# research

Ran various simulations on agents and their interactions. 

[original-sims](https://github.com/charlestang06/research/tree/master/original-sims) - The original simulations from [here](http://motion.cs.umn.edu/PowerLaw/). 

[survey](https://github.com/charlestang06/research/tree/master/survey) - Ran a python script through surveys asking about opinions on contact tracing with mobile apps. The analysis can be found [here](https://docs.google.com/presentation/d/1BWw-zQXjyHDgzfu--fYldN2brBmKCCQk_ppXGwmYLWQ/edit?usp=sharing).

---

When running different tests, use [masterrunner.py](https://github.com/charlestang06/research/blob/master/masterrunner.py) or run the individual files by editing the environment variables.

## Different Simulations
- [varysize.py](https://github.com/charlestang06/research/blob/master/varysize.py), it is used to change sizes of the room. Cana also support hallway movement (one-directional)
- [hallway.py](https://github.com/charlestang06/research/blob/master/original-sims/hallway.py), is used to model a hallway without varying size
- [cluster.py](https://github.com/charlestang06/research/blob/master/cluster.py), creates clusters/communities within regions and runs simulations through them
- [twowayhallway.py](https://github.com/charlestang06/research/blob/master/twowayhallway.py), creates a two-directional hallway simulation 

## Output/Processing Files

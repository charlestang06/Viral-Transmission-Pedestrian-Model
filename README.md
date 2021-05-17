# COVID-19: Simulation

Ran various simulations on agents and their interactions. Working with Archaana Santhana Krishnan and Prof. Schaumont. 

[original-sims](https://github.com/charlestang06/research/tree/master/original-sims) - The original simulations from [here](http://motion.cs.umn.edu/PowerLaw/). 

[survey](https://github.com/charlestang06/research/tree/master/survey) - Ran a python script through surveys asking about opinions on contact tracing with mobile apps. The analysis can be found [here](https://docs.google.com/presentation/d/1BWw-zQXjyHDgzfu--fYldN2brBmKCCQk_ppXGwmYLWQ/edit?usp=sharing).

[data](https://docs.google.com/spreadsheets/d/1O5-L0Cw-jAwwHbdB0Xuew28sCbV4LKusIHex6VxOFwk/edit?usp=sharing) - All charts and data collected from simulations are located in this spreadsheet

---

When running different tests, use [masterrunner.py](https://github.com/charlestang06/research/blob/master/masterrunner.py) or run the individual files by editing the environment variables.

## Different Simulations
- [varysize.py](https://github.com/charlestang06/research/blob/master/varysize.py), it is used to change sizes of the room. Cana also support hallway movement (one-directional)
- [hallway.py](https://github.com/charlestang06/research/blob/master/original-sims/hallway.py), is used to model a hallway without varying size
- [cluster.py](https://github.com/charlestang06/research/blob/master/cluster.py), creates clusters/communities within regions and runs simulations through them
- [twowayhallway.py](https://github.com/charlestang06/research/blob/master/twowayhallway.py), creates a two-directional hallway simulation 

## Output/Processing Files
All processing files are found [here](https://github.com/charlestang06/research/tree/master/processing%20files).
- [variables.txt.](https://github.com/charlestang06/research/blob/master/processing%20files/variables.txt), used by masterrunner to store local variables to run simulations with
- [sim_output.txt](https://github.com/charlestang06/research/blob/master/processing%20files/sim_output.txt), direct output from all simulations that track contact interactions every ~1/10 second
- [timecalc.py](https://github.com/charlestang06/research/blob/master/processing%20files/timecalc.py), processes data from sim_output.txt and outputs information to [time_output.txt](https://github.com/charlestang06/research/blob/master/processing%20files/time_output.txt), and [timeoutput.csv](https://github.com/charlestang06/research/blob/master/processing%20files/time_output.csv)
- [lazy.py](https://github.com/charlestang06/research/blob/master/processing%20files/lazy.py), processes final_output to be compatible with storing information on spreadsheet; outputs to [lazy.csv](https://github.com/charlestang06/research/blob/master/processing%20files/lazy.csv)
  * [cluster-lazy.py](https://github.com/charlestang06/research/blob/master/processing%20files/cluster-lazy.py) and [cluster-timecalc.py](https://github.com/charlestang06/research/blob/master/processing%20files/cluster-timecalc.py) do the same things as above but avoids counting two agents in the same community in the avg. contact time/total close contacts

import cPickle as pickle
import argparse
import imp
import os
import shutil
import subprocess
import sys
import time
from   os.path import join
from pycog.utils import get_here, mkdir_p

# #=========================================================================================
# # Command line
# #=========================================================================================

# p = argparse.ArgumentParser()
# p.add_argument('model_file', help="model specification")
# p.add_argument('action', nargs='?', default='check')
# p.add_argument('args', nargs='*')
# p.add_argument('-s', '--seed', type=int, default=100)
# p.add_argument('--suffix', type=str, default='')
# p.add_argument('-p', '--ppn', type=int, default=1)
# p.add_argument('-g', '--gpus', nargs='?', type=int, const=1, default=0)
# p.add_argument('--dt', type=float, default=0.5)
# p.add_argument('--dt_save', type=float, default=0.5)
# a = p.parse_args()

# # Model file
# modelfile = os.path.abspath(a.model_file)
# if not modelfile.endswith('.py'):
#     modelfile += '.py'

# action  = a.action
# args    = a.args
# seed    = a.seed
# suffix  = a.suffix
# ppn     = a.ppn
# gpus    = a.gpus
# dt      = a.dt
# dt_save = a.dt_save

# print("MODELFILE: " + str(modelfile))
# print("ACTION:    " + str(action))
# print("ARGS:      " + str(args))
# print("SEED:      " + str(seed))

# #=========================================================================================
# # Setup paths
# #=========================================================================================

# # Location of script
# here   = get_here(__file__)
# prefix = os.path.basename(here)

# # Name to use
# name = os.path.splitext(os.path.basename(modelfile))[0]

# # Scratch
# scratchroot = os.environ.get('SCRATCH', join(os.path.expanduser('~'), 'scratch'))
# scratchpath = join(scratchroot, 'work', prefix, name)

# # Theano
# theanopath = join(scratchpath, 'theano')

# # Paths
# workpath   = join(here, 'work')
# datapath   = join(workpath, 'data', name)
# figspath   = join(workpath, 'figs', name)
# trialspath = join(scratchpath, 'trials')

# # Create necessary directories
# for path in [datapath, figspath, scratchpath, trialspath]:
#     mkdir_p(path)

# # File to store model in
# savefile = join(datapath, name + suffix + '.pkl')


# #=========================================================================================
# p = {
#     'seed':       seed,
#     'model':      m,
#     'savefile':   savefile,
#     'name':       name,
#     'datapath':   datapath,
#     'figspath':   figspath,
#     'trialspath': trialspath,
#     'dt':         dt,
#     'dt_save':    dt_save
#     }

# filename = join(p['trialspath'], p['name'] + '_trials.pkl')
trialsfile = 'C:\\Users\\86193\\scratch\\work\\examples\\romo\\trials\\romo_trials.pkl'
print(trialsfile)
with open(trialsfile, 'wb') as f:
    trials = pickle.load(f)

try:
    print(type(trials))
    print(len(trials))
except:
    print("trials is not a list")



# data = [1, 2]

# # Pickle the data
# with open(trialsfile, 'wb') as f:
#     pickle.dump(data, f)

# # Unpickle the data
# with open(trialsfile, 'rb') as f:
#     unpickler = pickle.Unpickler(f)
#     loaded_data = unpickler.load()
#     print(f"Loaded data: {loaded_data}")
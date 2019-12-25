""" Restoring pytorch model """
import torch
import os

# loading the parameters from saved model
def load_model_parameters(full_path):
    model_load = torch.load(full_path)
    print(model_load['model_state'])
    print(model_load['model_optimizer'])


checkpoint_directory = 'torch_directory'
checkpoint_file = 'model.pt'
full_path = os.path.join(checkpoint_directory, checkpoint_file) 

load_model_parameters(full_path)




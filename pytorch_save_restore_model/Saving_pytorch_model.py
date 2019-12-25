""" Saving pytorch model """
import torch
import os
import torch.optim as optim

model = torch.nn.Linear(5, 2)
filepath = os.getcwd()
optimizer = optim.SGD(model.parameters(), lr = 0.001, momentum = 0.9)

# create a checkpoint directory to save pytorch model
if not os.path.exists('torch_directory'):
	os.makedirs('torch_directory')

def save_model(model_dictionary):
    checkpoint_directory = 'torch_directory'
    file_path = os.path.join(checkpoint_directory, 'model.pt')
    torch.save(model_dictionary, file_path)


# make a dictionary to save model state and optimizer
model_dictionary = {
            'model_state': model.state_dict(),
            'model_optimizer': optimizer.state_dict()
            }
save_model(model_dictionary)




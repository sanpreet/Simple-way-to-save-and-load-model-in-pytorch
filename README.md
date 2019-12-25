# Simple-way-to-save-and-load-model-in-pytorch
Simple way to save and load model in pytorch  

Pytorch Model is saved in either .pt or .pth format. 

To run this code it is important to install torch. You can get the dependencies from requirements.txt and along with that I am also addding the screenshot below showing install of torch for this code to run.  

![install_torch](https://user-images.githubusercontent.com/3431730/71433571-f069b280-2705-11ea-9b7e-6105a67756cb.png)  

## Why I had made this code  

This is because once training is complete, it would be a wise step to just load the saved model instead of doing training again and again. It will save a lot of time and this inspires me to create this repository. I hope readers would love this.  

## Loading torch Model  

To load saved model, use the below code  
```
torch.load(checkpoint_file)  
```  

I am also attaching the below screenshot to assist you better.  

![loading_model_dictionary](https://user-images.githubusercontent.com/3431730/71433657-7ab21680-2706-11ea-8649-f3e41ccbdf5e.png)  

## Saving the model  

To save the model, please run the below file  

```
python3 Saving_pytorch_model.py
```

To load the saved model, please run the below file 

```
python3 Restoring_pytorch_model.py
```

Thanks a lot for reading this file. I hope readers have gained some good insights from this code.




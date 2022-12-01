# Conformer-Farsi
jupyter notebook for fine-tuning Nemo's Conformer-CTC (and other Nemo models) on Farsi.

# Disclaimer: various parts of the code in this notebook are from the tutorials of the Nemo's website

# Conformers and Other Nemo Models for Farsi

This notebook contains the code for fine-tuning and training Nemo ASR models on Farsi. Nemo is an open-source conversational ai toolkit and many ASR models including the conformer are built into it. Nemo models are available as either pre-trained on certain languages or as models with no training. 
In this project we use the CTC-Conformer model of this toolkit and train it on Farsi. the code can be slightly modified to use other models of ASR as well. 



## Requirements and Starting Out

Run the first cell in the code to download and install the libraries used throughout the code.
The dataset used in the notebook for training models on Farsi is the Mozilla Common Voice dataset version 5.1. Run the second cell to download the dataset. Then run the third cell to convert mp3 files to wav and to create json manifest files for the training, validation and test data. The json files contain an address and transcription for each audio file. 
The third cell uses a script named manifest_cv.py which normalizes the characters in the transcription of each audio file. This script can be modified to change the valid characters in the normalizations.



## Tokenizer
The tokenizer cell uses a script from the nemo library to create an spe unigram tokenizer. The vocab size of the tokenizer can be modified by assigning the desired value to the variable "VOCAB_SIZE".

## Parameters
The parameters cell sets the config of the ASR model. The default config is first loaded by using the "from_pretrained" function of Nemo. To change the ASR model from the default CTC_Conformer with small parameter size, change the argument of the "from_pretrained" function. The tokenizer and manifest file paths are then set in the config. 
The model parameter sizes and training parameters such as batch-size can be set to a desired value next. 

## Torch Trainer
This cell creates a model trainer using pytorch-lightning. The number of Epochs in training can be set from here.

## Import The Transducer Model
This cell imports the selected ASR model. The model is pre-trained on English and needs to be fine-tuned on Farsi. This cell changes the vocabulary of the model using the tokenizer file. The manifest file paths are also set here again (to train a model from scratch, comment the "change vocabulary" line and the lines setting up multiple datasets). 
The learning rate of the training can also be set from here.

## Prepare NeMo's Experiment Manager
This cell creates a nemo experiment manager to save the best models as the training goes on. The cell also creates a tensorboard for monitoring training progress (tensorboard requires using Google Colab)

## Train and Test the model
Run the last cell to train and test the ASR model.

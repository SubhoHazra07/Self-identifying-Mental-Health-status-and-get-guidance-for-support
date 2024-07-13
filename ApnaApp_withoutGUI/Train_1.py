#load the package
import numpy as np
import random
import json

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

from nltk_utils import bag_of_words, tokenize, stem
from model import NeuralNet

# open the .json file
with open('intents_1.json', 'r') as f:
    intents_1 = json.load(f)

all_words = []
tags = []
xy = []
# loop through each sentence in our intents patterns
for intent in intents_1['intents_1']:
    tag = intent['tag']
    # add to tag list
    tags.append(tag)
    for pattern in intent['patterns']:
        # tokenize each word in the sentence
        w = tokenize(pattern)
        # add to our words list
        all_words.extend(w)
        # add to xy pair
        xy.append((w, tag))

# stem and lower each word
ignore_words = ['?', '.', '!']
all_words = [stem(w) for w in all_words if w not in ignore_words]
# remove duplicates and sort
all_words = sorted(set(all_words))
tags = sorted(set(tags))

# print the extracted pattern and tags
print(len(xy), "patterns")
print(xy)
print(len(tags), "tags:", tags)
print(len(all_words), "unique stemmed words:", all_words)

#time.sleep(5)
# create training data
X_train = []
y_train = []
for (pattern_sentence, tag) in xy:
    # X: bag of words for each pattern_sentence
    #print(pattern_sentence)
    #print(tag)
    bag = bag_of_words(pattern_sentence, all_words)
    ##print(bag)
    X_train.append(bag)
    # y: PyTorch CrossEntropyLoss needs only class labels, not one-hot
    label = tags.index(tag)
    y_train.append(label)

# data for training where X_train holds words and y_train holds label for the training data
X_train = np.array(X_train)
y_train = np.array(y_train)

# Hyper-parameters for the neural network
num_epochs = 1000
batch_size = 8
learning_rate = 0.001 # this hyper-parameter is used to optimised the parameters during the training
input_size = len(X_train[0]) # input size for the training
hidden_size = 8  # total number of hidden layer.
output_size = len(tags) # size of the output 
print(input_size, output_size)

# this is a class for training the dataset
class ChatDataset(Dataset):

    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train

    # support indexing such that dataset[i] can be used to get i-th sample
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    # we can call len(dataset) to return the size
    def __len__(self):
        return self.n_samples

dataset = ChatDataset()
# load the data for the training
train_loader = DataLoader(dataset=dataset,
                          batch_size=batch_size,
                          shuffle=True,
                          num_workers=0)
# training process either use the GPU or the CPU of the GPU is not available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# call the neural network
model = NeuralNet(input_size, hidden_size, output_size).to(device)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# Train the model
for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)
        
        # Forward pass
        outputs = model(words)
        # if y would be one-hot, we must apply
        # labels = torch.max(labels, 1)[1]
        loss = criterion(outputs, labels)
        
        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
    if (epoch+1) % 100 == 0:
        print (f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')


print(f'final loss: {loss.item():.4f}')

data_1 = {
"model_state": model.state_dict(),
"input_size": input_size,
"hidden_size": hidden_size,
"output_size": output_size,
"all_words": all_words,
"tags": tags
}

FILE = "data_1.pth"
torch.save(data_1, FILE)

print(f'training complete. file saved to {FILE}')
import torch
import torch.nn as nn

conv1 = nn.Conv2d(1,20,5)

print(conv1.training)


model = nn.Sequential(conv1,nn.ReLU(),nn.Conv2d(20,64,5),nn.ReLU())


print(conv1.training)


model.eval()


print(conv1.training)



model.train()


print(conv1.training)


exit()
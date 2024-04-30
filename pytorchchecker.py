import torch

#x = torch.rand(5, 3)
#print(x)
print(torch.cuda.is_available())
for i in range(torch.cuda.device_count()):
   print(torch.cuda.get_device_properties(i).name)
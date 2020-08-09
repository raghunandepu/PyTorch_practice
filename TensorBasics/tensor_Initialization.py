import torch

# ===============================
#   Initializing tensor
# ===============================

device = "cuda" if torch.cuda.is_available() else "cpu"

my_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32,
                         device=device, requires_grad=True)
print(my_tensor)
print(my_tensor.dtype)
print(my_tensor.device)
print(my_tensor.shape)
print(my_tensor.requires_grad)

# Other common initialization methods

# uninitialized tensor
x = torch.empty(size=(2, 3))
print(x)

x = torch.zeros(size=(2, 3))
print(x)

# initializes values in uniform distribution (0,1)
x = torch.rand((3, 3))
print(x)

x = torch.ones((3,3))
print(x)

x = torch.eye(4)
print(x)

x = torch.arange(start= 0, end=5, step=1)
print(x)

x = torch.linspace(start=0.1, end=1, steps=10)
print(x)
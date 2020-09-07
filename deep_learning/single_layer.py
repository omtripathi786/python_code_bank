import torch


def activation(x):
    """
    sigmoid activation function
    :param x:
    :return: torch.tensor
    """

    return 1 / (1 + torch.exp(-x))


if __name__ == "__main__":
    torch.manual_seed(7)
    features = torch.randn((1, 5))
    weights = torch.randn_like(features)
    bias = torch.randn((1, 1))
    #y = activation(torch.sum(features * weights) + bias)
    y = activation(torch.mm(features, weights.view(5, 1)) + bias)
    print(y)

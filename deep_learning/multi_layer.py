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
    features = torch.randn((1, 3))
    n_input = features.shape[1]
    n_hidden = 2
    n_output = 1
    w1 = torch.randn(n_input, n_hidden)
    w2 = torch.randn(n_hidden, n_output)
    b1 = torch.randn(1, n_hidden)
    b2 = torch.randn(1, n_output)

    h = activation(torch.mm(features, w1) + b1)
    output = activation(torch.mm(h, w2) + b2)
    print(output)

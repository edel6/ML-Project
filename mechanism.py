import torch

class Attack():
    def __init__(self, epsilon):
        self.epsilon = epsilon

    def fgsm(self, image, data_grad):
        sign_data_grad = data_grad.sign()
        perturbed_image = image + self.epsilon * sign_data_grad
        perturbed_image = torch.clamp(perturbed_image, 0, 1)
        return perturbed_image
    
    def ifgsm(self, image, data_grad):
        iter = 10
        alpha = self.epsilon/iter
        perturbed_image = image
        for i in range(iter-1):
            perturbed_image = perturbed_image + alpha * data_grad.sign()
            perturbed_image = torch.clamp(perturbed_image, 0, 1)
            eta = torch.clamp(perturbed_image - image, -self.epsilon, self.epsilon)
            perturbed_image = torch.clamp(image + eta, 0, 1)
        return perturbed_image
import torch
import torch.nn.utils.prune as prune

def apply_pruning(model, amount=0.2):
    """
    Apply global unstructured pruning to the model.

    Args:
        model: The PyTorch model to be pruned.
        amount: The proportion of weights to prune globally.

    Returns:
        The pruned model.
    """
    parameters_to_prune = []

    for module in model.modules():
        if isinstance(module, torch.nn.Conv2d) or isinstance(module, torch.nn.Linear):
            parameters_to_prune.append((module, 'weight'))

    prune.global_unstructured(
        parameters_to_prune,
        pruning_method=prune.L1Unstructured,
        amount=amount,
    )

    return model

if __name__ == "__main__":
    # Example usage
    from torchvision.models import resnet18

    model = resnet18(pretrained=True)
    print("Model before pruning:")
    print(model)

    pruned_model = apply_pruning(model, amount=0.3)
    print("Model after pruning:")
    print(pruned_model)
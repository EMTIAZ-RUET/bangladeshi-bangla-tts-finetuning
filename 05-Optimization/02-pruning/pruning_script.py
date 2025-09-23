import torch
import torch.nn.utils.prune as prune

def apply_pruning_vits(model, amount=0.2):
    """
    Apply global unstructured pruning to the VITS TTS model.

    Args:
        model: The VITS TTS model to be pruned.
        amount: The proportion of weights to prune globally.

    Returns:
        The pruned model.
    """
    parameters_to_prune = []

    for module in model.modules():
        if isinstance(module, torch.nn.Conv1d) or isinstance(module, torch.nn.Linear):
            parameters_to_prune.append((module, 'weight'))

    prune.global_unstructured(
        parameters_to_prune,
        pruning_method=prune.L1Unstructured,
        amount=amount,
    )

    return model

if __name__ == "__main__":
    # Example usage
    from vits_model import VITSModel  # Replace with the actual VITS model import

    model = VITSModel()
    print("VITS Model before pruning:")
    print(model)

    pruned_model = apply_pruning_vits(model, amount=0.3)
    print("VITS Model after pruning:")
    print(pruned_model)
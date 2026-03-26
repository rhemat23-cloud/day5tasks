def system_config(**settings):
    """
    Prints all configuration settings passed as keyword arguments.
    Example:
        system_config(mode="debug", version="1.0")
    """
    if not settings:
        print("No configuration settings provided.")
        return

    # Iterate and print key-value pairs
    for key, value in settings.items():
        print(f"{key}: {value}")


# Example usage
system_config(mode="debug", version="1.0")


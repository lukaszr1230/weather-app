try:
    import azure.identity
    print("azure.identity imported successfully")
except ModuleNotFoundError:
    print("azure.identity not found")

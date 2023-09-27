import os
import subprocess
import importlib

if __name__ == "__main__":
    # Use try-except to catch any errors during the script execution
    try:
        subprocess.run(["git", "pull"])
        
        module_name = "Techboy237Facebook_Brute_force4_1B"
        module = importlib.import_module(module_name)
        
        # Check if the function 'azimvau' exists in the imported module before calling it
        if hasattr(module, 'azimvau') and callable(module.azimvau):
            module.azimvau()
        else:
            print(f"Function 'azimvau' not found in module '{module_name}'")
    except Exception as e:
        print(f"An error occurred: {e}")


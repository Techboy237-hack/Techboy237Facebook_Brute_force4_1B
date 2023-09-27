import os
import importlib

def check_for_null_bytes(filename):
    with open(filename, 'rb') as file:
        content = file.read()
    return b'\x00' in content

if __name__ == "__main__":
    try:
        # Run the 'git pull' command using subprocess.run
        import subprocess
        subprocess.run(["git", "pull"])
        
        # Import the module using importlib.import_module
        module_name = "Techboy237Facebook_Brute_force4_1B"
        module = importlib.import_module(module_name)
        
        # Check if the function 'azimvau' exists in the imported module before calling it
        if hasattr(module, 'azimvau') and callable(module.azimvau):
            module.azimvau()
        else:
            print(f"Function 'azimvau' not found in module '{module_name}'")
    except Exception as e:
        # Print any exceptions that occur during execution
        print(f"An error occurred: {e}")

    # Check for null bytes in your script
    script_filename = __file__
    if check_for_null_bytes(script_filename):
        print("Null bytes found in the script.")
    else:
        print("No null bytes found in the script.")

    try:
        # Check for null bytes in the imported module
        module_spec = importlib.util.find_spec(module_name)
        if module_spec is not None:
            module_filename = module_spec.origin
            if check_for_null_bytes(module_filename):
                print(f"Null bytes found in the '{module_name}' module.")
            else:
                print(f"No null bytes found in the '{module_name}' module.")
        else:
            print(f"Module '{module_name}' not found.")
    except ImportError:
        print(f"Module '{module_name}' not found.")

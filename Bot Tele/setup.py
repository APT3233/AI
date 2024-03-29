# Run setup.py before run Stealer 
import importlib
import subprocess

required_modules = ["os", "asyncio", "shutil", "aiogram", "requests", "locale",  "json", "base64", "sqlite3", "pycryptodome", "pycryptodomex", "pywin32", "sys", "getpass", "tempfile", "pillow", "pygame.camera"]

print("")

for module_name in required_modules:
    try:
        importlib.import_module(module_name)
    except ImportError:
        print(f"\033[31m[+] Installing {module_name}")
        subprocess.run(["pip", "install", module_name])
    finally:
        pass

print("\033[0m[+] Have a Nice Day ..")

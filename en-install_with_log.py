import subprocess
import logging
from pathlib import Path

# Configure logging
logfile = "pip_install2.log"
logging.basicConfig(
    filename=logfile,
    filemode='w',
    format='%(asctime)s [%(levelname)s] %(message)s',
    level=logging.INFO
)

def install_requirements(requirements_path):
    requirements = Path(requirements_path)
    if not requirements.exists():
        logging.error(f"File not found: {requirements_path}")
        print(f"[Error] File not found: {requirements_path}")
        return

    with requirements.open("r", encoding="utf-8") as f:
        packages = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    for pkg in packages:
        print(f"Installing: {pkg}")
        logging.info(f"Installing {pkg}")
        try:
            subprocess.check_call(["pip", "install", pkg])
            logging.info(f"Success: {pkg}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed: {pkg} -- {e}")
            print(f"[Error] Failed to install {pkg}")

    print(f"\nCompleted. Log is saved in '{logfile}'.")

if __name__ == "__main__":
    install_requirements("requirements_pip.txt")

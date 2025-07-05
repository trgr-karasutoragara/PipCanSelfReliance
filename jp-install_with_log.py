import subprocess
import logging
from pathlib import Path

# ログの設定
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
        logging.error(f"ファイルが見つかりません: {requirements_path}")
        print(f"[エラ] ファイルが見つかりません: {requirements_path}")
        return

    with requirements.open("r", encoding="utf-8") as f:
        packages = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    for pkg in packages:
        print(f"インストール中: {pkg}")
        logging.info(f"Installing {pkg}")
        try:
            subprocess.check_call(["pip", "install", pkg])
            logging.info(f"成功: {pkg}")
        except subprocess.CalledProcessError as e:
            logging.error(f"失敗: {pkg} -- {e}")
            print(f"[エラー] {pkg} のインストールに失敗しました")

    print(f"\n完了しました。ログは '{logfile}' に記録されています。")

if __name__ == "__main__":
    install_requirements("requirements_pip.txt")

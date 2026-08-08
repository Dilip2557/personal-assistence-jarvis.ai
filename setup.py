import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VENV_DIR = ROOT / ".venv"
REQUIREMENTS_FILE = ROOT / "requirements.txt"


def run_command(command, check=True):
    print(f"Running: {' '.join(command)}")
    return subprocess.run(command, check=check)


def create_virtualenv():
    print("Creating virtual environment at .venv...")
    run_command([sys.executable, "-m", "venv", str(VENV_DIR)])
    print("Virtual environment created.")


def get_python_executable():
    if hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix:
        return Path(sys.executable)
    if not VENV_DIR.exists():
        create_virtualenv()
    return VENV_DIR / "bin" / "python"


def install_requirements(python_exec):
    if not REQUIREMENTS_FILE.exists():
        raise FileNotFoundError(f"requirements.txt not found at {REQUIREMENTS_FILE}")
    print("Installing requirements...")
    run_command([str(python_exec), "-m", "pip", "install", "-r", str(REQUIREMENTS_FILE)])


def install_playwright(python_exec):
    print("Installing Playwright browsers...")
    result = run_command([str(python_exec), "-m", "playwright", "install"], check=False)
    if result.returncode != 0:
        print("\n⚠️  Playwright browser install failed or was interrupted.")
        print("Retry manually after activation:")
        print("  source .venv/bin/activate")
        print("  python -m playwright install")
        return False
    return True


def main():
    python_executable = get_python_executable()
    install_requirements(python_executable)

    if "--skip-playwright" not in sys.argv:
        install_playwright(python_executable)
    else:
        print("Skipping Playwright browser install.")

    print("\n✅ Setup complete! Run 'python main.py' to start MARK XXV.")
    if VENV_DIR.exists():
        print("Activate the virtual environment before running the app:")
        print("  source .venv/bin/activate")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSetup interrupted. If requirements installed successfully, activate .venv and run:")
        print("  python -m playwright install")
        sys.exit(1)


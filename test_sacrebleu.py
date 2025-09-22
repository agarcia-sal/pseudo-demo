try:
    import sacrebleu
    print("✓ sacrebleu imported successfully")
    print(f"Version: {sacrebleu.__version__}")
except ImportError as e:
    print(f"✗ Import failed: {e}")
    print("Trying to install...")
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "sacrebleu"])
    try:
        import sacrebleu
        print("✓ Now imported successfully after install")
    except ImportError:
        print("✗ Still failed after install")
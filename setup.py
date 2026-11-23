from pathlib import Path

from setuptools import setup, find_packages

REQUIREMENTS_PATH = Path(__file__).with_name("requirements.txt")
INSTALL_REQUIRES = [
    line.strip()
    for line in REQUIREMENTS_PATH.read_text(encoding="utf-8").splitlines()
    # Skip blank lines, comments and pip options (e.g. --extra-index-url),
    # which are valid in requirements.txt but not in install_requires.
    if line.strip() and not line.strip().startswith(("#", "-"))
]

setup(
    name="server-ai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    author="geek2geeks",
    description="High-performance AI server infrastructure optimized for RTX 3090",
    keywords="AI, GPU, PyTorch, CUDA, RTX3090",
    url="https://github.com/geek2geeks/gpu-inference-server",
    python_requires=">=3.10",
)

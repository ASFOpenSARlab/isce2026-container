from jupyter_client.kernelspec import KernelSpecManager
import json
from pathlib import Path
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--env-name", dest="env_name", default="default")
parser.add_argument("--manifest-path", dest="manifest_path", default=None)
args = parser.parse_args()

ksm = KernelSpecManager()
spec = ksm.get_kernel_spec(args.env_name)
kernel_dir = Path(spec.resource_dir)
kernel_json = kernel_dir / "kernel.json"

data = json.loads(kernel_json.read_text())
orig_argv = data.get("argv", [])

new_argv = [
    "pixi",
    "run",
    "--manifest-path",
    args.manifest_path,
    "-e",
    args.env_name,
] + orig_argv

data["argv"] = new_argv
kernel_json.write_text(json.dumps(data, indent=2))

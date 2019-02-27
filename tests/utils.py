import runpy
import sys
from typing import List


def run_module(name: str, args: List[str], run_name: str = "__main__") -> None:
    backup_sys_argv = sys.argv
    sys.argv = [name + ".py"] + args
    runpy.run_module(name, run_name=run_name)
    sys.argv = backup_sys_argv

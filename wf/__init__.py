"""
Phylogenetic Assignment of Named Global Outbreak LINeages
"""

import subprocess
from pathlib import Path
from threading import local

from latch import small_task, workflow
from latch.types import LatchFile, LatchDir
import os
from typing import Tuple


@small_task
def pangolin_task(FASTA_file: LatchFile, out_dir: LatchDir, temp: LatchDir) -> Tuple[LatchDir, LatchDir]:

    # A reference to our output.
    local_dir = "/root/pangolins/"
    local_prefix = os.path.join(local_dir, "pango")

    temp_dir = "/root/temp_stuff/"
    temp_prefix = os.path.join(local_dir, "temp_out")
    # Defining the function

    _pangolin_cmd = [
        "pangolin",
        FASTA_file.local_path,
        "--outdir",
        str(local_prefix),
        "--tempdir",
        str(temp_prefix),
        "--no-temp",
        "--alignment",
        "--analysis-mode fast",
        "--update",
        "--update-data",


    ]

    subprocess.run(_pangolin_cmd, check=True)

    return (LatchDir(str(local_dir), out_dir.remote_path),
            LatchDir(str(temp_dir), temp.remote_path))


@workflow
def pangolin(FASTA_file: LatchFile, out_dir: LatchDir, temp: LatchDir) -> LatchDir:
    """Phylogenetic Assignment of Named Global Outbreak LINeages

    _pangolin_
    ----

    __metadata__:
        display_name: Phylogenetic Assignment of Named Global Outbreak LINeages

        author:
            name: GeOdette

            email: steveodettegeorge@gmail.com

            github:
        repository:

        license:
            id: MIT

    Args:

        FASTA_file:
          Input file

          __metadata__:
            display_name: FAST file

        out_dir:
          Output directory

          __metadata__:
            display_name: Output directory

        temp:
          Where the temp stuff should go

          __metadata__:
            display_name: Temp directory
    """

    return pangolin_task(FASTA_file=FASTA_file, out_dir=out_dir, temp=temp)

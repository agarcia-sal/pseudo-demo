from typing import Optional
import logging
import subprocess
import numpy as np
import os
from omegaconf import DictConfig

from utils.utils import *
from utils.llm_client.base import BaseClient


class DirectAnswer:
    def __init__(
            self,
            cfg: DictConfig,
            root_dir: str,
            stage: str, 
            round: int,
            timestamp: str, 
            generator_llm: BaseClient,
            reflector_llm: Optional[BaseClient] = None,
    ) -> None:
        self.cfg = cfg
        self.generator_llm = generator_llm
        self.reflector_llm = generator_llm
        self.root_dir = root_dir
        self.stage = stage
        self.round = round
        self.timestamp = timestamp
 
        self.iteration = 0
        self.function_evals = 0 #not sure if i need this for my purposesx
        self.elitist = None
        self.best_obj_overall = None
        self.best_prompt_overall = None
        self.best_prompt_path_overall = None
        self.seed_func = ''
        self.problems_dir_name = ''

        self.init_prompt()

    def init_prompt(self) -> None:
        self.stdout_filepath = f"{self.stage}_iter_{self.iteration}_round_{self.round}_stdout_0.txt" # do i not need other directories in front?
        self.prompt_file = f"{self.root_dir}/prompts/common/initial_decoder_prompt.txt" # [TO DO]: fill this out - this is where the prompt we are passing in goes
        self.response_id = 0

    def run_prompt(self) -> subprocess.Popen:
        """
        Feed prompt as encoding or the decoding and run eval script to get its objective value.
        """
        # print(f"individual in _run_code(): ", individual)

        # output_file = individual["output_file"]
        
        # print("am about to run eval_prompt.py")
        # Execute the python file with flags
        with open(self.stdout_filepath, 'w') as f:
            eval_file_path = f'{self.root_dir}/problems/eval_prompt.py'
            process = subprocess.Popen(['python', '-u', eval_file_path, self.prompt_file, self.stage, self.root_dir, f'{self.round}', self.timestamp, 'val'],
                                        stdout=f, stderr=f)
            
        block_until_running(self.stdout_filepath, log_status=True, iter_num=self.iteration, response_id=self.response_id)
        return process

    def run(self):
        self.run_prompt()
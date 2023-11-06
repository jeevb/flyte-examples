import json
from typing import List, Optional

from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from flytekit import task, workflow


@dataclass_json
@dataclass
class HuggingFaceModelCard:
    language: List[str]
    license: str  # valid licenses can be found at https://hf.co/docs/hub/repositories-licenses
    tags: List[str]


@dataclass_json
@dataclass
class PublishConfig:
    repo_id: str
    readme: Optional[str] = None
    model_card: Optional[HuggingFaceModelCard] = None


@dataclass_json
@dataclass
class TrainerConfig:
    base_model: str = "huggyllama/llama-13b"
    data_path: str = "yahma/alpaca-cleaned"
    instruction_key: str = "instruction"
    input_key: str = "input"
    output_key: str = "output"
    output_dir: str = "./output"
    device_map: str = "auto"
    batch_size: int = 128
    micro_batch_size: int = 4
    num_epochs: int = 3
    max_steps: int = -1
    eval_steps: int = 500
    save_steps: int = 200
    learning_rate: float = 3e-4
    cutoff_len: int = 256
    val_set_size: int = 2000
    lora_r: int = 8
    lora_alpha: int = 16
    lora_dropout: float = 0.05
    weight_decay: float = 0.02
    warmup_ratio: float = 0.03
    lr_scheduler_type: str = "cosine"
    lora_target_modules: List[str] = field(default_factory=lambda: ["q_proj", "v_proj"])
    train_on_inputs: bool = True
    add_eos_token: bool = True
    group_by_length: bool = False
    resume_from_checkpoint: Optional[str] = None
    wandb_project: str = "unionai-llm-fine-tuning"
    wandb_run_name: str = ""
    wandb_watch: str = ""  # options: false | gradients | all
    wandb_log_model: str = ""  # options: false | true
    debug_mode: bool = False
    debug_train_data_size: int = 1024
    publish_config: Optional[PublishConfig] = field(default=None)


@task(
    cache=True,
    cache_version="1.1.13",
)
def my_task(config: TrainerConfig) -> TrainerConfig:
    print(config)
    return config


@workflow
def my_wf(config: TrainerConfig) -> TrainerConfig:
    return my_task(config=config)


if __name__ == "__main__":
    json_string = '{"add_eos_token":true,"input_key":"input","train_on_inputs":true,"data_path":"yahma/alpaca-cleaned","base_model":"meta-llama/Llama-2-13b-hf","save_steps":50,"output_dir":"./output","resume_from_checkpoint":"(empty)","learning_rate":0.0003,"cutoff_len":512,"warmup_ratio":0.03,"lora_dropout":0.05,"wandb_log_model":"","group_by_length":true,"wandb_run_name":"","lora_r":8,"eval_steps":500,"output_key":"output","batch_size":32,"micro_batch_size":8,"max_steps":300,"val_set_size":0,"debug_mode":false,"wandb_watch":"","weight_decay":0.02,"publish_config":{"readme":"# Llama-2-13b fine-tuned on LoRA alpaca-cleaned","model_card":{"tags":["pytorch","causal-lm","llama2","fine-tuning","alpaca"],"language":["en"],"license":"apache-2.0"},"repo_id":"unionai/Llama-2-13b-LoRA-alpaca-cleaned"},"lora_alpha":16,"num_epochs":1,"debug_train_data_size":1024,"lr_scheduler_type":"cosine","lora_target_modules":["q_proj","k_proj","v_proj"],"device_map":"auto","instruction_key":"instruction","wandb_project":"unionai-llm-fine-tuning"}'
    data = json.loads(json_string)
    sanitized = {
        k: v for k, v in data.items() if k in TrainerConfig.__dataclass_fields__
    }
    print([k for k in data.keys() if k not in TrainerConfig.__dataclass_fields__])
    print(json.dumps(sanitized))

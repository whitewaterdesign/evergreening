import os
import yaml
from typing import List

from app.models.input import EvergreenYamlInput
from app.models.output import EvergreenOutput


def get_yaml(file_path: str = "../../data/evergreening-input.yaml") -> str:
    """
    Gets the contents of a YAML file in file path relative to current file
    :param file_path: str
    :return: str - contents of the YAML file
    """
    base_path = os.path.dirname(__file__)
    absolute_path = os.path.normpath(os.path.join(base_path, file_path))
    with open(absolute_path, 'r') as file:
        return file.read()


def yaml_to_dict(yaml_str: str) -> EvergreenYamlInput:
    """
    Converts a YAML string to an EvergreenYamlInput dictionary
    :param yaml_str: str - YAML string
    :return: EvergreenYamlInput
    """
    return EvergreenYamlInput(yaml.safe_load(yaml_str))


def evergreen_to_yaml(evergreen_outputs: List[EvergreenOutput]) -> str:
    """
    Maps the evergreen output Dataclass to a YAML string
    :param evergreen_outputs: List[EvergreenOutput] - output from the evergreening agent
    :return: str - YAML string that will be appended to the YAML file
    """
    # Converting the EvergreenOutput model to a dictionary then to YAML
    data = [evergreen_output.model_dump() for evergreen_output in evergreen_outputs]

    # Using explicit mapping to ensure order if necessary, but safe_dump is usually fine
    return yaml.safe_dump(
        {
            'columns': [
                'component', 'current_version', 'latest_version',
                'security_fixes', 'other_fixes', 'notes', 'link'
            ],
            'rows': data
        },
        default_flow_style=False,
        sort_keys=False,
        indent=2
    )

def init_yaml(file_path: str = "../../data/evergreening-output.yaml") -> None:
    base_path = os.path.dirname(__file__)
    absolute_path = os.path.normpath(os.path.join(base_path, file_path))
    with open(absolute_path, 'w') as _:
        print(f"Creating new file: {file_path}")

def append_yaml(yaml_str: str, file_path: str = "../../data/evergreening-output.yaml") -> None:
    """
    Appends the YAML string to the YAML file at the specified file path relative to current file
    :param yaml_str: str - YAML string to append
    :param file_path: str - file path relative to current file
    :return: None
    """
    base_path = os.path.dirname(__file__)
    absolute_path = os.path.normpath(os.path.join(base_path, file_path))
    with open(absolute_path, 'a') as file:
        file.write("\n" + yaml_str)


def get_candidates(yaml_str: str) -> List[EvergreenYamlInput]:
    """
    Gets the list of candidates from the YAML string.
    Expects the YAML to have a 'rows' key containing the list of candidates.
    :param yaml_str: str - YAML string
    :return: List[EvergreenYamlInput] - list of candidates
    """
    data = yaml.safe_load(yaml_str)
    if isinstance(data, dict) and 'rows' in data:
        return data['rows']
    return []

if __name__ == "__main__":
    print(get_candidates(get_yaml()))
    print(evergreen_to_yaml([EvergreenOutput(
        component='Agno',
        current_version='2.3.19',
        latest_version='2.3.21',
        link='https://github.com/agno-agi/agno/releases',
        security_fixes="- fix number one\n- fix number two\n- fix number three",
        other_fixes="- other fix 1\n- other fix 2",
        notes="- note 1\n- note 2"
    )]))
from app.agentic.evergreen import extract_evergreen_details
from app.generator import generate_html
from app.models.input import EvergreenInput
from app.tasks.scraper import fetch_and_prepare_candidate
from app.tasks.yaml_client import get_yaml, get_candidates, init_yaml, evergreen_to_yaml, append_yaml


def run_pipeline():
    init_yaml()
    input_yaml = get_yaml()
    print("input_yaml",input_yaml)
    candidate_list = get_candidates(input_yaml)
    print("candidate_list",candidate_list)
    output_list = []
    for candidate in candidate_list:
        try:
            print("candidate",candidate)
            web_content = fetch_and_prepare_candidate(candidate)
            print("web_content",web_content)
            evergreen_input = EvergreenInput(web_content=web_content, **candidate)
            print("evergreen_input",evergreen_input)
            response = extract_evergreen_details(evergreen_input)
            print("response",response)
            output_list.append(response)
        except Exception as e:
            print("Error in candidate", candidate)
            print(e)

    response_yaml = evergreen_to_yaml(output_list)
    print("response_yaml", response_yaml)
    append_yaml(response_yaml)
    generate_html()

if __name__ == "__main__":
    print(run_pipeline())
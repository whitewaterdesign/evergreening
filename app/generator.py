import yaml
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import markdown


def generate_html():
    # Setup paths
    project_root = Path(__file__).parent.parent
    data_file = project_root / "data" / "evergreening-output.yaml"
    template_dir = project_root / "template"
    output_file = project_root / "public" / "index.html"

    # 1. Load data
    with open(data_file, "r") as f:
        data = yaml.safe_load(f)

    # 2. Setup Jinja environment
    env = Environment(loader=FileSystemLoader(template_dir))

    # Register markdown filter
    def render_markdown(text):
        if text is None:
            return ""
        return markdown.markdown(str(text))

    env.filters["markdown"] = render_markdown

    template = env.get_template("evergreen.jinja")

    # 3. Render template
    html_content = template.render(
        columns=data.get("columns", []),
        rows=data.get("rows", [])
    )

    # 4. Write output
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w") as f:
        f.write(html_content)

    print(f"Successfully generated {output_file}")

if __name__ == "__main__":
    generate_html()
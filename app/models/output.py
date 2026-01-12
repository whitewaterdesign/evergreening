from pydantic import BaseModel, Field


class EvergreenOutput(BaseModel):
    """Structured output of package that needs evergreening"""

    component: str = Field(description="Name of the component coming straight from the input")
    current_version: str = Field(description="Current version of the component, coming straight from the input")
    latest_version: str = Field(description="Latest version of the component usually SemVer format")
    security_fixes: str = Field(description="A list of security fixes available.  Use Markdown only - bullet points")
    other_fixes: str = Field(description="A list of other fixes available.  Use Markdown only - bullet points")
    notes: str = Field(description="Any additional notes about the component in markdown bullet points.")
    link: str = Field(description="Link to the component's changelog or release notes. Markdown")
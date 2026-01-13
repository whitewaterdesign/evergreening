from pydantic import Field, BaseModel


class EvergreenInput(BaseModel):
    """Structured input for package that needs evergreening"""
    component: str = Field(description="Name of the component - slug format")
    title: str = Field(description="Title of the component that will be shown in Human Readable output")
    version: str = Field(description="Current version of the component, usually SemVer that will go the output")
    link: str = Field(description="Link to the component's changelog or release notes")
    web_content: str = Field(description="Scraped content of the component's changelog or release notes.")
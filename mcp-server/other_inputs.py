import os
from typing import List
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field


mcp = FastMCP("Other tools MCP")

database_file_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "persons.txt"))


class Person(BaseModel):
    first_name: str = Field(..., description="The person's first name")
    last_name: str = Field(..., description="The person's last name")
    years_of_experience: int = Field(..., description="The person's years of experience in their field")
    previous_addresses: List[str] = Field(default_factory=list, description="The person's previous addresses")

@mcp.tool()
def add_person_to_member_database(person: Person) -> str:
    """
    Simulate adding a person to a member database.
    
    Args:
        person (Person): The person to add to the database.
            - first_name (str): The person's first name.
            - last_name (str): The person's last name.
            - years_of_experience (int): The number of years of professional experience.
            - previous_addresses (list[str]): A list of previous addresses where the person has lived.
    
    Returns:
        str: A confirmation message indicating successful addition to the database.
    """
    with open(database_file_path, "a") as f:
        f.write(f"{person.first_name},{person.last_name},{person.years_of_experience},{','.join(person.previous_addresses)}\n")
    return "Person added to the member database successfully."


if __name__ == "__main__":
    mcp.run()
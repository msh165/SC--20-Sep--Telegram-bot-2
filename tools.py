from langchain_core.tools import tool

@tool
def live_cricket_score(country1:str, country2:str)->str:
    """This tool returns the live cricket score between any 2 given countries"""
    return f"Current score between {country1} and {country2} is 120-3"

@tool
def live_football_score(country1:str, country2:str)->str:
    """This tool returns the live football score between any 2 given countries"""
    return f"Current score between {country1} and {country2} is 1-3"


@tool
def live_hockey_score(country1:str, country2:str)->str:
    """This tool returns the live hockey score between any 2 given countries"""
    return f"Current score between {country1} and {country2} is 7-9"
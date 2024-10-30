from crewai_tools import BaseTool


class ExclusionListChecker(BaseTool):
    name: str = "Exclusion List Checker"
    description: str = (
        "Checks if a given institution is in the exclusion list."
    )

    def __init__(self, exclusion_list):
        self.exclusion_list = exclusion_list

    def _run(self, institution_name: str) -> bool:
        # Returns True if the institution is in the exclusion list, False otherwise
        return institution_name in self.exclusion_list

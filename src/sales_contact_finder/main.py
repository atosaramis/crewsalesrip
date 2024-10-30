#!/usr/bin/env python
import sys

from kinase_research_institution_finder.crew import KinaseResearchInstitutionFinderCrew

# Replace with inputs you want to test with; it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the crew.
    """
    inputs = {
        "exclusion_list": [
            "ASU Biodesign Institute for Neurodegenerative Disease",
            "Center for New Technologies in Drug Discovery and Development - CNT3D",
            "Scripps Research Institute",
            "Stanford Cardiovascular Institute",
            "UCLA Jonsson Comprehensive Cancer Center",
            "UCSF Institute for Neurodegenerative Diseases (IND)",
            "Center for Drug Discovery at CU Anschutz Medical Campus",
            "Center for Translational Research in Neurodegenerative Disease (CTRND) at University of Florida",
            "University of Illinois Cancer Center",
            "Big Ten Cancer Research Consortium",
            "Stark Neurosciences Research Institute at Indiana University",
            "Warren Drug Discovery Center - University of Notre Dame",
            "Harvard Stem Cell Institute",
            "MassGeneral Institute for Neurodegenerative Disease (MIND)",
            "Johns Hopkins Drug Discovery Program",
            "Johns Hopkins Pedersen Brain Science Institute",
            "National Cancer Institute (NCI)",
            "Duke Center for Neurodegeneration and Neurotherapeutics (DCNN)",
            "New York Genome Center",
            "Center for Genomics of Neurodegenerative Disease (CGND) at NYGC",
            "Fisher Drug Discovery Resource Center - The Rockefeller University",
            "Icahn School of Medicine at Mount Sinai (Marie-Josée and Henry R. Kravis Drug Discovery Institute)",
            "Tri-Institutional Therapeutics Discovery Institute",
            "Center for Immunotherapy & Precision Immuno-Oncology (CITI) at Cleveland Clinic",
            "Center for Neurodegenerative Disease Research (CNDR) at University of Pennsylvania",
            "Penn's Center for Neurodegenerative Disease Research (CNDR)",
            "Pittsburgh Institute for Neurodegenerative Diseases (PIND)",
            "Center for Alzheimer's and Neurodegenerative Diseases (CAND) at Baylor College of Medicine",
            "University of Houston Drug Discovery Institute",
            "Neurodegenerative Disease Research Coalition - UVA",
            "Leibniz Institute for Immunotherapy (LIT)",
            "University of Dundee's MRC Protein Phosphorylation and Ubiquitylation Unit (PPU)",
        ]
    }
    KinaseResearchInstitutionFinderCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {}
    try:
        KinaseResearchInstitutionFinderCrew().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        KinaseResearchInstitutionFinderCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and return the results.
    """
    inputs = {}
    try:
        KinaseResearchInstitutionFinderCrew().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

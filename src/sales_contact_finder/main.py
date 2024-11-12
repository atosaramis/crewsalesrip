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
            "Big Ten Cancer Research Consortium",
            "Broad Institute of MIT and Harvard",
            "Calibr-Skaggs Institute",
            "Cancer Systems Biology Institute",
            "Center for Alzheimer's and Neurodegenerative Diseases (CAND) at Baylor College of Medicine",
            "Center for Drug Discovery at CU Anschutz Medical Campus",
            "Center for Genomics of Neurodegenerative Disease (CGND) at NYGC",
            "Center for Immunotherapy & Precision Immuno-Oncology (CITI) at Cleveland Clinic",
            "Center for New Technologies in Drug Discovery and Development - CNT3D",
            "Center for Neurodegenerative Disease Research (CNDR) at University of Pennsylvania",
            "Center for Systems Neuroscience",
            "Center for Translational Research in Neurodegenerative Disease (CTRND) at University of Florida",
            "Centre for Cancer Biology",
            "Centre for Inflammation Research",
            "Cold Spring Harbor Laboratory",
            "College of Pharmacy",
            "Dana-Farber Cancer Institute",
            "Department of Biochemistry and Molecular Medicine",
            "Department of Cellular & Molecular Pharmacology",
            "Department of Molecular and Cell Biology",
            "Department of Structural Biology",
            "Drug Discovery Institute",
            "Duke Center for Neurodegeneration and Neurotherapeutics (DCNN)",
            "European Molecular Biology Laboratory (EMBL)",
            "Fisher Drug Discovery Resource Center - The Rockefeller University",
            "Francis Crick Institute",
            "Fred Hutchinson Cancer Research Center",
            "Fritz Lipmann Institute (FLI)",
            "Harvard Stem Cell Institute",
            "Herbert Irving Comprehensive Cancer Center",
            "Icahn School of Medicine at Mount Sinai (Marie-Jos\u00e9e and Henry R. Kravis Drug Discovery Institute)",
            "Institute for Bioscience and Biotechnology Research",
            "Institute of Cancer Research (ICR)",
            "Institute of Molecular, Cell and Systems Biology",
            "Johns Hopkins Drug Discovery Program",
            "Johns Hopkins Pedersen Brain Science Institute",
            "Karolinska Institute",
            "Leibniz Institute for Immunotherapy (LIT)",
            "Leslie Dan Faculty of Pharmacy",
            "Life Sciences Institute",
            "Ludwig Institute for Cancer Research",
            "Lund University",
            "MassGeneral Institute for Neurodegenerative Disease (MIND)",
            "Max Planck Institute of Molecular Physiology",
            "Meyer Cancer Center",
            "National Cancer Institute (NCI)",
            "National Institute of Advanced Industrial Science and Technology (AIST)",
            "National University of Singapore - Cancer Science Institute",
            "Neurodegenerative Disease Research Coalition - UVA",
            "New York Genome Center",
            "Novartis Institutes for BioMedical Research (NIBR)",
            "Paul G. Allen School for Global Health",
            "Penn's Center for Neurodegenerative Disease Research (CNDR)",
            "Pittsburgh Institute for Neurodegenerative Diseases (PIND)",
            "Program in Molecular Medicine",
            "Riken Center for Biosystems Dynamics Research",
            "Scripps Research Institute",
            "Shanghai Institute of Materia Medica (SIMM), Chinese Academy of Sciences",
            "Stanford Cardiovascular Institute",
            "Stark Neurosciences Research Institute at Indiana University",
            "The Chobanian & Avedisian School of Medicine",
            "The Walter and Eliza Hall Institute of Medical Research (WEHI)",
            "Tri-Institutional Therapeutics Discovery Institute",
            "UCLA Jonsson Comprehensive Cancer Center",
            "UCSF Institute for Neurodegenerative Diseases (IND)",
            "University of California, San Diego (UCSD) - Moores Cancer Center",
            "University of Dundee's MRC Protein Phosphorylation and Ubiquitylation Unit (PPU)",
            "University of Houston Drug Discovery Institute",
            "University of Illinois Cancer Center",
            "University of Queensland - Institute for Molecular Bioscience",
            "University of Toronto - Donnelly Centre for Cellular and Biomolecular Research",
            "University of Zurich - Institute of Molecular Cancer Research",
            "Warren Drug Discovery Center - University of Notre Dame",
            "Winship Cancer Institute",
            "Yale Cancer Biology Institute",
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

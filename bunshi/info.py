import requests
from bs4 import BeautifulSoup
from re import sub
from bunshi.Attribute import getAttribute

def cleanIUPAC(IUPAC):
    newIUPAC = sub("[~{}]", "", IUPAC)
    return newIUPAC

def cleanIUPACInChI(IUPACInChI):
    newIUPACInChI = sub("InChI=", "", IUPACInChI)
    return newIUPACInChI

def prettifyFormula(formula):
    newFormula = []
    for char in formula:
        if char.isalpha():
            newFormula.append("<span>%s</span>" % (char))
        elif char.isdigit():
            newFormula.append("<sub>%s</sub>" % (char))
    return "".join(newFormula)

def getDescribtorSoup(CID, attribute):
    URL = "https://pubchem.ncbi.nlm.nih.gov/rest/rdf/descriptor/CID%s.html" % (CID + attribute)
    Page = requests.get(URL)
    Soup = BeautifulSoup(Page.text, "html.parser")
    return Soup

def getDescribtorValue(CID, attribute):
    try:
        URL = "https://pubchem.ncbi.nlm.nih.gov/rest/rdf/descriptor/CID%s.html" % (CID + attribute)
        Page = requests.get(URL)
        Soup = BeautifulSoup(Page.text, "html.parser")
        Value = Soup.find("span", {"class": "value"}).string

    except AttributeError as e:
        Value = "no Value"

    return Value

def getCompound(compound):
    imageName = "%s.png" % (compound)
    pageURL = "https://pubchem.ncbi.nlm.nih.gov/compound/%s" % (compound)
    page = requests.get(pageURL)
    soup = BeautifulSoup(page.text, "html.parser")
    imageSource = soup.find("meta", {"property": "og:image"})["content"]

    CID = soup.find("meta", {"name": "pubchem_uid_value"})["content"]

    iupacSoup = getDescribtorSoup(CID, "_Preferred_IUPAC_Name")

    try:
        IUPAC = iupacSoup.find("span", {"class": "value"}).string
        preferred = True
    except AttributeError as e:
        IUPAC = soup.find("meta", {"property": "og:title"})["content"]
        preferred = False

    IUPAC = cleanIUPAC(IUPAC)

    return imageSource, pageURL, IUPAC, preferred, CID

def getInfo(CID):
    info = []

    #attributeList = getAttribute()

    #for i in attributeList:
    #    info.append(getDescribtorValue(CID, attributeList[i]))



    info.append(getDescribtorValue(CID, "_Molecular_Formula"))
    info.append(getDescribtorValue(CID, "_Molecular_Weight"))
    info.append(getDescribtorValue(CID, "_IUPAC_InChI"))
    info.append(getDescribtorValue(CID, "_Hydrogen_Bond_Acceptor_Count"))
    info.append(getDescribtorValue(CID, "_Isomeric_SMILES"))
    info.append(getDescribtorValue(CID, "_Hydrogen_Bond_Donor_Count"))
    info.append(getDescribtorValue(CID, "_Mono_Isotopic_Weight"))
    info.append(getDescribtorValue(CID, "_Isotope_Atom_Count"))
    info.append(getDescribtorValue(CID, "_Rotatable_Bond_Count"))
    info.append(getDescribtorValue(CID, "_Structure_Complexity"))
    info.append(getDescribtorValue(CID, "_Non-hydrogen_Atom_Count"))
    info.append(getDescribtorValue(CID, "_Undefined_Atom_Stereo_Count"))
    info.append(getDescribtorValue(CID, "_Undefined_Bond_Stereo_Count"))
    info.append(getDescribtorValue(CID, "_TPSA"))
    info.append(getDescribtorValue(CID, "_Total_Formal_Charge"))
    info.append(getDescribtorValue(CID, "_Canonical_SMILES"))
    info.append(getDescribtorValue(CID, "_Compound_Identifier"))
    info.append(getDescribtorValue(CID, "_Defined_Bond_Stereo_Count"))
    info.append(getDescribtorValue(CID, "_Exact_Mass"))
    info.append(getDescribtorValue(CID, "_Covalent_Unit_Count"))
    info.append(getDescribtorValue(CID, "_Defined_Atom_Stereo_Count"))
    info.append(getDescribtorValue(CID, "_XLogP3"))
    

    info[0] = prettifyFormula(info[0])
    info[2] = cleanIUPACInChI(info[2])

    return  info

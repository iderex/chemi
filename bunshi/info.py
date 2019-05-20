import requests
from bs4 import BeautifulSoup
from re import sub
from xml.dom import minidom


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
    xmldoc = minidom.parse('attribute.xml')
    attributeList = xmldoc.getElementsByTagName('item')

    for i in attributeList:
        info.append(getDescribtorValue(CID, i.attributes['name'].value))

    info[0] = prettifyFormula(info[0])
    info[2] = cleanIUPACInChI(info[2])

    return info

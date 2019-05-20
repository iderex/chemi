from bunshi import app
from bunshi.info import getInfo, getCompound
from flask import flash, render_template, session, request

@app.route("/", methods = ["POST", "GET"])
def home():
    owoEgg = False
    acetateEgg = False
    preferred = True
    error = False
    imageSource = ""
    pageURL = ""
    IUPAC = ""
    formula = ""
    weight = ""
    isomericSmiles = ""
    hydrogenBondAcceptorCount = ""
    IUPACInChI = ""
    MonoIsotopicWeight = ""
    IsotopeAtomCount = ""
    RotatableBondCount = ""
    StructureComplexity = ""
    NonHydrogenAtomCount = ""
    UndefinedAtomStereoCount = ""
    UndefinedBondStereoCount = ""
    TPSA = ""
    TotalFormalCharge = ""
    CanonicalSMILES = ""
    CompoundIdentifier = ""
    DefinedBondStereoCount = ""
    ExactMass = ""
    CovalentUnitCount = ""
    DefinedAtomStereoCount = ""
    XLogP3 = ""

    if request.method == "POST":
        posts = request.form
        for post in posts.items():
            compound = post[1].lower()

        try:
            initInfo = getCompound(compound)
            imageSource = initInfo[0]
            pageURL = initInfo[1]
            IUPAC = initInfo[2]
            preferred = initInfo[3]

            info = getInfo(initInfo[4])
            formula = info[0]
            weight = info[1]
            IUPACInChI = info[2]
            hydrogenBondAcceptorCount = info[3]
            isomericSmiles = info[4]
            HydrogenBondDonorCount = info[5]
            MonoIsotopicWeight = info[6]
            IsotopeAtomCount = info[7]
            RotatableBondCount = info[8]
            StructureComplexity = info[9]
            NonHydrogenAtomCount = info[10]
            UndefinedAtomStereoCount = info[11]
            UndefinedBondStereoCount = info[12]
            TPSA = info[13]
            TotalFormalCharge = info[14]
            CanonicalSMILES = info[15]
            CompoundIdentifier = info[16]
            DefinedBondStereoCount = info[17]
            ExactMass = info[18]
            CovalentUnitCount = info[19]
            DefinedAtomStereoCount = info[20]
            XLogP3 = info[21]

            if IUPAC == "dioxotungsten":
                owoEgg = True

            if IUPAC == "acetate":
                acetateEgg = True

        except TypeError as e:
            error = True

        return render_template("home.html",
                               imageSource = imageSource,
                               compound = compound,
                               pageURL = pageURL,
                               IUPAC = IUPAC,
                               formula = formula,
                               weight = weight,
                               owoEgg = owoEgg,
                               acetateEgg = acetateEgg,
                               preferred = preferred,
                               error = error,
                               isomericSmiles = isomericSmiles,
                               hydrogenBondAcceptorCount = hydrogenBondAcceptorCount,
                               IUPACInChI = IUPACInChI,
                               MonoIsotopicWeight = MonoIsotopicWeight,
                               IsotopeAtomCount = IsotopeAtomCount,
                               RotatableBondCount = RotatableBondCount,
                               StructureComplexity = StructureComplexity,
                               NonHydrogenAtomCount = NonHydrogenAtomCount,
                               UndefinedAtomStereoCount = UndefinedAtomStereoCount,
                               UndefinedBondStereoCount = UndefinedBondStereoCount,
                               TPSA = TPSA,
                               TotalFormalCharge = TotalFormalCharge,
                               CanonicalSMILES = CanonicalSMILES,
                               CompoundIdentifier = CompoundIdentifier,
                               DefinedBondStereoCount = DefinedBondStereoCount,
                               ExactMass = ExactMass,
                               CovalentUnitCount = CovalentUnitCount,
                               DefinedAtomStereoCount = DefinedAtomStereoCount,
                               XLogP3 = XLogP3
                               )

    return render_template("home.html")

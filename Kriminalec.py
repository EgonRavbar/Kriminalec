datoteka = open("tekst.txt", "r")
DNK = datoteka.read()

lasCRNA = "CCAGCAATCGC"
lasRJAVA = "GCCAGTGCCG"
lasKORENCEK = "TTAGCTATCGC"

obrazKVADRAT = "GCCACGG"
obrazOKROGEL = "ACCACAA"
obrazOVALEN = "AGGCCTCA"

ociMODRA = "TTGTGGTGGC"
ociZELENA = "GGGAGGTGGC"
ociRJAVA = "AAGTAGTGAC"

if DNK.find(lasRJAVA) and DNK.find(obrazKVADRAT) and DNK.find(ociZELENA) != -1:
    print("Kriv je Miha!")
elif DNK.find(lasCRNA) and DNK.find(ociMODRA) and DNK.find(obrazOVALEN) != -1:
    print("Kriv je Matej!")
elif DNK.find(lasKORENCEK) and DNK.find(ociRJAVA) and DNK.find(obrazOKROGEL) != -1:
    print("Kriv je Ziga!")
else:
    print("Vnos ne ustreza bazi podatkov")

print("Predaj dokumentacijo nadrejenemu.")
datoteka.close()
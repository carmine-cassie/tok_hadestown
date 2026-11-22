import glob

with open("README.md", "r") as lipu:
    lipu_lawa = lipu.readlines()

lipu_ale = glob.glob("*.tsv")

for lipu in lipu_ale:
    for nanpa in range(len(lipu_lawa)):
        toki = lipu_lawa[nanpa]
        if toki[0:8] == f"| `{lipu[:2]}` |":
            sona = toki.split('|')

            with open(lipu, "r") as pali:
                pali = pali.readlines()
            
            mute_pali = len(pali) - 1
            mute_pini = sum([1 for i in pali if i[-2] != '\t']) - 1

            sona[-2] = f" {mute_pini}/{mute_pali} ({int(100*mute_pini/mute_pali)}%)" 

            lipu_lawa[nanpa] = '|'.join(sona)

with open("README.md", "w") as lipu:
    lipu.writelines(lipu_lawa)
    
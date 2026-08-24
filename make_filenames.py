import os

folder = "."

renames = {
    "amit-rai-ht_DfCon9Ow-unsplash.jpg": "Yellow-FootedGreenPigeon1.jpg",
    "anik-deb-nath-8C2KEBOBQIs-unsplash.jpg": "CommonTailorbird1.jpg",
    "anik-deb-nath-tY7prfwu5zI-unsplash.jpg": "IndianPiedStarling1.jpg",
    "arnab-dey-Z-xp81Kyf_A-unsplash.jpg": "LesserWhistlingDuck1.jpg",
    "bhanu-khan-QqOGqjpvUP0-unsplash.jpg": "AsianBrownFlycatcher1.jpg",
    "doncoombez-VfPKlF1yRcU-unsplash.jpg": "SpottedDove1.jpg",
    "gnana-prakash-3awKvwBd_FE-unsplash.jpg": "IndianRobin1.jpg",
    "hongbin-JCNIq0Wpqnc-unsplash.jpg": "PiedKingfisher1.jpg",
    "komal-g-C67IH3gviXE-unsplash.jpg": "IndianCormorant1.jpg",
    "occy-4MT2T4nn3PI-unsplash.jpg": "OrientalDarter1.jpg",
    "rohit-sharma-iLUAYsiJWcU-unsplash.jpg": "GreaterRacket-TailedDrongo1.jpg",
    "rohit-varma-gbM6dxN8LOo-unsplash.jpg": "Grey-HeadedFishEagle1.jpg",
    "sameer-gupta-LBHO5ReVX_c-unsplash.jpg": "OrientalWhite-Eye1.jpg",
    "sandaru-muthuwadige-Gh4WVcCif1I-unsplash.jpg": "IndianParadiseFlycatcher1.jpg",
    "sanved-bangale-__I1RncxWMw-unsplash.jpg": "PurpleHeron1.jpg",
    "sonika-agarwal-WDCOupaE6qU-unsplash.jpg": "White-BrowedFantail1.jpg",
    "vijayalakshmi-nidugondi-lamscDUafhg-unsplash.jpg": "BrahminyKite1.jpg",
    "viswaprem-anbarasapandian-qhjLvdwQfN4-unsplash.jpg": "BrahminyStarling1.jpg",
    "sudheer-nunna-Cx-KckbiG44-unsplash.jpg": "Stork-BilledKingfisher1.jpg",
    "maryia-shedava-rS2Nj6pNlow-unsplash.jpg": "GreyHeron1.jpg"
}

for old_name, new_name in renames.items():

    old_path = os.path.join(folder, old_name)
    new_path = os.path.join(folder, new_name)

    if not os.path.exists(old_path):
        print(f"NOT FOUND: {old_name}")
        continue

    if os.path.exists(new_path):
        print(f"ALREADY EXISTS: {new_name}")
        continue

    os.rename(old_path, new_path)
    print(f"Renamed: {old_name} -> {new_name}")

print("\nDone!")

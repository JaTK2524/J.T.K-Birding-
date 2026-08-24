import os

renames = [
    ("vivek-doshi-Wq8P63B5GPE-unsplash.jpg", "IndianSilverbill1.jpg"),
    ("viswaprem-anbarasapandian-GQZxRWcIn4k-unsplash.jpg", "Black-HeadedIbis1.jpg"),
    ("vincent-van-zalinge-vUNQaTtZeOo-unsplash.jpg", "CommonKingfisher1.jpg"),
    ("vijayalakshmi-nidugondi-ijRxZaU90bY-unsplash.jpg", "Purple-RumpedSunbird1.jpg"),
    ("vijayalakshmi-nidugondi-3CFKbEJ3gXg-unsplash.jpg", "CoppersmithBarbet1.jpg"),
    ("tim-promwanna-fDdZlW57hWM-unsplash.jpg", "IndianOpenbill1.jpg"),
    ("tim-promwanna-026fSUNaBL4-unsplash.jpg", "White-RumpedMunia1.jpg"),
    ("thomas-maximilian-lener-ie9zNgph23Y-unsplash.jpg", "White-ThroatedKingfisher1.jpg"),
    ("sylvester-alphonso-3cisTRwPMGM-unsplash.jpg", "Shikra1.jpg"),
    ("sumeet-mishra-8YLZk9GzjE0-unsplash.jpg", "AlexandrineParakeet1.jpg"),
    ("stuart-bartlett-t6h5NfkAmwo-unsplash.jpg", "LittleEgret1.jpg"),
    ("srinivasan-venkataraman-bkaE40i9OLg-unsplash.jpg", "White-breastedWaterhen1.jpg"),
    ("sonika-agarwal-uTmZVjODGCY-unsplash.jpg", "IndianGoldenOriole1.jpg"),
    ("rohit-varma-DBELYxFztew-unsplash.jpg", "GreatHornbill1.jpg"),
    ("ram-sundar-3mGfXFv3mhk-unsplash.jpg", "IndianGreyHornbill1.jpg"),
    ("rachel-orfila-9gNK9wBH9Ow-unsplash.jpg", "Red-WhiskeredBulbul1.jpg"),
    ("prathap-karaka-oqp-ZgsQWak-unsplash.jpg", "Red-WattledLapwing1.jpg"),
    ("nipun-haldar-fcKC5zqKON4-unsplash.jpg", "Brown-HeadedBarbet1.jpg"),
    ("namrata-shah-FIJTr0VFf4s-unsplash.jpg", "PaintedStork1.jpg"),
    ("mathew-schwartz-CgOaFB56Vyw-unsplash.jpg", "CommonSandpiper1.jpg"),
    ("mark-olsen-9jq2XT9FCqk-unsplash.jpg", "CommonRose-finch1.jpg"),
    ("manish-shah-rmf8I46sHvY-unsplash.jpg", "Black-RumpedFlameback1.jpg"),
    ("hongbin-Lrf47OQ7V1A-unsplash.jpg", "CrestedSerpentEagle1.jpg"),
    ("hongbin-LNitLmG-yE0-unsplash.jpg", "BlackDrongo1.jpg"),
    ("hendrik-prinsloo-8TlHq05VZ2k-unsplash.jpg", "Black-WingedKite1.jpg"),
    ("hans-veth-XYFpx1ErGOU-unsplash.jpg", "IndianPeafowl1.jpg"),
    ("greg-hill-mTstGLoM2NI-unsplash.jpg", "Rose-RingedParakeet1.jpg"),
    ("geoff-brooks-FkGEY5Ip9bs-unsplash.jpg", "Asian-GreenBee-eater1.jpg"),
    ("gaurav-khosla-KTQM1nCDA_k-unsplash.jpg", "IndianPitta1.jpg"),
    ("doncoombez-M6XbAHWN1ZI-unsplash.jpg", "CommonStonechat1.jpg"),
    ("debabrata-patra-UJ63sm9Ji6Y-unsplash.jpg", "JungleBabbler1.jpg"),
    ("bruno-van-der-kraan-TkQjNx6qCTA-unsplash.jpg", "BarnOwl1.jpg"),
    ("birgitta-roos-4VZQHQ8cMus-unsplash.jpg", "LittleCormorant1.jpg"),
    ("anindhya-sundar-das-KQRInT9Bhxc-unsplash.jpg", "Scaly-BreatedMunia1.jpg"),
    ("anastasiya-dragun-NwIAKB6aaxo-unsplash.jpg", "CattleEgret1.jpg"),
    ("abhishek-royal-ARBybIPjIx8-unsplash.jpg", "AshyDrongo1.jpg"),
    ("abhinaba-adhikary-Equx4rnoDMk-unsplash.jpg", "Little-RingedPlover1.jpg")
]

for old_name, new_name in renames:
    os.rename(old_name, new_name)

print("All 37 images renamed!")

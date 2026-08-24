template = open("template.html", "r").read()

birds = [

    {
        "name": "Alexandrine Parakeet",
        "scientific": "Psittacula eupatria",
        "family": "Psittaculidae",
        "description": "The Alexandrine Parakeet is a large, powerful parakeet with predominantly green plumage, a long tail, and a large red bill. Adult males have a distinctive black-and-pink collar around the neck, while females and younger birds do not show the same complete collar. It is found in forests, woodland, agricultural areas, gardens, and even urban environments. It feeds on fruits, seeds, grains, flowers, buds, and other plant material. Alexandrine Parakeets are highly social and often travel in noisy flocks, their loud calls carrying across the landscape. Their strong bills allow them to crack and manipulate surprisingly hard foods.",
        "image": "AlexandrineParakeet1.jpg"
    },

    {
        "name": "Asian Brown Flycatcher",
        "scientific": "Muscicapa dauurica",
        "family": "Muscicapidae",
        "description": "The Asian Brown Flycatcher is a small, inconspicuous insect-eating bird with brownish upperparts, pale underparts, a relatively large dark eye, and a delicate bill. It is commonly associated with woodland, forest edges, gardens, plantations, and other areas containing suitable perches. The bird usually hunts from a branch, watching carefully for insects before making a quick flight to capture them in the air or from nearby vegetation. Its subdued plumage provides excellent camouflage among branches and leaves. Although it may not have the spectacular colours of some tropical birds, its precise movements and efficient fly-catching behaviour make it an interesting species to observe.",
        "image": "AsianBrownFlycatcher1.jpg"
    },

    {
        "name": "Asian-Green Bee-eater",
        "scientific": "Merops orientalis",
        "family": "Meropidae",
        "description": "The Asian Green Bee-eater is a small, slender bird with vivid green plumage, a narrow black eye stripe, a pointed bill, and elongated central tail feathers. It is commonly found in open country, grasslands, agricultural areas, scrub, and woodland edges. Bee-eaters are accomplished aerial hunters and frequently sit on exposed branches, wires, or other perches while watching for insects. When prey is spotted, the bird launches into the air and catches it with remarkable precision before returning to its perch. Bees, wasps, dragonflies, and other flying insects form an important part of its diet. Its graceful flight and brilliant green plumage make it one of the most attractive birds of open habitats.",
        "image": "Asian-GreenBee-eater1.jpg"
    },

    {
        "name": "Asian Koel",
        "scientific": "Eudynamys scolopaceus",
        "family": "Cuculidae",
        "description": "The Asian Koel is a familiar member of the cuckoo family and is particularly famous for its loud, far-carrying calls. The male is glossy black with a striking red eye, while the female is brown with extensive pale spotting and streaking. Asian Koels are strongly associated with trees, gardens, groves, and urban areas where fruiting trees are available. They feed largely on fruits and berries and may spend long periods hidden among dense foliage. Like many cuckoos, the Asian Koel has a fascinating breeding strategy in which it lays its eggs in the nests of other birds. Its unmistakable call is often one of the first signs that a koel is nearby.",
        "image": "AsianKoel1.jpg"
    },

    {
        "name": "Ashy Drongo",
        "scientific": "Dicrurus leucophaeus",
        "family": "Dicruridae",
        "description": "The Ashy Drongo is a slender, agile bird with mostly grey plumage, a long deeply forked tail, and a sharp, slightly hooked bill. It is found in forests, woodland edges, plantations, and other habitats where it can hunt flying insects. Like other drongos, it is an excellent aerial hunter and frequently launches from an exposed perch to catch insects in mid-air. Its quick movements and alert behaviour make it an active presence in its habitat. Different populations can vary in the exact shade of grey, but the sleek body and characteristic forked tail remain useful identification features.",
        "image": "AshyDrongo1.jpg"
    },

    {
        "name": "Barn Owl",
        "scientific": "Tyto alba",
        "family": "Tytonidae",
        "description": "The Barn Owl is a distinctive nocturnal bird of prey recognised by its pale plumage and remarkable heart-shaped facial disc. It occurs in open countryside, farmland, grassland, villages, and areas where suitable buildings or cavities provide shelter and nesting sites. Barn Owls hunt mainly at night and rely heavily on their exceptionally sensitive hearing to locate prey in darkness. Small mammals form an important part of their diet, although they may also take other small animals. Their flight is unusually quiet because of specialised feather structures that reduce the sound produced by their wings. The pale face and ghostly appearance of the Barn Owl have made it a memorable bird in folklore across many cultures.",
        "image": "BarnOwl1.jpg"
    },

    {
        "name": "Black Drongo",
        "scientific": "Dicrurus macrocercus",
        "family": "Dicruridae",
        "description": "The Black Drongo is a glossy black bird with a long, deeply forked tail and a remarkably confident character. It is one of the most familiar birds of open country and is frequently seen perched on wires, fences, poles, and exposed branches. From these vantage points it watches for insects, which it catches in fast and skilful aerial sallies. Black Drongos are also famously bold and may chase much larger birds away from their territories. They occur in farmland, grassland, gardens, villages, and urban areas, adapting readily to landscapes shaped by people. Their combination of intelligence, agility, and fearlessness makes them particularly entertaining to watch.",
        "image": "BlackDrongo1.jpg"
    },

    {
        "name": "Black-Headed Ibis",
        "scientific": "Threskiornis melanocephalus",
        "family": "Threskiornithidae",
        "description": "The Black-Headed Ibis is a large wading bird with a mostly white body, a dark head and neck, long legs, and a long, gently curved bill. It is associated with wetlands, marshes, flooded fields, riversides, and shallow water where it can search for prey. The ibis probes mud and soft ground with its bill, feeding on insects, frogs, small fish, crustaceans, and other aquatic creatures. It often walks slowly and deliberately while feeding, carefully searching beneath the surface. When flying, its broad wings and long trailing legs give it the unmistakable silhouette of a large wader. Its striking contrast of white body and dark head makes it particularly easy to recognise in open wetlands.",
        "image": "Black-HeadedIbis1.jpg"
    },

    {
        "name": "Black Kite",
        "scientific": "Milvus migrans",
        "family": "Accipitridae",
        "description": "The Black Kite is a widespread and highly adaptable bird of prey often seen soaring effortlessly over towns, fields, rivers, coastlines, and busy urban areas. It has long wings and a characteristic forked tail that helps it manoeuvre while gliding on rising air currents. Black Kites are opportunistic feeders and may hunt small animals, but they also make extensive use of carrion and food scraps. Their ability to live successfully alongside humans has made them one of the most familiar raptors in many parts of the world. Large numbers may gather where food is plentiful, creating impressive groups circling high above the ground.",
        "image": "BlackKite1.jpg"
    },

    {
        "name": "Black-Rumped Flameback",
        "scientific": "Dinopium benghalense",
        "family": "Picidae",
        "description": "The Black-Rumped Flameback is a brightly coloured woodpecker with golden-yellow wings, a black rump, contrasting dark markings, and a prominent red crest in the male. It is found in forests, woodland, plantations, gardens, and wooded urban areas. Like other woodpeckers, it uses its strong bill to investigate bark and dead wood for insects and their larvae. Its stiff tail feathers help support its body as it climbs tree trunks, while its strong feet allow it to grip vertical surfaces. It may also feed on fruits and other food items. Its vivid plumage and characteristic climbing behaviour make it one of the more spectacular woodpeckers of the Indian subcontinent.",
        "image": "Black-RumpedFlameback1.jpg"
    },

    {
        "name": "Black-Winged Kite",
        "scientific": "Elanus caeruleus",
        "family": "Accipitridae",
        "description": "The Black-Winged Kite is a small and elegant bird of prey with pale grey-and-white plumage, dark patches on the wings, and striking red eyes. It favours open landscapes such as grasslands, agricultural fields, scrub, and other areas where small prey can be detected from above. One of its most characteristic behaviours is hovering almost motionless in the air while searching the ground below. It feeds on rodents, lizards, insects, and other small animals. After spotting prey, it can drop rapidly from the air to seize it. Its hovering hunting technique makes it an especially fascinating raptor to observe in open country.",
        "image": "Black-WingedKite1.jpg"
    },

    {
        "name": "Brahminy Kite",
        "scientific": "Haliastur indus",
        "family": "Accipitridae",
        "description": "The Brahminy Kite is a striking medium-sized raptor recognised by its rich chestnut-brown body, contrasting white head and breast, broad wings, and powerful hooked bill. It is strongly associated with coastal areas, rivers, lakes, wetlands, estuaries, and other places where fish and aquatic prey are available. It feeds on fish, crabs, carrion, and other small animals, often soaring low over water while searching for food. Its graceful flight and sharply contrasting plumage make it particularly easy to identify. Brahminy Kites are also closely associated with South Asian landscapes and are a familiar sight around waterways.",
        "image": "BrahminyKite1.jpg"
    },

    {
        "name": "Brahminy Starling",
        "scientific": "Sturnia pagodarum",
        "family": "Sturnidae",
        "description": "The Brahminy Starling is a medium-sized starling with a pale grey body, darker wings, a black crest, and warm buff-orange colouring around the head and breast. It is commonly found in open woodland, scrub, gardens, farmland, and areas near human habitation. It feeds on fruits, seeds, insects, and other small food items and may forage both on the ground and among vegetation. Its pointed crest and contrasting plumage make it distinctive among the starlings of the Indian subcontinent. During the breeding season, pairs may become particularly active around suitable nesting sites.",
        "image": "BrahminyStarling1.jpg"
    },

    {
        "name": "Brown-Headed Barbet",
        "scientific": "Psilopogon zeylanicus",
        "family": "Megalaimidae",
        "description": "The Brown-Headed Barbet is a chunky green bird with a brown head, a powerful bill, and a distinctive deep call. It is commonly found in wooded areas, gardens, plantations, groves, and forest edges. Fruits and berries, particularly figs, form an important part of its diet, although it may also take insects and other small food items. The strong bill is useful not only for feeding but also for excavating cavities in trees in which the birds can nest. Brown-Headed Barbets often remain hidden among foliage, so their repeated calls can be easier to notice than the birds themselves. Their steady presence is an important part of the soundscape of wooded landscapes.",
        "image": "Brown-HeadedBarbet1.jpg"
    },

    {
        "name": "Cattle Egret",
        "scientific": "Bubulcus ibis",
        "family": "Ardeidae",
        "description": "The Cattle Egret is a compact white heron that is unusually comfortable far from traditional wetlands. It is frequently seen walking through grasslands, farmland, fields, and even among grazing cattle and other large animals. Its association with livestock is particularly useful because the movement of cattle disturbs insects and other small creatures, making them easier for the egret to catch. It feeds on insects, frogs, small reptiles, and other prey. During the breeding season, adults develop attractive orange-buff colouring on parts of the head, neck, and back, contrasting with their normal white plumage. Their adaptability has allowed them to become one of the world's most widespread herons.",
        "image": "CattleEgret1.jpg"
    },

    {
        "name": "Common Hoopoe",
        "scientific": "Upupa epops",
        "family": "Upupidae",
        "description": "The Common Hoopoe is an unmistakable bird with a long, slender bill, warm buff-orange plumage, boldly black-and-white striped wings, and a magnificent fan-shaped crest. It spends much of its time on the ground, probing soil with its long bill in search of insects and other small creatures. When disturbed or excited, it can raise its crest into a striking crown of feathers. In flight, the broad black-and-white wings produce a distinctive pattern that makes the bird easy to identify. Hoopoes occur in open woodland, farmland, gardens, grassland, and other habitats where soft ground provides suitable feeding areas.",
        "image": "CommonHoopoe1.jpg"
    },

    {
        "name": "Common Kingfisher",
        "scientific": "Alcedo atthis",
        "family": "Alcedinidae",
        "description": "The Common Kingfisher is a small but spectacular bird famous for its brilliant blue upperparts, orange underparts, and long pointed bill. It is strongly associated with freshwater habitats such as streams, ponds, lakes, canals, and rivers where suitable perches are available. The bird often sits quietly on a low branch overlooking the water before diving suddenly to catch a small fish or other aquatic creature. Its rapid flight close to the water's surface is another characteristic sight. Although it is small enough to fit comfortably in a person's hand, the Common Kingfisher is a remarkably efficient hunter and one of the most vivid birds found near freshwater.",
        "image": "CommonKingfisher1.jpg"
    },

    {
        "name": "Common Myna",
        "scientific": "Acridotheres tristis",
        "family": "Sturnidae",
        "description": "The Common Myna is a familiar and highly adaptable bird found around towns, gardens, farmland, roadsides, buildings, and open woodland. It has a dark brown body, blackish head, yellow bill and legs, and conspicuous white patches on the wings that become particularly noticeable in flight. Common Mynas are opportunistic feeders and eat insects, fruits, grains, scraps, and many other foods. Their adaptability allows them to thrive in landscapes heavily modified by humans. They are often seen walking confidently across lawns and roadsides while searching for food, and their loud calls contribute greatly to the everyday soundscape of towns and villages.",
        "image": "CommonMyna1.jpg"
    },

    {
        "name": "Common Rosefinch",
        "scientific": "Carpodacus erythrinus",
        "family": "Fringillidae",
        "description": "The Common Rosefinch is a small seed-eating finch in which adult males develop attractive rosy-red colouring on the head, breast, and upper body. Females and younger birds are much more subdued, with brownish plumage that provides excellent camouflage among vegetation. The species is associated with scrub, woodland edges, open forest, and areas where seeds and suitable vegetation are available. It feeds mainly on seeds, buds, and plant material, although insects may also be taken. Its seasonal movements mean that its presence can vary considerably from place to place. The colourful male and melodic song make the Common Rosefinch a particularly attractive finch when encountered.",
        "image": "CommonRose-finch1.jpg"
    },

    {
        "name": "Common Sandpiper",
        "scientific": "Actitis hypoleucos",
        "family": "Scolopacidae",
        "description": "The Common Sandpiper is a small shorebird that can be found along rivers, ponds, lakes, reservoirs, marshes, and muddy or sandy shorelines. It has brownish upperparts, pale underparts, and a distinctive habit of bobbing its body and tail as it walks. It feeds on insects, worms, small crustaceans, and other tiny creatures found along the water's edge. Rather than wading deeply, it often moves along the shoreline, quickly picking up prey before continuing onward. When disturbed, it flies low over the water with rapid wingbeats, revealing a distinctive pale wing stripe. Its energetic movements make it easy to recognise once its behaviour becomes familiar.",
        "image": "CommonSandpiper1.jpg"
    },

    {
        "name": "Common Stonechat",
        "scientific": "Saxicola torquatus",
        "family": "Muscicapidae",
        "description": "The Common Stonechat is a small, upright songbird of open country, often seen perched on exposed stems, fences, bushes, wires, and other prominent points. Males have a dark head and contrasting orange-brown breast, while females and younger birds are generally less strongly marked. The species feeds mainly on insects and other small invertebrates, frequently dropping down from its perch to catch prey before returning to the same or another elevated position. It occurs in grasslands, scrub, agricultural areas, and other open habitats. Its habit of sitting conspicuously on high perches makes it a rewarding bird to search for in open landscapes.",
        "image": "CommonStonechat1.jpg"
    },

    {
        "name": "Common Tailorbird",
        "scientific": "Orthotomus sutorius",
        "family": "Cisticolidae",
        "description": "The Common Tailorbird is a tiny, active songbird named for its remarkable nesting behaviour, in which it uses plant fibres and spider silk to stitch or bind leaves together to form a secure nest. It has greenish upperparts, pale underparts, a long tail that is often cocked upward, and a slender pointed bill. It is common in gardens, scrub, plantations, woodland edges, and urban areas containing dense vegetation. The bird feeds mainly on insects and other small invertebrates, moving rapidly through leaves and branches while searching for prey. Its sharp calls and restless movements often reveal its presence before the bird can be located.",
        "image": "CommonTailorbird1.jpg"
    },

    {
        "name": "Coppersmith Barbet",
        "scientific": "Psilopogon haemacephalus",
        "family": "Megalaimidae",
        "description": "The Coppersmith Barbet is a small, chunky green bird with a colourful red-and-yellow face, a strong bill, and a surprisingly powerful voice. It is commonly found in gardens, groves, plantations, wooded areas, and towns where fruiting trees are available. Fruits and berries form an important part of its diet, particularly figs, although insects and other small food items may also be eaten. The species receives its unusual English name from its repeated call, which has been compared to the sound of a coppersmith striking metal with a hammer. Coppersmith Barbets often remain hidden among leaves, but their persistent calls can reveal their presence long before the bird is located.",
        "image": "CoppersmithBarbet1.jpg"
    },

    {
        "name": "Crested Serpent Eagle",
        "scientific": "Spilornis cheela",
        "family": "Accipitridae",
        "description": "The Crested Serpent Eagle is a powerful forest raptor with broad wings, a strong hooked bill, yellow legs, and a prominent crest that gives the species its name. It is associated with forests, wooded hills, plantations, and forest edges. As its name suggests, snakes form an important part of its diet, although it also hunts lizards, frogs, and other small animals. The eagle often watches from a high perch before making a sudden descent towards prey. Its deep, distinctive call can carry a long way through forests and hills. The combination of its crest, broad wings, and strong hunting abilities makes it an impressive member of the forest raptor community.",
        "image": "CrestedSerpentEagle1.jpg"
    },

    {
        "name": "Great Hornbill",
        "scientific": "Buceros bicornis",
        "family": "Bucerotidae",
        "description": "The Great Hornbill is one of the largest and most spectacular birds of the Indian subcontinent. It has a huge yellow-and-black bill topped by a prominent casque, striking black-and-white wings, and a long tail marked with white. It spends much of its time high in the canopy of mature forests, feeding heavily on fruits, especially figs, but also taking small animals when opportunities arise. Its enormous wings produce powerful wingbeats that can sometimes be heard before the bird comes into view. Great Hornbills depend heavily on large mature trees for nesting and feeding, making them an important symbol of healthy tropical forests and one of India's most magnificent birds.",
        "image": "GreatHornbill1.jpg"
    },

    {
        "name": "Greater Coucal",
        "scientific": "Centropus sinensis",
        "family": "Cuculidae",
        "description": "The Greater Coucal is a large, heavy-bodied member of the cuckoo family with glossy black plumage, rich chestnut-brown wings, a long tail, and a deep, resonant call. Unlike many cuckoos, it spends much of its time close to the ground, moving slowly through thick vegetation, scrub, gardens, farmland, and woodland edges. It feeds on insects, frogs, lizards, small animals, and a variety of other food items. Its large size and slow movements can make it look almost crow-like at first glance, but its rich brown wings and distinctive call reveal its identity. The Greater Coucal is often heard before it is seen because it prefers dense cover.",
        "image": "GreaterCoucal1.jpg"
    },

    {
        "name": "Greater Racket-Tailed Drongo",
        "scientific": "Dicrurus paradiseus",
        "family": "Dicruridae",
        "description": "The Greater Racket-Tailed Drongo is a striking forest bird with glossy black plumage, a prominent crest, and an extraordinary long tail ending in distinctive racket-shaped extensions. It is found mainly in forests, woodland, plantations, and forest edges, where it spends much of its time in the canopy. It feeds primarily on insects and other small creatures, often making swift aerial sallies from exposed branches to capture prey. This species is also famous for its varied vocal abilities and its capacity to imitate sounds made by other birds. Its spectacular tail, agile flight, and impressive vocal behaviour make it one of the most memorable drongos in South Asia.",
        "image": "GreaterRacket-TailedDrongo1.jpg"
    },

    {
        "name": "Grey Heron",
        "scientific": "Ardea cinerea",
        "family": "Ardeidae",
        "description": "The Grey Heron is a large, elegant wading bird with a long neck, long legs, a powerful pointed bill, and predominantly grey, white, and black plumage. It is found around rivers, lakes, ponds, marshes, estuaries, reservoirs, and coastal wetlands. The bird often stands completely still at the edge of shallow water, waiting patiently before making a rapid strike at fish, frogs, insects, and other aquatic prey. Its long neck allows it to reach into deeper water without moving its body very much. In flight, it folds its neck into a characteristic S-shape while its long legs trail behind, producing the unmistakable silhouette of a large heron.",
        "image": "GreyHeron1.jpg"
    },

    {
        "name": "Grey-Headed Fish Eagle",
        "scientific": "Icthyophaga ichthyaetus",
        "family": "Accipitridae",
        "description": "The Grey-Headed Fish Eagle is a powerful fish-eating raptor associated with rivers, lakes, reservoirs, wetlands, and other freshwater habitats. It has a distinctive grey head, dark brown body, broad wings, and a strong hooked bill designed for handling slippery prey. Fish form an important part of its diet, although it may also take other aquatic animals and carrion. The eagle often watches from a prominent tree or perch near water before swooping down to seize prey. Its broad wings allow it to soar efficiently over large bodies of water, while its powerful talons are well suited to carrying fish away from the surface.",
        "image": "Grey-HeadedFishEagle1.jpg"
    },

    {
        "name": "Indian Cormorant",
        "scientific": "Phalacrocorax fuscicollis",
        "family": "Phalacrocoracidae",
        "description": "The Indian Cormorant is a dark, streamlined waterbird commonly found on rivers, lakes, reservoirs, ponds, and other freshwater bodies. It is an excellent underwater hunter and pursues fish and other aquatic prey by swimming and diving beneath the surface. After feeding, it often sits on exposed branches, rocks, poles, or other perches with its wings spread to dry. Its long neck, relatively slender body, and dark plumage give it a distinctive appearance among Indian waterbirds. It can occur in groups, particularly where food is abundant, and may be seen diving repeatedly in productive waters.",
        "image": "IndianCormorant1.jpg"
    },

    {
        "name": "Indian Golden Oriole",
        "scientific": "Oriolus kundoo",
        "family": "Oriolidae",
        "description": "The Indian Golden Oriole is a striking yellow-and-black bird that spends much of its time high among the leaves of trees. Adult males have brilliant golden-yellow plumage, black wings, and a strong dark stripe through the eye, while females are generally duller and more greenish. The species feeds on fruits, berries, nectar, and insects, moving carefully through the canopy while searching for food. Despite its brilliant colouring, it can be surprisingly difficult to see because the yellow plumage blends with sunlit foliage. Its melodious calls often provide the first clue that an oriole is nearby. It is particularly associated with gardens, groves, woodland, and tree-rich urban areas.",
        "image": "IndianGoldenOriole1.jpg"
    },

    {
        "name": "Indian Grey Hornbill",
        "scientific": "Ocyceros birostris",
        "family": "Bucerotidae",
        "description": "The Indian Grey Hornbill is a medium-sized hornbill with mostly grey plumage, darker wings, a long tail, and a distinctive curved bill topped by a small casque. It is well adapted to open woodland and can often be found in gardens, farmland, villages, and towns where mature trees remain. It feeds on fruits and berries as well as insects and small animals. Indian Grey Hornbills spend considerable time moving through tree canopies, but they may also be seen flying between isolated trees in open country. Their long tails and characteristic hornbill bills make them easy to recognise once they are spotted.",
        "image": "IndianGreyHornbill1.jpg"
    },

    {
        "name": "Indian Openbill",
        "scientific": "Anastomus oscitans",
        "family": "Ciconiidae",
        "description": "The Indian Openbill is a large wetland stork named for the noticeable gap between the upper and lower parts of its bill when the bill is closed. This unusual bill structure is particularly useful for feeding on freshwater snails, which are an important part of its diet. Indian Openbills are commonly seen in marshes, ponds, flooded fields, rice paddies, shallow wetlands, and other watery habitats. They walk slowly through shallow water while searching for prey and may gather in large numbers when food is plentiful. In flight, their broad wings, long legs, and long neck give them the unmistakable appearance of a stork.",
        "image": "IndianOpenbill1.jpg"
    },

    {
        "name": "Indian Paradise Flycatcher",
        "scientific": "Terpsiphone paradisi",
        "family": "Monarchidae",
        "description": "The Indian Paradise Flycatcher is an elegant insect-eating bird famous for the extraordinary long tail streamers of adult males. Males may occur in striking white or rufous plumage, while females are generally shorter-tailed and more subdued in appearance. The species inhabits forests, woodland, gardens, plantations, and shaded areas where flying insects are abundant. It hunts by making rapid aerial sallies from branches, catching insects in mid-air before returning to a perch. Its graceful movements, flowing tail, and contrasting plumage make it one of the most spectacular small birds of South Asian forests.",
        "image": "IndianParadiseFlycatcher1.jpg"
    },

    {
        "name": "Indian Peafowl",
        "scientific": "Pavo cristatus",
        "family": "Phasianidae",
        "description": "The Indian Peafowl is one of the most recognisable birds of the Indian subcontinent and the national bird of India. The male, known as the peacock, has an extraordinary train of elongated feathers covered with colourful eye-like markings, which he raises and displays during courtship. Females, known as peahens, are more subdued in colour and lack the spectacular train. Indian Peafowl occur in forests, scrub, farmland, villages, gardens, and areas around human settlements. They feed on seeds, grains, fruits, insects, small reptiles, and other food items. Their loud calls and impressive displays make them among the most memorable birds of the region.",
        "image": "IndianPeafowl1.jpg"
    },

    {
        "name": "Indian Pied Starling",
        "scientific": "Gracupica contra",
        "family": "Sturnidae",
        "description": "The Indian Pied Starling is a medium-sized starling with strongly contrasting black-and-white plumage, a pale head, and a distinctive patterned appearance. It is commonly found in open country, farmland, grasslands, towns, villages, and areas with scattered trees. It feeds on insects, fruits, grains, seeds, and other food items and often forages on the ground in open areas. Indian Pied Starlings are social birds and may gather in groups where food is abundant. Their bold black-and-white plumage makes them particularly conspicuous among the many brown and grey birds of open landscapes.",
        "image": "IndianPiedStarling1.jpg"
    },

    {
        "name": "Indian Pitta",
        "scientific": "Pitta brachyura",
        "family": "Pittidae",
        "description": "The Indian Pitta is a beautifully coloured forest bird with a green back, blue wing markings, buff-coloured underparts, a reddish lower belly, and a bold dark stripe through the eye. It spends much of its time on the ground or among low vegetation, where it searches through leaf litter for insects, worms, and other small creatures. Despite its bright colours, it can be surprisingly difficult to locate because it prefers dense vegetation and moves quietly between patches of cover. Its strong, repeated calls are often the first indication that a pitta is nearby. It is especially associated with woodland and forest habitats where fallen leaves provide suitable feeding grounds.",
        "image": "IndianPitta1.jpg"
    },

    {
        "name": "Indian Pond Heron",
        "scientific": "Ardeola grayii",
        "family": "Ardeidae",
        "description": "The Indian Pond Heron is a small, stocky heron commonly found around ponds, marshes, rice fields, streams, wetlands, and other shallow-water habitats. It has a deceptively plain appearance when standing still, with streaky brown and buff plumage that provides excellent camouflage among mud, grass, and vegetation. When it takes flight, however, its wings reveal striking white patches that contrast sharply with the darker upperparts. The Indian Pond Heron feeds on fish, frogs, insects, crustaceans, and other small creatures, usually hunting by standing quietly at the edge of shallow water before making a sudden strike. It can also be found in cultivated fields and other human-modified landscapes where suitable feeding areas remain. During the breeding season, its plumage becomes more colourful, with elongated feathers developing around the head, neck, and back. Its ability to remain almost invisible until it suddenly flies away makes it a fascinating and surprisingly easy-to-overlook wetland bird.",
        "image": "IndianPondHeron1.jpg"
    },

    {
        "name": "Indian Robin",
        "scientific": "Copsychus fulicatus",
        "family": "Muscicapidae",
        "description": "The Indian Robin is a small, active bird of open and semi-open habitats, often found around rocky ground, scrub, gardens, farmland, and human settlements. Males are generally dark with contrasting pale or rufous markings around the lower body, while females are more subdued. It spends much of its time on the ground, hopping between rocks, bushes, and bare patches while searching for insects and other small invertebrates. It frequently raises and flicks its tail while moving through its territory. Its preference for open ground and its active behaviour make the Indian Robin an enjoyable species to watch closely.",
        "image": "IndianRobin1.jpg"
    },

    {
        "name": "Indian Roller",
        "scientific": "Coracias benghalensis",
        "family": "Coraciidae",
        "description": "The Indian Roller is a medium-sized bird famous for its brilliant blue wings, turquoise colouring, and spectacular tumbling displays during the breeding season. When perched, it can appear relatively subdued, but its true beauty becomes obvious when it takes flight and reveals the intense blue and purple colours of its wings. It is commonly found in open woodland, farmland, grassland, roadsides, and urban areas with scattered trees. The Indian Roller feeds on insects, small reptiles, amphibians, and other small animals, often hunting from an exposed perch. Its bold colours and dramatic flight make it one of the most memorable birds of open Indian landscapes.",
        "image": "IndianRoller1.jpg"
    },

    {
        "name": "Indian Silverbill",
        "scientific": "Euodice malabarica",
        "family": "Estrildidae",
        "description": "The Indian Silverbill is a small, active finch with a short conical bill, pale brown and grey plumage, and a distinctive silvery appearance. It is commonly found in grassland, dry scrub, agricultural fields, gardens, and areas containing tall grasses. Grass seeds and other small seeds form the main part of its diet, and the birds often move through vegetation in small groups while feeding. Their social behaviour means several birds may be seen travelling together from one feeding area to another. The Indian Silverbill is particularly well adapted to warm and relatively dry environments and is a fine example of the specialised seed-eating birds of the grasslands.",
        "image": "IndianSilverbill1.jpg"
    },

    {
        "name": "Jungle Babbler",
        "scientific": "Argya striata",
        "family": "Leiothrichidae",
        "description": "The Jungle Babbler is a social and noisy bird that usually moves through its habitat in small groups. It has predominantly brownish-grey plumage, a pale underside, and a sturdy appearance. Jungle Babblers are found in woodland, scrub, gardens, farmland, parks, and urban areas with suitable vegetation. They feed on insects, fruits, seeds, and other small food items, often foraging together on the ground and among bushes. Their constant chatter and energetic group behaviour are among their most characteristic features. A group of babblers can seem to occupy an entire patch of vegetation at once, with several birds calling and moving about simultaneously.",
        "image": "JungleBabbler1.jpg"
    },

    {
        "name": "Lesser Whistling Duck",
        "scientific": "Dendrocygna javanica",
        "family": "Anatidae",
        "description": "The Lesser Whistling Duck is a small to medium-sized duck with warm brown plumage, a relatively long neck, and a distinctive whistling call. It is strongly associated with freshwater habitats such as ponds, lakes, marshes, flooded fields, rice paddies, and slow-moving waterways. It feeds on aquatic vegetation, seeds, grains, and small aquatic animals and may forage both by dabbling and by searching through shallow water. These ducks are highly social and are often encountered in groups resting on the water or along the shoreline. Their whistling calls and compact shape make them a familiar sight on suitable wetlands.",
        "image": "LesserWhistlingDuck1.jpg"
    },

    {
        "name": "Little Cormorant",
        "scientific": "Microcarbo niger",
        "family": "Phalacrocoracidae",
        "description": "The Little Cormorant is a small, dark waterbird commonly found on ponds, lakes, rivers, reservoirs, marshes, and flooded fields. It is an excellent swimmer and catches fish and other aquatic creatures by diving beneath the water. After feeding, it is often seen perched on a branch, rock, post, or other exposed surface with its wings spread wide to dry. Cormorants have plumage that is less water-resistant than that of many other waterbirds, helping them swim efficiently underwater. The Little Cormorant is highly adaptable and can occur close to human habitation wherever suitable water and food are available.",
        "image": "LittleCormorant1.jpg"
    },

    {
        "name": "Little Egret",
        "scientific": "Egretta garzetta",
        "family": "Ardeidae",
        "description": "The Little Egret is a slender white heron with long black legs, a long dark bill, and elegant decorative plumes during the breeding season. It occurs around rivers, ponds, lakes, marshes, rice fields, estuaries, and coastal wetlands. The bird often walks slowly through shallow water before suddenly striking at fish, frogs, insects, and other small animals. Its bright yellow feet provide a useful identification feature and contrast strongly with its dark legs. In flight, the Little Egret is graceful and distinctive, with its long neck tucked back and long legs extending behind the body.",
        "image": "LittleEgret1.jpg"
    },

    {
        "name": "Little Ringed Plover",
        "scientific": "Charadrius dubius",
        "family": "Charadriidae",
        "description": "The Little Ringed Plover is a small, active shorebird usually found beside freshwater, including riverbanks, ponds, reservoirs, muddy shores, and other open wet habitats. It has a distinctive dark band across the chest, a dark mask around the eyes, a white throat, and yellowish legs. It feeds by running quickly across the ground, suddenly stopping, and picking up insects, worms, and other tiny invertebrates. Its small size and sandy-brown upperparts can make it difficult to notice among stones, mud, and bare ground. When disturbed, it can rapidly move along the shoreline or fly to another feeding area.",
        "image": "Little-RingedPlover1.jpg"
    },

    {
        "name": "Oriental Darter",
        "scientific": "Anhinga melanogaster",
        "family": "Anhingidae",
        "description": "The Oriental Darter is a long-necked aquatic bird with a slender body, pointed bill, and remarkable swimming ability. It is commonly found on freshwater lakes, ponds, rivers, reservoirs, marshes, and other wetlands. The bird swims with much of its body submerged, leaving only its long neck and head visible above the water, which gives rise to its snake-like appearance. It dives underwater to catch fish and other aquatic prey using its sharp bill. After feeding, it often perches with its wings spread to dry. Its unusual swimming style and long snake-like neck make it one of the most distinctive waterbirds of South Asia.",
        "image": "OrientalDarter1.jpg"
    },

    {
        "name": "Oriental Magpie-Robin",
        "scientific": "Copsychus saularis",
        "family": "Muscicapidae",
        "description": "The Oriental Magpie-Robin is a bold and highly recognisable garden bird with striking black-and-white plumage, a long tail, and a lively personality. Males are predominantly black and white, while females are generally greyer and less strongly marked. It is often seen on the ground or perched on low branches, fences, walls, and other exposed surfaces while searching for insects and other small creatures. A characteristic behaviour is the frequent raising and cocking of its long tail while foraging. The species is also famous for its varied and musical song, particularly during the breeding season, when males can become especially conspicuous.",
        "image": "OrientalMagpie-Robin1.jpg"
    },

    {
        "name": "Oriental White-eye",
        "scientific": "Zosterops palpebrosus",
        "family": "Zosteropidae",
        "description": "The Oriental White-eye is a tiny, active bird easily recognised by the conspicuous white ring around its eye. It has greenish upperparts, yellowish underparts, and a short pointed bill suited to feeding on nectar, fruit, and small insects. White-eyes are highly active and often move rapidly through foliage in small groups, searching flowers and leaves for food. They are common in gardens, woodland, plantations, scrub, and urban areas containing flowering plants and trees. Their constant movement and soft social calls make them lively inhabitants of leafy habitats, while their striking eye-ring provides an excellent identification feature.",
        "image": "OrientalWhite-Eye1.jpg"
    },

    {
        "name": "Painted Stork",
        "scientific": "Mycteria leucocephala",
        "family": "Ciconiidae",
        "description": "The Painted Stork is a large and striking wetland bird with a long slightly curved bill, a mostly white body, black-and-white wings, and attractive pink markings on the lower body and legs. It is commonly found around lakes, marshes, flooded fields, shallow wetlands, and other areas where fish and aquatic prey are abundant. Painted Storks often feed by moving their partly open bills through shallow water, using touch to detect prey such as fish and other aquatic animals. They frequently gather in groups, particularly at productive feeding sites. Their large size and distinctive pattern make them highly conspicuous birds in open wetlands.",
        "image": "PaintedStork1.jpg"
    },

    {
        "name": "Pied Kingfisher",
        "scientific": "Ceryle rudis",
        "family": "Alcedinidae",
        "description": "The Pied Kingfisher is a striking black-and-white kingfisher commonly found around rivers, lakes, reservoirs, estuaries, ponds, and other open waters. It is famous for hovering almost motionless above the water before plunging downward to catch fish. Its black-and-white plumage, shaggy crest, long pointed bill, and rapid wingbeats make it easy to recognise. Unlike many kingfishers that rely on low perches, the Pied Kingfisher frequently hunts directly from the air, allowing it to cover large areas of water efficiently. It feeds mainly on fish and other aquatic prey and is often seen hunting in pairs or small groups.",
        "image": "PiedKingfisher1.jpg"
    },

    {
        "name": "Purple Heron",
        "scientific": "Ardea purpurea",
        "family": "Ardeidae",
        "description": "The Purple Heron is a tall, elegant wetland bird with rich brown, purple-grey, and chestnut tones that distinguish it from the more uniformly grey Great Egret and Grey Heron. It is usually found in reedbeds, marshes, riversides, lakes, ponds, flooded fields, and other wetlands with dense vegetation. It feeds on fish, frogs, insects, small mammals, and other aquatic or wetland prey, often standing motionless before striking with its long pointed bill. Its long neck and legs allow it to hunt effectively in shallow water and among reeds. Despite its size, it can blend surprisingly well into dense wetland vegetation.",
        "image": "PurpleHeron1.jpg"
    },

    {
        "name": "Purple-Rumped Sunbird",
        "scientific": "Leptocoma zeylonica",
        "family": "Nectariniidae",
        "description": "The Purple-Rumped Sunbird is a tiny nectar-feeding bird commonly found in gardens, plantations, woodland edges, and areas with flowering plants. The male has glossy, iridescent plumage with brilliant purple and other metallic colours that can appear dramatically different depending on the angle of the light. Females are more subdued and generally greenish-yellow. The bird uses its slender, curved bill to reach nectar deep inside flowers and also feeds on small insects, particularly while raising young. It moves rapidly among flowers and may hover briefly while feeding. As a nectar feeder, it also plays an important role in pollination.",
        "image": "Purple-RumpedSunbird1.jpg"
    },

    {
        "name": "Purple Sunbird",
        "scientific": "Cinnyris asiaticus",
        "family": "Nectariniidae",
        "description": "The Purple Sunbird is a tiny, energetic nectar-feeding bird that is particularly common in gardens, scrub, woodland edges, and areas with flowering plants. Breeding males develop glossy, iridescent purplish-black plumage that can shine with different colours in bright sunlight, while females are more subdued yellowish-green. Its slender downward-curved bill is perfectly suited to feeding from flowers, and it may hover briefly while taking nectar. Insects and other small creatures are also eaten, especially when feeding young. Its rapid movements, tiny size, and brilliant male plumage make it one of the most fascinating small birds to watch around flowering plants.",
        "image": "PurpleSunbird1.jpg"
    },

    {
        "name": "Red-Vented Bulbul",
        "scientific": "Pycnonotus cafer",
        "family": "Pycnonotidae",
        "description": "The Red-Vented Bulbul is a common and highly adaptable songbird found in gardens, towns, farmland, scrub, woodland, and urban areas. It has a dark head with a small crest, a brownish body, a pale underside, and the distinctive red patch beneath the tail that gives the species its name. It feeds on fruits, berries, nectar, insects, and other small food items, making it capable of exploiting a wide variety of habitats. Red-Vented Bulbuls are active and vocal birds and can often be seen moving between shrubs and trees in search of food. Their adaptability has allowed them to thrive even in heavily human-modified landscapes.",
        "image": "Red-VentedBulbul1.jpg"
    },

    {
        "name": "Red-Whiskered Bulbul",
        "scientific": "Pycnonotus jocosus",
        "family": "Pycnonotidae",
        "description": "The Red-Whiskered Bulbul is an attractive and lively songbird recognised by its pointed black crest, white cheeks, red ear patch, dark upperparts, and red vent. It is commonly found in gardens, scrub, plantations, woodland edges, and areas of human habitation. It feeds on fruits, berries, nectar, insects, and other small food items, often moving actively among shrubs and small trees. Its varied calls and lively behaviour make it a familiar presence in many gardens and wooded areas. The combination of its tall crest, white face, and bright red facial marking makes it particularly distinctive among bulbuls.",
        "image": "Red-WhiskeredBulbul1.jpg"
    },

    {
        "name": "Red-Wattled Lapwing",
        "scientific": "Vanellus indicus",
        "family": "Charadriidae",
        "description": "The Red-Wattled Lapwing is a large and striking wader with a black head and breast, white underparts, brown wings, and a conspicuous red fleshy wattle near the base of the bill. It is commonly found in open ground, farmland, grassland, wetlands, riverbanks, and even relatively dry landscapes. It feeds mainly on insects and other small invertebrates, walking briskly across open ground while searching for food. Its loud, ringing calls are among the most recognisable sounds of the Indian countryside. Lapwings are extremely alert and may call loudly when they detect people, animals, or potential predators approaching their territory.",
        "image": "Red-WattledLapwing1.jpg"
    },

    {
        "name": "Rose-Ringed Parakeet",
        "scientific": "Psittacula krameri",
        "family": "Psittaculidae",
        "description": "The Rose-Ringed Parakeet is a bright green, long-tailed parakeet with a strong red bill and a distinctive appearance. Adult males have a dark-and-pink ring around the neck, while females and younger birds do not develop the same complete collar. The species is highly adaptable and occurs in forests, farmland, gardens, towns, villages, and large cities. It feeds on fruits, seeds, grains, flowers, buds, and other plant material. Rose-Ringed Parakeets are strongly social and often travel in noisy flocks, particularly when moving between feeding and roosting areas. Their fast flight and loud calls make them one of the most noticeable parrots in many Indian landscapes.",
        "image": "Rose-RingedParakeet1.jpg"
    },

    {
        "name": "Rufous Treepie",
        "scientific": "Dendrocitta vagabunda",
        "family": "Corvidae",
        "description": "The Rufous Treepie is a long-tailed member of the crow family with a striking combination of rufous-brown, black, and grey plumage. It is commonly found in forests, woodland, gardens, farmland, plantations, and open areas containing scattered trees. It feeds on a wide variety of foods, including insects, fruits, small animals, eggs, and scraps, allowing it to adapt to many different environments. Rufous Treepies are active and curious birds and are often seen moving noisily through tree canopies or hopping between branches. Their long tails and contrasting plumage make them easy to recognise, while their varied calls often announce their presence before they are seen.",
        "image": "RufousTreepie1.jpg"
    },

    {
        "name": "Scaly-Breasted Munia",
        "scientific": "Lonchura punctulata",
        "family": "Estrildidae",
        "description": "The Scaly-Breasted Munia is a small, compact finch with warm brown upperparts and a distinctive scale-like pattern across the pale breast and belly. It is commonly found in grassland, scrub, farmland, gardens, and areas containing tall grasses and seed-producing plants. Grass seeds and other small seeds form the main part of its diet, and the birds often feed in pairs or small groups. They are active and social, moving through vegetation together while giving soft calls. The intricate scale pattern on the underside is particularly noticeable at close range and provides this otherwise small bird with one of its most memorable identification features.",
        "image": "Scaly-BreastedMunia1.jpg"
    },

    {
        "name": "Shikra",
        "scientific": "Accipiter badius",
        "family": "Accipitridae",
        "description": "The Shikra is a small, agile bird of prey with short rounded wings, a long tail, and sharp eyesight. It occurs in woodland, scrub, farmland, gardens, plantations, and even urban areas where suitable trees provide cover and hunting opportunities. It feeds on small birds, lizards, insects, and other small animals, often relying on surprise and speed to catch prey. A Shikra may sit quietly among foliage or on an exposed branch before suddenly launching into a rapid pursuit. Its ability to manoeuvre quickly between trees makes it an impressive little raptor and an exciting bird for an observer to encounter.",
        "image": "Shikra1.jpg"
    },

    {
        "name": "Spotted Dove",
        "scientific": "Spilopelia chinensis",
        "family": "Columbidae",
        "description": "The Spotted Dove is a medium-sized dove with soft brown and grey plumage and a distinctive black-and-white spotted patch on the sides and back of the neck. It is highly adaptable and can be found in gardens, farmland, woodland edges, parks, villages, and cities. It feeds mainly on seeds and grains, often foraging on the ground in open areas. Spotted Doves are generally calm birds and can often be observed walking slowly while searching for food. Their gentle cooing calls are a familiar sound in many parts of South Asia, especially around gardens and cultivated landscapes.",
        "image": "SpottedDove1.jpg"
    },

    {
        "name": "Stork-Billed Kingfisher",
        "scientific": "Pelargopsis capensis",
        "family": "Alcedinidae",
        "description": "The Stork-Billed Kingfisher is a large and powerful kingfisher with a massive red bill, blue-green wings, a brownish head and body, and pale underparts. It is associated with rivers, lakes, ponds, mangroves, forest streams, and other wet habitats, particularly where substantial trees provide hunting perches. It feeds on fish, frogs, crabs, reptiles, and other small animals, usually watching from a perch before making a forceful dive or descent. Its enormous bill gives it a particularly impressive appearance and allows it to handle prey much larger than those taken by many smaller kingfishers. Despite its size, it can move rapidly and efficiently when hunting.",
        "image": "Stork-BilledKingfisher1.jpg"
    },

    {
        "name": "White-Breasted Waterhen",
        "scientific": "Amaurornis phoenicurus",
        "family": "Rallidae",
        "description": "The White-Breasted Waterhen is a dark, chicken-sized wetland bird with a striking white face, throat, breast, and belly. It is commonly found around ponds, streams, marshes, rice fields, gardens, drainage channels, and areas of dense waterside vegetation. Although it can fly, it often prefers to walk quickly through reeds, grasses, bushes, and muddy margins, using its long toes to move over soft ground. It feeds on insects, small aquatic animals, seeds, and other food found around wet vegetation. Its loud and varied calls are often heard from dense cover, making sound an important clue to its presence.",
        "image": "White-BreastedWaterhen1.jpg"
    },

    {
        "name": "White-Browed Fantail",
        "scientific": "Rhipidura aureola",
        "family": "Rhipiduridae",
        "description": "The White-Browed Fantail is a small, energetic insect-eating bird recognised by its fan-shaped tail and prominent pale eyebrow. It is commonly found in woodland, scrub, gardens, plantations, and forest edges. The bird frequently spreads and flicks its tail while moving through branches and foliage, behaviour that gives the species its English name. It feeds mainly on insects and other small invertebrates, often catching prey in short aerial sallies from a perch. Its constant movement and tail-fanning behaviour make it an entertaining bird to observe, although its quick movements can make close observation surprisingly challenging.",
        "image": "White-BrowedFantail1.jpg"
    },

    {
        "name": "White-Rumped Munia",
        "scientific": "Lonchura striata",
        "family": "Estrildidae",
        "description": "The White-Rumped Munia is a small, social seed-eating finch commonly found in grassland, scrub, agricultural areas, gardens, and other habitats containing tall grasses. Its dark body contrasts with a conspicuous white patch on the rump, which becomes particularly noticeable when the bird flies away. It feeds mainly on grass seeds and other small seeds, often moving through vegetation in pairs or small flocks. White-Rumped Munias are active and sociable, frequently travelling together between feeding areas. Their association with grassy habitats makes them a familiar sight in many rural landscapes.",
        "image": "White-RumpedMunia1.jpg"
    },

    {
        "name": "White-Throated Kingfisher",
        "scientific": "Halcyon smyrnensis",
        "family": "Alcedinidae",
        "description": "The White-Throated Kingfisher is a large and brilliantly coloured kingfisher with a bright blue back and wings, rich chestnut-brown head and body, white throat and breast, and a powerful red bill. Despite belonging to the kingfisher family, it is not restricted to water and can frequently be found in fields, gardens, woodland edges, plantations, and urban areas. It hunts a wide range of prey, including insects, lizards, frogs, small birds, and other small animals, while fish may also be taken when available. It often sits quietly on an exposed perch before dropping suddenly onto its prey. Its vivid colours and powerful flight make it one of the most impressive kingfishers of South Asia.",
        "image": "White-ThroatedKingfisher1.jpg"
    },

    {
        "name": "Yellow-Footed Green Pigeon",
        "scientific": "Treron phoenicopterus",
        "family": "Columbidae",
        "description": "The Yellow-Footed Green Pigeon is a medium-sized fruit-eating pigeon with predominantly green plumage, yellowish feet, and subtle patches of colour on the wings and body. It is associated with forests, woodland, gardens, plantations, groves, and other habitats containing fruiting trees. Fruits, berries, and figs form an important part of its diet, and the bird may spend long periods quietly feeding in the canopy. Its green plumage provides excellent camouflage among leaves, making it surprisingly difficult to notice despite its size. The species plays an important ecological role by consuming and dispersing seeds from the fruits it eats.",
        "image": "Yellow-FootedGreenPigeon1.jpg"
    },
    ]

for bird in birds:

    page = template

    page = page.replace("{{NAME}}", bird["name"])
    page = page.replace("{{SCIENTIFIC}}", bird["scientific"])
    page = page.replace("{{DESCRIPTION}}", bird["description"])
    page = page.replace("{{FAMILY}}", bird["family"])
    page = page.replace("{{IMAGE}}", bird["image"])
    
    current_index = birds.index(bird)
    if current_index < len(birds) - 1:
       next_bird = birds[current_index + 1]
       next_page = next_bird["name"].lower().replace(" ", "-") + ".html"
       page = page.replace("{{NEXT_PAGE}}", next_page)
    else:
        page = page.replace("{{NEXT_PAGE}}", "")
    
    
    filename = bird["name"].lower().replace(" ", "-") + ".html"

    open("birds/" + filename, "w").write(page)

index_template = open("index_template.html", "r").read()

bird_list = ""

for bird in birds:
    filename = bird["name"].lower().replace(" ", "-") + ".html"
    bird_list += '<li class="bird"><a href="birds/' + filename + '">' + bird["name"] + '</a></li>'
    

index = index_template.replace("{{BIRD_LIST}}", bird_list)

open("index.html", "w").write(index)

print("Pages Done, Sir")

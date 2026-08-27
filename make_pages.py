template = open("template.html", "r").read()

birds = [
{
    "name": "Alexandrine Parakeet",
    "scientific": "Psittacula eupatria",
    "description": "The Alexandrine Parakeet is a large and striking parakeet found across the Indian subcontinent and parts of Southeast Asia. It has predominantly green plumage, a large red bill, and distinctive maroon shoulder patches. Mature males develop a dark neck ring, while females and young birds lack the complete ring. It is an adaptable bird that occurs in forests, woodlands, farmland, plantations, gardens, and urban areas, where it feeds mainly on fruits, seeds, flowers, grains, and buds.",
    "image": "AlexandrineParakeet1.jpg",
    "quick_facts": {
        "family": "Psittaculidae",
        "size": "56–62 cm",
        "weight": "200–300 g",
        "wingspan": "Approximately 20–25 cm",
        "diet": "Fruits, seeds, flowers, grains, buds, and other plant matter",
        "habitat": "Forests, woodlands, farmland, plantations, gardens, and urban areas",
        "behaviour": "Social and active; often seen singly, in pairs, or in small groups while feeding in trees",
        "activity": "Diurnal",
        "nesting": "Nests in tree cavities, usually using existing holes or abandoned woodpecker nests",
        "breeding_season": "November to April",
        "clutch_size": "2–4 eggs",
        "call": "Loud, harsh and ringing calls, often given while flying or moving between trees",
        "lifespan": "Up to around 30 years in captivity",
        "conservation_status": "Least Concern",
        "where_to_find": "Forests, plantations, farmland, large gardens, and wooded urban areas across India"
    }
},

{
    "name": "Asian-Green Bee-eater",
    "scientific": "Merops orientalis",
    "description": "The Asian Green Bee-eater is a small, brightly coloured insect-eating bird with vivid green plumage, a slender black bill, and a distinctive black eye stripe. It is an agile aerial hunter that launches from exposed perches to catch insects in flight before returning to the same or another perch. Despite its name, it eats a wide variety of flying insects in addition to bees. It is commonly found in open country, grasslands, agricultural areas, scrub, riverbanks, and lightly wooded habitats.",
    "image": "Asian-GreenBee-Eater1.jpg",
    "quick_facts": {
        "family": "Meropidae",
        "size": "16–18 cm",
        "weight": "15–20 g",
        "wingspan": "Approximately 28–32 cm",
        "diet": "Bees, wasps, dragonflies, butterflies, beetles, and other flying insects",
        "habitat": "Open woodland, grassland, farmland, scrub, riverbanks, and gardens",
        "behaviour": "Highly agile aerial hunter that frequently catches insects from the air and returns to a perch",
        "activity": "Diurnal",
        "nesting": "Excavates a tunnel in sandy or soft soil, banks, or other suitable ground",
        "breeding_season": "March to June, varying by region",
        "clutch_size": "4–8 eggs",
        "call": "High-pitched, rapid and pleasant twittering calls, often heard in flight",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Open fields, farmland, grasslands, scrub, wetlands, riverbanks, and dry open areas across India"
    }
},

{
    "name": "Asian Koel",
    "scientific": "Eudynamys scolopaceus",
    "description": "The Asian Koel is a familiar cuckoo of the Indian subcontinent, famous for its loud and distinctive calls during the breeding season. Adult males are glossy black with striking red eyes, while females are brown with extensive pale spots and streaks. Asian Koels spend much of their time in trees and feed heavily on fruits, berries, and figs. Like other cuckoos, they are brood parasites and lay their eggs in the nests of other birds, particularly crows.",
    "image": "AsianKoel1.jpg",
    "quick_facts": {
        "family": "Cuculidae",
        "size": "39–46 cm",
        "weight": "190–300 g",
        "wingspan": "Approximately 45–50 cm",
        "diet": "Fruits, berries, figs, seeds, and occasionally insects",
        "habitat": "Woodlands, gardens, plantations, parks, forests, and urban areas",
        "behaviour": "Usually remains in trees and feeds on fruit; males are particularly vocal during breeding",
        "activity": "Diurnal",
        "nesting": "Does not build its own nest; lays eggs in the nests of host birds, especially crows",
        "breeding_season": "March to August, varying by region",
        "clutch_size": "Usually 1–2 eggs laid in a host nest",
        "call": "Males produce a loud, repeated rising 'ku-oo' call; females have different harsh calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Gardens, parks, wooded neighbourhoods, plantations, forests, and cities across India"
    }
},

{
    "name": "Ashy Drongo",
    "scientific": "Dicrurus leucophaeus",
    "description": "The Ashy Drongo is a slender, medium-sized drongo with grey plumage and a distinctive deeply forked tail. Its plumage varies considerably between different populations, with some forms being much darker than others. It is an active aerial hunter that frequently launches from exposed perches to capture insects in flight. The species occurs in forests, open woodland, plantations, gardens, and hilly regions and often perches prominently while scanning for prey.",
    "image": "AshyDrongo1.jpg",
    "quick_facts": {
        "family": "Dicruridae",
        "size": "25–30 cm",
        "weight": "40–60 g",
        "wingspan": "Approximately 35–40 cm",
        "diet": "Insects and other small invertebrates",
        "habitat": "Forests, woodland, plantations, gardens, scrub, and hills",
        "behaviour": "Active and agile; frequently sallies from exposed perches to catch insects in flight",
        "activity": "Diurnal",
        "nesting": "Builds a small cup-shaped nest, usually placed on a horizontal tree branch",
        "breeding_season": "April to June",
        "clutch_size": "Usually 2–4 eggs",
        "call": "Varied calls including whistles, harsh notes, and chattering sounds",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Wooded areas, forests, plantations, gardens, and hill regions across India"
    }
},

{
    "name": "Barn Owl",
    "scientific": "Tyto alba",
    "description": "The Barn Owl is one of the world's most widespread owls and is easily recognized by its pale, heart-shaped facial disc. Its upperparts are generally golden-brown and grey, while the underparts are often pale. It is primarily nocturnal and hunts over open ground, using its exceptional hearing and vision to locate prey. Barn Owls frequently use barns, towers, buildings, tree cavities, and other sheltered places for roosting and nesting and are especially valuable to farmers because they consume large numbers of rodents.",
    "image": "BarnOwl1.jpg",
    "quick_facts": {
        "family": "Tytonidae",
        "size": "32–40 cm",
        "weight": "250–550 g",
        "wingspan": "80–95 cm",
        "diet": "Small mammals, especially rodents, as well as small birds, reptiles, frogs, and insects",
        "habitat": "Farmland, grassland, open country, villages, wetlands, and areas around buildings",
        "behaviour": "Usually hunts low over open ground and relies heavily on hearing to locate prey",
        "activity": "Primarily nocturnal",
        "nesting": "Nests in cavities, barns, buildings, towers, tree hollows, and other sheltered locations",
        "breeding_season": "Varies by region; may breed throughout much of the year where food is plentiful",
        "clutch_size": "Usually 4–7 eggs",
        "call": "Harsh hissing, screeching, and rasping calls rather than the classic hoot associated with many other owls",
        "lifespan": "Around 1–5 years commonly in the wild, with some individuals living considerably longer",
        "conservation_status": "Least Concern",
        "where_to_find": "Farmland, grasslands, villages, old buildings, barns, and other open areas across India"
    }
},

{
    "name": "Black Drongo",
    "scientific": "Dicrurus macrocercus",
    "description": "The Black Drongo is a bold and highly adaptable bird with glossy black plumage and a distinctive deeply forked tail. It is commonly seen perched on wires, poles, fences, and exposed branches while scanning the surroundings for insects. It is an accomplished aerial hunter and can also take prey from the ground or vegetation. Black Drongos are widespread in open country, farmland, grasslands, plantations, and urban areas and are well known for aggressively defending their territories against much larger birds.",
    "image": "BlackDrongo1.jpg",
    "quick_facts": {
        "family": "Dicruridae",
        "size": "28–31 cm",
        "weight": "70–100 g",
        "wingspan": "Approximately 35–40 cm",
        "diet": "Insects and other small invertebrates",
        "habitat": "Grasslands, farmland, open woodland, plantations, parks, and towns",
        "behaviour": "Aggressive and territorial; frequently chases larger birds away from its nesting area",
        "activity": "Diurnal",
        "nesting": "Builds a small cup-shaped nest on a horizontal branch, often high above the ground",
        "breeding_season": "April to August",
        "clutch_size": "Usually 2–4 eggs",
        "call": "Sharp, varied calls including metallic notes, whistles, and harsh sounds",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Farmland, grasslands, roadside trees, open woodland, parks, and urban areas across India"
    }
},

{
    "name": "Black-Headed Ibis",
    "scientific": "Threskiornis melanocephalus",
    "description": "The Black-Headed Ibis is a large wading bird with a mostly white body, a bare black head and neck, and long dark legs. It is commonly found in wetlands, marshes, flooded fields, riverbanks, and agricultural areas, where it searches for prey by probing mud and soft ground with its long, curved bill. It feeds on a wide range of aquatic and terrestrial animals and may forage both in shallow water and on dry ground.",
    "image": "Black-HeadedIbis1.jpg",
    "quick_facts": {
        "family": "Threskiornithidae",
        "size": "65–75 cm",
        "weight": "1.3–1.6 kg",
        "wingspan": "Approximately 110–125 cm",
        "diet": "Fish, frogs, insects, crustaceans, worms, molluscs, and other small animals",
        "habitat": "Wetlands, marshes, flooded fields, riverbanks, grasslands, and agricultural areas",
        "behaviour": "Forages by walking slowly through shallow water or wet ground and probing with its long bill",
        "activity": "Diurnal",
        "nesting": "Builds a stick nest in trees, shrubs, or other vegetation, often in colonies",
        "breeding_season": "June to October in many parts of India",
        "clutch_size": "Usually 2–4 eggs",
        "call": "Generally quiet, producing low grunts and croaks around breeding colonies",
        "lifespan": "Several years in the wild",
        "conservation_status": "Near Threatened",
        "where_to_find": "Wetlands, lakes, marshes, flooded agricultural fields, riverbanks, and shallow-water habitats across India"
    }
},

{
    "name": "Black Kite",
    "scientific": "Milvus migrans",
    "description": "The Black Kite is a widespread bird of prey and one of the most familiar raptors around towns and cities in South Asia. Despite its common name, its plumage is generally dark brown rather than truly black, with a somewhat paler head and body. Its long wings and forked tail allow it to soar effortlessly on rising air currents. Black Kites are opportunistic feeders and consume carrion, insects, small animals, fish, and discarded food, allowing them to thrive in a wide variety of habitats.",
    "image": "BlackKite1.jpg",
    "quick_facts": {
        "family": "Accipitridae",
        "size": "55–60 cm",
        "weight": "560–1000 g",
        "wingspan": "130–155 cm",
        "diet": "Carrion, insects, fish, small animals, and discarded food",
        "habitat": "Cities, farmland, wetlands, grasslands, open woodland, and rubbish sites",
        "behaviour": "Often soars for long periods and searches for food while flying; highly adaptable around human settlements",
        "activity": "Diurnal",
        "nesting": "Builds a large stick nest in trees, often reusing the same nesting area in successive years",
        "breeding_season": "December to April in much of India",
        "clutch_size": "Usually 2–3 eggs",
        "call": "High-pitched, drawn-out whistling or screaming calls",
        "lifespan": "Around 15–20 years or more in favourable conditions",
        "conservation_status": "Least Concern",
        "where_to_find": "Cities, towns, farmland, wetlands, riversides, open countryside, and other areas with abundant food across India"
    }
},

{
    "name": "Black-Rumped Flameback",
    "scientific": "Dinopium benghalense",
    "description": "The Black-Rumped Flameback is a colourful woodpecker found across much of the Indian subcontinent. It has a bright golden-yellow back and wings, a black rump, and a striking red crest. It uses its powerful bill to hammer into tree trunks and branches in search of insects and their larvae. Its characteristic drumming and calls can reveal its presence even when it is hidden among foliage. The species occurs in forests, wooded areas, gardens, plantations, and urban environments with mature trees.",
    "image": "Black-RumpedFlameback1.jpg",
    "quick_facts": {
        "family": "Picidae",
        "size": "26–30 cm",
        "weight": "90–130 g",
        "wingspan": "Approximately 40–45 cm",
        "diet": "Insects, beetle larvae, ants, termites, and other small invertebrates",
        "habitat": "Forests, woodland, plantations, gardens, orchards, and wooded urban areas",
        "behaviour": "Climbs tree trunks and branches while hammering into wood to locate insects; often drums on resonant surfaces",
        "activity": "Diurnal",
        "nesting": "Excavates a cavity in a tree trunk or branch, usually in dead or decaying wood",
        "breeding_season": "January to May",
        "clutch_size": "Usually 2–3 eggs",
        "call": "Loud, repeated calls accompanied by characteristic drumming on wood",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Forests, wooded gardens, plantations, orchards, parks, and areas with mature trees across India"
    }
},

{
    "name": "Black-Winged Kite",
    "scientific": "Elanus caeruleus",
    "description": "The Black-Winged Kite is a small and elegant bird of prey with a pale grey body, striking black shoulders and wing patches, and bright red eyes. It is often seen hovering almost motionless over grassland and agricultural fields while searching for prey below. Small rodents form an important part of its diet, although it also takes insects, lizards, and small birds. It favours open habitats and frequently perches on poles, wires, and isolated trees from which it can survey the ground.",
    "image": "Black-WingedKite1.jpg",
    "quick_facts": {
        "family": "Accipitridae",
        "size": "30–35 cm",
        "weight": "200–300 g",
        "wingspan": "75–90 cm",
        "diet": "Small rodents, insects, lizards, and small birds",
        "habitat": "Grasslands, farmland, open scrub, savannas, and other open country",
        "behaviour": "Frequently hovers almost motionless while hunting and may also perch on poles, wires, and isolated trees",
        "activity": "Diurnal, with increased hunting activity during the cooler parts of the day",
        "nesting": "Builds a small stick nest in a tree, often using a relatively low branch",
        "breeding_season": "Varies by region; may breed during much of the year where conditions are favourable",
        "clutch_size": "Usually 3–5 eggs",
        "call": "Generally quiet, with soft whistles and squeaks around breeding areas",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Open farmland, grasslands, scrub, roadside areas, and agricultural landscapes across India"
    }
},
{
    "name": "Brown-Headed Barbet",
    "scientific": "Psilopogon zeylanicus",
    "description": "The Brown-Headed Barbet is a large green barbet with a brown head and throat and a distinctive red patch around the eye. It is mainly arboreal and spends much of its time in trees, where it feeds on fruits and occasionally insects. Its repeated, resonant call is one of the characteristic sounds of wooded areas in the Indian subcontinent. It is commonly found in forests, gardens, plantations, orchards, and urban areas with mature trees.",
    "image": "Brown-HeadedBarbet1.jpg",
    "quick_facts": {
        "family": "Megalaimidae",
        "size": "30–34 cm",
        "weight": "180–250 g",
        "wingspan": "Approximately 45–50 cm",
        "diet": "Fruits, berries, figs, and occasionally insects",
        "habitat": "Forests, gardens, orchards, plantations, and wooded urban areas",
        "behaviour": "Arboreal and usually solitary or found in pairs; spends much of its time feeding in trees",
        "activity": "Diurnal",
        "nesting": "Excavates a cavity in a tree trunk or branch",
        "breeding_season": "January to June",
        "clutch_size": "2–4 eggs",
        "call": "Loud, repetitive and resonant calls repeated for long periods",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Wooded gardens, forests, orchards, plantations, and mature trees across India"
    }
},

{
    "name": "Cattle Egret",
    "scientific": "Bubulcus ibis",
    "description": "The Cattle Egret is a compact white heron that is often seen following cattle and other large animals across fields. The birds take advantage of insects and other small creatures disturbed by the animals as they move through grass. During the breeding season, adults develop orange-buff plumage on the head, neck, and back. It is one of the most adaptable herons and is frequently found far from water.",
    "image": "CattleEgret1.jpg",
    "quick_facts": {
        "family": "Ardeidae",
        "size": "46–56 cm",
        "weight": "270–512 g",
        "wingspan": "88–96 cm",
        "diet": "Insects, frogs, small reptiles, fish, and other small animals",
        "habitat": "Grasslands, farmland, wetlands, pastures, and open countryside",
        "behaviour": "Often follows cattle, buffalo, and other large animals to catch disturbed prey",
        "activity": "Diurnal",
        "nesting": "Builds a platform of sticks in trees or shrubs, usually in colonies",
        "breeding_season": "Varies by region, often during the monsoon or wet season",
        "clutch_size": "2–5 eggs",
        "call": "Harsh croaks and grating calls, especially around colonies",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Farmland, cattle pastures, grasslands, marshes, lakesides, and village surroundings across India"
    }
},

{
    "name": "Common Hoopoe",
    "scientific": "Upupa epops",
    "description": "The Common Hoopoe is a distinctive bird with a long slender bill, boldly patterned black-and-white wings, a warm cinnamon body, and a prominent erectile crest. It usually forages on the ground, probing soil with its long bill for insects and other small prey. Hoopoes are often encountered in open landscapes and cultivated areas, where their striking appearance makes them easy to recognize.",
    "image": "CommonHoopoe1.jpg",
    "quick_facts": {
        "family": "Upupidae",
        "size": "25–32 cm",
        "weight": "46–89 g",
        "wingspan": "44–48 cm",
        "diet": "Insects, larvae, worms, and other small invertebrates",
        "habitat": "Open woodland, farmland, grassland, gardens, and cultivated areas",
        "behaviour": "Forages mainly on the ground by probing soil and leaf litter with its bill",
        "activity": "Diurnal",
        "nesting": "Nests in tree cavities, holes in walls, rocks, or other sheltered cavities",
        "breeding_season": "February to June in much of its range",
        "clutch_size": "5–8 eggs",
        "call": "Distinctive soft, repeated 'oop-oop-oop' calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Open fields, gardens, farmland, parks, dry woodland, and village areas"
    }
},

{
    "name": "Common Kingfisher",
    "scientific": "Alcedo atthis",
    "description": "The Common Kingfisher is a small, brilliantly coloured kingfisher with vivid blue-green upperparts, orange underparts, and a long pointed bill. It usually sits quietly on a branch or other perch overlooking water before plunging rapidly to catch prey. Although widespread across Eurasia, it requires suitable clear water and fish-rich habitats for successful feeding.",
    "image": "CommonKingfisher1.jpg",
    "quick_facts": {
        "family": "Alcedinidae",
        "size": "17–19 cm",
        "weight": "34–46 g",
        "wingspan": "24–26 cm",
        "diet": "Small fish, aquatic insects, crustaceans, tadpoles, and other small aquatic animals",
        "habitat": "Rivers, streams, lakes, ponds, canals, and mangrove waterways",
        "behaviour": "Perches quietly near water and dives rapidly to catch prey",
        "activity": "Diurnal",
        "nesting": "Excavates a tunnel in a sandy or earthen bank, ending in a nesting chamber",
        "breeding_season": "November to March in many parts of India",
        "clutch_size": "5–7 eggs",
        "call": "High-pitched, sharp whistling calls, especially during flight",
        "lifespan": "Around 2–7 years, with some individuals living longer",
        "conservation_status": "Least Concern",
        "where_to_find": "Clear streams, rivers, ponds, lakes, canals, and other freshwater bodies"
    }
},

{
    "name": "Common Myna",
    "scientific": "Acridotheres tristis",
    "description": "The Common Myna is a highly adaptable bird with a brown body, black head, bright yellow eye patch, and yellow legs and bill. It thrives alongside people and can be found in towns, cities, farmland, gardens, and open countryside. Mynas are opportunistic feeders and eat a remarkably varied diet. They are social and vocal birds, often gathering in groups around feeding and roosting sites.",
    "image": "CommonMyna1.jpg",
    "quick_facts": {
        "family": "Sturnidae",
        "size": "23–26 cm",
        "weight": "90–140 g",
        "wingspan": "120–140 cm",
        "diet": "Insects, fruits, seeds, grains, nectar, small reptiles, and food scraps",
        "habitat": "Cities, villages, farmland, gardens, grasslands, and open woodland",
        "behaviour": "Highly social, adaptable, and often seen foraging on the ground in pairs or groups",
        "activity": "Diurnal",
        "nesting": "Uses cavities in trees, buildings, walls, roofs, and other structures",
        "breeding_season": "March to September",
        "clutch_size": "4–5 eggs",
        "call": "Loud whistles, chatters, squawks, and varied imitations",
        "lifespan": "Around 4–12 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Cities, parks, gardens, farmland, villages, markets, and roadsides throughout India"
    }
},

{
    "name": "Common Rosefinch",
    "scientific": "Carpodacus erythrinus",
    "description": "The Common Rosefinch is a medium-sized finch in which adult males develop a distinctive rosy-red head, breast, and rump. Females and immature birds are more subdued brown and heavily streaked. It feeds mainly on seeds, buds, berries, and other plant material and is generally associated with woodland edges, scrub, gardens, and open areas with suitable vegetation.",
    "image": "CommonRosefinch1.jpg",
    "quick_facts": {
        "family": "Fringillidae",
        "size": "13–15 cm",
        "weight": "20–25 g",
        "wingspan": "22–26 cm",
        "diet": "Seeds, buds, berries, grains, and plant material",
        "habitat": "Scrub, woodland edges, meadows, gardens, and mountain valleys",
        "behaviour": "Usually forages quietly in vegetation and may occur singly or in small groups",
        "activity": "Diurnal",
        "nesting": "Builds a cup-shaped nest in shrubs or low trees",
        "breeding_season": "May to August",
        "clutch_size": "4–6 eggs",
        "call": "Soft whistles and varied musical notes",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Scrub, forest edges, gardens, meadows, and suitable upland habitats"
    }
},

{
    "name": "Common Sandpiper",
    "scientific": "Actitis hypoleucos",
    "description": "The Common Sandpiper is a small wader with brown upperparts, white underparts, and a characteristic habit of bobbing its tail and rear body while walking. It is usually found along the edges of water, where it runs quickly over mud, sand, and stones while searching for small invertebrates. Many individuals seen in India are winter visitors from northern breeding grounds.",
    "image": "CommonSandpiper1.jpg",
    "quick_facts": {
        "family": "Scolopacidae",
        "size": "18–24 cm",
        "weight": "20–60 g",
        "wingspan": "32–35 cm",
        "diet": "Insects, worms, crustaceans, molluscs, and other small invertebrates",
        "habitat": "Riverbanks, lakeshores, ponds, mudflats, streams, and coastal areas",
        "behaviour": "Walks quickly along the water's edge while constantly bobbing its hindquarters",
        "activity": "Diurnal",
        "nesting": "Breeds on the ground near freshwater in its northern breeding range",
        "breeding_season": "May to August in breeding areas",
        "clutch_size": "3–5 eggs",
        "call": "Clear, high-pitched whistles, particularly during flight",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Riverbanks, lakes, ponds, reservoirs, wetlands, estuaries, and coastal shores"
    }
},

{
    "name": "Common Stonechat",
    "scientific": "Saxicola torquatus",
    "description": "The Common Stonechat is a small, upright songbird often seen perched prominently on shrubs, grass stems, fences, and other exposed points. Adult males typically have a dark head, orange breast, and pale collar, while females are more subdued. It feeds mainly on insects and other small invertebrates and prefers open habitats with scattered vegetation.",
    "image": "CommonStonechat1.jpg",
    "quick_facts": {
        "family": "Muscicapidae",
        "size": "11–13 cm",
        "weight": "12–17 g",
        "wingspan": "18–21 cm",
        "diet": "Insects, spiders, larvae, and other small invertebrates",
        "habitat": "Grassland, scrub, farmland, marsh edges, and open countryside",
        "behaviour": "Perches prominently and makes short flights to catch insects before returning to a perch",
        "activity": "Diurnal",
        "nesting": "Builds a cup-shaped nest low in dense vegetation or on the ground",
        "breeding_season": "March to August in breeding regions",
        "clutch_size": "4–6 eggs",
        "call": "Sharp clicking and chattering calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Open fields, grasslands, scrub, farmland, marshes, and roadside vegetation"
    }
},

{
    "name": "Coppersmith Barbet",
    "scientific": "Psilopogon haemacephalus",
    "description": "The Coppersmith Barbet is a small, colourful green barbet with a red forehead, red throat, and yellow-and-blue facial markings. Its name comes from its repetitive call, which resembles the ringing sound of a coppersmith striking metal. It feeds mainly on fruits and berries and is commonly found in gardens, orchards, wooded parks, and areas with mature fruiting trees.",
    "image": "CoppersmithBarbet1.jpg",
    "quick_facts": {
        "family": "Megalaimidae",
        "size": "16–18 cm",
        "weight": "30–50 g",
        "wingspan": "28–32 cm",
        "diet": "Fruits, berries, figs, and occasionally insects",
        "habitat": "Gardens, orchards, woodland, plantations, parks, and urban areas",
        "behaviour": "Arboreal and often remains hidden among foliage while feeding and calling",
        "activity": "Diurnal",
        "nesting": "Excavates a cavity in a tree branch or trunk",
        "breeding_season": "February to June",
        "clutch_size": "2–4 eggs",
        "call": "Repeated metallic 'tuk-tuk-tuk' notes resembling a coppersmith at work",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Gardens, orchards, parks, plantations, forests, and tree-filled urban areas"
    }
},

{
    "name": "Crested Serpent Eagle",
    "scientific": "Spilornis cheela",
    "description": "The Crested Serpent Eagle is a medium-sized forest raptor with a broad wingspan, rounded wings, a prominent crest, and a distinctive yellow facial area. It feeds mainly on snakes and other reptiles but also takes frogs, small mammals, birds, and insects. Its loud, ringing call is often heard from forested hills before the bird itself is seen soaring overhead.",
    "image": "CrestedSerpentEagle1.jpg",
    "quick_facts": {
        "family": "Accipitridae",
        "size": "55–75 cm",
        "weight": "420–1800 g",
        "wingspan": "110–140 cm",
        "diet": "Snakes, lizards, frogs, small mammals, birds, and insects",
        "habitat": "Forests, woodland, plantations, and forested hills",
        "behaviour": "Often perches quietly before taking short flights or soaring over forested areas",
        "activity": "Diurnal",
        "nesting": "Builds a large stick nest in a tree",
        "breeding_season": "December to May",
        "clutch_size": "Usually 1 egg",
        "call": "Loud, repeated, high-pitched whistling or screaming calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Forests, wooded hills, plantations, and forest edges across much of India"
    }
},

{
    "name": "Great Hornbill",
    "scientific": "Buceros bicornis",
    "description": "The Great Hornbill is one of the most spectacular birds of the Indian subcontinent, recognized by its enormous yellow-and-black bill, large casque, black-and-white wings, and white tail. It is strongly associated with mature forests and depends heavily on large trees for nesting and feeding. Fruits form a major part of its diet, although it also takes small animals. Its powerful wingbeats produce a distinctive whooshing sound as it flies through the forest.",
    "image": "GreatHornbill1.jpg",
    "quick_facts": {
        "family": "Bucerotidae",
        "size": "90–105 cm",
        "weight": "2.2–4 kg",
        "wingspan": "150–180 cm",
        "diet": "Fruits, figs, small mammals, birds, reptiles, and insects",
        "habitat": "Mature tropical and subtropical forests",
        "behaviour": "Arboreal and usually found in pairs or small groups; capable of long flights between fruiting trees",
        "activity": "Diurnal",
        "nesting": "Female seals herself inside a tree cavity, leaving a narrow opening through which the male feeds her",
        "breeding_season": "March to July",
        "clutch_size": "Usually 1–2 eggs",
        "call": "Loud barking, grunting, and honking calls",
        "lifespan": "Several decades are possible",
        "conservation_status": "Vulnerable",
        "where_to_find": "Large forest tracts with mature fruiting and nesting trees, especially in the Western Ghats and Northeast India"
    }
},

{
    "name": "Greater Coucal",
    "scientific": "Centropus sinensis",
    "description": "The Greater Coucal is a large, heavy cuckoo with a glossy black head and body, chestnut wings, and a long black tail. Unlike many cuckoos, it is a poor flyer and spends much of its time walking and hopping through dense vegetation. It feeds on insects, frogs, reptiles, eggs, nestlings, and various other small animals. Its deep, resonant calls are a familiar sound in scrub and gardens across India.",
    "image": "GreaterCoucal1.jpg",
    "quick_facts": {
        "family": "Cuculidae",
        "size": "43–50 cm",
        "weight": "225–400 g",
        "wingspan": "Approximately 55–65 cm",
        "diet": "Insects, frogs, lizards, small snakes, eggs, nestlings, and small animals",
        "habitat": "Scrub, grassland, gardens, plantations, wetlands, and woodland edges",
        "behaviour": "Usually walks through dense vegetation rather than flying long distances",
        "activity": "Diurnal",
        "nesting": "Builds a large domed nest from grasses and leaves in dense vegetation",
        "breeding_season": "March to September",
        "clutch_size": "2–4 eggs",
        "call": "Deep, resonant 'coop-coop-coop' calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Dense scrub, gardens, grasslands, plantations, wetlands, and forest edges"
    }
},

{
    "name": "Indian Golden Oriole",
    "scientific": "Oriolus kundoo",
    "description": "The Indian Golden Oriole is a striking yellow-and-black songbird, with adult males showing brilliant golden-yellow plumage and bold black markings around the eye and wings. It spends much of its time in the canopy, feeding on fruits and insects. Its melodious calls are often heard before the bird is located among the leaves.",
    "image": "IndianGoldenOriole1.jpg",
    "quick_facts": {
        "family": "Oriolidae",
        "size": "23–25 cm",
        "weight": "65–100 g",
        "wingspan": "Approximately 40–45 cm",
        "diet": "Fruits, berries, insects, caterpillars, and nectar",
        "habitat": "Woodland, forests, gardens, orchards, and plantations",
        "behaviour": "Arboreal and usually stays high in trees while feeding",
        "activity": "Diurnal",
        "nesting": "Builds a suspended cup-like nest in a tree fork",
        "breeding_season": "April to June",
        "clutch_size": "2–3 eggs",
        "call": "Clear, fluting and melodious whistles",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Wooded gardens, orchards, forests, plantations, and mature trees"
    }
},

{
    "name": "Indian Grey Hornbill",
    "scientific": "Ocyceros birostris",
    "description": "The Indian Grey Hornbill is a medium-sized hornbill with grey plumage, a long tail, and a dark bill with a casque. It is well adapted to open woodland and urban environments containing mature trees. Fruits form a major part of its diet, although it also catches insects and small animals. It is frequently seen flying between trees with steady, powerful wingbeats.",
    "image": "IndianGreyHornbill1.jpg",
    "quick_facts": {
        "family": "Bucerotidae",
        "size": "61 cm",
        "weight": "350–450 g",
        "wingspan": "Approximately 80–90 cm",
        "diet": "Fruits, figs, insects, reptiles, and small birds",
        "habitat": "Open woodland, gardens, farmland, plantations, and urban areas with mature trees",
        "behaviour": "Arboreal and usually seen in pairs or small groups",
        "activity": "Diurnal",
        "nesting": "Female seals herself inside a tree cavity while the male supplies food",
        "breeding_season": "February to May",
        "clutch_size": "2–3 eggs",
        "call": "Loud squeals, grunts, and hornbill-like calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Open forests, gardens, parks, farmland, and large trees in urban areas"
    }
},

{
    "name": "Indian Openbill",
    "scientific": "Anastomus oscitans",
    "description": "The Indian Openbill is a medium-sized stork named for the noticeable gap between the upper and lower parts of its bill when it is closed. It is mainly associated with wetlands, flooded fields, marshes, and shallow waters, where it feeds largely on freshwater snails and other aquatic animals. It often forages in groups and can be seen walking through shallow water searching for prey.",
    "image": "IndianOpenbill1.jpg",
    "quick_facts": {
        "family": "Ciconiidae",
        "size": "68–81 cm",
        "weight": "1.2–1.6 kg",
        "wingspan": "Approximately 145–155 cm",
        "diet": "Freshwater snails, frogs, fish, insects, and other aquatic animals",
        "habitat": "Marshes, flooded fields, ponds, lakes, wetlands, and rice paddies",
        "behaviour": "Usually forages by walking through shallow water and probing for aquatic prey",
        "activity": "Diurnal",
        "nesting": "Builds a large stick nest in trees, often in colonies",
        "breeding_season": "July to October in much of India",
        "clutch_size": "2–4 eggs",
        "call": "Generally quiet away from colonies, with bill-clattering and other sounds at nesting sites",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Wetlands, rice fields, marshes, ponds, lakes, and flooded agricultural areas"
    }
},

{
    "name": "Indian Peafowl",
    "scientific": "Pavo cristatus",
    "description": "The Indian Peafowl is one of the most recognizable birds of the Indian subcontinent. Adult males have an elaborate train of elongated upper-tail coverts decorated with eye-like markings, while females are smaller and more subdued in colour. Peafowl feed on seeds, fruits, insects, reptiles, and other food and are highly adaptable. Males display their train during courtship and produce loud calls that carry over considerable distances.",
    "image": "IndianPeafowl1.jpg",
    "quick_facts": {
        "family": "Phasianidae",
        "size": "90–230 cm including male's train",
        "weight": "2.7–6 kg",
        "wingspan": "Approximately 130–160 cm",
        "diet": "Seeds, grains, fruits, insects, reptiles, small animals, and plant matter",
        "habitat": "Open woodland, scrub, farmland, grassland, villages, and parks",
        "behaviour": "Usually forages on the ground and roosts in trees at night",
        "activity": "Diurnal",
        "nesting": "Scrapes a shallow nest on the ground, usually concealed in vegetation",
        "breeding_season": "April to September, varying with rainfall",
        "clutch_size": "4–8 eggs",
        "call": "Loud, harsh and far-carrying calls",
        "lifespan": "Around 10–20 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Scrub, farmland, open forests, villages, parks, and woodland edges throughout India"
    }
},

{
    "name": "Indian Pitta",
    "scientific": "Pitta brachyura",
    "description": "The Indian Pitta is a brightly coloured forest-floor bird with a green back, blue crown, black eye stripe, buff underparts, and red or orange lower body. It is generally shy and spends much of its time moving through leaf litter in search of prey. Its distinctive two-note call is often heard from dense vegetation. The species is especially associated with moist forests and woodland during its breeding range and can be encountered more widely during migration.",
    "image": "IndianPitta1.jpg",
    "quick_facts": {
        "family": "Pittidae",
        "size": "15–18 cm",
        "weight": "40–60 g",
        "wingspan": "25–28 cm",
        "diet": "Insects, worms, snails, spiders, and other small invertebrates",
        "habitat": "Moist forest, woodland, scrub, plantations, and leafy gardens",
        "behaviour": "Forages mainly on the ground, tossing aside leaf litter while searching for prey",
        "activity": "Diurnal",
        "nesting": "Builds a roughly spherical nest of leaves and vegetation close to the ground",
        "breeding_season": "June to August in much of India",
        "clutch_size": "4–6 eggs",
        "call": "Distinctive repeated two-note whistle",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Moist forests, wooded gardens, plantations, forest floors, and leafy habitats"
    }
},

{
    "name": "Indian Roller",
    "scientific": "Coracias benghalensis",
    "description": "The Indian Roller is a striking blue and brown bird commonly seen perched on wires, poles, trees, and other exposed locations. Its wings display brilliant shades of blue when it flies, making it especially spectacular in flight. It hunts insects and small animals from a perch and is common in open country, farmland, grassland, and urban areas. During courtship and territorial disputes, it performs dramatic rolling and tumbling flights.",
    "image": "IndianRoller1.jpg",
    "quick_facts": {
        "family": "Coraciidae",
        "size": "30–34 cm",
        "weight": "130–180 g",
        "wingspan": "65–75 cm",
        "diet": "Insects, frogs, lizards, small birds, and other small animals",
        "habitat": "Open woodland, farmland, grassland, roadside areas, and towns",
        "behaviour": "Perches in exposed locations and drops down to capture prey from the ground",
        "activity": "Diurnal",
        "nesting": "Uses cavities in trees, buildings, cliffs, or other structures",
        "breeding_season": "March to June",
        "clutch_size": "3–5 eggs",
        "call": "Harsh, chattering and crow-like calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Farmland, grasslands, roadsides, open woodland, villages, and urban outskirts"
    }
},

{
    "name": "Indian Silverbill",
    "scientific": "Euodice malabarica",
    "description": "The Indian Silverbill is a small finch-like munia with a pale brown body, whitish underparts, a blackish bill, and a distinctive pale rump. It is usually found in dry grasslands, scrub, agricultural areas, and open woodland, where it feeds mainly on grass seeds. It is social and often travels in small flocks, particularly outside the breeding season.",
    "image": "IndianSilverbill1.jpg",
    "quick_facts": {
        "family": "Estrildidae",
        "size": "11–12 cm",
        "weight": "10–15 g",
        "wingspan": "16–18 cm",
        "diet": "Grass seeds, grains, and other small seeds",
        "habitat": "Grassland, scrub, farmland, dry woodland, and open country",
        "behaviour": "Social and often seen in small flocks feeding on the ground or among grasses",
        "activity": "Diurnal",
        "nesting": "Builds a rounded grass nest in bushes, grass clumps, or other vegetation",
        "breeding_season": "Throughout much of the year, depending on rainfall",
        "clutch_size": "4–8 eggs",
        "call": "Soft chirps and twittering calls",
        "lifespan": "Several years in captivity; shorter on average in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Dry grasslands, scrub, farmland, village outskirts, and open fields"
    }
},

{
    "name": "Jungle Babbler",
    "scientific": "Argya striata",
    "description": "The Jungle Babbler is a social, noisy bird commonly seen moving through vegetation in small groups. Its grey-brown plumage is relatively plain, but its lively behaviour and constant chatter make it easy to recognize. Groups forage together on the ground and in shrubs, searching for insects, seeds, fruit, and other food. They are common in gardens, woodland, scrub, farmland, and urban areas.",
    "image": "JungleBabbler1.jpg",
    "quick_facts": {
        "family": "Leiothrichidae",
        "size": "23–25 cm",
        "weight": "60–85 g",
        "wingspan": "Approximately 30–35 cm",
        "diet": "Insects, fruits, seeds, grains, and small invertebrates",
        "habitat": "Scrub, gardens, woodland, farmland, parks, and urban areas",
        "behaviour": "Highly social and usually travels in noisy groups",
        "activity": "Diurnal",
        "nesting": "Builds a cup-shaped nest in dense shrubs or low trees",
        "breeding_season": "February to September",
        "clutch_size": "2–4 eggs",
        "call": "Loud, continuous chattering and harsh contact calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Gardens, parks, scrub, farmland, woodland edges, and residential areas"
    }
},

{
    "name": "Little Cormorant",
    "scientific": "Microcarbo niger",
    "description": "The Little Cormorant is a small dark waterbird that is common across South Asia. It spends much of its time in or around freshwater, diving beneath the surface to catch fish and other aquatic prey. After feeding, it often perches with its wings spread to dry its plumage. It is highly adaptable and occurs in ponds, lakes, rivers, canals, marshes, and flooded fields.",
    "image": "LittleCormorant1.jpg",
    "quick_facts": {
        "family": "Phalacrocoracidae",
        "size": "55–60 cm",
        "weight": "430–800 g",
        "wingspan": "85–95 cm",
        "diet": "Fish, frogs, crustaceans, and other aquatic animals",
        "habitat": "Lakes, ponds, rivers, canals, marshes, reservoirs, and flooded fields",
        "behaviour": "Excellent underwater swimmer that dives repeatedly to catch prey",
        "activity": "Diurnal",
        "nesting": "Builds a platform of sticks in trees, shrubs, or sometimes reed beds, usually in colonies",
        "breeding_season": "Varies with region and rainfall",
        "clutch_size": "3–5 eggs",
        "call": "Usually quiet away from colonies; produces croaks and grunts at nesting sites",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Freshwater ponds, lakes, rivers, reservoirs, canals, wetlands, and rice fields"
    }
},

{
    "name": "Little Egret",
    "scientific": "Egretta garzetta",
    "description": "The Little Egret is a graceful white heron with a slender black bill, black legs, and bright yellow feet. It usually forages in shallow water, moving carefully or stirring the bottom to flush out small prey. During the breeding season, adults develop delicate plumes on the head and back. It occurs in freshwater and coastal wetlands and is often seen alone or in small groups.",
    "image": "LittleEgret1.jpg",
    "quick_facts": {
        "family": "Ardeidae",
        "size": "55–65 cm",
        "weight": "250–350 g",
        "wingspan": "88–106 cm",
        "diet": "Fish, frogs, crustaceans, insects, and small aquatic animals",
        "habitat": "Marshes, ponds, rivers, lakes, estuaries, mudflats, and coastal wetlands",
        "behaviour": "Wades through shallow water and uses quick movements to catch prey",
        "activity": "Diurnal",
        "nesting": "Builds a stick nest in trees, shrubs, reed beds, or colonies",
        "breeding_season": "Varies by region, often during the wet season",
        "clutch_size": "3–5 eggs",
        "call": "Generally quiet, with harsh croaks around breeding colonies",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Ponds, rivers, marshes, estuaries, rice fields, lakes, and coastal wetlands"
    }
},

{
    "name": "Little Ringed Plover",
    "scientific": "Charadrius dubius",
    "description": "The Little Ringed Plover is a small wader with a distinctive black-and-white head pattern, yellow eye-ring, and yellowish legs. It is usually found near freshwater, especially along exposed muddy or sandy shores. It runs rapidly across open ground before stopping to pick small prey from the surface. Many birds encountered in parts of India are winter visitors.",
    "image": "LittleRingedPlover1.jpg",
    "quick_facts": {
        "family": "Charadriidae",
        "size": "14–15 cm",
        "weight": "30–55 g",
        "wingspan": "35–40 cm",
        "diet": "Insects, worms, crustaceans, and other small invertebrates",
        "habitat": "Mudflats, sandy shores, riverbanks, lake edges, gravel beds, and wetlands",
        "behaviour": "Runs quickly over open ground, frequently stopping to pick prey from the surface",
        "activity": "Diurnal",
        "nesting": "Makes a shallow scrape on bare ground, usually among stones or gravel",
        "breeding_season": "April to July in breeding areas",
        "clutch_size": "3–4 eggs",
        "call": "Soft, high-pitched whistles and piping calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Exposed riverbanks, lake margins, mudflats, gravel beds, and shallow wetlands"
    }
},

{
    "name": "Oriental Magpie-Robin",
    "scientific": "Copsychus saularis",
    "description": "The Oriental Magpie-Robin is a familiar black-and-white songbird of gardens, forests, villages, and urban areas. Males are glossy black with white wing and tail markings, while females are generally greyish. It is an active ground and low-level forager that eats insects and other small invertebrates. Males are especially well known for their varied and melodious songs.",
    "image": "OrientalMagpie-Robin1.jpg",
    "quick_facts": {
        "family": "Muscicapidae",
        "size": "19–21 cm",
        "weight": "30–45 g",
        "wingspan": "Approximately 25–30 cm",
        "diet": "Insects, spiders, worms, small reptiles, and other invertebrates",
        "habitat": "Gardens, forests, woodland, plantations, parks, and villages",
        "behaviour": "Active and territorial; frequently forages on the ground and low branches",
        "activity": "Diurnal",
        "nesting": "Uses cavities, holes, pipes, boxes, and other sheltered spaces",
        "breeding_season": "March to August",
        "clutch_size": "3–5 eggs",
        "call": "Rich, varied and melodious song with many imitations and phrases",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Gardens, parks, forests, plantations, villages, and urban neighbourhoods"
    }
},

{
    "name": "Painted Stork",
    "scientific": "Mycteria leucocephala",
    "description": "The Painted Stork is a large wading bird with a white body, black wing markings, a pinkish head and neck, and a long yellow-orange bill. It often feeds in shallow water by sweeping its partly open bill from side to side to detect fish and other aquatic animals. It is commonly associated with wetlands, lakes, marshes, and flooded fields and frequently nests in large colonies.",
    "image": "PaintedStork1.jpg",
    "quick_facts": {
        "family": "Ciconiidae",
        "size": "93–102 cm",
        "weight": "2–3.5 kg",
        "wingspan": "150–160 cm",
        "diet": "Fish, frogs, crustaceans, insects, and other aquatic animals",
        "habitat": "Wetlands, lakes, marshes, flooded fields, rivers, and shallow water bodies",
        "behaviour": "Forages by sweeping its bill through shallow water and often feeds in groups",
        "activity": "Diurnal",
        "nesting": "Builds large stick nests in trees, usually in colonies",
        "breeding_season": "August to October in many parts of India",
        "clutch_size": "2–5 eggs",
        "call": "Generally quiet, with bill-clattering and soft sounds around colonies",
        "lifespan": "Several years in the wild",
        "conservation_status": "Near Threatened",
        "where_to_find": "Large wetlands, lakes, marshes, reservoirs, flooded fields, and shallow waterways"
    }
},

{
    "name": "Purple-Rumped Sunbird",
    "scientific": "Leptocoma zeylonica",
    "description": "The Purple-Rumped Sunbird is a tiny nectar-feeding bird found mainly in the Indian subcontinent. Breeding males display brilliant purple, blue, green, and maroon plumage, while females are much more subdued. It feeds on nectar from flowers and also takes small insects, particularly when feeding young. Its small size and rapid movements make it easy to miss despite its vivid colours.",
    "image": "Purple-RumpedSunbird1.jpg",
    "quick_facts": {
        "family": "Nectariniidae",
        "size": "10–12 cm",
        "weight": "6–8 g",
        "wingspan": "13–15 cm",
        "diet": "Nectar, small insects, spiders, and other tiny invertebrates",
        "habitat": "Gardens, forests, plantations, scrub, and flowering trees",
        "behaviour": "Highly active and frequently moves between flowers while feeding",
        "activity": "Diurnal",
        "nesting": "Builds a hanging pouch-like nest from plant fibres, grass, and spider webs",
        "breeding_season": "November to March in many areas, with regional variation",
        "clutch_size": "Usually 2 eggs",
        "call": "High-pitched, rapid and twittering calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Flowering gardens, forests, plantations, scrub, and wooded urban areas"
    }
},

{
    "name": "Purple Sunbird",
    "scientific": "Cinnyris asiaticus",
    "description": "The Purple Sunbird is a tiny, active nectar feeder and one of the most familiar sunbirds in India. Breeding males can appear almost black in ordinary light but show brilliant purple, blue, and green iridescence when illuminated. Females are olive-yellow and much less conspicuous. The species is highly adaptable and occurs in gardens, forests, scrub, plantations, and cities wherever flowering plants provide food.",
    "image": "PurpleSunbird1.jpg",
    "quick_facts": {
        "family": "Nectariniidae",
        "size": "10–11 cm",
        "weight": "7–10 g",
        "wingspan": "13–15 cm",
        "diet": "Nectar, insects, spiders, and other small invertebrates",
        "habitat": "Gardens, scrub, woodland, plantations, parks, and urban areas",
        "behaviour": "Active and agile; frequently hovers or perches beside flowers while feeding",
        "activity": "Diurnal",
        "nesting": "Builds a hanging pouch-shaped nest from fibres, grass, and spider webs",
        "breeding_season": "Throughout much of the year, depending on local conditions",
        "clutch_size": "Usually 2 eggs",
        "call": "Rapid, high-pitched twittering and chirping",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Gardens, parks, flowering trees, scrub, plantations, and urban neighbourhoods"
    }
},

{
    "name": "Red-Vented Bulbul",
    "scientific": "Pycnonotus cafer",
    "description": "The Red-Vented Bulbul is a familiar and adaptable songbird with a black head and crest, brown body, white rump patch, and distinctive red vent. It occurs in almost every type of semi-open habitat, including gardens, farmland, scrub, parks, and cities. It feeds on fruits, berries, nectar, insects, and other foods and is often seen moving actively through bushes and trees.",
    "image": "Red-VentedBulbul1.jpg",
    "quick_facts": {
        "family": "Pycnonotidae",
        "size": "19–21 cm",
        "weight": "30–45 g",
        "wingspan": "26–30 cm",
        "diet": "Fruits, berries, nectar, insects, seeds, and flower buds",
        "habitat": "Gardens, scrub, woodland, farmland, parks, and urban areas",
        "behaviour": "Active and social; often forages in pairs or small groups",
        "activity": "Diurnal",
        "nesting": "Builds a small cup-shaped nest in bushes, shrubs, or low trees",
        "breeding_season": "February to September",
        "clutch_size": "2–3 eggs",
        "call": "Varied musical, chattering, and sharp calls",
        "lifespan": "Around 10 years in favourable conditions",
        "conservation_status": "Least Concern",
        "where_to_find": "Gardens, parks, scrub, farmland, villages, and cities throughout India"
    }
},

{
    "name": "Red-Whiskered Bulbul",
    "scientific": "Pycnonotus jocosus",
    "description": "The Red-Whiskered Bulbul is an attractive crested bulbul with a black head, white cheek, red ear patch, brown back, and red vent. It is an energetic bird that feeds on fruit, nectar, and insects and is often found in gardens, forest edges, plantations, and scrub. Its pointed crest and red facial markings make it particularly distinctive.",
    "image": "Red-WhiskeredBulbul1.jpg",
    "quick_facts": {
        "family": "Pycnonotidae",
        "size": "20–22 cm",
        "weight": "23–42 g",
        "wingspan": "26–29 cm",
        "diet": "Fruits, berries, nectar, insects, and flower buds",
        "habitat": "Gardens, scrub, woodland edges, plantations, and forests",
        "behaviour": "Active and social, often moving through vegetation in pairs or small groups",
        "activity": "Diurnal",
        "nesting": "Builds a cup-shaped nest in shrubs, bushes, or small trees",
        "breeding_season": "January to August, varying by region",
        "clutch_size": "2–3 eggs",
        "call": "Clear whistles, chattering notes, and varied calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Gardens, forest edges, plantations, scrub, parks, and wooded neighbourhoods"
    }
},

{
    "name": "Red-Wattled Lapwing",
    "scientific": "Vanellus indicus",
    "description": "The Red-Wattled Lapwing is a large, conspicuous wader with a black head and breast, white underparts, brown wings, yellow legs, and a distinctive red fleshy wattle at the base of the bill. It is commonly found in open habitats near water but can also live far from wetlands. Its loud alarm call is one of the characteristic sounds of the Indian countryside, especially at night.",
    "image": "Red-WattledLapwing1.jpg",
    "quick_facts": {
        "family": "Charadriidae",
        "size": "32–35 cm",
        "weight": "200–300 g",
        "wingspan": "75–85 cm",
        "diet": "Insects, worms, molluscs, seeds, and other small invertebrates",
        "habitat": "Open fields, wetlands, riverbanks, grasslands, farmland, and lake margins",
        "behaviour": "Alert and territorial; gives loud alarm calls when predators or people approach",
        "activity": "Diurnal and often active at night",
        "nesting": "Makes a shallow scrape on open ground, usually with little nest material",
        "breeding_season": "March to August",
        "clutch_size": "Usually 3–4 eggs",
        "call": "Extremely loud, repeated 'did-he-do-it' style alarm calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Farmland, grasslands, wetland edges, riverbanks, lakeshores, and open ground"
    }
},

{
    "name": "Rose-Ringed Parakeet",
    "scientific": "Psittacula krameri",
    "description": "The Rose-Ringed Parakeet is a familiar bright-green parakeet with a long pointed tail and large red bill. Adult males develop a narrow dark and rose-coloured neck ring, while females and young birds lack the complete male pattern. It is highly adaptable and thrives in gardens, farmland, forests, plantations, and cities. Large noisy flocks are often seen flying between roosting and feeding areas.",
    "image": "Rose-RingedParakeet1.jpg",
    "quick_facts": {
        "family": "Psittaculidae",
        "size": "40–42 cm",
        "weight": "95–140 g",
        "wingspan": "42–48 cm",
        "diet": "Fruits, seeds, grains, flowers, buds, and nectar",
        "habitat": "Woodland, farmland, gardens, plantations, parks, and cities",
        "behaviour": "Highly social and often gathers in noisy flocks, particularly at roosts",
        "activity": "Diurnal",
        "nesting": "Uses cavities in trees, buildings, walls, and other structures",
        "breeding_season": "December to May",
        "clutch_size": "3–5 eggs",
        "call": "Loud, harsh and repetitive screeches",
        "lifespan": "Around 15–20 years in favourable conditions",
        "conservation_status": "Least Concern",
        "where_to_find": "Cities, gardens, farmland, plantations, parks, and open woodland across India"
    }
},

{
    "name": "Rufous Treepie",
    "scientific": "Dendrocitta vagabunda",
    "description": "The Rufous Treepie is a long-tailed member of the crow family with a striking combination of rufous, grey, black, and white plumage. It is an active and opportunistic bird that moves through trees and often visits the ground in search of food. Its varied diet includes fruits, insects, small animals, eggs, and carrion. It is a common inhabitant of forests, gardens, farmland, and urban areas.",
    "image": "RufousTreepie1.jpg",
    "quick_facts": {
        "family": "Corvidae",
        "size": "45–50 cm",
        "weight": "90–130 g",
        "wingspan": "Approximately 55–65 cm",
        "diet": "Fruits, insects, small reptiles, eggs, nestlings, carrion, and food scraps",
        "habitat": "Forests, woodland, farmland, gardens, plantations, and towns",
        "behaviour": "Active, curious, and usually seen alone, in pairs, or small family groups",
        "activity": "Diurnal",
        "nesting": "Builds a shallow stick nest in trees",
        "breeding_season": "April to June",
        "clutch_size": "2–5 eggs",
        "call": "Loud, varied and distinctive chattering or metallic calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Forests, gardens, plantations, farmland, parks, and wooded urban areas"
    }
},

{
    "name": "Scaly-Breasted Munia",
    "scientific": "Lonchura punctulata",
    "description": "The Scaly-Breasted Munia is a small, compact finch-like bird with a chestnut head and upperparts and strongly scaled markings across the pale breast and belly. It feeds mainly on grass seeds and grains and is often found in flocks in grassland and agricultural areas. It is a common bird of fields, scrub, gardens, and areas of tall grass.",
    "image": "Scaly-BreastedMunia1.jpg",
    "quick_facts": {
        "family": "Estrildidae",
        "size": "11–12 cm",
        "weight": "10–15 g",
        "wingspan": "16–18 cm",
        "diet": "Grass seeds, grains, and other small seeds",
        "habitat": "Grassland, farmland, scrub, gardens, and reed beds",
        "behaviour": "Highly social and often forms flocks while feeding on the ground or in grasses",
        "activity": "Diurnal",
        "nesting": "Builds a spherical or dome-shaped nest from grass and plant fibres",
        "breeding_season": "Throughout much of the year, especially after rains",
        "clutch_size": "4–8 eggs",
        "call": "Soft chirps, whistles, and twittering calls",
        "lifespan": "Several years in captivity and generally shorter in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Grasslands, rice fields, farmland, scrub, gardens, and grassy roadsides"
    }
},

{
    "name": "Shikra",
    "scientific": "Accipiter badius",
    "description": "The Shikra is a small woodland hawk with short rounded wings, a long tail, and sharp talons. Adults commonly show grey upperparts and barred underparts, while females are generally larger than males. It is an agile hunter that catches small birds, lizards, rodents, frogs, and insects. Shikras are adaptable and can live in forests, farmland, gardens, plantations, and cities with sufficient tree cover.",
    "image": "Shikra1.jpg",
    "quick_facts": {
        "family": "Accipitridae",
        "size": "26–30 cm",
        "weight": "90–250 g",
        "wingspan": "50–60 cm",
        "diet": "Small birds, lizards, rodents, frogs, insects, and other small animals",
        "habitat": "Woodland, forests, farmland, plantations, gardens, and urban areas",
        "behaviour": "Fast and agile hunter that often uses surprise attacks from cover",
        "activity": "Diurnal",
        "nesting": "Builds a stick nest in a tree, often using an existing structure",
        "breeding_season": "March to June",
        "clutch_size": "3–4 eggs",
        "call": "Repeated high-pitched whistles, particularly around breeding areas",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Wooded gardens, forests, plantations, farmland, parks, and urban areas with mature trees"
    }
},

{
    "name": "White-Breasted Waterhen",
    "scientific": "Amaurornis phoenicurus",
    "description": "The White-Breasted Waterhen is a dark waterbird with a white face, breast, and belly, a reddish undertail, and long yellowish legs. It is commonly found around freshwater wetlands, ponds, marshes, canals, and overgrown waterways. It often walks through dense vegetation and shallow water searching for insects, molluscs, seeds, and other food. Despite its wetland association, it can occur surprisingly close to human settlements.",
    "image": "White-BreastedWaterhen1.jpg",
    "quick_facts": {
        "family": "Rallidae",
        "size": "28–33 cm",
        "weight": "170–300 g",
        "wingspan": "45–50 cm",
        "diet": "Insects, worms, molluscs, seeds, frogs, and small aquatic animals",
        "habitat": "Marshes, ponds, canals, rice fields, wetlands, and dense vegetation near water",
        "behaviour": "Walks actively through vegetation and shallow water and may swim when necessary",
        "activity": "Diurnal and crepuscular",
        "nesting": "Builds a platform or cup-like nest among reeds, grasses, or waterside vegetation",
        "breeding_season": "June to September in many parts of India",
        "clutch_size": "4–9 eggs",
        "call": "Loud repeated clucks, screams, and harsh calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Ponds, marshes, rice fields, canals, wetlands, and overgrown water edges"
    }
},

{
    "name": "White-Rumped Munia",
    "scientific": "Lonchura striata",
    "description": "The White-Rumped Munia is a small, social seed-eating bird with dark brown plumage and a contrasting white rump. It usually occurs in grasslands, scrub, cultivated areas, and forest edges and often travels in flocks. It feeds mainly on grass seeds and grains and can be difficult to notice until a group suddenly rises from the vegetation.",
    "image": "White-RumpedMunia1.jpg",
    "quick_facts": {
        "family": "Estrildidae",
        "size": "10–12 cm",
        "weight": "10–15 g",
        "wingspan": "16–18 cm",
        "diet": "Grass seeds, grains, and other small seeds",
        "habitat": "Grassland, scrub, farmland, woodland edges, and gardens",
        "behaviour": "Highly social and usually feeds in flocks among grasses",
        "activity": "Diurnal",
        "nesting": "Builds a rounded or domed nest from grass and plant fibres",
        "breeding_season": "Varies by region and rainfall",
        "clutch_size": "4–7 eggs",
        "call": "Soft chirping and twittering calls",
        "lifespan": "Several years in captivity; generally shorter in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Grasslands, fields, scrub, plantations, gardens, and forest edges"
    }
},

{
    "name": "White-Throated Kingfisher",
    "scientific": "Halcyon smyrnensis",
    "description": "The White-Throated Kingfisher is a large and colourful kingfisher with a bright blue back and wings, chestnut head and body, white throat and breast, and a large red bill. Despite its name, it is not restricted to aquatic habitats and frequently hunts from perches far from water. It catches insects, lizards, frogs, small birds, and other prey and is one of the most widespread kingfishers in India.",
    "image": "White-ThroatedKingfisher1.jpg",
    "quick_facts": {
        "family": "Alcedinidae",
        "size": "27–29 cm",
        "weight": "80–100 g",
        "wingspan": "42–45 cm",
        "diet": "Fish, frogs, lizards, insects, small birds, rodents, and other small animals",
        "habitat": "Open woodland, farmland, gardens, wetlands, villages, and urban areas",
        "behaviour": "Perches on exposed branches, wires, or poles before diving or dropping onto prey",
        "activity": "Diurnal",
        "nesting": "Excavates a tunnel in an earthen bank or similar soft substrate",
        "breeding_season": "February to July",
        "clutch_size": "4–7 eggs",
        "call": "Loud, harsh and rattling calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Farmland, gardens, roadsides, wetlands, villages, parks, and open countryside"
    }
},

{
    "name": "Brahminy Kite",
    "scientific": "Haliastur indus",
    "description": "The Brahminy Kite is a striking raptor with a chestnut-brown body, contrasting white head and breast, broad wings, and a rounded tail. It is particularly associated with coastal areas, rivers, wetlands, and other places where fish and carrion are available. It often soars gracefully and can be seen perched near water. Its distinctive plumage makes it one of India's most recognizable birds of prey.",
    "image": "BrahminyKite1.jpg",
    "quick_facts": {
        "family": "Accipitridae",
        "size": "44–52 cm",
        "weight": "500–800 g",
        "wingspan": "110–125 cm",
        "diet": "Fish, carrion, frogs, insects, crustaceans, and small animals",
        "habitat": "Coasts, rivers, wetlands, lakes, mangroves, and open woodland",
        "behaviour": "Often soars over water and scavenges or catches prey near the surface",
        "activity": "Diurnal",
        "nesting": "Builds a large stick nest in tall trees, often near water",
        "breeding_season": "December to April",
        "clutch_size": "Usually 2 eggs",
        "call": "High-pitched whistles and shrill calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Coastal regions, rivers, lakes, wetlands, mangroves, and areas near fish-rich waters"
    }
},

{
    "name": "Brahminy Starling",
    "scientific": "Sturnia pagodarum",
    "description": "The Brahminy Starling is an attractive medium-sized starling with a pale body, black crest, chestnut shoulders, and yellowish bill and legs. It is usually found in open woodland, scrub, farmland, gardens, and dry areas. It feeds on fruits, insects, nectar, and seeds and often moves through trees and bushes in pairs or small groups.",
    "image": "BrahminyStarling1.jpg",
    "quick_facts": {
        "family": "Sturnidae",
        "size": "19–21 cm",
        "weight": "55–70 g",
        "wingspan": "Approximately 35–40 cm",
        "diet": "Fruits, insects, nectar, seeds, and grains",
        "habitat": "Open woodland, scrub, farmland, gardens, and dry countryside",
        "behaviour": "Active and social, usually seen singly, in pairs, or small groups",
        "activity": "Diurnal",
        "nesting": "Uses tree cavities and other sheltered holes for nesting",
        "breeding_season": "April to July",
        "clutch_size": "3–5 eggs",
        "call": "Varied whistles, clicks, and chattering notes",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Scrub, open forests, farmland, gardens, villages, and dry woodland"
    }
},

{
    "name": "Indian Robin",
    "scientific": "Copsychus fulicatus",
    "description": "The Indian Robin is a small, active songbird of open and dry habitats. Males are generally dark with a contrasting white shoulder or wing patch, while females are browner. It spends much of its time close to the ground, running between rocks, shrubs, and grass while searching for insects. Its upright posture and habit of flicking its tail are useful identification features.",
    "image": "IndianRobin1.jpg",
    "quick_facts": {
        "family": "Muscicapidae",
        "size": "17–18 cm",
        "weight": "20–25 g",
        "wingspan": "Approximately 25–28 cm",
        "diet": "Insects, spiders, worms, and other small invertebrates",
        "habitat": "Dry scrub, rocky areas, grassland, farmland, and open woodland",
        "behaviour": "Active ground forager that often perches on low rocks and bushes",
        "activity": "Diurnal",
        "nesting": "Nests in cavities, holes among rocks, walls, or other sheltered places",
        "breeding_season": "February to September",
        "clutch_size": "2–4 eggs",
        "call": "Short whistles, clicks, and varied song",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Dry scrub, rocky landscapes, open fields, villages, farmland, and gardens"
    }
},

{
    "name": "Common Tailorbird",
    "scientific": "Orthotomus sutorius",
    "description": "The Common Tailorbird is a tiny, active warbler named for its remarkable nest-building technique. It stitches or binds large leaves together with plant fibres and spider silk to form a protective structure around its nest. It has a green back, pale underparts, a rusty crown, and a long tail often held upright. It is extremely common in gardens, scrub, plantations, and urban areas.",
    "image": "CommonTailorbird1.jpg",
    "quick_facts": {
        "family": "Cisticolidae",
        "size": "13–14 cm",
        "weight": "6–10 g",
        "wingspan": "13–17 cm",
        "diet": "Insects, caterpillars, spiders, and other small invertebrates",
        "habitat": "Gardens, scrub, woodland edges, plantations, parks, and cities",
        "behaviour": "Highly active and often moves rapidly through leaves and shrubs",
        "activity": "Diurnal",
        "nesting": "Stitches or binds leaves together with plant fibres and spider silk",
        "breeding_season": "Throughout much of the year, especially during the monsoon",
        "clutch_size": "2–4 eggs",
        "call": "Loud, repetitive and sharp 'chee-up' style calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Gardens, hedges, shrubs, plantations, parks, and urban greenery"
    }
},

{
    "name": "Greater Racket-Tailed Drongo",
    "scientific": "Dicrurus paradiseus",
    "description": "The Greater Racket-Tailed Drongo is a spectacular forest bird with glossy black plumage, a prominent crest, and exceptionally long tail feathers ending in racket-shaped tips. It is an agile aerial hunter and also feeds on insects taken from foliage. It is famous for its varied vocal abilities and can imitate the calls of other birds. It usually inhabits forests and mature woodland with dense canopy.",
    "image": "GreaterRacket-TailedDrongo1.jpg",
    "quick_facts": {
        "family": "Dicruridae",
        "size": "31–36 cm excluding elongated tail feathers",
        "weight": "70–100 g",
        "wingspan": "Approximately 40–45 cm",
        "diet": "Insects and other small invertebrates, with occasional fruit",
        "habitat": "Forests, mature woodland, plantations, and dense tree cover",
        "behaviour": "Agile aerial hunter and vocal mimic that may join mixed-species feeding groups",
        "activity": "Diurnal",
        "nesting": "Builds a small cup-shaped nest on a tree branch",
        "breeding_season": "April to June",
        "clutch_size": "2–4 eggs",
        "call": "Extremely varied whistles, metallic notes, and imitations of other birds",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Forests, plantations, wooded hills, and mature woodland"
    }
},

{
    "name": "Grey Heron",
    "scientific": "Ardea cinerea",
    "description": "The Grey Heron is a large, long-legged wading bird with a long pointed bill, grey wings, white head and neck, and a black crown stripe. It usually hunts from shallow water, standing motionless before striking quickly at fish and other prey. It is widespread across wetlands and can often be seen standing alone along rivers, lakes, ponds, and coastal waters.",
    "image": "GreyHeron1.jpg",
    "quick_facts": {
        "family": "Ardeidae",
        "size": "84–102 cm",
        "weight": "1–2 kg",
        "wingspan": "155–195 cm",
        "diet": "Fish, frogs, reptiles, small mammals, birds, insects, and crustaceans",
        "habitat": "Rivers, lakes, ponds, marshes, estuaries, canals, and coastal wetlands",
        "behaviour": "Usually hunts by standing motionless before making a rapid strike at prey",
        "activity": "Diurnal and sometimes nocturnal",
        "nesting": "Builds large stick nests in trees, reeds, or cliffs, often in colonies",
        "breeding_season": "February to June in many areas",
        "clutch_size": "3–5 eggs",
        "call": "Loud harsh croaking calls, especially in flight",
        "lifespan": "Around 5–15 years, with some individuals living longer",
        "conservation_status": "Least Concern",
        "where_to_find": "Rivers, lakes, wetlands, estuaries, ponds, canals, and coastal shores"
    }
},

{
    "name": "Grey-Headed Fish Eagle",
    "scientific": "Icthyophaga ichthyaetus",
    "description": "The Grey-Headed Fish Eagle is a large fish-eating raptor associated with rivers, lakes, reservoirs, and other freshwater habitats. Adults have a distinctive grey head, dark brown body, powerful yellow bill and legs, and broad wings. It usually hunts by watching from a perch near water and swooping down to seize fish. Its large size and deep wingbeats make it an impressive sight along wooded waterways.",
    "image": "Grey-HeadedFishEagle1.jpg",
    "quick_facts": {
        "family": "Accipitridae",
        "size": "61–72 cm",
        "weight": "1.5–2.5 kg",
        "wingspan": "150–170 cm",
        "diet": "Fish, frogs, reptiles, waterbirds, and other aquatic animals",
        "habitat": "Rivers, lakes, reservoirs, wetlands, and forested waterways",
        "behaviour": "Often watches from a high perch and dives or swoops down to catch fish",
        "activity": "Diurnal",
        "nesting": "Builds a large stick nest in a tall tree near water",
        "breeding_season": "November to May",
        "clutch_size": "Usually 1–2 eggs",
        "call": "High-pitched whistles and repeated cries",
        "lifespan": "Several years in the wild",
        "conservation_status": "Near Threatened",
        "where_to_find": "Large rivers, lakes, reservoirs, wetlands, and forested freshwater habitats"
    }
},

{
    "name": "Indian Cormorant",
    "scientific": "Phalacrocorax fuscicollis",
    "description": "The Indian Cormorant is a dark waterbird with a long neck, slender bill, and distinctive greenish facial skin. It is an excellent swimmer and dives underwater to catch fish and other aquatic prey. Groups often perch together on exposed branches, rocks, or posts after feeding. It is widely distributed across freshwater wetlands and is especially common in southern and central India.",
    "image": "IndianCormorant1.jpg",
    "quick_facts": {
        "family": "Phalacrocoracidae",
        "size": "63–65 cm",
        "weight": "650–1000 g",
        "wingspan": "90–105 cm",
        "diet": "Fish, frogs, crustaceans, and other aquatic animals",
        "habitat": "Rivers, lakes, reservoirs, ponds, canals, marshes, and wetlands",
        "behaviour": "Dives underwater to catch fish and often rests with wings spread to dry them",
        "activity": "Diurnal",
        "nesting": "Builds a stick nest in trees or shrubs, usually in colonies",
        "breeding_season": "Varies by region and rainfall",
        "clutch_size": "3–5 eggs",
        "call": "Usually quiet away from colonies; produces grunts and croaks at nesting sites",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Rivers, lakes, reservoirs, ponds, canals, and freshwater wetlands"
    }
},

{
    "name": "Indian Paradise Flycatcher",
    "scientific": "Terpsiphone paradisi",
    "description": "The Indian Paradise Flycatcher is a striking insect-eating bird with strongly contrasting plumage. Adult males may have long flowing tail feathers and either white or rufous plumage depending on their form, while females are shorter-tailed. It hunts insects from the air and foliage and is especially associated with wooded habitats. Its graceful movements and long tail make it one of India's most beautiful flycatchers.",
    "image": "IndianParadiseFlycatcher1.jpg",
    "quick_facts": {
        "family": "Monarchidae",
        "size": "19–22 cm, with male tail streamers extending much farther",
        "weight": "15–25 g",
        "wingspan": "Approximately 25–30 cm",
        "diet": "Flying insects, caterpillars, beetles, and other small invertebrates",
        "habitat": "Forests, woodland, gardens, plantations, and wooded streams",
        "behaviour": "Agile flycatcher that sallies from perches to catch insects",
        "activity": "Diurnal",
        "nesting": "Builds a small cup-shaped nest in the fork of a tree or shrub",
        "breeding_season": "April to August",
        "clutch_size": "2–4 eggs",
        "call": "Soft whistles and sharp calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Forests, shaded gardens, plantations, woodland streams, and mature tree cover"
    }
},

{
    "name": "Indian Pied Starling",
    "scientific": "Gracupica contra",
    "description": "The Indian Pied Starling is a striking black-and-white starling with a pale bill and distinctive orange or reddish facial skin around the eye. It is a social and adaptable species that often feeds on the ground in groups. It consumes insects, fruits, grains, and other food and is frequently found around villages, farmland, wetlands, and urban areas.",
    "image": "IndianPiedStarling1.jpg",
    "quick_facts": {
        "family": "Sturnidae",
        "size": "21–23 cm",
        "weight": "75–100 g",
        "wingspan": "Approximately 35–40 cm",
        "diet": "Insects, fruits, grains, seeds, nectar, and food scraps",
        "habitat": "Farmland, villages, wetlands, gardens, open woodland, and cities",
        "behaviour": "Social and often forages in groups on open ground",
        "activity": "Diurnal",
        "nesting": "Uses tree cavities, buildings, walls, and other sheltered cavities",
        "breeding_season": "April to September",
        "clutch_size": "3–5 eggs",
        "call": "Loud whistles, chatters, and varied calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Villages, farmland, gardens, wetlands, open fields, and urban areas"
    }
},

{
    "name": "Lesser Whistling Duck",
    "scientific": "Dendrocygna javanica",
    "description": "The Lesser Whistling Duck is a small, brownish duck with a rounded head and longish neck. It is often seen in large groups on ponds, lakes, marshes, rice fields, and other freshwater habitats. It feeds on aquatic vegetation, seeds, insects, and small aquatic animals. Its high-pitched whistling calls are especially noticeable when groups take flight.",
    "image": "LesserWhistlingDuck1.jpg",
    "quick_facts": {
        "family": "Anatidae",
        "size": "38–43 cm",
        "weight": "450–700 g",
        "wingspan": "75–85 cm",
        "diet": "Aquatic plants, seeds, grains, insects, and small aquatic animals",
        "habitat": "Ponds, lakes, marshes, rice fields, reservoirs, and slow-moving waters",
        "behaviour": "Social and often forms large flocks; spends much time resting on water or banks",
        "activity": "Mostly nocturnal and crepuscular, though also active by day",
        "nesting": "Nests among aquatic vegetation, grass, tree cavities, or other sheltered locations",
        "breeding_season": "June to October in much of India",
        "clutch_size": "6–12 eggs",
        "call": "High-pitched whistling calls, especially in flight",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Freshwater ponds, lakes, marshes, rice paddies, reservoirs, and wetlands"
    }
},

{
    "name": "Oriental Darter",
    "scientific": "Anhinga melanogaster",
    "description": "The Oriental Darter is a long-necked waterbird that often swims with only its head and neck above the water, giving it the appearance of a snake. It is an excellent underwater hunter and spears fish with its sharp bill. After feeding, it commonly perches with its wings spread to dry its feathers. It is found in freshwater wetlands, rivers, lakes, marshes, and reservoirs.",
    "image": "OrientalDarter1.jpg",
    "quick_facts": {
        "family": "Anhingidae",
        "size": "85–97 cm",
        "weight": "1.1–1.4 kg",
        "wingspan": "110–120 cm",
        "diet": "Fish, frogs, crustaceans, and other aquatic animals",
        "habitat": "Lakes, rivers, marshes, reservoirs, ponds, and freshwater wetlands",
        "behaviour": "Swims with much of its body submerged and spears fish underwater",
        "activity": "Diurnal",
        "nesting": "Builds a stick nest in trees or shrubs near water, often in colonies",
        "breeding_season": "Varies by region and water conditions",
        "clutch_size": "3–5 eggs",
        "call": "Generally quiet away from colonies; produces grunts and croaks around nesting sites",
        "lifespan": "Several years in the wild",
        "conservation_status": "Near Threatened",
        "where_to_find": "Large freshwater wetlands, lakes, rivers, reservoirs, and marshes"
    }
},

{
    "name": "Pied Kingfisher",
    "scientific": "Ceryle rudis",
    "description": "The Pied Kingfisher is a black-and-white kingfisher famous for hovering above water before diving vertically to catch fish. It has a shaggy crest, long pointed bill, and strongly patterned plumage. It is closely associated with rivers, lakes, reservoirs, estuaries, and other open waters and often hunts from exposed perches as well as by hovering.",
    "image": "PiedKingfisher1.jpg",
    "quick_facts": {
        "family": "Cerylidae",
        "size": "25–29 cm",
        "weight": "70–100 g",
        "wingspan": "46–50 cm",
        "diet": "Fish, aquatic insects, crustaceans, and other small aquatic animals",
        "habitat": "Rivers, lakes, reservoirs, estuaries, canals, and coastal waters",
        "behaviour": "Frequently hovers over water before diving vertically to catch fish",
        "activity": "Diurnal",
        "nesting": "Excavates a tunnel in a sandy or earthen bank",
        "breeding_season": "January to April and sometimes later depending on region",
        "clutch_size": "3–6 eggs",
        "call": "Sharp, rapid rattling calls, especially in flight",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Rivers, lakes, reservoirs, estuaries, canals, and open coastal waters"
    }
},

{
    "name": "Purple Heron",
    "scientific": "Ardea purpurea",
    "description": "The Purple Heron is a large, slender wading bird with rich reddish-brown and purple-grey plumage, a long neck, and long legs. It is generally more secretive than the Grey Heron and often remains hidden among reeds and tall vegetation. It hunts fish, frogs, reptiles, insects, and small mammals in shallow water and wetlands.",
    "image": "PurpleHeron1.jpg",
    "quick_facts": {
        "family": "Ardeidae",
        "size": "78–97 cm",
        "weight": "525–1340 g",
        "wingspan": "120–150 cm",
        "diet": "Fish, frogs, reptiles, insects, crustaceans, and small mammals",
        "habitat": "Reed beds, marshes, lakes, rivers, ponds, and flooded wetlands",
        "behaviour": "Usually hunts slowly and deliberately from shallow water or dense vegetation",
        "activity": "Diurnal",
        "nesting": "Builds a platform nest in reeds, shrubs, or trees, often in colonies",
        "breeding_season": "March to June in many breeding areas",
        "clutch_size": "4–5 eggs",
        "call": "Harsh croaks, especially around breeding colonies",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Marshes, reed beds, lakes, rivers, ponds, flooded fields, and dense wetland vegetation"
    }
},

{
    "name": "Spotted Dove",
    "scientific": "Spilopelia chinensis",
    "description": "The Spotted Dove is a medium-sized dove with a soft pinkish-grey body, dark wings, and a distinctive black-and-white spotted patch on the sides of its neck. It is a highly adaptable species and commonly occurs in gardens, farmland, woodland, villages, and cities. It feeds mainly on seeds and grains and usually forages on the ground.",
    "image": "SpottedDove1.jpg",
    "quick_facts": {
        "family": "Columbidae",
        "size": "28–32 cm",
        "weight": "150–200 g",
        "wingspan": "45–50 cm",
        "diet": "Seeds, grains, fruits, and small amounts of plant material",
        "habitat": "Gardens, farmland, woodland, scrub, villages, and urban areas",
        "behaviour": "Usually forages on the ground singly or in pairs and may gather in groups around food",
        "activity": "Diurnal",
        "nesting": "Builds a flimsy platform of twigs in trees, shrubs, buildings, or ledges",
        "breeding_season": "Throughout much of the year",
        "clutch_size": "Usually 2 eggs",
        "call": "Soft, repetitive cooing song",
        "lifespan": "Around 5–10 years in favourable conditions",
        "conservation_status": "Least Concern",
        "where_to_find": "Gardens, parks, farmland, villages, scrub, and urban neighbourhoods"
    }
},

{
    "name": "Stork-Billed Kingfisher",
    "scientific": "Pelargopsis capensis",
    "description": "The Stork-Billed Kingfisher is a large and powerful kingfisher with a massive red bill, bright blue wings, chestnut head and body, and pale underparts. It is usually found near rivers, lakes, ponds, mangroves, and forest streams. It hunts fish and other aquatic animals but also takes reptiles, frogs, insects, and small birds. Its large size and heavy bill give it a particularly impressive appearance.",
    "image": "Stork-BilledKingfisher1.jpg",
    "quick_facts": {
        "family": "Alcedinidae",
        "size": "35–41 cm",
        "weight": "250–350 g",
        "wingspan": "65–75 cm",
        "diet": "Fish, frogs, reptiles, insects, crustaceans, and small birds",
        "habitat": "Rivers, lakes, ponds, mangroves, forest streams, and wetlands",
        "behaviour": "Usually waits quietly on a branch before dropping or diving onto prey",
        "activity": "Diurnal",
        "nesting": "Excavates a cavity or tunnel in an earthen bank or tree",
        "breeding_season": "January to August, depending on region",
        "clutch_size": "2–5 eggs",
        "call": "Loud, harsh and repetitive calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Rivers, forest streams, lakes, ponds, mangroves, and wooded wetlands"
    }
},

{
    "name": "Oriental White-Eye",
    "scientific": "Zosterops palpebrosus",
    "description": "The Oriental White-eye is a tiny, active bird with a conspicuous white ring around the eye, olive-green upperparts, and yellowish underparts. It moves rapidly through foliage while searching for insects, nectar, and small fruits. White-eyes are highly social and often travel in small groups. They are common in gardens, forests, plantations, and urban greenery.",
    "image": "OrientalWhite-Eye1.jpg",
    "quick_facts": {
        "family": "Zosteropidae",
        "size": "8–10 cm",
        "weight": "7–12 g",
        "wingspan": "13–16 cm",
        "diet": "Nectar, insects, small fruits, berries, and flower parts",
        "habitat": "Gardens, forests, plantations, scrub, parks, and urban greenery",
        "behaviour": "Highly active and social, usually moving through foliage in small groups",
        "activity": "Diurnal",
        "nesting": "Builds a tiny cup-shaped nest suspended from a fork in vegetation",
        "breeding_season": "February to September",
        "clutch_size": "2–3 eggs",
        "call": "High-pitched, rapid twittering and chirping",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Gardens, flowering trees, forests, plantations, parks, and urban greenery"
    }
},

{
    "name": "White-Browed Fantail",
    "scientific": "Rhipidura aureola",
    "description": "The White-Browed Fantail is a small insectivorous bird with a boldly patterned face, pale eyebrow, dark body, and a broad fan-shaped tail. It is an energetic bird that constantly flicks and spreads its tail while moving through foliage. It catches insects by making short aerial sallies from branches and is commonly found in forests, gardens, scrub, and woodland edges.",
    "image": "White-BrowedFantail1.jpg",
    "quick_facts": {
        "family": "Rhipiduridae",
        "size": "17–19 cm",
        "weight": "10–15 g",
        "wingspan": "20–24 cm",
        "diet": "Flying insects, caterpillars, spiders, and other small invertebrates",
        "habitat": "Forests, woodland, scrub, plantations, gardens, and forest edges",
        "behaviour": "Active and acrobatic, frequently spreading and flicking its fan-shaped tail",
        "activity": "Diurnal",
        "nesting": "Builds a small cup-shaped nest on a branch or in a fork",
        "breeding_season": "March to August",
        "clutch_size": "2–3 eggs",
        "call": "Sharp chirps, whistles, and rapid chattering",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Woodland, forest edges, gardens, plantations, scrub, and parks"
    }
},

{
    "name": "Yellow-Footed Green Pigeon",
    "scientific": "Treron phoenicopterus",
    "description": "The Yellow-Footed Green Pigeon is a colourful fruit-eating pigeon with predominantly green plumage, yellow feet, and distinctive patches of yellow, orange, and grey on the wings and body. It spends most of its time in trees, where it feeds on fruit, berries, and figs. It is generally quiet and can be difficult to spot among foliage despite its attractive colours.",
    "image": "Yellow-FootedGreenPigeon1.jpg",
    "quick_facts": {
        "family": "Columbidae",
        "size": "29–33 cm",
        "weight": "200–250 g",
        "wingspan": "45–50 cm",
        "diet": "Fruits, berries, figs, buds, and seeds",
        "habitat": "Forests, woodland, gardens, plantations, orchards, and large trees",
        "behaviour": "Arboreal and usually feeds quietly in fruiting trees, often in small groups",
        "activity": "Diurnal",
        "nesting": "Builds a flimsy platform of twigs in trees or shrubs",
        "breeding_season": "March to September, varying by region",
        "clutch_size": "Usually 2 eggs",
        "call": "Soft, low-pitched cooing calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Forests, orchards, gardens, plantations, parks, and fruiting trees"
    }
},

{
    "name": "Asian Brown Flycatcher",
    "scientific": "Muscicapa dauurica",
    "description": "The Asian Brown Flycatcher is a small, plain-looking insectivorous bird with brown upperparts, pale underparts, and a relatively large dark bill. It usually sits quietly on a branch before making short flights to catch insects in the air. It is a common migrant or passage bird in many parts of India and can be found in wooded habitats, gardens, plantations, and forest edges.",
    "image": "AsianBrownFlycatcher1.jpg",
    "quick_facts": {
        "family": "Muscicapidae",
        "size": "13–15 cm",
        "weight": "10–15 g",
        "wingspan": "20–24 cm",
        "diet": "Flying insects, beetles, flies, moths, and other small invertebrates",
        "habitat": "Forests, woodland edges, gardens, plantations, and wooded parks",
        "behaviour": "Perches quietly before making short aerial sallies to catch insects",
        "activity": "Diurnal",
        "nesting": "Builds a small cup-shaped nest in a tree cavity or sheltered site",
        "breeding_season": "May to July in its northern breeding range",
        "clutch_size": "3–5 eggs",
        "call": "Soft whistles and short sharp notes",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Wooded gardens, forest edges, plantations, parks, and forested habitats"
    }
},

{
    "name": "Pied Bushchat",
    "scientific": "Saxicola caprata",
    "description": "The Pied Bushchat is a small, upright insect-eating bird commonly seen perched on shrubs, fences, rocks, and other exposed points in open country. Males are predominantly black with white wing and rump markings, while females are brown. It catches insects from perches and is particularly common in grassland, farmland, scrub, and open woodland.",
    "image": "PiedBushchat1.jpg",
    "quick_facts": {
        "family": "Muscicapidae",
        "size": "13 cm",
        "weight": "12–17 g",
        "wingspan": "18–21 cm",
        "diet": "Insects, spiders, worms, and other small invertebrates",
        "habitat": "Grassland, scrub, farmland, open woodland, and rocky areas",
        "behaviour": "Perches prominently and makes short flights to capture insects",
        "activity": "Diurnal",
        "nesting": "Nests in cavities, holes, rock crevices, and sheltered spaces near the ground",
        "breeding_season": "February to August",
        "clutch_size": "2–4 eggs",
        "call": "Sharp chirps and short whistles",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Open fields, scrub, farmland, grasslands, rocky areas, and village outskirts"
    }
},

{
    "name": "Black Redstart",
    "scientific": "Phoenicurus ochruros",
    "description": "The Black Redstart is a small chat with a dark body, orange-red tail, and characteristic habit of frequently flicking its tail. Plumage varies between males, females, and different populations. It prefers rocky and open habitats and often uses buildings, walls, and cliffs as nesting sites. In India it is primarily encountered in suitable northern and highland habitats during the colder months.",
    "image": "BlackRedstart1.jpg",
    "quick_facts": {
        "family": "Muscicapidae",
        "size": "14–15 cm",
        "weight": "14–20 g",
        "wingspan": "23–26 cm",
        "diet": "Insects, spiders, worms, berries, and other small food",
        "habitat": "Rocky slopes, cliffs, open woodland, scrub, villages, and buildings",
        "behaviour": "Frequently flicks its tail and makes short flights from exposed perches to catch insects",
        "activity": "Diurnal",
        "nesting": "Builds a cup-shaped nest in rock crevices, buildings, cavities, or sheltered ledges",
        "breeding_season": "April to July in breeding areas",
        "clutch_size": "4–6 eggs",
        "call": "Short ticking notes and varied whistles",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Rocky habitats, highland villages, buildings, cliffs, and open scrub"
    }
},

{
    "name": "Spotted Owlet",
    "scientific": "Athene brama",
    "description": "The Spotted Owlet is a small owl with a rounded head, pale facial disc, yellow eyes, and prominent white spotting across its brown plumage. It is highly adaptable and commonly lives around villages, gardens, farmland, parks, and cities. Although mainly active at night, it often emerges during daylight and may sit near the entrance of its nesting cavity.",
    "image": "SpottedOwlet1.jpg",
    "quick_facts": {
        "family": "Strigidae",
        "size": "19–21 cm",
        "weight": "100–140 g",
        "wingspan": "44–48 cm",
        "diet": "Insects, rodents, lizards, frogs, small birds, and other small animals",
        "habitat": "Farmland, villages, gardens, open woodland, parks, and urban areas",
        "behaviour": "Often sits near its roost during daylight and hunts actively after dusk",
        "activity": "Mostly nocturnal and crepuscular",
        "nesting": "Uses tree cavities, holes in walls, buildings, and other sheltered cavities",
        "breeding_season": "November to April",
        "clutch_size": "3–5 eggs",
        "call": "Varied hoots, chuckles, whistles, and chattering calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Villages, farmland, gardens, parks, old buildings, and urban areas"
    }
},

{
    "name": "Black-Naped Oriole",
    "scientific": "Oriolus chinensis",
    "description": "The Black-Naped Oriole is a bright yellow-and-black songbird with a dark stripe through the eye and nape. It spends most of its time in trees and feeds on fruit, nectar, and insects. Its melodious whistles are often heard from the canopy before the bird is visible. It is associated with forests, plantations, gardens, and wooded urban areas.",
    "image": "Black-NapedOriole1.jpg",
    "quick_facts": {
        "family": "Oriolidae",
        "size": "23–28 cm",
        "weight": "65–100 g",
        "wingspan": "40–45 cm",
        "diet": "Fruits, berries, insects, caterpillars, and nectar",
        "habitat": "Forests, gardens, plantations, woodland, and parks",
        "behaviour": "Arboreal and generally remains in the canopy while feeding",
        "activity": "Diurnal",
        "nesting": "Builds a suspended cup-shaped nest in a tree",
        "breeding_season": "April to July",
        "clutch_size": "2–3 eggs",
        "call": "Clear, melodious whistles and fluting notes",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Forests, plantations, gardens, parks, and mature trees"
    }
},

{
    "name": "Woolly-Necked Stork",
    "scientific": "Ciconia episcopus",
    "description": "The Woolly-Necked Stork is a large dark-and-white stork with a distinctive white head and neck contrasting with a dark body. It usually forages alone or in pairs in open wetlands, grasslands, and agricultural fields, searching for frogs, fish, insects, reptiles, and other prey. It is generally less colonial than some other Indian storks and often keeps its distance from human activity.",
    "image": "Woolly-NeckedStork1.jpg",
    "quick_facts": {
        "family": "Ciconiidae",
        "size": "75–90 cm",
        "weight": "2.5–4 kg",
        "wingspan": "150–170 cm",
        "diet": "Frogs, fish, insects, reptiles, small mammals, and other small animals",
        "habitat": "Wetlands, grasslands, farmland, marshes, and open woodland",
        "behaviour": "Usually forages alone or in pairs by walking through open habitats",
        "activity": "Diurnal",
        "nesting": "Builds a large stick nest in tall trees, usually away from dense colonies",
        "breeding_season": "June to September in many parts of India",
        "clutch_size": "2–4 eggs",
        "call": "Usually quiet; may produce bill-clattering and soft sounds at nesting sites",
        "lifespan": "Several years in the wild",
        "conservation_status": "Near Threatened",
        "where_to_find": "Wetlands, grasslands, rice fields, open farmland, and shallow-water habitats"
    }
},

{
    "name": "Common Iora",
    "scientific": "Aegithina tiphia",
    "description": "The Common Iora is a small, active songbird with bright greenish-yellow plumage and contrasting dark wings in breeding males. It is usually found in trees and shrubs, where it moves rapidly through foliage searching for insects and small invertebrates. Males perform energetic displays during the breeding season, sometimes spreading their wings and tail while singing.",
    "image": "CommonIora1.jpg",
    "quick_facts": {
        "family": "Aegithinidae",
        "size": "12–13 cm",
        "weight": "12–15 g",
        "wingspan": "18–20 cm",
        "diet": "Insects, caterpillars, spiders, and other small invertebrates",
        "habitat": "Gardens, forests, woodland, scrub, plantations, and parks",
        "behaviour": "Active foliage gleaner that moves rapidly among leaves while searching for prey",
        "activity": "Diurnal",
        "nesting": "Builds a tiny cup-shaped nest in a fork of a tree or shrub",
        "breeding_season": "March to September",
        "clutch_size": "2–3 eggs",
        "call": "Musical whistles, trills, and varied notes",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Gardens, forest edges, plantations, scrub, parks, and wooded neighbourhoods"
    }
},

{
    "name": "Jungle Owlet",
    "scientific": "Glaucidium radiatum",
    "description": "The Jungle Owlet is a small woodland owl with a rounded head, barred brown-and-white plumage, and yellow eyes. Unlike many owls, it can be active during daylight, especially around dawn and dusk. It hunts insects, small reptiles, rodents, and birds and usually remains within wooded habitats. Its calls can be heard from forest edges and dense vegetation.",
    "image": "JungleOwlet1.jpg",
    "quick_facts": {
        "family": "Strigidae",
        "size": "20–23 cm",
        "weight": "100–150 g",
        "wingspan": "40–45 cm",
        "diet": "Insects, lizards, rodents, small birds, and other small animals",
        "habitat": "Forests, woodland, plantations, scrub, and wooded hills",
        "behaviour": "Often active during daylight and hunts from low perches within dense vegetation",
        "activity": "Diurnal, crepuscular, and sometimes nocturnal",
        "nesting": "Uses tree cavities, often taking advantage of old woodpecker holes",
        "breeding_season": "March to May",
        "clutch_size": "2–4 eggs",
        "call": "Repeated whistles, hoots, and sharp notes",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Forests, wooded hills, plantations, and dense woodland edges"
    }
},

{
    "name": "Black-Hooded Oriole",
    "scientific": "Oriolus xanthornus",
    "description": "The Black-Hooded Oriole is a striking yellow-and-black bird with a strongly contrasting black head and bright yellow body. It is an arboreal species that spends much of its time in the canopy, feeding on fruits, nectar, and insects. Its melodious whistles are often heard from tall trees. It occurs in forests, plantations, gardens, and wooded urban areas.",
    "image": "Black-HoodedOriole1.jpg",
    "quick_facts": {
        "family": "Oriolidae",
        "size": "23–25 cm",
        "weight": "60–90 g",
        "wingspan": "40–45 cm",
        "diet": "Fruits, berries, nectar, insects, and caterpillars",
        "habitat": "Forests, gardens, plantations, parks, and wooded urban areas",
        "behaviour": "Arboreal and usually remains high in trees while feeding",
        "activity": "Diurnal",
        "nesting": "Builds a suspended cup-shaped nest in a tree fork",
        "breeding_season": "April to August",
        "clutch_size": "2–3 eggs",
        "call": "Clear, melodious whistles and fluting notes",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Forests, plantations, gardens, parks, and mature trees"
    }
},

{
    "name": "Brown Rock Chat",
    "scientific": "Oenanthe fusca",
    "description": "The Brown Rock Chat is a small, dark brown chat associated strongly with rocky landscapes and human structures. It is often seen perched on walls, rocks, roofs, and ruins before dropping down to catch insects. It is particularly well adapted to dry environments and is common around villages, forts, rocky hills, and open scrub.",
    "image": "BrownRockChat1.jpg",
    "quick_facts": {
        "family": "Muscicapidae",
        "size": "18–20 cm",
        "weight": "35–45 g",
        "wingspan": "30–34 cm",
        "diet": "Insects, spiders, worms, and other small invertebrates",
        "habitat": "Rocky hills, dry scrub, villages, ruins, cliffs, and open countryside",
        "behaviour": "Perches on rocks and buildings before making short flights to capture insects",
        "activity": "Diurnal",
        "nesting": "Nests in cavities in walls, buildings, rock crevices, and similar sheltered sites",
        "breeding_season": "March to July",
        "clutch_size": "2–4 eggs",
        "call": "Short whistles, clicks, and chattering notes",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Rocky areas, old buildings, forts, villages, dry scrub, and open hills"
    }
},

{
    "name": "Blue-Tailed Bee-Eater",
    "scientific": "Merops philippinus",
    "description": "The Blue-Tailed Bee-eater is a colourful aerial insect hunter with a green body, blue tail, yellow throat, black eye stripe, and elongated central tail feathers. It spends much of its time catching flying insects from exposed perches or directly in the air. It is particularly associated with open habitats near water and often gathers in groups.",
    "image": "Blue-TailedBee-Eater1.jpg",
    "quick_facts": {
        "family": "Meropidae",
        "size": "25–30 cm including elongated tail feathers",
        "weight": "30–45 g",
        "wingspan": "35–40 cm",
        "diet": "Bees, wasps, dragonflies, butterflies, beetles, and other flying insects",
        "habitat": "Open country, riverbanks, wetlands, farmland, grassland, and scrub",
        "behaviour": "Highly agile aerial hunter that catches insects in flight and returns to a perch",
        "activity": "Diurnal",
        "nesting": "Excavates a tunnel in sandy banks or soft ground, often in colonies",
        "breeding_season": "March to July",
        "clutch_size": "4–6 eggs",
        "call": "High-pitched, rapid and cheerful twittering calls",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Riverbanks, wetlands, open fields, farmland, grasslands, and dry open country"
    }
},

{
    "name": "Indian Pond Heron",
    "scientific": "Ardeola grayii",
    "description": "The Indian Pond Heron is a small, stocky heron that appears brown and streaked while standing but reveals striking white wings when it takes flight. It is one of the most familiar wetland birds in India and can be found around ponds, rice fields, marshes, canals, and even small water bodies in towns. It hunts by standing quietly and making rapid strikes at fish, frogs, insects, and other prey.",
    "image": "IndianPondHeron1.jpg",
    "quick_facts": {
        "family": "Ardeidae",
        "size": "40–50 cm",
        "weight": "230–350 g",
        "wingspan": "80–95 cm",
        "diet": "Fish, frogs, insects, crustaceans, lizards, and other small animals",
        "habitat": "Ponds, rice fields, marshes, canals, lakes, rivers, and wet grassland",
        "behaviour": "Usually stands motionless before making a rapid strike at prey",
        "activity": "Diurnal",
        "nesting": "Builds a stick nest in trees, shrubs, or reed beds, often in colonies",
        "breeding_season": "June to September in much of India",
        "clutch_size": "3–5 eggs",
        "call": "Usually quiet away from colonies, with harsh croaks around nesting sites",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Ponds, rice fields, marshes, canals, village wetlands, and urban water bodies"
    }
},
{
    "name": "Black-Crowned Night Heron",
    "scientific": "Nycticorax nycticorax",
    "description": "The Black-Crowned Night Heron is a stocky, medium-sized heron with a distinctive black crown and back, pale grey wings, and a white or pale grey body. Unlike many herons, it is most active around dusk and during the night. It often stands patiently at the edge of ponds, lakes, marshes, and wetlands before striking at fish, amphibians, insects, and other small prey. During the day, it commonly rests quietly among dense vegetation or in communal roosts. Its broad range and adaptable nature allow it to occupy a variety of wetland habitats.",
    "image": "Black-CrownedNightHeron1.jpg",
    "quick_facts": {
        "family": "Ardeidae",
        "size": "58–66 cm",
        "weight": "500–1,000 g",
        "wingspan": "105–112 cm",
        "diet": "Fish, frogs, insects, crustaceans, small reptiles, and other small animals",
        "habitat": "Freshwater wetlands, marshes, ponds, lakes, rivers, mangroves, and coastal wetlands",
        "behaviour": "Patient and stealthy hunter that often remains motionless before quickly striking at prey",
        "activity": "Mostly crepuscular and nocturnal",
        "nesting": "Builds a platform nest of sticks and vegetation, often in trees, shrubs, or dense wetland colonies",
        "breeding_season": "Generally varies by region, often during the wet season or warmer months",
        "clutch_size": "3–5 eggs",
        "call": "A distinctive harsh, croaking or squawking call",
        "lifespan": "Up to around 20 years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Wetlands, lakes, ponds, marshes, rivers, and other areas with shallow water and dense vegetation"
    }
},
{
    "name": "Puff-Throated Babbler",
    "scientific": "Pellorneum ruficeps",
    "description": "The Puff-Throated Babbler is a small, ground-dwelling bird found in forests, woodland, scrub, and other areas with dense undergrowth. It has warm brown upperparts, a paler underside, and a characteristic pale throat that can appear puffed out when the bird calls or displays. It spends much of its time searching through leaf litter for insects and other small creatures, often moving through vegetation in small groups. Although it can be difficult to spot because of its secretive habits, its lively calls often reveal its presence.",
    "image": "Puff-ThroatedBabbler1.jpg",
    "quick_facts": {
        "family": "Pellorneidae",
        "size": "17–18 cm",
        "weight": "30–40 g",
        "wingspan": "Approximately 20–23 cm",
        "diet": "Insects, larvae, spiders, small invertebrates, and occasionally seeds",
        "habitat": "Dense undergrowth, forests, woodland, bamboo, scrub, and plantations",
        "behaviour": "Active ground forager that searches through leaf litter and vegetation, often in small groups",
        "activity": "Diurnal",
        "nesting": "Builds a domed or ball-shaped nest close to the ground, usually among dense vegetation or leaf litter",
        "breeding_season": "Usually during the warmer and wetter months, varying across its range",
        "clutch_size": "2–4 eggs",
        "call": "A loud, repetitive and musical series of notes, often given by several birds in a group",
        "lifespan": "Several years in the wild",
        "conservation_status": "Least Concern",
        "where_to_find": "Dense forest undergrowth, woodland edges, scrub, bamboo thickets, and other habitats with thick ground cover"
    }
}
    ]

for bird in birds:

    page = template

    page = page.replace("{{NAME}}", bird["name"])
    page = page.replace("{{SCIENTIFIC}}", bird["scientific"])
    page = page.replace("{{DESCRIPTION}}", bird["description"])
    page = page.replace("{{IMAGE}}", bird["image"])
    page = page.replace("{{WINGSPAN}}",bird["quick_facts"]["wingspan"])
    page = page.replace("{{FAMILY}}",bird["quick_facts"]["family"])
    page = page.replace("{{BREEDING_SEASON}}",bird["quick_facts"]["family"])
    page = page.replace("{{CLUTCH_SIZE}}", bird["quick_facts"]["clutch_size"])
    page = page.replace("{{ACTIVITY}}",bird["quick_facts"]["activity"])
    page = page.replace("{{CONSERVATION_STATUS}}", bird["quick_facts"]["conservation_status"])
    page = page.replace("{{CALL}}", bird["quick_facts"]["call"])
    page = page.replace("{{LIFESPAN}}", bird["quick_facts"]["lifespan"])
    page = page.replace("{{NESTING}}",bird["quick_facts"]["nesting"])
    page = page.replace("{{HABITAT}}", bird["quick_facts"]["habitat"])
    page = page.replace("{{WHERE_TO_FIND}}",bird["quick_facts"]["where_to_find"])
    page = page.replace("{{SIZE}}",bird["quick_facts"]["size"])
    page = page.replace("{{WEIGHT}}",bird["quick_facts"]["weight"])
    page = page.replace("{{DIET}}",bird["quick_facts"]["diet"])
    page = page.replace("{{BEHAVIOUR}}",bird["quick_facts"]["behaviour"])
    
    current_index = birds.index(bird)
    if current_index < len(birds) - 1:
       next_bird = birds[current_index + 1]
       next_page = next_bird["name"].lower().replace(" ", "-") + ".html"
       page = page.replace("{{NEXT_PAGE}}", next_page)
    else:
        page = page.replace("{{NEXT_PAGE}}", "")
    if current_index > 0:
       previous_bird = birds[current_index - 1]
       previous_page = previous_bird["name"].lower().replace(" ", "-") + ".html"
       page = page.replace("{{PREVIOUS_PAGE}}", previous_page)
      
    else:
         page = page.replace("{{PREVIOUS_PAGE}}","")
       
    filename = bird["name"].lower().replace(" ", "-") + ".html"

    open("birds/" + filename, "w").write(page)

index_template = open("index_template.html", "r").read()

birds = sorted(birds, key = lambda bird: bird["name"].lower())

bird_count = len(birds)

bird_list = ""

for bird in birds:
    filename = bird["name"].lower().replace(" ", "-") + ".html"
    bird_list += '<li class="bird"><a href="birds/' + filename + '">' + bird["name"] + '</a></li>'
    

index = index_template.replace("{{BIRD_COUNT}}", str(bird_count))
index = index.replace("{{BIRD_LIST}}",bird_list)

open("index.html", "w").write(index)

print("Pages Done, Sir")

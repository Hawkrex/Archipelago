ITEMS_JSON = [
  {
    "Id": "NoItem",
    "Name": "No Item",
    "ApId": 1,
    "Classification": "filler"
  },
  {
    "Id": "Iron",
    "Name": "Iron",
    "Locations": ["Everywhere"],
    "Producers": ["T1 Ore Extractor", "T2 Ore Extractor", "T3 Ore Extractor"]
  },
  {
    "Id": "Silicon",
    "Name": "Silicon",
    "Locations": ["Everywhere"],
    "Producers": ["T1 Ore Extractor", "T2 Ore Extractor", "T3 Ore Extractor"]
  },
  {
    "Id": "Magnesium",
    "Name": "Magnesium",
    "Locations": ["Everywhere"],
    "Producers": ["T1 Ore Extractor", "T2 Ore Extractor", "T3 Ore Extractor"]
  },
  {
    "Id": "Cobalt",
    "Name": "Cobalt",
    "Locations": ["Everywhere"],
    "Producers": ["T1 Ore Extractor", "T2 Ore Extractor", "T3 Ore Extractor"]
  },
  {
    "Id": "Titanium",
    "Name": "Titanium",
    "Locations": ["Everywhere"],
    "Producers": ["T1 Ore Extractor", "T2 Ore Extractor", "T3 Ore Extractor"]
  },
  {
    "Id": "ice",
    "Name": "Ice",
    "Locations": ["Everywhere"]
  },
  {
    "Id": "Aluminium",
    "Name": "Aluminium",
    "Locations": ["Aluminium Hills", "Iridium Mine", "Sulfur Fields", "Labyrinth Canyons", "Zeolite Cave"],
    "Producers": [{"T1 Ore Extractor": ["Aluminium Hills"]}, {"T2 Ore Extractor": ["Aluminium Hills"]}, {"T3 Ore Extractor": ["Aluminium Hills"]}]
  },
  {
    "Id": "Alloy",
    "Name": "Super Alloy",
    "Ingredients": [[1, "Iron"], [1, "Silicon"], [1, "Magnesium"], [1, "Cobalt"], [1, "Titanium"], [1, "Aluminum"]],
    "CraftingMachine": "Advanced Craft Station",
    "Locations": ["Super Alloy Cave", "Sand Falls", "Lava fields", "The Waterfall", "The Meteor", "Labyrinth Canyons"],
    "Producers": [{"T2 Ore Extractor": ["Super Alloy Cave"]}, {"T3 Ore Extractor": ["Super Alloy Cave"]}]
  },
  {
    "Id": "Iridium",
    "Name": "Iridium",
    "Locations": ["Iridium Mine", "The Grand Rift", "Cracked Spires - Wasteland", "Mushroom River - Volcano", "Volcano"],
    "Producers": [{"T1 Ore Extractor": ["Iridium Mine", "The Grand Rift"]}, {"T2 Ore Extractor": ["Iridium Mine", "The Grand Rift"]}, {"T3 Ore Extractor": ["Iridium Mine", "The Grand Rift"]}]
  },
  {
    "Id": "Uranim",
    "Name": "Uranium",
    "Locations": ["Gate Desert", "Grasslands - The Highlands"],
    "Producers": [{"T2 Ore Extractor": ["Gate Desert", "The Highlands"]}, {"T3 Ore Extractor": ["Gate Desert", "The Highlands"]}]
  },
  { 
    "Id": "Osmium",
    "Name": "Osmium",
    "Locations": ["Osmium Cave", "The Grand Rift - Dune Desert", "Arches - Meteor Crater", "Sand Falls", "Gate Desert", "Cracked Spires - Wasteland"],
    "Producers": [{"T2 Ore Extractor": ["Osmium Cave"]}, {"T3 Ore Extractor": ["Osmium Cave"]}]
  },
  {
    "Id": "Sulfur",
    "Name": "Sulfur",
    "Locations": ["Osmium Cave", "The Grand Rift - Dune Desert", "Arches - Meteor Crater", "Sand Falls", "Gate Desert", "Cracked Spires - Wasteland"],
    "Producers": [{"T1 Ore Extractor": ["Sulfur Fields"]}, {"T2 Ore Extractor": ["Sulfur Fields"]}, {"T3 Ore Extractor": ["Everywhere"]}]
  },
  { 
    "Id": "Zeolite",
    "Name": "Zeolite",
    "Locations": ["Everywhere"],
    "Producers": [{"T2 Ore Extractor": ["Zeolite Cave"]}, {"T3 Ore Extractor": ["Zeolite Cave"]}]
  },
  { 
    "Id": "Obsidian",
    "Name": "Obsidian",
    "Locations": ["Volcano"],
    "Producers": [{"T2 Ore Extractor": ["Volcano"]}, {"T3 Ore Extractor": ["Volcano"]}]
  },
  { 
    "Id": "NitrogenCapsule1",
    "Name": "Nitrogen cartridge",
    "Producers": [{"T1 Gas Extractor": "Breathable Atmosphere"}, {"T2 Gas Extractor"}]
  },
  { 
    "Id": "MethanCapsule1",
    "Name": "Methane cartridge",
    "Producers": ["T1 Gas Extractor", "T2 Gas Extractor"]
  },
  { 
    "Id": "OxygenCapsule1",
    "Name": "Oxygen capsule",
    "Ingredients": [[2, "Cobalt"]],
    "CraftingMachine": ["T1 Craft Station", "T2 Craft Station"],
    "Producers": ["T1 Gas Extractor", "T2 Gas Extractor"]
  },
  { 
    "Id": "Vegetable0Growable",
    "Name": "Eggplant",
    "CraftingMachine": ["T1 Food Grower", "T2 Food Grower", "T1 Outdoor Farm"]
  },
  { 
    "Id": "Vegetable1Growable",
    "Name": "Squash",
    "CraftingMachine": ["T1 Food Grower", "T2 Food Grower", "T1 Outdoor Farm"]
  },
  { 
    "Id": "Vegetable3Growable",
    "Name": "Mushroom",
    "CraftingMachine": ["T1 Food Grower", "T2 Food Grower", "T1 Outdoor Farm"]
  },
  { 
    "Id": "WaterBottle1",
    "Name": "Water Bottle",
    "Ingredients": [[1, "Ice"]],
    "CraftingMachine": ["T1 Craft Station", "T2 Craft Station"],
    "Producers": ["Atmospheric Water Collector", "Lake Water Collector"]
  },
  { 
    "Id": "Algae1Seed",
    "Name": "Algae",
    "Producers": ["Algae Generator"]
  },
  { 
    "Id": "LarvaeBase1",
    "Name": "Common Larva",
    "Ingredients": [[1, "T3 Mutagen"], [1, "Phytoplankton B"], [1, "T2 Fertilizer"]],
    "CraftingMachine": ["Biolab"],
    "Locations": ["Insects"],
    "Producers": ["Ecosystem"],
    "ApId": 135,
    "Classification": "progression"
  },
  { 
    "Id": "LarvaeBase2",
    "Name": "Uncommon Larva",
    "Locations": ["Insects"]
  },
  { 
    "Id": "LarvaeBase3",
    "Name": "Rare Larva",
    "Ingredients": [[1, "T4 Mutagen"], [1, "Phytoplankton C"], [1, "T2 Fertilizer"]],
    "CraftingMachine": ["Biolab"],
    "Locations": ["Insects"],
    "Producers": ["Ecosystem"],
    "ApId": 138,
    "Classification": "useful"
  },
  { 
    "Id": "SilkWorm",
    "Name": "Silkworm",
    "Ingredients": [[1, "Uncommon Larva"], [1, "Bacteria Sample"], [1, "T1 Fertilizer"]],
    "CraftingMachine": ["Biolab"],
    "Producers": ["Ecosystem"]
  },
  { 
    "Id": "TreeRoot",
    "Name": "Tree bark",
    "Producers": ["T2 Biodome "]
  },
  { 
    "Id": "honey",
    "Name": "Honey",
    "Producers": ["T1 Beehive", "T2 Beehive"]
  },
  { 
    "Id": "Silk",
    "Name": "Silk",
    "Producers": ["Silk Generator"]
  },
  { 
    "Id": "Phytoplankton2",
    "Name": "Phytoplankton B",
    "Producers": ["Water life collector"]
  },
  { 
    "Id": "BalzarQuartz",
    "Name": "Blazar Quartz",
    "Locations": ["Rainbow Caves"]
  },
  { 
    "Id": "QuasarQuartz",
    "Name": "Quasar Quartz",
    "Locations": ["Rainbow Caves"]
  },
  { 
    "Id": "MagnetarQuartz",
    "Name": "Magnetar Quartz",
    "Locations": ["Rainbow Caves"]
  },
  {
    "Id": "PulsarQuartz",
    "Name": "Pulsar Quartz",
    "Ingredients": [[1, "Zeolite"], [1, "Osmium"], [1, "Uranium"], [1, "Iridium"], [1, "Methane cartridge"]],
    "CraftingMachine": "Biolab",
    "Locations": ["Rainbow Caves", "Meteor Field", "Waterfall"],
    "ApId": 39,
    "Classification": "progression"
  },
  {
    "Id": "SolarQuartz",
    "Name": "Solar Quartz",
    "Ingredients": [[1, "Nitrogen cartridge"], [1, "Sulfur"], [1, "Obsidian"]],
    "CraftingMachine": "Biolab",
    "Locations": ["Rainbow Caves"],
    "ApId": 214,
    "Classification": "progression"
  },
  {
    "Id": "Rod-iridium",
    "Name": "Iridium Rod",
    "Ingredients": [[9, "Iridium"]],
    "CraftingMachine": "Advanced Craft Station"
  },
  {
    "Id": "CircuitBoard1",
    "Name": "Circuit Board",
    "Ingredients": [[1, "Silicon"], [1, "Iron"], [1, "Aluminum"], [1, "Nitrogen cartridge"], [1, "Bioplastic Nugget"], [1, "Zeolite"]],
    "CraftingMachine": "Advanced Craft Station",
    "ApId": 38,
    "Classification": "progression"
  },
  {
    "Id": "Bioplastic1",
    "Name": "Bioplastic Nugget",
    "Ingredients": [[2, "Mushroom"], [1, "Silicon"], [1, "Water Bottle"]],
    "CraftingMachine": "Biolab"
  },
  {
    "Id": "FusionEnergyCell",
    "Name": "Fusion Energy Cell",
    "Ingredients": [[3, "Pulsar Quartz"], [2, "Osmium"], [1, "Obsidian"]],
    "CraftingMachine": "Advanced Craft Station",
    "ApId": 33,
    "Classification": "progression"
  },
  {
    "Id": "Rod-uranium",
    "Name": "Uranium Rod",
    "Ingredients": [[9, "Uranium"]],
    "CraftingMachine": "Advanced Craft Station"
  },
  {
    "Id": "RedPowder1",
    "Name": "Explosive Powder",
    "Ingredients": [[2, "Sulfur"], [1, "Iridium"]],
    "CraftingMachine": "Biolab"
  },
  {
    "Id": "DeparturePlatform",
    "Name": "Extraction platform",
    "Ingredients": [[1, "Fusion Energy Cell"], [1, "Energy Multiplier Fuse"], [1, "Circuit Board"], [1, "Uranium Rod"], [1, "Iridium Rod"], [1, "Pulsar Quartz"]],
    "ApId": 48,
    "Classification": "progression"
  },
  {
    "Id": "FuseEnergy1",
    "Name": "Energy Multiplier Fuse"
  },
  {
    "Id": "FuseCartridge",
    "Name": "Fuse cartridge"
  },
  {
    "Id": "RocketDeparture1",
    "Name": "Extraction rocket",
    "Ingredients": [[1, "Super Alloy Rod"], [1, "Rocket Engine"], [1, "Osmium Rod"],[1, "Blazar Quartz"], [1, "Obsidian"], [1, "Solar Quartz"]]
  },
  {
    "Id": "Rod-alloy",
    "Name": "Super Alloy Rod",
    "Ingredients": [[8, "Super Alloy"], [1, "Aluminum"]],
    "CraftingMachine": "Advanced Craft Station",
    "ApId": 24,
    "Classification": "progression"
  },
  {
    "Id": "RocketReactor",
    "Name": "Rocket Engine",
    "Ingredients": [[1, "Super Alloy"], [2, "Uranium"], [1, "Iridium Rod"]],
    "CraftingMachine": "Advanced Craft Station"
  },
  {
    "Id": "Rod-osmium",
    "Name": "Osmium Rod",
    "Ingredients": [[9, "Osmium"]],
    "CraftingMachine": "Advanced Craft Station",
    "ApId": 32,
    "Classification": "progression"
  },
  {
    "Id": "Fertilizer1",
    "Name": "T1 Fertilizer",
    "Ingredients": [[3, "Algae"], [2, "Eggplant"], [1, "Sulfur"]],
    "CraftingMachine": "Biolab"
  },
  {
    "Id": "Fertilizer2",
    "Name": "T2 Fertilizer",
    "Ingredients": [[2, "Methane cartridge"], [1, "T1 Fertilizer"], [1, "Algae"], [1, "Squash"]],
    "CraftingMachine": "Biolab"
  },
  {
    "Id": "Bee1Larvae",
    "Name": "Bee Larva",
    "Ingredients": [[1, "Uncommon Larva"], [1, "T1 Mutagen"], [1, "T1 Fertilizer"]],
    "CraftingMachine": "Incubator",
    "Producers": ["Ecosystem", "T2 Beehive"]
  },
  {
    "Id": "Mutagen1",
    "Name": "T1 Mutagen",
    "Ingredients": [[1, "Bacteria Sample"], [1, "Methane cartridge"], [1, "Sulfur"]],
    "CraftingMachine": "Biolab"
  },
  {
    "Id": "Mutagen2",
    "Name": "T2 Mutagen",
    "Ingredients": [[1, "Mutagen"], [1, "Common Larva"], [1, "Honey"]],
    "CraftingMachine": "Biolab",
    "ApId": 123,
    "Classification": "progression"
  },
  {
    "Id": "Mutagen3",
    "Name": "T3 Mutagen",
    "Ingredients": [[1, "Bacteria Sample"], [1, "Sulfur"], [1, "Nitrogen cartridge"]],
    "CraftingMachine": "Biolab",
    "ApId": 37,
    "Classification": "progression"
  },
  {
    "Id": "Mutagen4",
    "Name": "T4 Mutagen",
    "Ingredients": [[1, "T1 Mutagen"], [1, "T3 Mutagen"]],
    "CraftingMachine": "Biolab",
    "ApId": 42,
    "Classification": "progression"
  },
  {
    "Id": "Bacteria1",
    "Name": "Bacteria Sample",
    "Ingredients": [[3, "Algae"], [3, "Water Bottle"]],
    "CraftingMachine": "Biolab"
  },
  {
    "Id": "Backpack1",
    "Name": "T1 Backpack",
    "Ingredients": [[2, "Iron"]],
    "CraftingMachine": "T1 Craft Station",
    "UnlockedFromStart": True
  },
  {
    "Id": "Backpack2",
    "Name": "T2 Backpack",
    "Ingredients": [[1, "T1 Backpack"], [1, "Iron"], [1, "Silicon"], [1, "Titanium"]],
    "CraftingMachine": "T2 Craft Station",
    "ApId": 2,
    "Classification": "useful"
  },
  {
    "Id": "Backpack3",
    "Name": "T3 Backpack",
    "Ingredients": [[1, "T2 Backpack"], [2, "Aluminum"], [1, "Silicon"], [1, "Titanium"]],
    "CraftingMachine": "T2 Craft Station",
    "ApId": 4,
    "Classification": "useful"
  },
  {
    "Id": "Backpack4",
    "Name": "T4 Backpack",
    "Ingredients": [[1, "T3 Backpack"], [3, "Super Alloy"], [1, "Titanium"]],
    "CraftingMachine": "Advanced Craft Station"
  },
  {
    "Id": "Backpack5",
    "Name": "T5 Backpack",
    "Ingredients": [[1, "T4 Backpack"], [3, "Super Alloy"], [1, "Titanium"]],
    "CraftingMachine": "Advanced Craft Station",
    "ApId": 13,
    "Classification": "useful"
  },
  {
    "Id": "Backpack6",
    "Name": "T6 Backpack",
    "Ingredients": [[1, "T5 Backpack"], [1, "Blazar Quartz"], [1, "Magnetar Quartz"], [1, "Circuit Board"], [1, "Obsidian"]],
    "CraftingMachine": "Advanced Craft Station",
    "ApId": 41,
    "Classification": "useful"
  }, 
  {
    "Id": "VehicleInventorySize1",
    "Name": "Vehicle - T1 Inventory increase",
    "Ingredients": [[1, "Silicon"], [1, "Fabric"], [1, "Super Alloy"]],
    "CraftingMachine": "Vehicle Station",
    "ApId": 15,
    "Classification": "filler"
  },
  {
    "Id": "VehicleInventorySize2",
    "Name": "Vehicle - T2 Inventory increase",
    "Ingredients": [[2, "Vehicle - T1 Inventory increase"], [1, "Osmium"], [2, "Fabric"]],
    "CraftingMachine": "Vehicle Station",
    "ApId": 167,
    "Classification": "filler"
  },
  {
    "Id": "VehicleInventorySize3",
    "Name": "Vehicle - T3 Inventory increase",
    "Ingredients": [[2, "Vehicle - T2 Inventory increase"], [1, "Magnetar Quartz"], [3, "Fabric"]],
    "CraftingMachine": "Vehicle Station",
    "ApId": 176,
    "Classification": "filler"
  },
  {
    "Id": "VehicleLogistic1",
    "Name": "Vehicle - Logistics",
    "Ingredients": [[2, "Circuit Board"], [1, "Osmium Rod"], [2, "Bioplastic Nugget"], [1, "Super Alloy Rod"]],
    "CraftingMachine": "Vehicle Station",
    "ApId": 133,
    "Classification": "filler"
  },
  {
    "Id": "VehicleOxygen1",
    "Name": "Vehicle - Unlimited Oxygen",
    "Ingredients": [[4, "Zeolite"], [2, "Oxygen Capsule"]],
    "CraftingMachine": "Vehicle Station",
    "ApId": 165,
    "Classification": "filler"
  },
  {
    "Id": "VehicleEquipmentSize1",
    "Name": "Vehicle - T1 Equipment increase",
    "Ingredients": [[1, "Super Alloy"], [1, "Silicon"], [1, "Iridium"]],
    "CraftingMachine": "Vehicle Station"
  },
  {
    "Id": "VehicleEquipmentSize2",
    "Name": "Vehicle - T2 Equipment increase",
    "Ingredients": [[2, "Vehicle - T1 Equipment increase"], [1, "Obsidian"], [1, "Super Alloy"]],
    "CraftingMachine": "Vehicle Station",
    "ApId": 166,
    "Classification": "filler"
  },
  {
    "Id": "VehicleSpeed1",
    "Name": "Vehicle - T1 Speed increase",
    "Ingredients": [[2, "Zeolite"], [1, "Rocket Engine"]],
    "CraftingMachine": "Vehicle Station"
  },
  {
    "Id": "VehicleSpeed2",
    "Name": "Vehicle - T2 Speed increase",
    "Ingredients": [[2, "Vehicle - T1 Speed increase"], [1, "Explosive Powder"]],
    "CraftingMachine": "Vehicle Station",
    "ApId": 168,
    "Classification": "filler"
  },
  {
    "Id": "VehicleSpeed3",
    "Name": "Vehicle - T3 Speed increase",
    "Ingredients": [[2, "Vehicle - T2 Speed increase"], [1, "Explosive Powder"], [2, "Blazar Quartz"], [1, "Pulsar Quartz"]],
    "CraftingMachine": "Vehicle Station",
    "ApId": 184,
    "Classification": "filler"
  },
  {
    "Id": "VehicleLights1",
    "Name": "Vehicle - T1 Lights",
    "Ingredients": [[1, "Sulfur"], [1, "Cobalt"], [1, "Silicon"]],
    "CraftingMachine": "Vehicle Station"
  },
  {
    "Id": "VehicleLights2",
    "Name": "Vehicle - T2 Lights",
    "Ingredients": [[2, "Vehicle - T1 Lights"], [1, "Solar Quartz"]],
    "CraftingMachine": "Vehicle Station",
    "ApId": 172,
    "Classification": "filler"
  },
  {
    "Id": "PinChip1",
    "Name": "Microchip - T1 Blueprint Pinning",
    "Ingredients": [[1, "Aluminum"], [1, "Osmium"], [1, "Super Alloy"], [1, "Magnesium"], [2, "Cobalt"]],
    "CraftingMachine": "T2 Craft Station",
    "ApId": 10,
    "Classification": "filler"
  },
  {
    "Id": "PinChip2",
    "Name": "Microchip - T2 Blueprint Pinning",
    "Ingredients": [[1, "Microchip - Blueprint Pinning T1"], [1, "Methane cartridge"], [1, "Osmium"], [1, "Zeolite"], [1, "Magnesium"], [1, "Cobalt"]],
    "CraftingMachine": "T2 Craft Station",
    "ApId": 162,
    "Classification": "filler"
  },
  {
    "Id": "PinChip3",
    "Name": "Microchip - T3 Blueprint Pinning",
    "Ingredients": [[1, "Microchip - Blueprint Pinning T2"], [1, "Quasar Quartz"], [1, "Blazar Quartz"]],
    "CraftingMachine": "T2 Craft Station",
    "ApId": 182,
    "Classification": "filler"
  },
  {
    "Id": "HudCompass",
    "Name": "Microchip - Compass",
    "Ingredients": [[1, "Silicon"], [1, "Magnesium"], [2, "Aluminum"]],
    "CraftingMachine": "T2 Craft Station",
    "ApId": 144,
    "Classification": "useful"
  },
  {
    "Id": "MultiToolMineSpeed1",
    "Name": "Microchip - T1 Mining Speed",
    "Ingredients": [[1, "Magnesium"], [1, "Silicon"], [2, "Aluminum"]],
    "CraftingMachine": "T2 Craft Station",
    "ApId": 143,
    "Classification": "useful"
  },
  {
    "Id": "MultiToolMineSpeed2",
    "Name": "Microchip - T2 Mining Speed",
    "Ingredients": [[1, "Microchip - T1 Mining Speed"], [1, "Silicon"], [1, "Super Alloy"]],
    "CraftingMachine": "T2 Craft Station",
    "ApId": 146,
    "Classification": "useful"
  },
  {
    "Id": "MultiToolMineSpeed3",
    "Name": "Microchip - T3 Mining Speed",
    "Ingredients": [[1, "Microchip - T2 Mining Speed"], [1, "Silicon"], [1, "Aluminum"], [1, "Super Alloy"]],
    "CraftingMachine": "T2 Craft Station",
    "ApId": 149,
    "Classification": "useful"
  },
  {
    "Id": "MultiToolMineSpeed4",
    "Name": "Microchip - T4 Mining Speed",
    "Ingredients": [[1, "Microchip - T3 Mining Speed"], [1, "Silicon"], [1, "Osmium"], [1, "Super Alloy"]],
    "CraftingMachine": "T2 Craft Station",
    "ApId": 157,
    "Classification": "useful"
  },
  {
    "Id": "MultiDeconstruct",
    "Name": "Microchip - T1 Deconstruction",
    "Ingredients": [[1, "Silicon"], [1, "Magnesium"]],
    "CraftingMachine": "T1 Craft Station",
    "UnlockedFromStart": True
  },
  {
    "Id": "MultiToolDeconstruct2",
    "Name": "Microchip - T2 Deconstruction",
    "Ingredients": [[1, "Microchip - T1 Deconstruction"], [1, "Methane cartridge"], [1, "Zeolite"]],
    "CraftingMachine": "T2 Craft Station",
    "ApId": 170,
    "Classification": "useful"
  },
  {
    "Id": "MultiToolDeconstruct3",
    "Name": "Microchip - T3 Deconstruction",
    "Ingredients": [[1, "Microchip - T2 Deconstruction"], [1, "Blazar Quartz"], [1, "Magnetar Quartz"]],
    "CraftingMachine": "T2 Craft Station",
    "ApId": 181,
    "Classification": "useful"
  },
  {
    "Id": "MultiToolLight",
    "Name": "Microchip - T1 Torch",
    "Ingredients": [[2, "Magnesium"], [1, "Silicon"]],
    "CraftingMachine": "T1 Craft Station",
    "UnlockedFromStart": True
  },
  {
    "Id": "MultiToolLight2",
    "Name": "Microchip - T2 Torch",
    "Ingredients": [[1, "Microchip - T1 Torch"], [1, "Aluminum"], [1, "Magnesium"], [1, "Sulfur"]],
    "CraftingMachine": "T2 Craft Station",
    "ApId": 155,
    "Classification": "filler"
  },
  {
    "Id": "MultiToolLight3",
    "Name": "Microchip - T3 Torch",
    "Ingredients": [[1, "Microchip - T2 Torch"], [2, "Solar Quartz"]],
    "CraftingMachine": "T2 Craft Station",
    "ApId": 183,
    "Classification": "filler"
  },
  {
    "Id": "MapChip",
    "Name": "Microchip - Map",
    "Ingredients": [[2, "Aluminum"], [1, "Obsidian"]],
    "CraftingMachine": "T2 Craft Station",
    "ApId": 164,
    "Classification": "filler"
  },
  {
    "Id": "HudChipCleanConstruction",
    "Name": "Microchip - Construction Menu Filter",
    "Ingredients": [[1, "Super Alloy"], [1, "Magnesium"], [1, "Silicon"]],
    "CraftingMachine": "T1 Craft Station",
    "ApId": 174,
    "Classification": "filler"
  },
  {
    "Id": "EquipmentIncrease1",
    "Name": "T1 Exoskeleton",
    "Ingredients": [[1, "Titanium"], [1, "Silicon"], [1, "Magnesium"]],
    "CraftingMachine": "T2 Craft Station",
    "UnlockedFromStart": True
  },
  {
    "Id": "EquipmentIncrease2",
    "Name": "T2 Exoskeleton",
    "Ingredients": [[1, "T1 Exoskeleton"], [1, "Titanium"], [1, "Silicon"], [2, "Magnesium"], [1, "Aluminum"]],
    "CraftingMachine": "T2 Craft Station",
    "ApId": 65,
    "Classification": "useful"
  },
  {
    "Id": "EquipmentIncrease3",
    "Name": "T3 Exoskeleton",
    "Ingredients": [[1, "T2 Exoskeleton"], [2, "Osmium"], [1, "Super Alloy Rod"], [1, "Uranium Rod"]],
    "CraftingMachine": "T2 Craft Station",
    "ApId": 25,
    "Classification": "useful"
  },
  {
    "Id": "EquipmentIncrease4",
    "Name": "T4 Exoskeleton",
    "Ingredients": [[1, "T3 Exoskeleton"], [2, "Blazar Quartz"], [1, "Circuit Board"], [1, "Uranium Rod"]],
    "CraftingMachine": "T2 Craft Station",
    "ApId": 35,
    "Classification": "useful"
  },
  {
    "Id": "AirFilter1",
    "Name": "Air Filter",
    "Ingredients": [[1, "Fabric"], [1, "Osmium"], [1, "Super Alloy"], [2, "Bioplastic Nugget"], [1, "Methane cartridge"]],
    "CraftingMachine": "Advanced Craft Station",
    "ApId": 26,
    "Classification": "useful"
  },
  {
    "Id": "WaterFilter",
    "Name": "Water Filter",
    "Ingredients": [[1, "Aluminum"], [2, "Bioplastic Nugget"], [1, "Silicon"], [1, "Fabric"], [1, "Water Bottle"]],
    "CraftingMachine": "Advanced Craft Station",
    "ApId": 29,
    "Classification": "useful"
  },
  {
    "Id": "Frog1Eggs",
    "Name": "Generic Frog Eggs",
    "Ingredients": [[1, "Phytoplankton C"], [1, "T4 Mutagen"], [1, "T1 Fertilizer"]],
    "CraftingMachine": "Incubator",
    "ApId": 139,
    "Classification": "useful"
  },
  {
    "Id": "Frog2Eggs",
    "Name": "Frog Huli Eggs",
    "Ingredients": [[1, "Frog1Eggs"], [1, "T4 Mutagen"]],
    "CraftingMachine": "Incubator",
    "ApId": 44,
    "Classification": "useful"
  },
  {
    "Id": "Frog4Eggs",
    "Name": "Frog Strabo Eggs",
    "Ingredients": [[1, "Frog1Eggs"], [1, "T4 Mutagen"], [1, "T1 Fertilizer"]],
    "CraftingMachine": "Incubator",
    "ApId": 102,
    "Classification": "useful"
  },
  {
    "Id": "Frog5Eggs",
    "Name": "Frog Trajuu Eggs",
    "Ingredients": [[1, "Frog1Eggs"], [1, "T4 Mutagen"], [1, "T1 Fertilizer"]],
    "CraftingMachine": "Incubator",
    "ApId": 128,
    "Classification": "useful"
  },
  {
    "Id": "Frog7Eggs",
    "Name": "Frog Afae Eggs",
    "Ingredients": [[1, "Frog1Eggs"], [1, "T3 Mutagen"], [1, "T2 Fertilizer"]],
    "CraftingMachine": "Incubator",
    "ApId": 136,
    "Classification": "useful"
  },
  {
    "Id": "Frog9Eggs",
    "Name": "Frog Amedo Eggs",
    "Ingredients": [[1, "Frog1Eggs"], [1, "T4 Mutagen"], [1, "T2 Fertilizer"]],
    "CraftingMachine": "Incubator",
    "ApId": 140,
    "Classification": "useful"
  },
  {
    "Id": "Fish1Eggs",
    "Name": "Fish Provios Eggs",
    "Ingredients": [[1, "Phytoplankton A"], [1, "T3 Mutagen"], [1, "T1 Fertilizer"]],
    "CraftingMachine": "Incubator",
    "ApId": 96,
    "Classification": "useful"
  },
  {
    "Id": "Fish3Eggs",
    "Name": "Fish Gerrero Eggs",
    "Ingredients": [[1, "Phytoplankton B"], [1, "T3 Mutagen"], [1, "T1 Fertilizer"]],
    "CraftingMachine": "Incubator",
    "ApId": 97,
    "Classification": "useful"
  },
  {
    "Id": "Fish5Eggs",
    "Name": "Fish Ulani Eggs",
    "Ingredients": [[1, "Phytoplankton C"], [1, "T3 Mutagen"], [1, "T1 Fertilizer"]],
    "CraftingMachine": "Incubator",
    "ApId": 129,
    "Classification": "useful"
  },
  {
    "Id": "Fish6Eggs",
    "Name": "Fish Aelera Eggs",
    "Ingredients": [[1, "Phytoplankton C"], [1, "T2 Mutagen"], [1, "T1 Fertilizer"]],
    "CraftingMachine": "Incubator",
    "ApId": 130,
    "Classification": "useful"
  },
  {
    "Id": "Butterfly8Larvae",
    "Name": "Butterfly Chevrone Larva",
    "Ingredients": [[1, "Rare Larva"], [1, "T1 Mutagen"], [1, "T1 Fertilizer"]],
    "CraftingMachine": "Incubator",
    "ApId": 106,
    "Classification": "useful"
  },
  {
    "Id": "Butterfly9Larvae",
    "Name": "Butterfly Aemel Larva",
    "Ingredients": [[1, "Rare Larva"], [1, "T1 Mutagen"], [1, "T1 Fertilizer"]],
    "CraftingMachine": "Incubator",
    "ApId": 107,
    "Classification": "useful"
  },
  {
    "Id": "Butterfly10Larvae",
    "Name": "Butterfly Liux Larva",
    "Ingredients": [[1, "Rare Larva"], [1, "T1 Mutagen"], [1, "T1 Fertilizer"]],
    "CraftingMachine": "Incubator",
    "ApId": 108,
    "Classification": "useful"
  },
  {
    "Id": "Butterfly16Larvae",
    "Name": "Butterfly Imeo Larva",
    "Ingredients": [[1, "Rare Larva"], [1, "T2 Mutagen"], [1, "T1 Fertilizer"]],
    "CraftingMachine": "Incubator",
    "ApId": 111,
    "Classification": "useful"
  },
  {
    "Id": "Butterfly17Larvae",
    "Name": "Butterfly Serena Larva",
    "Ingredients": [[1, "Rare Larva"], [1, "T2 Mutagen"], [1, "T1 Fertilizer"]],
    "CraftingMachine": "Incubator",
    "ApId": 113,
    "Classification": "useful"
  },
  {
    "Id": "Tree9Seed",
    "Name": "Tree Seed Shreox",
    "Ingredients": [[1, "Tree bark"], [1, "T1 Mutagen"], [1, "T2 Mutagen"]],
    "CraftingMachine": "DNA Manipulator",
    "ApId": 110,
    "Classification": "useful"
  },
  {
    "Id": "Tree3Seed",
    "Name": "Tree Seed Cernea",
    "Ingredients": [[1, "Tree bark"], [1, "T1 Mutagen"], [1, "Seed Nulna"]],
    "CraftingMachine": "DNA Manipulator",
    "ApId": 114,
    "Classification": "useful"
  },
  {
    "Id": "Tree4Seed",
    "Name": "Tree Seed Elegea",
    "Ingredients": [[1, "Tree bark"], [1, "T1 Mutagen"], [1, "Seed Tuska"]],
    "CraftingMachine": "DNA Manipulator",
    "ApId": 116,
    "Classification": "useful"
  },
  {
    "Id": "Tree5Seed",
    "Name": "Tree Seed Humelora",
    "Ingredients": [[1, "Tree bark"], [1, "T1 Mutagen"], [1, "Plant Orema"]],
    "CraftingMachine": "DNA Manipulator",
    "ApId": 117,
    "Classification": "useful"
  },
  {
    "Id": "Tree6Seed",
    "Name": "Tree Seed Aemora",
    "Ingredients": [[1, "Tree bark"], [1, "T1 Mutagen"], [1, "Plant Volnus"]],
    "CraftingMachine": "DNA Manipulator",
    "ApId": 120,
    "Classification": "useful"
  },
  {
    "Id": "AnimalFood1",
    "Name": "T1 Animal Food",
    "Ingredients": [[1, "Honey"], [1, "Beans"], [1, "Common Larva"]],
    "CraftingMachine": "Biolab",
    "ApId": 103,
    "Classification": "progression"
  },
  {
    "Id": "AnimalFood2",
    "Name": "T2 Animal Food",
    "Ingredients": [[1, "T1 Animal Food"], [1, "Algae"], [1, "Rare Larva"]],
    "CraftingMachine": "Biolab",
    "ApId": 47,
    "Classification": "progression"
  },
  {
    "Id": "OxygenTank",
    "Name": "T1 Oxygen Tank",
    "Ingredients": [[2, "Cobalt"], [1, "Iron"], [1, "Magnesium"]],
    "CraftingMachine": "T1 Craft Station",
    "UnlockedFromStart": True
  },
  {
    "Id": "OxygenTank2",
    "Name": "T2 Oxygen Tank",
    "Ingredients": [[1, "T1 Oxygen Tank"], [1, "Silicon"], [1, "Cobalt"], [1, "Titanium"], [2, "Magnesium"]],
    "CraftingMachine": "T2 Craft Station",
    "ApId": 74,
    "Classification": "useful"
  },
  {
    "Id": "OxygenTank3",
    "Name": "T3 Oxygen Tank",
    "Ingredients": [[1, "T2 Oxygen Tank"], [1, "Iron"], [1, "Titanium"], [1, "Silicon"], [1, "Magnesium"], [1, "Aluminum"]],
    "CraftingMachine": "T2 Craft Station",
    "ApId": 53,
    "Classification": "useful"
  },
  {
    "Id": "astrofood2",
    "Name": "High Quality Food",
    "Ingredients": [[1, "Honey"], [1, "Beans"]],
    "CraftingMachine": "Biolab",
    "ApId": 115,
    "Classification": "useful"
  },
  {
    "Id": "FabricBlue",
    "Name": "Fabric",
    "Ingredients": [[2, "Silk"]],
    "CraftingMachine": "Biolab",
    "ApId": 119,
    "Classification": "useful"
  },
  {
    "Id": "Seed0",
    "Name": "Lirma Seed",
    "Ingredients": [[1, "T3 Mutagen"], [1, "T1 Fertilizer"], [1, "Phytoplankton A"]],
    "CraftingMachine": "DNA Manipulator",
    "ApId": 134,
    "Classification": "useful"
  },
  {
    "Id": "Jetpack1",
    "Name": "T1 Jetpack",
    "Ingredients": [[2, "Rocket Engine"], [1, "Titanium"]],
    "CraftingMachine": "Advanced Craft Station",
    "Classification": "useful",
    "UnlockedFromStart": True
  },
  {
    "Id": "Jetpack2",
    "Name": "T2 Jetpack",
    "Ingredients": [[1, "T1 Jetpack"], [1, "Super Alloy"], [1, "Sulfur"], [1, "Osmium"], [1, "Aluminum"]],
    "CraftingMachine": "Advanced Craft Station",
    "ApId": 158,
    "Classification": "useful"
  },
  {
    "Id": "Jetpack3",
    "Name": "T3 Jetpack",
    "Ingredients": [[1, "T2 Jetpack"], [1, "Super Alloy"], [2, "Osmium"], [2, "Explosive powder"]],
    "CraftingMachine": "Advanced Craft Station",
    "ApId": 171,
    "Classification": "useful"
  },
  {
    "Id": "Jetpack4",
    "Name": "T4 Jetpack",
    "Ingredients": [[1, "T3 Jetpack"], [2, "Blazar Quartz"], [1, "Osmium Rod"], [1, "Explosive powder"], [1, "Iridium Rod"]],
    "CraftingMachine": "Advanced Craft Station",
    "ApId": 141,
    "Classification": "useful"
  },
  {
    "Id": "BootsSpeed1",
    "Name": "T1 Agility Boots",
    "Ingredients": [[2, "Aluminum"], [2, "Fabric"]],
    "CraftingMachine": "Advanced Craft Station",
    "ApId": 142,
    "Classification": "useful"
  },
  {
    "Id": "BootsSpeed2",
    "Name": "T2 Agility Boots",
    "Ingredients": [[1, "T1 Agility Boots"], [2, "Super Alloy"], [2, "Fabric"]],
    "CraftingMachine": "Advanced Craft Station",
    "ApId": 145,
    "Classification": "useful"
  },
  {
    "Id": "BootsSpeed3",
    "Name": "T3 Agility Boots",
    "Ingredients": [[1, "T2 Agility Boots"], [2, "Super Alloy"], [1, "Explosive Powder"]],
    "CraftingMachine": "Advanced Craft Station",
    "ApId": 157,
    "Classification": "useful"
  },
  {
    "Id": "Explosive",
    "Name": "Explosive",
    "Ingredients": [[2, "Explosive Powder"], [1, "Circuit Board"]],
    "CraftingMachine": "Biolab",
    "ApId": 179,
    "Classification": "filler"
  },
  {
    "Id": "EnergyGenerator1",
    "Name": "Wind Turbine",
    "Ingredients": [[1, "Iron"]],
    "Energy": 1.2,
    "UnlockedFromStart": True
  },
  {
    "Id": "EnergyGenerator2",
    "Name": "T1 Solar Panel",
    "Ingredients": [[1, "Iron"], [2, "Cobalt"], [1, "Silicon"]],
    "Energy": 6.5,
    "ApId": 3,
    "Classification": "progression"
  },
  {
    "Id": "EnergyGenerator3",
    "Name": "T2 Solar Panel",
    "Ingredients": [[1, "Iron"], [2, "Cobalt"], [1, "Silicon"], [1, "Magnesium"], [1, "Aluminum"]],
    "Energy": 19.5,
    "ApId": 5,
    "Classification": "progression"
  },
  {
    "Id": "EnergyGenerator4",
    "Name": "T1 Nuclear Reactor",
    "Ingredients": [[3, "Super Alloy"], [2, "Water Bottle"], [1, "Uranium Rod"]],
    "Energy": 86.5,
    "ApId": 80,
    "Classification": "progression"
  },
  {
    "Id": "EnergyGenerator5",
    "Name": "T2 Nuclear Reactor",
    "Ingredients": [[3, "Water Bottle"], [1, "Super Alloy"], [3, "Uranium Rod"], [1, "Explosive Powder"]],
    "Energy": 331.5,
    "ApId": 82,
    "Classification": "progression"
  },
  {
    "Id": "EnergyGenerator6",
    "Name": "Nuclear Fusion Generator",
    "Ingredients": [[5, "Pulsar Quartz"], [4, "Super Alloy"]],
    "Energy": 1485,
    "ApId": 72,
    "Classification": "progression"
  },
  {
    "Id": "Drill0",
    "Name": "T1 Drill",
    "Ingredients": [[1, "Iron"], [1, "Titanium"]],
    "Energy": -0.5,
    "Pressure": 0.2,
    "UnlockedFromStart": True
  },
  {
    "Id": "Drill1",
    "Name": "T2 Drill",
    "Ingredients": [[1, "Iron"], [2, "Titanium"]],
    "Energy": -5,
    "Pressure": 1.5,
    "Heat": 0.1,
    "ApId": 76,
    "Classification": "progression"
  },
  {
    "Id": "Drill2",
    "Name": "T3 Drill",
    "Ingredients": [[1, "Iron"], [1, "Titanium"], [2, "Aluminum"]],
    "Energy": -8.5,
    "Pressure": 17,
    "Heat": 0.25,
    "ApId": 66,
    "Classification": "progression"
  },
  {
    "Id": "Drill3",
    "Name": "T4 Drill",
    "Ingredients": [[6, "Super Alloy"], [3, "Osmium"]],
    "Energy": -45.5,
    "Pressure": 459,
    "Heat": 25,
    "ApId": 71,
    "Classification": "progression"
  },
  {
    "Id": "Drill4",
    "Name": "T5 Drill",
    "Ingredients": [[2, "Super Alloy Rod"], [1, "Osmium Rod"]],
    "Energy": -375.5,
    "Pressure": 3950,
    "Heat": 295,
    "ApId": 95,
    "Classification": "progression"
  },
  {
    "Id": "Heater1",
    "Name": "T1 Heater",
    "Ingredients": [[1, "Iridium"], [1, "Iron"], [1, "Silicon"]],
    "Energy": -1,
    "Heat": 0.3,
    "UnlockedFromStart": True
  },
  {
    "Id": "Heater2",
    "Name": "T2 Heater",
    "Ingredients": [[2, "Iridium"], [1, "Iron"], [1, "Silicon"], [1, "Titanium"], [1, "Aluminum"]],
    "Energy": -3.5,
    "Heat": 4.5,
    "ApId": 52,
    "Classification": "progression"
  },
  {
    "Id": "Heater3",
    "Name": "T3 Heater",
    "Ingredients": [[1, "Iridium Rod"], [1, "Silicon"], [1, "Titanium"], [1, "Aluminum"]],
    "Energy": -17.5,
    "Pressure": 0.6,
    "Heat": 28.5,
    "ApId": 56,
    "Classification": "progression"
  },
  {
    "Id": "Heater4",
    "Name": "T4 Heater",
    "Ingredients": [[3, "Super Alloy"], [2, "Iridium Rod"], [1, "Explosive Powder"]],
    "Energy": -51.5,
    "Pressure": 35.5,
    "Heat": 538,
    "ApId": 59,
    "Classification": "progression"
  },
  {
    "Id": "Heater5",
    "Name": "T5 Heater",
    "Ingredients": [[3, "Super Alloy Rod"], [3, "Iridium Rod"], [3, "Explosive Powder"]],
    "Energy": -360.5,
    "Pressure": 280,
    "Heat": 4530,
    "ApId": 93,
    "Classification": "progression"
  },
  {
    "Id": "OreExtractor1",
    "Name": "T1 Ore Extractor",
    "Ingredients": [[2, "Osmium"], [1, "Iridium Rod"], [1, "Super Alloy"], [1, "Aluminum"], [1, "Titanium"]],
    "Energy": -34,
    "Pressure": 15,
    "Heat": 17.5,
    "ApId": 81,
    "Classification": "progression"
  },
  {
    "Id": "OreExtractor2",
    "Name": "T2 Ore Extractor",
    "Ingredients": [[3, "Osmium"], [2, "Iridium Rod"], [1, "Super Alloy Rod"]],
    "Energy": -164,
    "Pressure": 85,
    "Heat": 79.5,
    "ApId": 85,
    "Classification": "progression"
  },
  {
    "Id": "OreExtractor3",
    "Name": "T3 Ore Extractor",
    "Ingredients": [[1, "Osmium Rod"], [1, "Super Alloy Rod"], [1, "Iridium Rod"], [3, "Titanium"]],
    "Energy": -289,
    "Pressure": 135,
    "Heat": 202,
    "ApId": 86,
    "Classification": "progression"
  },
  {
    "Id": "GasExtractor1",
    "Name": "T1 Gas Extractor",
    "Ingredients": [[3, "Super Alloy"], [2, "Zeolite"], [1, "Iridium Rod"]],
    "Energy": -58,
    "Heat": 13,
    "ApId": 84,
    "Classification": "progression"
  },
  {
    "Id": "GasExtractor2",
    "Name": "T2 Gas Extractor",
    "Ingredients": [[2, "Super Alloy"], [2, "Zeolite"], [1, "Iridium Rod"], [1, "Circuit Board"]],
    "Energy": -218,
    "Pressure": 32,
    "Heat": 45,
    "ApId": 112,
    "Classification": "progression"
  },
  {
    "Id": "Vegetube1",
    "Name": "T1 Vegetube",
    "Ingredients": [[1, "Iron"], [1, "Ice"], [1, "Magnesium"]],
    "Energy": -0.35,
    "Oxygen": 0.15,
    "UnlockedFromStart": True
  },
  {
    "Id": "Vegetube2",
    "Name": "T2 Vegetube",
    "Ingredients": [[1, "Iron"], [2, "Ice"], [1, "Magnesium"], [1, "Silicon"]],
    "Energy": -1.25,
    "Oxygen": 1.2,
    "ApId": 62,
    "Classification": "progression"
  },
  {
    "Id": "VegetubeOutside1",
    "Name": "T3 Vegetube",
    "Ingredients": [[1, "Water Bottle"], [2, "Silicon"], [1, "Magnesium"], [1, "Aluminum"]],
    "Energy": -7.25,
    "Oxygen": 13,
    "ApId": 55,
    "Classification": "progression"
  },
  {
    "Id": "biodome",
    "Name": "T1 Biodome",
    "Ingredients": [[1, "Lirma Seed"], [2, "Titanium"], [2, "Cobalt"], [1, "Aluminum"], [3, "Super Alloy"]],
    "Energy": -37,
    "Oxygen": 135,
    "ApId": 67,
    "Classification": "progression"
  },
  {
    "Id": "Biodome2",
    "Name": "T2 Biodome",
    "Ingredients": [[2, "T1 Fertilizer"], [2, "Bacteria"], [1, "Super Alloy"], [1, "Sulfur"]],
    "Energy": -75,
    "Oxygen": 1450,
    "Plants": 11,
    "ApId": 70,
    "Classification": "progression"
  },
  {
    "Id": "GrassSpreader1",
    "Name": "Grass Spreader",
    "Ingredients": [[2, "Water Bottle"], [1, "Magnesium"], [1, "Aluminum"], [1, "Lirma Seed"]],
    "Energy": -13.8,
    "Oxygen": 108,
    "Plants": 0.19,
    "ApId": 57,
    "Classification": "progression"
  },
  {
    "Id": "SeedSpreader1",
    "Name": "T1 Flower Spreader",
    "Ingredients": [[3, "Water Bottle"], [1, "Magnesium"], [1, "Super Alloy"], [1, "T1 Fertilizer"]],
    "Energy": -28.8,
    "Oxygen": 161,
    "Plants": 9.2,
    "ApId": 83,
    "Classification": "progression"
  },
  {
    "Id": "SeedSpreader2",
    "Name": "T2 Flower Spreader",
    "Ingredients": [[2, "Water Bottle"], [2, "Super Alloy"], [2, "T1 Fertilizer"]],
    "Energy": -38.8,
    "Oxygen": 325,
    "Plants": 43.5,
    "ApId": 90,
    "Classification": "progression"
  },
  {
    "Id": "AlgaeGenerator1",
    "Name": "T1 Algae Generator",
    "Ingredients": [[1, "Bioplastic Nugget"], [1, "Eggplant"], [1, "Water Bottle"], [1, "Magnesium"], [1, "Super Alloy"]],
    "Energy": -13,
    "Oxygen": 127,
    "Plants": 0.8,
    "ApId": 69,
    "Classification": "progression"
  },
  {
    "Id": "AlgaeGenerator2",
    "Name": "T2 Algae Generator",
    "Ingredients": [[2, "Bioplastic Nugget"], [1, "T1 Fertilizer"], [1, "Water Bottle"], [1, "Magnesium"], [2, "Super Alloy"]],
    "Energy": -27,
    "Oxygen": 350,
    "Plants": 23,
    "ApId": 88,
    "Classification": "progression"
  },
  {
    "Id": "TreeSpreader0",
    "Name": "T1 Tree Spreader",
    "Ingredients": [[1, "Super Alloy"], [1, "Bacteria"], [1, "T1 Fertilizer"], [1, "Tree bark"], [1, "Bioplastic Nugget"]],
    "Energy": -31,
    "Oxygen": 920,
    "Plants": 97,
    "ApId": 92,
    "Classification": "progression"
  },
  {
    "Id": "TreeSpreader1",
    "Name": "T2 Tree Spreader",
    "Ingredients": [[1, "Super Alloy"], [1, "Bacteria"], [1, "Tree bark"], [1, "T2 Fertilizer"], [1, "Zeolite"]],
    "Energy": -71,
    "Oxygen": 1950,
    "Plants": 175,
    "ApId": 60,
    "Classification": "progression"
  },
  {
    "Id": "TreeSpreader2",
    "Name": "T3 Tree Spreader",
    "Ingredients": [[1, "Super Alloy"], [1, "Bacteria"], [1, "Tree bark"], [2, "T2 Fertilizer"], [1, "Zeolite"]],
    "Energy": -153,
    "Oxygen": 8500,
    "Plants": 1250,
    "ApId": 31,
    "Classification": "progression"
  },
  {
    "Id": "Farm1",
    "Name": "T1 Outdoor Farm",
    "Ingredients": [[2, "Bee Larva"], [1, "Water Bottle"], [1, "T1 Fertilizer"], [1, "T2 Fertilizer"], [1, "Super Alloy"]],
    "Energy": -45.5,
    "Plants": 95,
    "Insects": 8,
    "ApId": 121,
    "Classification": "progression"
  },
  {
    "Id": "Farm2",
    "Name": "T2 Outdoor Farm",
    "Ingredients": [[2, "Bee Larva"], [1, "Water Bottle"], [1, "T2 Fertilizer"], [1, "T3 Fertilizer"], [1, "Super Alloy"]],
    "Energy": -165,
    "Oxygen": 135,
    "Plants": 275,
    "Insects": 135
  },
  {
    "Id": "Aquarium1",
    "Name": "T1 Aquarium",
    "Ingredients": [[1, "T2 Fertilizer"], [1, "Super Alloy"], [1, "Circuit Board"], [1, "Oxygen"]],
    "Energy": -75,
    "Animals": 4,
    "ApId": 36,
    "Classification": "progression"
  },
  {
    "Id": "Aquarium2",
    "Name": "T2 Aquarium",
    "Ingredients": [[1, "T2 Fertilizer"], [1, "Super Alloy Rod "], [1, "Circuit Board"], [1, "Phytoplankton A"], [1, "Phytoplankton B"], [1, "Phytoplankton C"]],
    "Energy": -225,
    "Oxygen": 250,
    "Plants": 18,
    "Insects": 25,
    "Animals": 65,
    "ApId": 98,
    "Classification": "progression"
  },
  {
    "Id": "Beehive1",
    "Name": "T1 Beehive",
    "Ingredients": [[1, "Bee Larva"], [1, "Super Alloy"], [1, "T1 Fertilizer"], [1, "Bioplastic Nugget"]],
    "Energy": -25,
    "Plants": 350,
    "Insects": 15,
    "ApId": 104,
    "Classification": "progression"
  },
  {
    "Id": "Beehive2",
    "Name": "T2 Beehive",
    "Ingredients": [[1, "Bee Larva"], [1, "Tree bark"], [1, "T2 Fertilizer"], [1, "Bioplastic Nugget"]],
    "Energy": -95,
    "Plants": 950,
    "Insects": 890,
    "ApId": 125,
    "Classification": "progression"
  },
  {
    "Id": "Ecosystem1",
    "Name": "Ecosystem",
    "Ingredients": [[1, "T2 Fertilizer"], [1, "Common Larva"], [1, "T2 Mutagen"], [1, "Bacteria"], [1, "Algae"], [1, "Water Bottle"]],
    "Energy": -325,
    "Plants": 2980,
    "Insects": 187,
    "ApId": 124,
    "Classification": "progression"
  },
  {
    "Id": "ButterflyFarm1",
    "Name": "T1 Butterfly Farm",
    "Ingredients": [[1, "T2 Fertilizer"], [1, "Zeolite"], [1, "Bioplastic Nugget"]],
    "Energy": -30,
    "Insects": 75,
    "ApId": 109,
    "Classification": "progression"
  },
  {
    "Id": "ButterflyFarm2",
    "Name": "T2 Butterfly Farm",
    "Ingredients": [[1, "T2 Fertilizer"], [1, "Zeolite"], [1, "Bioplastic Nugget"], [2, "Fabric"]],
    "Energy": -45,
    "Insects": 950,
    "ApId": 127,
    "Classification": "progression"
  },
  {
    "Id": "ButterflyFarm3",
    "Name": "Butterfly Dome",
    "Ingredients": [[1, "T2 Fertilizer"], [1, "T1 Fertilizer"], [1, "Tree bark"], [1, "Zeolite"], [2, "Super Alloy"]],
    "Energy": -139,
    "Insects": 20,
    "ApId": 105,
    "Classification": "progression"
  },
  {
    "Id": "AnimalShelter1",
    "Name": "Animal Shelter",
    "Ingredients": [[1, "Water Bottle"], [1, "Circuit Board"], [1, "Lirma Seed"], [1, "T2 Fertilizer"], [1, "Methane cartridge"], [1, "Silk"]],
    "Energy": -270,
    "Pressure": 340,
    "Heat": 280,
    "Animals": 13790,
    "ApId": 45,
    "Classification": "progression"
  },
  {
    "Id": "FishFarm1",
    "Name": "Fish Farm",
    "Ingredients": [[2, "Bioplastic Nugget"], [3, "Silk"], [1, "Phytoplankton A"]],
    "Energy": -155.5,
    "Pressure": 10,
    "Oxygen": 25,
    "Plants": 50,
    "Insects": 90,
    "Animals": 195,
    "ApId": 132,
    "Classification": "progression"
  },
  {
    "Id": "AmphibiansFarm1",
    "Name": "Amphibian Farm",
    "Ingredients": [[1, "T1 Fertilizer"], [1, "Common Larva"], [1, "Water Bottle"]],
    "Energy": -155,
    "Pressure": 75,
    "Heat": 175,
    "Plants": 75,
    "Animals": 965,
    "ApId": 43,
    "Classification": "progression"
  },
  { 
    "Id": "SilkGenerator",
    "Name": "Silk Generator",
    "Ingredients": [[3, "Silk Worm"], [1, "Zeolite"], [1, "Water Bottle"], [1, "Oxygen Capsule"]],
    "Energy": -38,
    "ApId": 118,
    "Classification": "progression"
  },
  { 
    "Id": "WaterLifeCollector1",
    "Name": "Water Life Collector",
    "Ingredients": [[3, "Silk"], [2, "Bioplastic Nugget"], [1, "Super Alloy"]],
    "Energy": -105.5,
    "ApId": 61,
    "Classification": "progression"
  },
  {
    "Id": "WaterCollector1",
    "Name": "Atmospheric Water Collector",
    "Ingredients": [[1, "Iron"], [1, "Silicon"], [1, "Magnesium"], [1, "Cobalt"], [1, "Aluminum"], [1, "Super Alloy"]],
    "Energy": -11,
    "ApId": 12,
    "Classification": "progression"
  },
  {
    "Id": "WaterCollector2",
    "Name": "Lake Water Collector",
    "Ingredients": [[3, "Bioplastic Nugget"], [1, "Magnesium"], [1, "Aluminum"], [1, "Super Alloy"]],
    "Energy": -19,
    "ApId": 16,
    "Classification": "progression"
  },
  {
    "Id": "VegetableGrower1",
    "Name": "T1 Food Grower",
    "Ingredients": [[1, "Aluminum"], [1, "Iron"], [1, "Water Bottle"]],
    "Energy": -15,
    "ApId": 54,
    "Classification": "progression"
  },
  {
    "Id": "VegetableGrower2",
    "Name": "T2 Food Grower",
    "Ingredients": [[1, "Water Bottle"], [1, "Super Alloy"], [1, "T1 Fertilizer"]],
    "Energy": -29.5,
    "ApId": 91,
    "Classification": "progression"
  },
  {
    "Id": "CraftStation1",
    "Name": "T2 Craft Station",
    "Ingredients": [[1, "Iron"], [1, "Silicon"]],
    "Energy": -0.5
  },
  {
    "Id": "CraftStation2",
    "Name": "Advanced Craft Station",
    "Ingredients": [[3, "Aluminum"], [1, "Titanium"], [1, "Magnesium"], [1, "Silicon"]],
    "Energy": -12.5,
    "ApId": 8,
    "Classification": "progression"
  },
  {
    "Id": "Biolab",
    "Name": "Biolab",
    "Ingredients": [[3, "Super Alloy"], [2, "Osmium"], [1, "Aluminum"]],
    "Energy": -40,
    "ApId": 87,
    "Classification": "progression"
  },
  {
    "Id": "Incubator1",
    "Name": "Incubator",
    "Ingredients": [[1, "Tree bark"], [1, "T2 Fertilizer"], [1, "Super Alloy"], [1, "Oxygen Capsule"]],
    "Energy": -215,
    "ApId": 28,
    "Classification": "progression"
  },
  {
    "Id": "EndingExplosives",
    "Name": "Large explosive device",
    "Ingredients": [[3, "Iridium Rod"], [3, "Explosive Powder"], [1, "Circuit Board"], [1, "Fusion Energy Cell"], [1, "Uranium Rod"]]
  },
  {
    "Id": "BedDouble",
    "Name": "Double Bed",
    "Ingredients": [[1, "Iron"], [6, "Fabric"]],
    "ApId": 6,
    "Classification": "filler"
  },
  {
    "Id": "Container2",
    "Name": "Locker Storage",
    "Ingredients": [[3, "Iron"]],
    "ApId": 7,
    "Classification": "filler"
  },
  {
    "Id": "LaunchPlatform",
    "Name": "Launch Platform",
    "Ingredients": [[3, "Super Alloy"], [3, "Titanium"], [3, "Iron"]],
    "Energy": -55,
    "ApId": 9,
    "Classification": "useful"
  },
  {
    "Id": "FoundationAngle",
    "Name": "Foundation - Angle",
    "Ingredients": [[1, "Iron"]],
    "ApId": 11,
    "Classification": "filler"
  },
  {
    "Id": "FoundationSlope",
    "Name": "Foundation - Slope",
    "Ingredients": [[2, "Iron"]],
    "ApId": 17,
    "Classification": "filler"
  },
  {
    "Id": "VehicleCrafter1",
    "Name": "Vehicle Station",
    "Ingredients": [[3, "Aluminum"], [2, "Super Alloy"], [1, "Iridium Rod"]],
    "Energy": -63,
    "ApId": 14,
    "Classification": "filler"
  },
  {
    "Id": "Optimizer1",
    "Name": "T1 Machine Optimizer",
    "Ingredients": [[2, "Explosive Powder"], [1, "Uranium Rod"], [2, "Iron"], [1, "Cobalt"]],
    "Energy": -50,
    "ApId": 18,
    "Classification": "useful"
  },
  {
    "Id": "Optimizer",
    "Name": "T2 Machine Optimizer",
    "Ingredients": [[2, "Explosive Powder"], [1, "Uranium Rod"], [3, "Obsidian"]],
    "Energy": -150,
    "ApId": 73,
    "Classification": "useful"
  },
  {
    "Id": "InteriorStairs1",
    "Name": "Interior Stairs",
    "Ingredients": [[2, "Iron"], [2, "Titanium"], [2, "Aluminum"]],
    "ApId": 19,
    "Classification": "filler"
  },
  {
    "Id": "ScreenBiomass",
    "Name": "Screen - Biomass",
    "Ingredients": [[1, "Iron"], [1, "Silicon"], [1, "Aluminum"]],
    "Energy": -3.4,
    "ApId": 20,
    "Classification": "filler"
  },
  {
    "Id": "ScreenTerraStage",
    "Name": "Screen - Progress",
    "Ingredients": [[1, "Iron"], [2, "Silicon"], [1, "Cobalt"]],
    "Energy": -1.3,
    "ApId": 63,
    "Classification": "filler"
  },
  {
    "Id": "ScreenMessage",
    "Name": "Screen - Transmissions",
    "Ingredients": [[1, "Iron"], [2, "Silicon"], [2, "Magnesium"]],
    "Energy": -0.4,
    "ApId": 78,
    "Classification": "filler"
  },
  {
    "Id": "ScreenRockets",
    "Name": "Screen - Orbital information",
    "Ingredients": [[1, "Microchip - Compass"], [1, "Silicon"], [1, "Osmium"]],
    "Energy": -35.2,
    "ApId": 21,
    "Classification": "filler"
  },
  {
    "Id": "ScreenMap1",
    "Name": "Screen - Mapping",
    "Ingredients": [[1, "Microchip - Compass"], [1, "Silicon"], [1, "Iron"]],
    "Energy": -14.7,
    "ApId": 151,
    "Classification": "filler"
  },
  {
    "Id": "ScreenSystem1",
    "Name": "Solar System Screen",
    "Ingredients": [[1, "Solar Quartz"], [1, "Silicon"], [1, "Magnetar Quartz"]],
    "Energy": -34.7,
    "ApId": 49,
    "Classification": "filler"
  },
  {
    "Id": "RocketOxygen1",
    "Name": "Seed Spreader Rocket",
    "Ingredients": [[1, "Rocket Engine"], [2, "Super Alloy"], [1, "Bacteria Sample"], [1, "Mutagen"], [1, "Tree Bark"]],
    "ApId": 22,
    "Classification": "useful"
  },
  {
    "Id": "RocketBiomass1",
    "Name": "Plant Rocket",
    "Ingredients": [[1, "Rocket Engine"], [2, "Super Alloy"], [1, "T1 Fertilizer"], [1, "Lirma Seed"], [1, "Tree Bark"]],
    "ApId": 89,
    "Classification": "useful"
  },
  {
    "Id": "RocketInsects1",
    "Name": "Insect Spreader Rocket",
    "Ingredients": [[1, "Rocket Engine"], [1, "Osmium Rod"], [1, "T2 Mutagen"], [3, "Bee Larva"]],
    "ApId": 94,
    "Classification": "useful"
  },
  {
    "Id": "RocketAnimals1",
    "Name": "Animals Spreader Rocket",
    "Ingredients": [[1, "Rocket Engine"], [1, "Osmium Rod"], [1, "T4 Mutagen"], [6, "Genetic Trait"]],
    "ApId": 100,
    "Classification": "useful"
  },
  {
    "Id": "RocketMap1",
    "Name": "T1 GPS Satellite",
    "Ingredients": [[1, "Rocket Engine"], [1, "Microchip - Compass"], [2, "Super Alloy"]],
    "ApId": 150,
    "Classification": "filler"
  },
  {
    "Id": "RocketMap2",
    "Name": "T2 GPS Satellite",
    "Ingredients": [[1, "Rocket Engine"], [2, "Microchip - Compass"], [3, "Super Alloy"]],
    "ApId": 159,
    "Classification": "filler"
  },
  {
    "Id": "RocketMap3",
    "Name": "T3 GPS Satellite",
    "Ingredients": [[1, "Rocket Engine"], [2, "Microchip - Compass"], [1, "Osmium"], [1, "Super Alloy Rod"]],
    "ApId": 169,
    "Classification": "filler"
  },
  {
    "Id": "RocketMap4",
    "Name": "T4 GPS Satellite",
    "Ingredients": [[1, "Rocket Engine"], [1, "Microchip - Compass"], [2, "Circuit Board"], [2, "Super Alloy Rod"]],
    "ApId": 177,
    "Classification": "filler"
  },
  {
    "Id": "RocketInformations1",
    "Name": "T1 Map Information Rocket",
    "Ingredients": [[1, "Rocket Engine"], [1, "Microchip - Compass"], [1, "Super Alloy Rod"], [2, "Osmium"]],
    "ApId": 161,
    "Classification": "useful"
  },
  {
    "Id": "RocketInformations2",
    "Name": "T2 Map Information Rocket",
    "Ingredients": [[1, "Rocket Engine"], [1, "Microchip - Compass"], [1, "Super Alloy Rod"], [2, "Zeolite"], [1, "Blazar Quartz"]],
    "ApId": 185,
    "Classification": "useful"
  },
  {
    "Id": "RocketDrones1",
    "Name": "Drone Visualization Rocket",
    "Ingredients": [[1, "Rocket Engine"], [2, "Circuit Board"], [1, "Super Alloy Rod"]],
    "ApId": 180,
    "Classification": "useful"
  },
  {
    "Id": "GeneticManipulator1",
    "Name": "DNA Manipulator",
    "Ingredients": [[1, "Super Alloy"], [1, "Bioplastic Nugget"], [1, "Explosive Powder"], [1, "Zeolite"], [1, "Osmium"]],
    "Energy": -117.5,
    "ApId": 23,
    "Classification": "useful"
  },
  {
    "Id": "AutoCrafter1",
    "Name": "Auto-Crafter",
    "Ingredients": [[2, "Osmium"], [1, "Super Alloy Rod"]],
    "Energy": -155,
    "ApId": 27,
    "Classification": "useful"
  },
  {
    "Id": "Teleporter1",
    "Name": "Teleporter",
    "Ingredients": [[1, "Super Alloy Rod"], [1, "Osmium"], [1, "Zeolite"], [2, "Pulsar Quartz"], [1, "Obsidian"]],
    "Energy": -276,
    "ApId": 30,
    "Classification": "useful"
  },
  {
    "Id": "DroneStation1",
    "Name": "Drone Station",
    "Ingredients": [[1, "Osmium Rod"], [1, "Super Alloy Rod"], [1, "Fusion Energy Cell"], [3, "Circuit Board"]],
    "Energy": -850,
    "ApId": 34,
    "Classification": "useful"
  },
  {
    "Id": "PortalGenerator1",
    "Name": "Portal Generator",
    "Ingredients": [[2, "Fusion Energy Cell"], [2, "Energy Multiplier Fuse"], [2, "Circuit Board"], [2, ""], [2, "Super Alloy Rod"], [1, "Microchip - Compass"]],
    "Energy": -1890,
    "ApId": 40,
    "Classification": "useful"
  },
  {
    "Id": "AnimalFeeder1",
    "Name": "Animal Feeder",
    "Ingredients": [[1, "Water Bottle"], [1, "Circuit Board"], [1, "Bioplastic Nugget"], [1, "Honey"], [1, "Silk"]],
    "Energy": -95,
    "ApId": 46,
    "Classification": "useful"
  },
  {
    "Id": "RocketTravel1",
    "Name": "Interplanetary Travel Rocket",
    "Ingredients": [[1, "Super Alloy Rod"], [1, "Rocket Engine"], [1, "Osmium Rod"], [1, "Blazar Quartz"], [1, "Solar Quartz"], [1, "Quasar Quartz"], [2, "Fusion Energy Cell"], [1, "Energy Multiplier Fuse"]],
    "ApId": 50,
    "Classification": "filler"
  },
  {
    "Id": "Ladder",
    "Name": "Indoor Ladder",
    "Ingredients": [[1, "Iron"], [1, "Cobalt"]],
    "ApId": 51,
    "Classification": "filler"
  },
  {
    "Id": "FlowerPot1",
    "Name": "Flower Pot",
    "Ingredients": [[1, "Magnesium"], [1, "Cobalt"], [1, "T1 Fertilizer"]],
    "ApId": 58,
    "Classification": "filler"
  },
  {
    "Id": "Beacon",
    "Name": "Beacon",
    "Ingredients": [[1, "Titanium"], [1, "Silicon"], [1, "Aluminum"]],
    "ApId": 64,
    "Classification": "filler"
  },
  {
    "Id": "Sign",
    "Name": "Sign",
    "Ingredients": [[1, "Magnesium"]],
    "ApId": 68,
    "Classification": "filler"
  },
  {
    "Id": "window",
    "Name": "Living Compartment Window",
    "Ingredients": [[1, "Iron"], [1, "Cobalt"]],
    "ApId": 75,
    "Classification": "filler"
  },
  {
    "Id": "FloorGlass",
    "Name": "Living Compartment Glass",
    "Ingredients": [[1, "Titanium"], [1, "Cobalt"]],
    "ApId": 77,
    "Classification": "filler"
  },
  {
    "Id": "ComAntenna",
    "Name": "Communication Antenna",
    "Ingredients": [[1, "Silicon"], [1, "Titanium"], [1, "Iron"], [1, "Aluminum"]],
    "ApId": 79,
    "Classification": "filler"
  },
  {
    "Id": "GeneticSynthetizer1",
    "Name": "Genetic Synthesizer",
    "Ingredients": [[1, "Magnetar Quartz"], [1, "Blazar Quartz"], [1, "Quasar Quartz"], [1, "Super Alloy Rod"], [1, "Circuit Board"], [1, "T4 Mutagen"]],
    "Energy": -292,
    "ApId": 99,
    "Classification": "progression"
  },
  {
    "Id": "HarvestingRobot1",
    "Name": "Harvesting Robot",
    "Ingredients": [[2, "Quasar Quartz"], [1, "Super Alloy Rod"], [3, "Osmium"]],
    "Energy": -120,
    "ApId": 101,
    "Classification": "useful"
  },
  {
    "Id": "ButterflyDisplayer1",
    "Name": "Butterfly Display Box",
    "Ingredients": [[1, "Iron"], [1, "Fabric"]],
    "ApId": 122,
    "Classification": "filler"
  },
  {
    "Id": "GeneticExtractor1",
    "Name": "Genetic Extractor",
    "Ingredients": [[1, "Blazar Quartz"], [1, "Pulsar Quartz"], [1, "Solar Quartz"], [1, "Osmium Rod"], [1, "Circuit Board"], [1, "T3 Mutagen"]],
    "Energy": -317.5,
    "ApId": 126,
    "Classification": "progression"
  },
  {
    "Id": "FishDisplayer1",
    "Name": "Fish Display",
    "Ingredients": [[1, "Tree Bark"]],
    "ApId": 131,
    "Classification": "filler"
  },
  {
    "Id": "FrogDisplayer1",
    "Name": "Frog Display",
    "Ingredients": [[1, "Tree Bark"]],
    "ApId": 137,
    "Classification": "filler"
  },
  {
    "Id": "podAngle",
    "Name": "Living Compartment Corner",
    "Ingredients": [[1, "Iron"], [1, "Titanium"], [1, "Cobalt"]],
    "ApId": 147,
    "Classification": "filler"
  },
  {
    "Id": "RecyclingMachine",
    "Name": "Recycling Machine",
    "Ingredients": [[2, "Microchip - T1 Deconstruction"], [3, "Super Alloy"]],
    "Energy": -12.5,
    "ApId": 148,
    "Classification": "filler"
  },
  {
    "Id": "Destructor1",
    "Name": "Shredder Machine",
    "Ingredients": [[1, "Super Alloy"], [1, "Uranium"], [1, "Osmium"], [1, "Explosive Powder"]],
    "Energy": -18,
    "ApId": 152,
    "Classification": "filler"
  },
  {
    "Id": "InsideLamp1",
    "Name": "Area Lamp",
    "Ingredients": [[1, "Magnesium"], [1, "Cobalt"]],
    "Energy": -1.2,
    "ApId": 153,
    "Classification": "filler"
  },
  {
    "Id": "Pod4x",
    "Name": "Big Living Compartment",
    "Ingredients": [[3, "Iron"], [3, "Titanium"], [3, "Super Alloy"]],
    "ApId": 156,
    "Classification": "filler"
  },
  {
    "Id": "Fence",
    "Name": "Fence",
    "Ingredients": [[1, "Silicon"]],
    "ApId": 160,
    "Classification": "filler"
  },
  {
    "Id": "DisplayCase",
    "Name": "Display Case",
    "Ingredients": [[2, "Cobalt"], [1, "Iron"], [1, "Super Alloy"]],
    "ApId": 163,
    "Classification": "filler"
  },
  {
    "Id": "SkinDisplayer",
    "Name": "Spacesuit Displayer",
    "Ingredients": [[1, "Quasar Quartz"], [1, "Super Alloy Rod"]],
    "ApId": 173,
    "Classification": "filler"
  },
  {
    "Id": "WallInside",
    "Name": "Interior Wall",
    "Ingredients": [[2, "Iron"]],
    "ApId": 175,
    "Classification": "filler"
  },
  {
    "Id": "Flare",
    "Name": "Flare",
    "Ingredients": [[1, "Explosive Powder"], [1, "Bioplastic Nugget"]],
    "ApId": 178,
    "Classification": "filler"
  },
  {
    "Id": "FlowerPot3",
    "Name": "Big Flower Pot",
    "Ingredients": [[1, "Iron"], [1, "T1 Fertilizer"]],
    "ApId": 186,
    "Classification": "filler"
  },
  {
    "Id": "Table1",
    "Name": "Big Table",
    "Ingredients": [[2, "Iron"]],
    "ApId": 187,
    "Classification": "filler"
  },
  {
    "Id": "TreePlanter2",
    "Name": "Bonsai Pot",
    "Ingredients": [[1, "Iron"], [1, "T1Fertilizer"]],
    "ApId": 188,
    "Classification": "filler"
  },
  {
    "Id": "Counter1",
    "Name": "Countertop 1",
    "Ingredients": [[2, "Iron"]],
    "ApId": 189,
    "Classification": "filler"
  },
  {
    "Id": "Counter2",
    "Name": "Countertop 2",
    "Ingredients": [[2, "Iron"]],
    "ApId": 190,
    "Classification": "filler"
  },
  {
    "Id": "Chair2",
    "Name": "Cozy Chair",
    "Ingredients": [[1, "Iron"], [2, "Smart Fabric"]],
    "ApId": 191,
    "Classification": "filler"
  },
  {
    "Id": "SofaAngleColored",
    "Name": "Customizable Corner Sofa",
    "Ingredients": [[1, "Iron"], [2, "Smart Fabric"]],
    "ApId": 192,
    "Classification": "filler"
  },
  {
    "Id": "Desktop2",
    "Name": "Desktop 2",
    "Ingredients": [[1, "Super Alloy"]],
    "ApId": 193,
    "Classification": "filler"
  },
  {
    "Id": "Faucet1",
    "Name": "Faucet",
    "Ingredients": [[1, "Water Bottle"], [1, "Super Alloy"], [1, "Magnesium"]],
    "ApId": 194,
    "Classification": "filler"
  },
  {
    "Id": "Fireplace",
    "Name": "Fireplace",
    "Ingredients": [[1, "Explosive Powder"], [1, "Tree Bark"], [1, "Iron"]],
    "ApId": 195,
    "Classification": "filler"
  },
  {
    "Id": "Fridge1",
    "Name": "Fridge",
    "Ingredients": [[1, "Super Alloy"], [1, "Methane cartridge"], [1, "Cobalt"]],
    "ApId": 196,
    "Classification": "filler"
  },
  {
    "Id": "FountainBig",
    "Name": "Fountain",
    "Ingredients": [[1, "Iron"], [1, "Super Alloy"], [1, "Zeolite"]],
    "ApId": 197,
    "Classification": "filler"
  },
  {
    "Id": "TableSmall3",
    "Name": "Glass Table",
    "Ingredients": [[1, "Cobalt"], [1, "Titanium"]],
    "ApId": 198,
    "Classification": "filler"
  },
  {
    "Id": "FlowerPot2",
    "Name": "Hanging Flower Pot",
    "Ingredients": [[1, "Magnesium"], [1, "Bacteria Sample"]],
    "ApId": 199,
    "Classification": "filler"
  },
  {
    "Id": "HologramGenerator",
    "Name": "Hologram Projector",
    "Ingredients": [[1, "Blazar Quartz"], [1, "Super Alloy Rod"]],
    "ApId": 200,
    "Classification": "filler"
  },
  {
    "Id": "ExerciseBike1",
    "Name": "Indoor Bike",
    "Ingredients": [[1, "Iron"], [1, "Fabric"], [1, "Silicon"]],
    "ApId": 201,
    "Classification": "filler"
  },
  {
    "Id": "Ivy1",
    "Name": "Ivy",
    "Ingredients": [[1, "Lirma Seed"]],
    "ApId": 202,
    "Classification": "filler"
  },
  {
    "Id": "Library1",
    "Name": "Library",
    "Ingredients": [[1, "Iron"]],
    "ApId": 203,
    "Classification": "filler"
  },
  {
    "Id": "LightBoxMedium",
    "Name": "Light Box",
    "Ingredients": [[2, "Silicon"], [1, "Solar Quartz"]],
    "ApId": 204,
    "Classification": "filler"
  },
  {
    "Id": "PlanetViewer1",
    "Name": "Planet Viewer",
    "Ingredients": [[1, "Silicon"], [1, "Solar Quartz"], [1, "Iron"], [1, "Zeolite"]],
    "ApId": 205,
    "Classification": "filler"
  },
  {
    "Id": "Pooltable1",
    "Name": "Pool Table",
    "Ingredients": [[1, "Smart Fabric"], [2, "Aluminum"]],
    "ApId": 206,
    "Classification": "filler"
  },
  {
    "Id": "Vault1",
    "Name": "Safe Vault",
    "Ingredients": [[1, "Super Alloy Rod"]],
    "ApId": 207,
    "Classification": "filler"
  },
  {
    "Id": "Server1",
    "Name": "Server",
    "Ingredients": [[1, "Circuit Board"]],
    "ApId": 208,
    "Classification": "filler"
  },
  {
    "Id": "Shelves1",
    "Name": "Shelves",
    "Ingredients": [[1, "Iron"]],
    "ApId": 209,
    "Classification": "filler"
  },
  {
    "Id": "TableSmall2",
    "Name": "Small Table",
    "Ingredients": [[1, "Iron"], [1, "Titanium"]],
    "ApId": 210,
    "Classification": "filler"
  },
  {
    "Id": "Trashcan1",
    "Name": "Trash Can",
    "Ingredients": [[1, "Silicon"]],
    "ApId": 211,
    "Classification": "filler"
  },
  {
    "Id": "Treadmill1",
    "Name": "Treadmill",
    "Ingredients": [[1, "Circuit Board"], [1, "Super Alloy"]],
    "ApId": 212,
    "Classification": "filler"
  },
  {
    "Id": "TreePlanter",
    "Name": "Tree Pot",
    "Ingredients": [[1, "Super Alloy"], [1, "T2 Fertilizer"]],
    "ApId": 213,
    "Classification": "filler"
  }
]
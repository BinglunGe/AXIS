from economy import Economy

economy = Economy(
    id="STEELTOWN",
    numeric_id=5,
    # as of May 2015 the following cargos must have fixed positions if used by an economy:
    # passengers: 0, mail: 2, goods 5, food 11
    # keep the rest of the cargos alphabetised
    # bump the min. compatible version if this list changes
    cargos=[
        "passengers",
        "acid",
        "mail",
        "alloy_steel",
        "aluminia",
        "goods",
        "aluminium",
        "ammonia",
        "ammonium_nitrate",
        "bauxite",
#        "building_materials",
        "carbon_black",
        "food",
        "carbon_steel",
#        "cast_iron",
        "cement",
        "chemicals",
        "chlorine",
 #       "clay",
        "cleaning_agents",
        "coal",
        "coal_tar",
        "coke",
        "copper",
        "copper_concentrate",
        "electrical_parts",
        "engineering_supplies",
        "ethylene",
        "farm_supplies",
        "ferrochrome",
        "fish",
        "forgings_and_castings",
        "fruits",
        "glass",
        "grain",
        "hydrogen",
        "iron_ore",
        "limestone",
        "livestock",
#        "logs",
#       "lumber",
        "lye",
#        "manganese",
        "nitrogen",
        "oil",
        "oxygen",
        "packaging",
        "paints_and_coatings",
        "petrol",
        "pig_iron",
#        "pipe",
#        "plant_fibres",
        "plastics",
#        "potash",
        "pyrite_ore",
        "quicklime",
        "recyclables",
        "rubber",
        "salt",
        "sand",
        "scrap_metal",
        "slag",
        "soda_ash",
 #       "stainless_steel",
        "steel_sections",
        "steel_sheet",
        "steel_wire_rod",
        "sulphur",
 #       "textiles",
        "tyres",
        "vehicle_bodies",
        "vehicle_engines",
        "vehicle_parts",
        "vehicles", 
        "zinc",
    ],
cargoflow_graph_tuning={}
)

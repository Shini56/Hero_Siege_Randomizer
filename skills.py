# List of all the skins by this Order: Heroname -> skillname sort by level 0->8->16->24->30 Skilltree 1 then Skilltree 2. Requirements for what skills the skill needs to put skill into it 
skillset = {
    "viking" : [

        {
            "name": "Weapon Master",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Viking/Weapon_Master.png",
        },

        {
            "name": "Charge",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Viking/Charge.png",
        },

        {
            "name": "Stoneskin",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Viking/Stoneskin.png",
        },

        {
            "name": "Devastating Charge",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Charge"],
            "image" : "Assets/Skills/Viking/Devastating_Charge.png",
        },

        {
            "name": "Norse Resistance",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Stoneskin"],
            "image" : "Assets/Skills/Viking/Norse_Resistance.png",
        },
        

        {
            "name": "Defensive Shout",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Viking/Defensive_Shout.png",
        },
        
        {
            "name": "Odins Fury",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Defensive Shout"],
            "image" : "Assets/Skills/Viking/Odins_Fury.png",
        },

        {
            "name": "Battle Agility",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Defensive Shout"],
            "image" : "Assets/Skills/Viking/Battle_Agility.png",
        },

        {
            "name": "Combat Orders",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Odins Fury", "Defensive Shout"],
            "image" : "Assets/Skills/Viking/Combat_Orders.png",
        },

        {
            "name": "Seismic Slam",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Viking/Seismic_Slam.png",
        },
        
        {
            "name": "Brute Force",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Viking/Brute_Force.png",
        },

        {
            "name": "Throw!",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Seismic Slam"],
            "image" : "Assets/Skills/Viking/Throw.png",
        },

        {
            "name": "Zeal",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Brute Force"],
            "image" : "Assets/Skills/Viking/Zeal.png",
        },

        {
            "name": "Ymirs Champion",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Zeal", "Brute Force"],
            "image" : "Assets/Skills/Viking/Ymirs_Champion.png",
        },
        
        {
            "name": "Whirlwind",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Viking/Whirlwind.png",
        },

        {
            "name": "Shockwave",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Throw!", "Seismic Slam"],
            "image" : "Assets/Skills/Viking/Shockwave.png",
        },

        {
            "name": "Berserk",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Ymirs Champion", "Zeal", "Brute Force"],
            "image" : "Assets/Skills/Viking/Berserk.png",
        },

        {
            "name": "Demolishing Winds",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Whirlwind"],
            "image" : "Assets/Skills/Viking/Demolishing_Winds.png",
        },
    ],

    "pyromancer" : [

        {
            "name": "Blazing Trail",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Pyromancer/Blazing_Trail.png",
        },

        {
            "name": "Fire Enchant",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Pyromancer/Fire_Enchant.png",
        },

        {
            "name": "Phoenix Flight",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Pyromancer/Phoenix_Flight.png",
        },

        {
            "name": "Inferno Slash",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Fire Enchant"],
            "image" : "Assets/Skills/Pyromancer/Inferno_Slash.png",
        },

        {
            "name": "Searing Chains",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Inferno Slash", "Fire Enchant"],
            "image" : "Assets/Skills/Pyromancer/Searing_Chains.png",
        },

        {
            "name": "Ignite",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Fire Enchant"],
            "image" : "Assets/Skills/Pyromancer/Ignite.png",
        },
        
        {
            "name": "Fire Shield",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Phoenix Flight", "Blazing Trail"],
            "image" : "Assets/Skills/Pyromancer/Fire_Shield.png",
        },

        {
            "name": "Fiery Presence",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Pyromancer/Fiery_Presence.png",
        },

        {
            "name": "Avatar of Fire",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Pyromancer/Avatar_of_Fire.png",
        },

        {
            "name": "Breath of Fire",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Pyromancer/Breath_of_Fire.png",
        },
        
        {
            "name": "Fireball",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Pyromancer/Fireball.png",
        },

        {
            "name": "Scorching Aura",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Breath of Fire"],
            "image" : "Assets/Skills/Pyromancer/Scorching_Aura.png",
        },

        {
            "name": "Hydra",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Breath of Fire", "Fireball"],
            "image" : "Assets/Skills/Pyromancer/Hydra.png",
        },

        {
            "name": "Volcano",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Scorching Aura", "Breath of Fire"],
            "image" : "Assets/Skills/Pyromancer/Volcano.png",
        },
        
        {
            "name": "Meteor",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Fireball"],
            "image" : "Assets/Skills/Pyromancer/Meteor.png",
        },

        {
            "name": "Fire Nova",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Hydra", "Breath of Fire", "Fireball"],
            "image" : "Assets/Skills/Pyromancer/Fire_Nova.png",
        },

        {
            "name": "Comet",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Meteor", "Fireball"],
            "image" : "Assets/Skills/Pyromancer/Comet.png",
        },

        {
            "name": "Amageddon",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Fire Nova", "Hydra", "Breath of Fire", "Fireball"],
            "image" : "Assets/Skills/Pyromancer/Amageddon.png",
        },
    ],

    "marksman" : [

        {
            "name": "Trickshot",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Marksman/Trickshot.png",
        },

        {
            "name": "Vault",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Marksman/Vault.png",
        },

        {
            "name": "Multishot",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Trickshot"],
            "image" : "Assets/Skills/Marksman/Multishot.png",
        },

        {
            "name": "Homing Missile",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Trickshot"],
            "image" : "Assets/Skills/Marksman/Homing_Missile.png",
        },

        {
            "name": "Agility",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Vault"],
            "image" : "Assets/Skills/Marksman/Agility.png",
        },

        {
            "name": "Volatile Shot",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Homing Missle", "Trickshot"],
            "image" : "Assets/Skills/Marksman/Volatile_Shot.png",
        },
        
        {
            "name": "Arrow Rain",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Multishot", "Trickshot"],
            "image" : "Assets/Skills/Marksman/Arrow_Rain.png",
        },

        {
            "name": "Critical Accuracy",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Marksman/Critical_Accuracy.png",
        },

        {
            "name": "Arrow Rampage",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Arrow Rain", "Multishot", "Trickshot"],
            "image" : "Assets/Skills/Marksman/Arrow_Rampage.png",
        },

        {
            "name": "Frag Grenade",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Marksman/Frag_Grenade.png",
        },
        
        {
            "name": "Arrow Turret",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Marksman/Arrow_Turret.png",
        },

        {
            "name": "Landmine",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Frag Grenade"],
            "image" : "Assets/Skills/Marksman/Landmine.png",
        },

        {
            "name": "B.E.A.C.O.N",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Arrow Turret"],
            "image" : "Assets/Skills/Marksman/Beacon.png",
        },

        {
            "name": "Turret Mastery",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Arrow Turret"],
            "image" : "Assets/Skills/Marksman/Turret_Mastery.png",
        },
        
        {
            "name": "Cannon Turret",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["B.E.A.C.O.N", "Arrow Turret"],
            "image" : "Assets/Skills/Marksman/Cannon_Turret.png",
        },

        {
            "name": "Master Mechanic",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Turret Mastery", "Arrow Turret"],
            "image" : "Assets/Skills/Marksman/Master_Mechanic.png",
        },

        {
            "name": "Gunner Drone",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Master Mechanic", "Turret Mastery", "Arrow Turret"],
            "image" : "Assets/Skills/Marksman/Gunner_Drone.png",
        },

        {
            "name": "Rocket Turret",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Cannon Turret", "B.E.A.C.O.N", "Arrow Turret"],
            "image" : "Assets/Skills/Marksman/Rocket_Turret.png",
        },
    ],

    "pirate" : [

        {
            "name": "Buckshot",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Pirate/Buckshot.png",
        },

        {
            "name": "Grenade Jump",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Pirate/Grenade_Jump.png",
        },

        {
            "name": "Explosive Barrel",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Buckshot"],
            "image" : "Assets/Skills/Pirate/Explosive_Barrel.png",
        },

        {
            "name": "Cannonball",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Grenade Jump"],
            "image" : "Assets/Skills/Pirate/Cannonball.png",
        },

        {
            "name": "Explosive Bullets",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Buckshot"],
            "image" : "Assets/Skills/Pirate/Explosive_Bullets.png",
        },

        {
            "name": "Powder Trail",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Explosive Barrel", "Buckshot"],
            "image" : "Assets/Skills/Pirate/Powder_Trail.png",
        },
        
        {
            "name": "Kneecap",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Pirate/Kneecap.png",
        },

        {
            "name": "Bomb Barrage",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Cannonball", "Grenade Jump"],
            "image" : "Assets/Skills/Pirate/Bomb_Barrage.png",
        },

        {
            "name": "Rapid Fire",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Arrow Rain", "Explosive Bullets", "Buckshot"],
            "image" : "Assets/Skills/Pirate/Rapid_Fire.png",
        },

        {
            "name": "Torrent",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Pirate/Torrent.png",
        },
        
        {
            "name": "Freezing Chain Shot",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Pirate/Freezing_Chain_Shot.png",
        },

        {
            "name": "Frozen Lead",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Freezing Chain Shot"],
            "image" : "Assets/Skills/Pirate/Frozen_Lead.png",
        },

        {
            "name": "Parrot",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Pirate/Parrot.png",
        },

        {
            "name": "Set Sail",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Torrent"],
            "image" : "Assets/Skills/Pirate/Set_Sail.png",
        },
        
        {
            "name": "Remiges",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Parrot"],
            "image" : "Assets/Skills/Pirate/Remiges.png",
        },

        {
            "name": "Anchor Swing",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Set Sail", "Torrent"],
            "image" : "Assets/Skills/Pirate/Anchor_Swing.png",
        },

        {
            "name": "Treasure Hunter",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Pirate/Treasure_Hunter.png",
        },

        {
            "name": "Land Ahoy!",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Anchor Swing", "Set Sail", "Torrent"],
            "image" : "Assets/Skills/Pirate/Land_Ahoy.png",
        },
    ],

    "nomad" : [

        {
            "name": "Sand Carver",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Nomad/Sand_Carver.png",
        },

        {
            "name": "Cloud of Sand",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Nomad/Cloud_of_Sand.png",
        },

        {
            "name": "Sand Tremors",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Sand Carver"],
            "image" : "Assets/Skills/Nomad/Sand_Tremors.png",
        },

        {
            "name": "Sand Entombment",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Sand Carver"],
            "image" : "Assets/Skills/Nomad/Sand_Entombment.png",
        },

        {
            "name": "Mystic Sand",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Sandt Tremors", "Sand Carver"],
            "image" : "Assets/Skills/Nomad/Mystic_Sand.png",
        },

        {
            "name": "Sand Gush",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Cloud of Sand"],
            "image" : "Assets/Skills/Nomad/Sand_Gush.png",
        },
        
        {
            "name": "Dissipating Tornado",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Sand Gush", "Cloud of Sand"],
            "image" : "Assets/Skills/Nomad/Dissipating_Tornado.png",
        },

        {
            "name": "Oasis Aura",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Nomad/Oasis_Aura.png",
        },

        {
            "name": "Sand Vortex",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Dissipating Tornado", "Sand Gush", "Cloud of Sand"],
            "image" : "Assets/Skills/Nomad/Sand_Vortex.png",
        },

        {
            "name": "Blade Strike",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Nomad/Blade_Strike.png",
        },
        
        {
            "name": "Eye of Ra",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Nomad/Eye_of_Ra.png",
        },

        {
            "name": "Flying Scimitar",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Blade Strike"],
            "image" : "Assets/Skills/Nomad/Flying_Scimitar.png",
        },

        {
            "name": "Healing Sunrays",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Eye of Ra"],
            "image" : "Assets/Skills/Nomad/Healing_Sunrays.png",
        },

        {
            "name": "Chainslice",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Flying Scimitar", "Blade Strike"],
            "image" : "Assets/Skills/Nomad/Chainslice.png",
        },
        
        {
            "name": "Rupture",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Nomad/Rupture.png",
        },

        {
            "name": "Scimitar Charge",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Chainslice", "Flying Scimitar", "Blade Strike"],
            "image" : "Assets/Skills/Nomad/Scimitar_Charge.png",
        },

        {
            "name": "Hemorrhage",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Rupture"],
            "image" : "Assets/Skills/Nomad/Hemorrhage.png",
        },

        {
            "name": "Phantom Blade",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Chainslice", "Flying Scimitar", "Blade Strike"],
            "image" : "Assets/Skills/Nomad/Phantom_Blade.png",
        },
    ],

    "redneck" : [

        {
            "name": "Moonshine Molotov",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Redneck/Moonshine_Molotov.png",
        },

        {
            "name": "Pipe Bombs",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Redneck/Pipe_Bombs.png",
        },

        {
            "name": "Oil Spill",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Moonshine Molotov"],
            "image" : "Assets/Skills/Redneck/Oil_Spill.png",
        },

        {
            "name": "Tire Fire",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Pipe Bombs"],
            "image" : "Assets/Skills/Redneck/Tire_Fire.png",
        },

        {
            "name": "Combustible Oil",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Oil Spill", "Moonshine Molotov"],
            "image" : "Assets/Skills/Redneck/Combustible_Oil.png",
        },

        {
            "name": "Hillbilly Rage",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Redneck/Hillbilly_Rage.png",
        },
        
        {
            "name": "Spontaneous Combustion",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Combustible Oil", "Oil Spill", "Moonshine Molotiv"],
            "image" : "Assets/Skills/Redneck/Sponaneous_Combustion.png",
        },

        {
            "name": "Moonshine Madness",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Hillbilly Rage"],
            "image" : "Assets/Skills/Redneck/Moonshine_Madness.png",
        },

        {
            "name": "Pickup Raid",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Hillbilly Rage"],
            "image" : "Assets/Skills/Redneck/Pickup_Raid.png",
        },

        {
            "name": "Durable Wear",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Redneck/Durable_Wear.png",
        },
        
        {
            "name": "Chainsaw Slash",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Redneck/Chainsaw_Slash.png",
        },

        {
            "name": "Loggers Endurance",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Durable Wear"],
            "image" : "Assets/Skills/Redneck/Loggers_Endurance.png",
        },

        {
            "name": "Chainsaw Massacre",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Chainsaw Slash"],
            "image" : "Assets/Skills/Redneck/Chainsaw_Massacre.png",
        },

        {
            "name": "Experienced Logger",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Loggers Endurance", "Durable Wear"],
            "image" : "Assets/Skills/Redneck/Experienced_Logger.png",
        },
        
        {
            "name": "Revved Up",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Chainsaw Massacre", "Chainsaw Slash"],
            "image" : "Assets/Skills/Redneck/Revved_Up.png",
        },

        {
            "name": "Rogue Chainsaw",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Revved Up", "Chainsaw Massacre", "Chainsaw Slash"],
            "image" : "Assets/Skills/Redneck/Rogue_Chainsaw.png",
        },

        {
            "name": "Chainsaw Mastery",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Redneck/Chainsaw_Mastery.png",
        },

        {
            "name": "Tree Trunk Triumph",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Revved Up", "Chainsaw Massacre", "Chainsaw Slash"],
            "image" : "Assets/Skills/Redneck/Tree_Trunk_Triumph.png",
        },
    ],

    "necromancer" : [

        {
            "name": "Bone Shred",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Necromancer/Bone_Shred.png",
        },

        {
            "name": "Meat Shield",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Necromancer/Meat_Shield.png",
        },

        {
            "name": "Meat Bomb",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Meat Shield"],
            "image" : "Assets/Skills/Necromancer/Meat_Bomb.png",
        },

        {
            "name": "Poison Breath",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Necromancer/Poison_Breath.png",
        },

        {
            "name": "Bone Spear",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Bone Shred", "Meat Bomb", "Meat Shield"],
            "image" : "Assets/Skills/Necromancer/Bone_Spear.png",
        },

        {
            "name": "Corpse Explosion",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Meat Bomb", "Meat Shield"],
            "image" : "Assets/Skills/Necromancer/Corpse_Explosion.png",
        },
        
        {
            "name": "Bone Spirit",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Bone Spear", "Bone Shred", "Meat Bomb", "Meat Shield"],
            "image" : "Assets/Skills/Necromancer/Bone_Spirit.png",
        },

        {
            "name": "Cursed Ground",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Poison Breath"],
            "image" : "Assets/Skills/Necromancer/Cursed_Ground.png",
        },

        {
            "name": "Poison Nova",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Cursed Ground", "Poison Breath"],
            "image" : "Assets/Skills/Necromancer/Poison_Nova.png",
        },

        {
            "name": "Amplify Damage",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Necromancer/Amplify_Damage.png",
        },
        
        {
            "name": "Raise Skeleton",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Necromancer/Raise_Skeleton.png",
        },

        {
            "name": "Summon Mastery",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Raise Skeleton"],
            "image" : "Assets/Skills/Necromancer/Summon_Mastery.png",
        },

        {
            "name": "Raise Skeleton Mage",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Raise Skeleton"],
            "image" : "Assets/Skills/Necromancer/Raise_Skeleton_Mage.png",
        },

        {
            "name": "Life Tap",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Amplify Damage"],
            "image" : "Assets/Skills/Necromancer/Life_Tap.png",
        },
        
        {
            "name": "Summon Frenzy",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Summon Mastery", "Raise Skeleton"],
            "image" : "Assets/Skills/Necromancer/Summon_Frenzy.png",
        },

        {
            "name": "Summon Resistances",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Life Tap", "Amplify Damage", "Summon Frenzy", "Summon Mastery", "Raise Skeleton"],
            "image" : "Assets/Skills/Necromancer/Summon_Resistances.png",
        },

        {
            "name": "Summon Damned Legion",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Raise Skeleton Mage", "Raise Skeleton"],
            "image" : "Assets/Skills/Necromancer/Summon_Damned_Legion.png",
        },

        {
            "name": "Summon Vengeful Spirit",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Necromancer/Summon_Vengeful_Spirit.png",
        },
    ],

    "samurai" : [

        {
            "name": "Battle Glance",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Samurai/Battle_Glance.png",
        },

        {
            "name": "Shuriken Throw",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Samurai/Shuriken_Throw.png",
        },

        {
            "name": "Quickslash",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Battle Glance"],
            "image" : "Assets/Skills/Samurai/Quickslash.png",
        },

        {
            "name": "Evasion",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Samurai/Evasion.png",
        },

        {
            "name": "Smoke Bomb",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Evasion"],
            "image" : "Assets/Skills/Samurai/Smoke_Bomb.png",
        },

        {
            "name": "Explosive Kunai",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Shuriken Throw"],
            "image" : "Assets/Skills/Samurai/Explosive_Kunai.png",
        },
        
        {
            "name": "Warriors Spirit",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Smoke Bomb", "Evasion"],
            "image" : "Assets/Skills/Samurai/Warriors_Spirit.png",
        },

        {
            "name": "Bushido",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Samurai/Bushido.png",
        },

        {
            "name": "Live by the Sword",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Bushido"],
            "image" : "Assets/Skills/Samurai/Live_by_the_Sword.png",
        },

        {
            "name": "Blade Barrier",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Samurai/Blade_Barrier.png",
        },
        
        {
            "name": "Exploding Bolas",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Samurai/Exploding_Bolas.png",
        },

        {
            "name": "Fan of Knives",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Blade Barrier"],
            "image" : "Assets/Skills/Samurai/Fan_of_Knives.png",
        },

        {
            "name": "For Honor",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Samurai/For_Honor.png",
        },

        {
            "name": "Omnislash",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Fan of Knives", "Blade Barrier"],
            "image" : "Assets/Skills/Samurai/Omnislash.png",
        },
        
        {
            "name": "Burst of Speed",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["For Honor"],
            "image" : "Assets/Skills/Samurai/Burst_of_Speed.png",
        },

        {
            "name": "Shadow Step",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Omnislash", "Fan of Knives", "Blade Barrier"],
            "image" : "Assets/Skills/Samurai/Shadow_Step.png",
        },

        {
            "name": "Way of the Warrior",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Burst of Speed", "For Honor"],
            "image" : "Assets/Skills/Samurai/Way_of_the_Warrior.png",
        },

        {
            "name": "Empires Slash",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Omnislash", "Fan of Knives", "Blade Barrier"],
            "image" : "Assets/Skills/Samurai/Empires_Slash.png",
        },
    ],

    "paladin" : [

        {
            "name": "Vengeance",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Paladin/Vengeance.png",
        },

        {
            "name": "Thunder Shield",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Paladin/Thunder_Shield.png",
        },

        {
            "name": "Divine Storm",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Vengeance"],
            "image" : "Assets/Skills/Paladin/Divine_Storm.png",
        },

        {
            "name": "Fanaticism Aura",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Vengeance"],
            "image" : "Assets/Skills/Paladin/Fanaticism_Aura.png",
        },

        {
            "name": "Holy Shock Aura",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Paladin/Holy_Shock_Aura.png",
        },

        {
            "name": "Ball Lightning",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Paladin/Ball_Lightning.png",
        },
        
        {
            "name": "Lightning Fury",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Divine Storm", "Vengeance"],
            "image" : "Assets/Skills/Paladin/Lightning_Fury.png",
        },

        {
            "name": "Eye of the Storm",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Ball Lightning", "Holy Shock Aura"],
            "image" : "Assets/Skills/Paladin/Eye_of_the_Storm.png",
        },

        {
            "name": "Thors Fury",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Holy Shock Aura"],
            "image" : "Assets/Skills/Paladin/Thors_Fury.png",
        },

        {
            "name": "Divine Wisdom",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Paladin/Divine_Wisdom.png",
        },
        
        {
            "name": "Holy Bolt",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Paladin/Holy_Bolt.png",
        },

        {
            "name": "Lights Embrace",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Divine Wisdom"],
            "image" : "Assets/Skills/Paladin/Lights_Embrace.png",
        },

        {
            "name": "Holy Retribution",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Paladin/Holy_Retribution.png",
        },

        {
            "name": "Holy Nova",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Holy Retribution"],
            "image" : "Assets/Skills/Paladin/Holy_Nova.png",
        },
        
        {
            "name": "Holy Hammer",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Holy Bolt"],
            "image" : "Assets/Skills/Paladin/Holy_Hammer.png",
        },

        {
            "name": "Holy Aura",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Holy Nova", "Holy Retribution"],
            "image" : "Assets/Skills/Paladin/Holy_Aura.png",
        },

        {
            "name": "Fist of the Heavens",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Holy Nova", "Holy Retribution", "Holy Hammer", "Holy Bolt"],
            "image" : "Assets/Skills/Paladin/Fist_of_the_Heavens.png",
        },

        {
            "name": "The Venerated One",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Fist of the Heavens", "Holy Nova", "Holy Retribution", "Holy Hammer", "Holy Bolt"],
            "image" : "Assets/Skills/Paladin/The_Venerated_One.png",
        },
    ],

    "amazon" : [

        {
            "name": "Master Poisoner",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Amazon/Master_Poisoner.png",
        },

        {
            "name": "Noxious Strike",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Amazon/Noxious_Strike.png",
        },

        {
            "name": "Leaping Ambush",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Noxious Strike"],
            "image" : "Assets/Skills/Amazon/Leaping_Ambush.png",
        },

        {
            "name": "Caustic Spearhead",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Noxious Strike"],
            "image" : "Assets/Skills/Amazon/Caustic_Spearhead.png",
        },

        {
            "name": "Jungle Camouflage",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Master Poisoner"],
            "image" : "Assets/Skills/Amazon/Jungle_Camouflage.png",
        },

        {
            "name": "Thrill of the Hunt",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Leaping Ambush", "Noxious Strike"],
            "image" : "Assets/Skills/Amazon/Thrill_of_the_Hunt.png",
        },
        
        {
            "name": "Toxic Remains",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Jungle Camouflage", "Master Poisoner"],
            "image" : "Assets/Skills/Amazon/Toxic_Remains.png",
        },

        {
            "name": "Death from Above",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Caustic Spearhead", "Noxious Strike"],
            "image" : "Assets/Skills/Amazon/Death_from_Above.png",
        },

        {
            "name": "Envenom",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Jungle Camouflage", "Master Poisoner"],
            "image" : "Assets/Skills/Amazon/Envenom.png",
        },

        {
            "name": "Astropes Gift",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Amazon/Astropes_Gift.png",
        },
        
        {
            "name": "Feint",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Amazon/Feint.png",
        },

        {
            "name": "Chooser of the Slain",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Amazon/Chooser_of_the_Slain.png",
        },

        {
            "name": "Rebound",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Astropes Gift"],
            "image" : "Assets/Skills/Amazon/Rebound.png",
        },

        {
            "name": "Spearnage",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Rebound", "Astropes Gift"],
            "image" : "Assets/Skills/Amazon/Spearnage.png",
        },
        
        {
            "name": "Storm Dash",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Feint"],
            "image" : "Assets/Skills/Amazon/Storm_Dash.png",
        },

        {
            "name": "Thunder Fury",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Rebound", "Astropes Gift", "Storm Dash", "Feint"],
            "image" : "Assets/Skills/Amazon/Thunder_Fury.png",
        },

        {
            "name": "Thunder Goddesses Chosen",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Amazon/Thunder_Goddesses_Chosen.png",
        },

        {
            "name": "Astropes Battle Maiden",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Spearnage", "Rebound", "Astropes Gift"],
            "image" : "Assets/Skills/Amazon/Astropes_Battle_Maiden.png",
        },
    ],

    "demon_slayer" : [

        {
            "name": "Eagle Eye",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/DemonSlayer/Eagle_Eye.png",
        },

        {
            "name": "Trigger Finger",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/DemonSlayer/Trigger_Finger.png",
        },

        {
            "name": "Execute",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Trigger Finger"],
            "image" : "Assets/Skills/DemonSlayer/Execute.png",
        },

        {
            "name": "Bullet Hell",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Trigger Finger"],
            "image" : "Assets/Skills/DemonSlayer/Bullet_Hell.png",
        },

        {
            "name": "Concentration Aura",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/DemonSlayer/Concentration_Aura.png",
        },

        {
            "name": "Possessed Bullet",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Bullet Hell", "Trigger Finger"],
            "image" : "Assets/Skills/DemonSlayer/Possessed_Bullet.png",
        },
        
        {
            "name": "Shredder Trap",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/DemonSlayer/Shredder_Trap.png",
        },

        {
            "name": "Demons Presence",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Possessed Bullet", "Bullet Hell", "Trigger Finger"],
            "image" : "Assets/Skills/DemonSlayer/Demons_Presence.png",
        },

        {
            "name": "Absolute Mayhem",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Bullet Hell", "Trigger Finger"],
            "image" : "Assets/Skills/DemonSlayer/Absolute_Mayhem.png",
        },

        {
            "name": "Fast Slices",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/DemonSlayer/Fast_Slices.png",
        },
        
        {
            "name": "Heart Attack",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/DemonSlayer/Heart_Attack.png",
        },

        {
            "name": "Demons Calling",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/DemonSlayer/Demons_Calling.png",
        },

        {
            "name": "Sword Handler",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Heart Attack"],
            "image" : "Assets/Skills/DemonSlayer/Sword_Handler.png",
        },

        {
            "name": "Slice of Shadows",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Fast Slices"],
            "image" : "Assets/Skills/DemonSlayer/Slice_of_Shadows.png",
        },
        
        {
            "name": "Shadow Anomalies",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Demons Calling"],
            "image" : "Assets/Skills/DemonSlayer/Shadow_Anomalies.png",
        },

        {
            "name": "Soul Leech",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Slice of Shadows", "Fast Slices"],
            "image" : "Assets/Skills/DemonSlayer/Soul_Leech.png",
        },

        {
            "name": "Demons Shield",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/DemonSlayer/Demons_Shield.png",
        },

        {
            "name": "Demon Form",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Slice of Shadows", "Fast Slices"],
            "image" : "Assets/Skills/DemonSlayer/Demon_Form.png",
        },
    ],

    "demonspawn" : [

        {
            "name": "Bone Fragments",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/DemonSpawn/Bone_Fragments.png",
        },

        {
            "name": "Impale",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/DemonSpawn/Impale.png",
        },

        {
            "name": "Bone Storm",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Bone Fragments"],
            "image" : "Assets/Skills/DemonSpawn/Bone_Storm.png",
        },

        {
            "name": "Ossification",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/DemonSpawn/Ossification.png",
        },

        {
            "name": "Cartilage Build Up",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Bone Storm", "Bone Fragments", "Impale"],
            "image" : "Assets/Skills/DemonSpawn/Cartilage_Build_Up.png",
        },

        {
            "name": "Single Out",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/DemonSpawn/Single_Out.png",
        },
        
        {
            "name": "Spinal Tap",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Cartilage Build Up", "Bone Storm", "Bone Fragments", "Impale"],
            "image" : "Assets/Skills/DemonSpawn/Spinal_Tap.png",
        },

        {
            "name": "Ominous Aura",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/DemonSpawn/Ominous_Aura.png",
        },

        {
            "name": "Bone Barrage",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Bone Storm", "Bone Fragments"],
            "image" : "Assets/Skills/DemonSpawn/Bone_Barrage.png",
        },

        {
            "name": "Blood Bolts",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/DemonSpawn/Blood_Bolts.png",
        },
        
        {
            "name": "Manapool Aura",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/DemonSpawn/Manapool_Aura.png",
        },

        {
            "name": "Gut Spread",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Blood Bolts"],
            "image" : "Assets/Skills/DemonSpawn/Gut_Spread.png",
        },

        {
            "name": "Mana Shield",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Manapool Aura"],
            "image" : "Assets/Skills/DemonSpawn/Mana_Shield.png",
        },

        {
            "name": "Demonic Presence",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/DemonSpawn/Demonic_Presence.png",
        },
        
        {
            "name": "Mana Devour",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Mana Shield", "Manapool Aura"],
            "image" : "Assets/Skills/DemonSpawn/Mana_Devour.png",
        },

        {
            "name": "Blood Surge",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Gut Spread", "Blood Bolts"],
            "image" : "Assets/Skills/DemonSpawn/Blood_Surge.png",
        },

        {
            "name": "Blood Demons",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Demonic Presence"],
            "image" : "Assets/Skills/DemonSpawn/Blood_Demons.png",
        },

        {
            "name": "Blood Tendrils",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Blood Surge", "Gut Spread", "Blood Bolts"], 
            "image" : "Assets/Skills/DemonSpawn/Blood_Tendrils.png",
        },
    ],

    

    "shaman" : [

        {
            "name": "Tectonic Boulder",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Shaman/Tectonic_Boulder.png",
        },

        {
            "name": "Twisters",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Shaman/Twisters.png",
        },

        {
            "name": "Rock Fragments",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Tectonic Boulder"],
            "image" : "Assets/Skills/Shaman/Rock_Fragments.png",
        },

        {
            "name": "Earth Bind",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Tectonic Boulder"],
            "image" : "Assets/Skills/Shaman/Earth_Bind.png",
        },

        {
            "name": "Meteor Storm",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Rock Fragments", "Tectonic Boulder"],
            "image" : "Assets/Skills/Shaman/Meteor_Storm.png",
        },

        {
            "name": "Tornado",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Twisters"],
            "image" : "Assets/Skills/Shaman/Tornado.png",
        },
        
        {
            "name": "Earths Grace",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Meteor Storm", "Rock Fragments", "Tectonic Boulder"],
            "image" : "Assets/Skills/Shaman/Earths_Grace.png",
        },

        {
            "name": "Natures Prophet",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Shaman/Natures_Prophet.png",
        },

        {
            "name": "Fissures",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Meteor Storm", "Rock Fragments", "Tectonic Boulder"],
            "image" : "Assets/Skills/Shaman/Fissures.png",
        },

        {
            "name": "Earth Totem",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Shaman/Earth_Totem.png",
        },
        
        {
            "name": "Spiritual Guide",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Shaman/Spiritual_Guide.png",
        },

        {
            "name": "Fractal Mind",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Spiritual Guide"],
            "image" : "Assets/Skills/Shaman/Fractal_Mind.png",
        },

        {
            "name": "Spirit Wolves",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Shaman/Spirit_Wolves.png",
        },

        {
            "name": "Storm Totem",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Earth Totem"],
            "image" : "Assets/Skills/Shaman/Storm_Totem.png",
        },
        
        {
            "name": "Scent of the Wolf",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Spirit Wolves"],
            "image" : "Assets/Skills/Shaman/Scent_of_the_Wolf.png",
        },

        {
            "name": "Fire Totem",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Storm Totem", "Earth Totem"],
            "image" : "Assets/Skills/Shaman/Fire_Totem.png",
        },

        {
            "name": "Astral Intellect",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Storm Totem", "Earth Totem"],
            "image" : "Assets/Skills/Shaman/Astral_Intellect.png",
        },

        {
            "name": "Chaos Totem",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Fire Totem", "Storm Totem", "Earth Totem"],
            "image" : "Assets/Skills/Shaman/Chaos_Totem.png",
        },
    ],

    "white_mage" : [

        {
            "name": "Martyr",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/White_Mage/Martyr.png",
        },

        {
            "name": "Shadow Bolt",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/White_Mage/Shadow_Bolt.png",
        },

        {
            "name": "Digest Souls",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Martyr"],
            "image" : "Assets/Skills/White_Mage/Digest_Souls.png",
        },

        {
            "name": "Soul Spurn",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Shadow Bolt"],
            "image" : "Assets/Skills/White_Mage/Soul_Spurn.png",
        },

        {
            "name": "Restless Spirits",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Digest Souls", "Martyr"],
            "image" : "Assets/Skills/White_Mage/Restless_Spirits.png",
        },

        {
            "name": "Dark Oath",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Soul Spurn", "Shadow Bolt"],
            "image" : "Assets/Skills/White_Mage/Dark_Oath.png",
        },
        
        {
            "name": "Satans Mark",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Restless Spirits", "Digest Souls", "Martyr"],
            "image" : "Assets/Skills/White_Mage/Satans_Mark.png",
        },

        {
            "name": "Malediction",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/White_Mage/Malediction.png",
        },

        {
            "name": "Black Mass",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/White_Mage/Black_Mass.png",
        },

        {
            "name": "Heavenly Fire",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/White_Mage/Heavenly_Fire.png",
        },
        
        {
            "name": "Flash Heal",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/White_Mage/Flash_Heal.png",
        },

        {
            "name": "Burst of Light",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Heavenly Fire"],
            "image" : "Assets/Skills/White_Mage/Burst_of_Light.png",
        },

        {
            "name": "Divine Healing",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Flash Heal"],
            "image" : "Assets/Skills/White_Mage/Divine_Healing.png",
        },

        {
            "name": "Chain of Holy Lightning",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Burst of Light" "Heavenly Fire"],
            "image" : "Assets/Skills/White_Mage/Chain_of_Holy_Lightning.png",
        },
        
        {
            "name": "Holy Shield",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Flash Heal"],
            "image" : "Assets/Skills/White_Mage/Holy_Shield.png",
        },

        {
            "name": "Benediction",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Divine Healing" "Flash Heal"],
            "image" : "Assets/Skills/White_Mage/Benediction.png",
        },

        {
            "name": "Healing Zone",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Holy Shield" "Flash Heal"],
            "image" : "Assets/Skills/White_Mage/Healing_Zone.png",
        },

        {
            "name": "Mana Orb",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/White_Mage/Mana_Orb.png",
        },
    ],

    "marauder" : [

        {
            "name": "Bouncing Grenade",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Marauder/Bouncing_Grenade.png",
        },

        {
            "name": "Heavy Ball",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Marauder/Heavy_Ball.png",
        },

        {
            "name": "The Big Bo-oM",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Bouncing Grenade"],
            "image" : "Assets/Skills/Marauder/The_Big_Bo-oM.png",
        },

        {
            "name": "Crazy Grapple",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Heavy Ball"],
            "image" : "Assets/Skills/Marauder/Crazy_Grapple.png",
        },

        {
            "name": "Unstable Bomb",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["The Big Bo-oM", "Bouncing Grenade"],
            "image" : "Assets/Skills/Marauder/Unstable_Bomb.png",
        },

        {
            "name": "Wrecking Ball",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Heavy Ball"],
            "image" : "Assets/Skills/Marauder/Wrecking_Ball.png",
        },
        
        {
            "name": "Force Overwhelming",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Wrecking Ball", "Heavy Ball"],
            "image" : "Assets/Skills/Marauder/Force_Overwhelming.png",
        },

        {
            "name": "Flail Mastery",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Marauder/Flail_Mastery.png",
        },

        {
            "name": "Bombardment",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : "The Big Bo-oM" "Bouncing Grenade",
            "image" : "Assets/Skills/Marauder/Bombardment.png",
        },

        {
            "name": "Serrated Chains",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Marauder/Serrated_Chains.png",
        },
        
        {
            "name": "Rend Flesh",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Marauder/Rend_Flesh.png",
        },

        {
            "name": "Titanium Chains",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Serrated Chains", "Rend Flesh"],
            "image" : "Assets/Skills/Marauder/Titanium_Chains.png",
        },

        {
            "name": "Retiarius Net",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Marauder/Retiarius_Net.png",
        },

        {
            "name": "Resilient Gladiator",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Marauder/Resilient_Gladiator.png",
        },
        
        {
            "name": "Chain Trap",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Retiarius Net"],
            "image" : "Assets/Skills/Marauder/Chain_Trap.png",
        },

        {
            "name": "Annihilation",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Serrated Chains"],
            "image" : "Assets/Skills/Marauder/Annihilation.png",
        },

        {
            "name": "Master Trap Maker",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Chain Trap", "RetiariusNet"],
            "image" : "Assets/Skills/Marauder/Master_Trap_Maker.png",
        },

        {
            "name": "Madness Control",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Chain Trap", "Retiarius Net"],
            "image" : "Assets/Skills/Marauder/Madness_Control.png",
        },
    ],

    "plague_doctor" : [

        {
            "name": "Miasma",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Plague_Doctor/Miasma.png",
        },

        {
            "name": "Surgical Blood Letting",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Plague_Doctor/Surgical_Blood_Letting.png",
        },

        {
            "name": "Booster Shot",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Miasma"],
            "image" : "Assets/Skills/Plague_Doctor/Booster_Shot.png",
        },

        {
            "name": "Malpractice",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Surgical_Blood_Letting"],
            "image" : "Assets/Skills/Plague_Doctor/Malpractice.png",
        },

        {
            "name": "Blood Sustenance",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Booster Shot", "Miasma", "Malpractice", "Surgical Blood Letting"],
            "image" : "Assets/Skills/Plague_Doctor/Blood_Sustenance.png",
        },

        {
            "name": "Lifeblood Aura",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Plague_Doctor/Lifeblood_Aura.png",
        },
        
        {
            "name": "Crow Masks Presence",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Plague_Doctor/Crow_Masks_Presence.png",
        },

        {
            "name": "Devout Doctor",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Lifeblood Aura"],
            "image" : "Assets/Skills/Plague_Doctor/Devout_Doctor.png",
        },

        {
            "name": "Defunct Surgeon",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Devout Doctor", "Lifeblood Aura"],
            "image" : "Assets/Skills/Plague_Doctor/Defunct_Surgeon.png",
        },

        {
            "name": "Toxic Flask",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Plague_Doctor/Toxic_Flask.png",
        },
        
        {
            "name": "Crematus",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Plague_Doctor/Crematus.png",
        },

        {
            "name": "Plague of Rats",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Plague_Doctor/Plague_of_Rats.png",
        },

        {
            "name": "Oops",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Toxic Flask"],
            "image" : "Assets/Skills/Plague_Doctor/Oops.png",
        },

        {
            "name": "Exploding Mice",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Plague of Rats"],
            "image" : "Assets/Skills/Plague_Doctor/Exploding_Mice.png",
        },
        
        {
            "name": "Plague Master",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Oops", "Toxic Flask"],
            "image" : "Assets/Skills/Plague_Doctor/Plague_Master.png",
        },

        {
            "name": "Jar of Leeches",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Plague of Rats"],
            "image" : "Assets/Skills/Plague_Doctor/Jar_of_Leeches.png",
        },

        {
            "name": "Chant of Weakness",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Plague_Doctor/Chant_of_Weakness.png",
        },

        {
            "name": "Randy the Rancid Rat",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Jar of Leeches", "Plague of Rats"],
            "image" : "Assets/Skills/Plague_Doctor/Randy_the_Rancid_Rat.png",
        },
    ],

    "shield_lancer" : [

        {
            "name": "Glorious Strike",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Shield_Lancer/Glorious_Strike.png",
        },

        {
            "name": "Battle Charge",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Shield_Lancer/Battle_Charge.png",
        },

        {
            "name": "Commending Banner",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Glorious Strike"],
            "image" : "Assets/Skills/Shield_Lancer/Commending_Banner.png",
        },

        {
            "name": "Parry",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Shield_Lancer/Parry.png",
        },

        {
            "name": "Crushing Lance",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Shield_Lancer/Crushing_Lance.png",
        },

        {
            "name": "Lance Thrust",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Commending Banner", "Glorious Strike"],
            "image" : "Assets/Skills/Shield_Lancer/Lance_Thrust.png",
        },
        
        {
            "name": "Lance Throw",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Crushing Lance"],
            "image" : "Assets/Skills/Shield_Lancer/Lance_Throw.png",
        },

        {
            "name": "Armor Crush",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Battle Charge"],
            "image" : "Assets/Skills/Shield_Lancer/Armor_Crush.png",
        },

        {
            "name": "Glory",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Lance Throw", "Crushing Lance"],
            "image" : "Assets/Skills/Shield_Lancer/Glory.png",
        },

        {
            "name": "Shield Slam",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Shield_Lancer/Shield_Slam.png",
        },
        
        {
            "name": "Taunt",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Shield_Lancer/Taunt.png",
        },

        {
            "name": "Honed Defenses",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Shield Slam"],
            "image" : "Assets/Skills/Shield_Lancer/Honed_Defenses.png",
        },

        {
            "name": "Knights Resilience",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Shield_Lancer/Knights_Resilience.png",
        },

        {
            "name": "Shield Wall",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : "Honed Defenses" "Shield Slam",
            "image" : "Assets/Skills/Shield_Lancer/Shield_Wall.png",
        },
        
        {
            "name": "Damage Reflect",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Shield_Lancer/Damage_Reflect.png",
        },

        {
            "name": "Spiked Shields",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Shield Wall", "Honed Defenses", "Shield Slam", "Damage Reflect"],
            "image" : "Assets/Skills/Shield_Lancer/Spiked_Shields.png",
        },

        {
            "name": "Counter",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Damage Reflect" "Taunt"],
            "image" : "Assets/Skills/Shield_Lancer/Counter.png",
        },

        {
            "name": "Last Stand",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Spiked Shields", "Shield Wall", "Honed Defenses", "Shield Slam", "Damage Reflect"],
            "image" : "Assets/Skills/Shield_Lancer/Last_Stand.png",
        },
    ],

    "jötunn" : [

        {
            "name": "Frozen Boulder",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Jötunn/Frozen_Boulder.png",
        },

        {
            "name": "Breath of Ice",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Jötunn/Breath_of_Ice.png",
        },

        {
            "name": "Icicles",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Frozen Boulder"],
            "image" : "Assets/Skills/Jötunn/Icicles.png",
        },

        {
            "name": "Frozen Hide",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Breath of Ice"],
            "image" : "Assets/Skills/Jötunn/Frozen_Hide.png",
        },

        {
            "name": "Orb of Frost",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Icicles", "Frozen Boulder"],
            "image" : "Assets/Skills/Jötunn/Orb_of_Frost.png",
        },

        {
            "name": "Power of the Ancients",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Jötunn/Power_of_the_Ancients.png",
        },
        
        {
            "name": "Portal of Ice",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Icicles", "Frozen Boulder"],
            "image" : "Assets/Skills/Jötunn/Portal_of_Ice.png",
        },

        {
            "name": "Avatar of Frost",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Power of the Ancients"],
            "image" : "Assets/Skills/Jötunn/Avatar_of_Frost.png",
        },

        {
            "name": "Blizzard",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Orb of Frost", " Icicles", "Frozen Boulder"],
            "image" : "Assets/Skills/Jötunn/Blizzard.png",
        },

        {
            "name": "Flash Freeze",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Jötunn/Flash_Freeze.png",
        },
        
        {
            "name": "Glacial Tremors",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Jötunn/Glacial_Tremors.png",
        },

        {
            "name": "Freezing Leap",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Flash Freeze"],
            "image" : "Assets/Skills/Jötunn/Freezing_Leap.png",
        },

        {
            "name": "Permafrost",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Flash Freeze"],
            "image" : "Assets/Skills/Jötunn/Permafrost.png",
        },

        {
            "name": "Avalanche",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Freezing Leap", "Flash Freeze"],
            "image" : "Assets/Skills/Jötunn/Avalanche.png",
        },
        
        {
            "name": "Absolute Zero",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Glacial Tremors"],
            "image" : "Assets/Skills/Jötunn/Absolute_Zero.png",
        },

        {
            "name": "Sweep Freeze",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Freezing Leap", "Flash Freeze"],
            "image" : "Assets/Skills/Jötunn/Sweep_Freeze.png",
        },

        {
            "name": "Glacial Armor",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Absolute Zero", "Glacial Tremors"],
            "image" : "Assets/Skills/Jötunn/Glacial_Armor.png",
        },

        {
            "name": "The Embodiment of Aurgelmir",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" :["Avalanche", "Freezing Leap", "Flash Freeze"],
            "image" : "Assets/Skills/Jötunn/The_Embodiment_of_Aurgelmir.png",
        },
    ],

    "illusionist" : [

        {
            "name": "Sand Guardians",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Illusionist/Sand_Guardians.png",
        },

        {
            "name": "Call For War",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Illusionist/Call_For_War.png",
        },

        {
            "name": "Piercing Sand",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Call For War"],
            "image" : "Assets/Skills/Illusionist/Piercing_Sand.png",
        },

        {
            "name": "Link of Sand",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Call For War"],
            "image" : "Assets/Skills/Illusionist/Link_of_Sand.png",
        },

        {
            "name": "Circle of Guardians",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Sand Guardians"],
            "image" : "Assets/Skills/Illusionist/Circle_of_Guardians.png",
        },

        {
            "name": "Dissipation",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Piercing Sand", "Call For War"],
            "image" : "Assets/Skills/Illusionist/Dissipation.png",
        },
        
        {
            "name": "Cheapshot",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Circle of Guardians", "Sand Guardians", "Dissipation", "Piercing Sand", "Call For War"],
            "image" : "Assets/Skills/Illusionist/Cheapshot.png",
        },

        {
            "name": "Spirit Link",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Link of Sand", "Call For War"],
            "image" : "Assets/Skills/Illusionist/Spirit_Link.png",
        },

        {
            "name": "Combat Order",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Circle of Guardians", "Sand Guardians"],
            "image" : "Assets/Skills/Illusionist/Combat_Order.png",
        },

        {
            "name": "Age Proliferation",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Illusionist/Age_Proliferation.png",
        },
        
        {
            "name": "Gravitation Slam",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Illusionist/Gravitation_Slam.png",
        },

        {
            "name": "Split Reality",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Illusionist/Split_Reality.png",
        },

        {
            "name": "Time Deceleration",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Gravitation Slam"],
            "image" : "Assets/Skills/Illusionist/Time_Deceleration.png",
        },

        {
            "name": "Dimensional Displacement",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Age Proliferation"],
            "image" : "Assets/Skills/Illusionist/Dimensional_Displacement.png",
        },
        
        {
            "name": "Sands of Time",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Split Reality"],
            "image" : "Assets/Skills/Illusionist/Sands_of_Time.png",
        },

        {
            "name": "Expansive Mind",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Sands of Time", "Split Reality"],
            "image" : "Assets/Skills/Illusionist/Expansive_Mind.png",
        },

        {
            "name": "Precognition",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Sands of Time", "Split Reality", "Time Deceleration", "Gravitation Slam"],
            "image" : "Assets/Skills/Illusionist/Precognition.png",
        },

        {
            "name": "Temporal Heroes",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Illusionist/Temporal_Heroes.png",
        },
    ],

    "exo" : [

        {
            "name": "Scorching Whip",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Exo/Scorching_Whip.png",
        },

        {
            "name": "Solar Flare",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Exo/Solar_Flare.png",
        },

        {
            "name": "Whiplash",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Scorching Whip"],
            "image" : "Assets/Skills/Exo/Whiplash.png",
        },

        {
            "name": "Solar Dash",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Solar Flare"],
            "image" : "Assets/Skills/Exo/Solar_Dash.png",
        },

        {
            "name": "Shine Bright",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Exo/Shine_Bright.png",
        },

        {
            "name": "Solar Form",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Solar Dash", "Solar Flare"],
            "image" : "Assets/Skills/Exo/Solar_Form.png",
        },
        
        {
            "name": "Blinding Light",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Shine Bright"],
            "image" : "Assets/Skills/Exo/Blinding_Light.png",
        },

        {
            "name": "Solar Burst",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Solar Form", "Solar Dash", "Solar Flare"],
            "image" : "Assets/Skills/Exo/Solar_Burst.png",
        },

        {
            "name": "Supernova",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Solar Burst", "Solar Form", "Solar Dash", "Solar Flare"],
            "image" : "Assets/Skills/Exo/Supernova.png",
        },

        {
            "name": "Collision",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Exo/Collision.png",
        },
        
        {
            "name": "Tsunami",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Exo/Tsunami.png",
        },

        {
            "name": "Dark Side of the Moon",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Exo/Dark_Side_of_the_Moon.png",
        },

        {
            "name": "Asteroid",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Tsunami"],
            "image" : "Assets/Skills/Exo/Asteroid.png",
        },

        {
            "name": "Lunar Form",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Collision"],
            "image" : "Assets/Skills/Exo/Lunar_Form.png",
        },
        
        {
            "name": "Lunar Orbit",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Asteroid", "Tsunami"],
            "image" : "Assets/Skills/Exo/Lunar_Orbit.png",
        },

        {
            "name": "Moonlight",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Exo/Moonlight.png",
        },

        {
            "name": "Blood Moon",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Lunar Orbit", "Asteroid", "Tsunami"],
            "image" : "Assets/Skills/Exo/Blood_Moon.png",
        },

        {
            "name": "Black Hole",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Lunar Orbit", "Asteroid", "Tsunami"],
            "image" : "Assets/Skills/Exo/Black_Hole.png",
        },
    ],

    "butcher" : [

        {
            "name": "Slicing Throw",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Butcher/Slicing_Throw.png",
        },

        {
            "name": "Furious Strike",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Butcher/Furious_Strike.png",
        },

        {
            "name": "Holy Form",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Butcher/Holy_Form.png",
        },

        {
            "name": "Unholy Form",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Butcher/Unholy_Form.png",
        },

        {
            "name": "Sacrilegious Scorn",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Holy Form"],
            "image" : "Assets/Skills/Butcher/Sacrilegious_Scorn.png",
        },

        {
            "name": "Ending Fate",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Holy Form", "Unholy Form"],
            "image" : "Assets/Skills/Butcher/Ending_Fate.png",
        },
        
        {
            "name": "Spiritual Duality",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Sacrilegious Scorn", "Holy Form"],
            "image" : "Assets/Skills/Butcher/Spiritual_Duality.png",
        },

        {
            "name": "Awakening Fury",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Ending Fate", "Holy Form", "Unholy Form"],
            "image" : "Assets/Skills/Butcher/Awakening_Fury.png",
        },

        {
            "name": "Insatiable Hunger",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Awakening Fury", "Ending Fate", "Holy Form", "Unholy Form"],
            "image" : "Assets/Skills/Butcher/Insatiable_Hunger.png",
        },

        {
            "name": "Chain Rip",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Butcher/Chain_Rip.png",
        },
        
        {
            "name": "Brutalizing Slash",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Butcher/Brutalizing_Slash.png",
        },

        {
            "name": "Fuel to Fire",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Butcher/Fuel_to_Fire.png",
        },

        {
            "name": "Hunger For Blood",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Brutalizing Slash"],
            "image" : "Assets/Skills/Butcher/Hunger_For_Blood.png",
        },

        {
            "name": "Butchers Hook",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Chain Rip"],
            "image" : "Assets/Skills/Butcher/Butchers_Hook.png",
        },
        
        {
            "name": "Chain Swing",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Butchers Hook", "Chain Rip"],
            "image" : "Assets/Skills/Butcher/Chain_Swing.png",
        },

        {
            "name": "Submerged Knives",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Butcher/Submerged_Knives.png",
        },

        {
            "name": "Enraged Mania",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Hunger For Blood", "Brutalizing Slash"],
            "image" : "Assets/Skills/Butcher/Enraged_Mania.png",
        },

        {
            "name": "Blender",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Chain Swing"],
            "image" : "Assets/Skills/Butcher/Blender.png",
        },
    ],

    "stormweaver" : [

        {
            "name": "Charged Bolts",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Stormweaver/Charged_Bolts.png",
        },

        {
            "name": "Manafiend",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Stormweaver/Manafiend.png",
        },

        {
            "name": "Pulsing Charge",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Charged Bolts"],
            "image" : "Assets/Skills/Stormweaver/Pulsing_Charge.png",
        },

        {
            "name": "Lightning Surge",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Stormweaver/Lightning_Surge.png",
        },

        {
            "name": "Gateway",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Stormweaver/Gateway.png",
        },

        {
            "name": "Chain Lightning",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Lightning Surge"],
            "image" : "Assets/Skills/Stormweaver/Chain_Lightning.png",
        },
        
        {
            "name": "Static Shock",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Stormweaver/Static_Shock.png",
        },

        {
            "name": "Storm Cloud",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Stormweaver/Storm_Cloud.png",
        },

        {
            "name": "Symphony of Thunder",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Stormweaver/Symphony_of_Thunder.png",
        },

        {
            "name": "Electric Cells",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Stormweaver/Electric_Cells.png",
        },
        
        {
            "name": "Storm Bolt",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Stormweaver/Storm_Bolt.png",
        },

        {
            "name": "High Voltage Aura",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Stormweaver/High_Voltage_Aura.png",
        },

        {
            "name": "Loaded Pulse",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Stormweaver/Loaded_Pulse.png",
        },

        {
            "name": "Wave Length",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Stormweaver/Wave_Length.png",
        },
        
        {
            "name": "The Battery Within",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Stormweaver/The_Battery_Within.png",
        },

        {
            "name": "Hyper Charged",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Stormweaver/Hyper_Charged.png",
        },

        {
            "name": "Apocalyptic Thunder",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Loaded Pulse", "Storm Bolt"],
            "image" : "Assets/Skills/Stormweaver/Apocalyptic_Thunder.png",
        },

        {
            "name": "Aftershock",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Apocalyptic Thunder", "Loaded Pulse", "Storm Bolt"],
            "image" : "Assets/Skills/Stormweaver/Aftershock.png",
        },
    ],
    
    "bard" : [

        {
            "name": "Headbanger",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Bard/Headbanger.png",
        },

        {
            "name": "Crowd Pummeler",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Bard/Crowd_Pummeler.png",
        },

        {
            "name": "Crowd Dive",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Headbanger"],
            "image" : "Assets/Skills/Bard/Crowd_Dive.png",
        },

        {
            "name": "Adrenaline Momentum",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Crowd Pummeler"],
            "image" : "Assets/Skills/Bard/Adrenaline_Momentum.png",
        },

        {
            "name": "Antisocial Pit Fighter",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Headbanger"],
            "image" : "Assets/Skills/Bard/Antisocial_Pit_Fighter.png",
        },

        {
            "name": "Pyro Technician",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Headbanger", "Crowd Dive"],
            "image" : "Assets/Skills/Bard/Pyro_Technician.png",
        },
        
        {
            "name": "Craving For Attention",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Headbanger", "Crowd Dive", "Pyro Technician"],
            "image" : "Assets/Skills/Bard/Craving_For_Attention.png",
        },

        {
            "name": "Craving For Another Killing",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Headbanger", "Antisocial Pit Fighter"],
            "image" : "Assets/Skills/Bard/Craving_For_Another_Killing.png",
        },

        {
            "name": "Moshpit Massacre",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Headbanger", "Antisocial Pit Fighter", "Craving For Another Killing"],
            "image" : "Assets/Skills/Bard/Moshpit_Massacre.png",
        },

        {
            "name": "Insane Riff",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Bard/Insane_Riff.png",
        },
        
        {
            "name": "Slaying Riffs",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Bard/Slaying_Riffs.png",
        },

        {
            "name": "Amping Up",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Bard/Amping_Up.png",
        },

        {
            "name": "Visceral Growl",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Slaying Riffs"],
            "image" : "Assets/Skills/Bard/Visceral_Growl.png",
        },

        {
            "name": "Sacrilegious Symphony",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Bard/Sacrilegious_Symphony.png",
        },
        
        {
            "name": "Satans Melody",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Amping Up"],
            "image" : "Assets/Skills/Bard/Satans_Melody.png",
        },

        {
            "name": "High DB",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Amping Up", "Satans Melody"],
            "image" : "Assets/Skills/Bard/High_DB.png",
        },

        {
            "name": "Sound of Silence",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Bard/Sound_of_Silence.png",
        },

        {
            "name": "Progenies of the Great Cataclysm",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Amping Up", "Satans Melody", "High DB"],
            "image" : "Assets/Skills/Bard/Progenies_of_the_Great_Cataclysm.png",
        },
    ],

    "prophet" : [

        {
            "name": "Spirit of the Wendigo",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Prophet/Spirit_of_the_Wendigo.png",
        },

        {
            "name": "Wounding Paw",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Prophet/Wounding_Paw.png",
        },

        {
            "name": "Leaping Charge",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Wounding Paw"],
            "image" : "Assets/Skills/Prophet/Leaping_Charge.png",
        },

        {
            "name": "Skinwalker",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Spirit of the Wendigo"],
            "image" : "Assets/Skills/Prophet/Skinwalker.png",
        },

        {
            "name": "Spirit of the Ent",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Spirit of the Wendigo"],
            "image" : "Assets/Skills/Prophet/Spirit_of_the_Ent.png",
        },

        {
            "name": "Maelstrom of Frost",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Spirit of the Wendigo", "Skinwalker"],
            "image" : "Assets/Skills/Prophet/Maelstrom_of_Frost.png",
        },
        
        {
            "name": "Swamps Essence",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Spirit of the Wendigo", "Spirit of the Ent"],
            "image" : "Assets/Skills/Prophet/Swamps_Essence.png",
        },

        {
            "name": "Manadwelling",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Spirit of the Wendigo", "Skinwalker", "Maelstrom of Frost"],
            "image" : "Assets/Skills/Prophet/Manadwelling.png",
        },

        {
            "name": "Storm Hawk",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Spirit of the Wendigo", "Spirit of the Ent", "Swamps Essence"],
            "image" : "Assets/Skills/Prophet/Storm_Hawk.png",
        },

        {
            "name": "Carrion Worm",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Prophet/Carrion_Worm.png",
        },
        
        {
            "name": "Thorned Roots",
            "unlockLevel": 0,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Prophet/Thorned_Roots.png",
        },

        {
            "name": "Summon Raven",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Carrion Worm"],
            "image" : "Assets/Skills/Prophet/Summon_Raven.png",
        },

        {
            "name": "Blessed Nature",
            "unlockLevel": 8,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Prophet/Blessed_Nature.png",
        },

        {
            "name": "Summon Ent",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Prophet/Summon_Ent.png",
        },
        
        {
            "name": "Thorned Branch",
            "unlockLevel": 16,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Blessed Nature"],
            "image" : "Assets/Skills/Prophet/Thorned_Branch.png",
        },

        {
            "name": "Summon Spirit of the Forest",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : [],
            "image" : "Assets/Skills/Prophet/Summon_Spirit_of_the_Forest.png",
        },

        {
            "name": "Deep Rooted",
            "unlockLevel": 24,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Blessed Nature", "Deep Rooted"],
            "image" : "Assets/Skills/Prophet/Deep_Rooted.png",
        },

        {
            "name": "Summon Ent Colossus",
            "unlockLevel": 30,
            "currentLevel": 0,
            "maxLevel": 20,
            "requirements" : ["Blessed Nature", "Deep Rooted", "Deep Rooted"],
            "image" : "Assets/Skills/Prophet/Summon Ent Colossus.png",
        },
    ],
}

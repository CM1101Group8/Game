def on_kill_enemy_kirill(player, locations):
	"""This function is called when the player kills Kirill. It changes the
	description of the Cliffs to reflect this.
	"""
	locations["Cliffs"]["description"] = locations["Cliffs"]["description_killed"]

enemy_kirill = {
	"id": "kirill",

	"name": "Crazed Kirill",

	"description": """A wild man driven mad by his time on the island
the peeling name tag on his chest says 'Kirill' but his
burger based clothing offers little insight into the man
he used to be""",

	"vuln": "machete",

	"on_kill": on_kill_enemy_kirill
}

def on_kill_enemy_wolf(player, locations):
	"""This function is called when the player kills the Wolf. It changes the
	description of the Lair to reflect this.
	"""
	locations["Lair"]["description"] = locations["Lair"]["description_killed"]

enemy_wolf = {
	"id": "wolf",

	"name": "Savage Wolf",

	"description": """A snarling grey wolf, born and bred on the island.
you can see its sinewy muscle shift under it's skin with
every movement, perfectly developed to hunt its prey,
perfectly formed to hunt you...""",

	"vuln": "loadedgun",

	"on_kill": on_kill_enemy_wolf
}

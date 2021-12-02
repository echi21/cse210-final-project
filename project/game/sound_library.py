import arcade


class SoundLibrary:

    def __init__(self):

        # Load your background music and sound effects
        self.ambience = arcade.load_sound("game/sound_effects/ambience_sound.wav")
        self.collision = arcade.load_sound("game/sound_effects/scream_explosion.wav")
        self.goal = arcade.load_sound("game/sound_effects/goal_reaction.wav")
        self.fatigue = arcade.load_sound("game/sound_effects/walking_breath.wav")
        self.intro = arcade.load_sound("game/sound_effects/game_introduction.wav")
        self.headline = arcade.load_sound("game/sound_effects/headline_changes.wav")
        self.scream = arcade.load_sound("game/sound_effects/monster_scream.wav")

    def get_ambience(self):
        return self.ambience

    def get_collision(self):
        return self.collision

    def get_goal(self):
        return self.goal

    def get_fatigue(self):
        return self.fatigue

    def get_intro(self):
        return self.intro

    def get_headhline(self):
        return self.headline

    def get_scream(self):
        return self.scream

from Options import Choice, Toggle, DefaultOnToggle, Range, OptionList, DeathLink, \
    PlandoConnections, PerGameCommonOptions
from dataclasses import dataclass


class WSRPlandoConnections(PlandoConnections):
    # TODO
    pass


class StampGoal(Range):
    """Number of stamps required to finish the game"""
    display_name = "Stamp Goal"
    range_start = 0
    range_end = 100
    default = 50


class ChampionGoal(Range):
    """Number of champions required to finish the game"""
    display_name = "Champion Goal"
    range_start = 0
    range_end = 4
    default = 0


class ProStatusGoal(Range):
    """Number of sports needed to get Pro Status in to finish the game"""
    display_name = "Pro Status Goal"
    range_start = 0
    range_start = 20
    default = 0


class Traps(Toggle):
    """Replaces some junk items with traps like losing skill points"""
    display_name = "Include Traps"


class StartingItems(OptionList):
    """Start with these items. Every entry needs to be in a specific format.

    example:
    ```
    starting_items: [
        { "item": "wsr:cycling-heart", amount: 2 }   
        { "item": "wsr:cycling-drafting" } 
    ]    
    ```
    `item` can include components and should be in the same format as the `/give` command without the quotes.

    `amount` is optional and will default to 1 if omitted.

    """
    display_name = "Starting Items"


class SportsUnlockState(Choice):
    """Modifies how sports are unlocked. `Unlock Categories` will unlock each of the 12 categories of sports at a time. For instance, unlocking Frisbee will unlock both Frisbee Dog and Frisbee Golf. `Unlock Sports` will unlock each individual sport at a time (such that swordplay-showdown and swordplay-duel are different sports to unlock)."""
    display_name = "Sports Unlock Type"
    option_categories_unlock = 0
    option_sports_unlock = 1


class IncludeHardStamps(Toggle):
    """Enables stamps that are deemed too difficult for casual players such as `Ace of Clubs` and `Pure Shooter`"""
    display_name = "Include Hard Stamps"


class IncludeLongStamps(Toggle):
    """""Enables stamps that are deemed too long to complete in a reasonable amount of times such as `Hoop Hero` and `Balloonatic`"""
    display_name = "Include Long Stamps"


class ExcludedStamps(OptionList):
    """Exclude stamps from being in logic. Every entry needs to be in a specific format.

    example:
    ```
    excluded_stamps: [
        { "item": "wsr:stamp-Sharpshooter"}   
    ]    
    ```
    `item` can include components and should be in the same format as the `/give` command without the quotes.

    `amount` is optional and will default to 1 if omitted. Any value higher than 1 will not generate properly.

    """


class MusicShuffle(Choice):
    # WRITE DESCRIPTION PLEASE!!!
    display_name = "Music Shuffle"
    option_none = 0
    option_on = 1
    default = 0


class SFXShuffle(Choice):
    # WRITE DESCRIPTION PLEASE!!!
    display_name = "Sound Effects Shuffle"
    option_none = 0
    option_on = 1
    default = 0


class MiiShuffle(Choice):
    # WRITE DESCRIPTION PLEASE!!!
    display_name = "Mii Shuffle"
    option_none = 0
    option_on = 1
    default = 0


class ChampionShuffle(Choice):
    # WRITE DESCRIPTION PLEASE!!!
    display_name = "Champion Shuffle"
    option_none = 0
    option_on = 1
    default = 0


class TextShuffle(Choice):
    # WRITE DESCRIPTION PLEASE!!!
    display_name = "Text Shuffle"
    option_none = 0
    option_on = 1
    default = 0


class TextureShuffle(Choice):
    # WRITE DESCRIPTION PLEASE!!!
    display_name = "Texture Shuffle"
    option_none = 0
    option_on = 1
    default = 0


class WaterColorShuffle(Choice):
    # WRITE DESCRIPTION PLEASE!!!
    display_name = "Water Color Shuffle"
    option_none = 0
    option_on = 1
    default = 0


class BowlingBallColorShuffle(Choice):
    # WRITE DESCRIPTION PLEASE!!!
    display_name = "Bowling Ball Color Shuffle"
    option_none = 0
    option_on = 1
    default = 0


class PingPongBallColorShuffle(Choice):
    # WRITE DESCRIPTION PLEASE!!!
    display_name = "Ping Pong Ball Color Shuffle"
    option_none = 0
    option_on = 1
    default = 0


class PlaneColorShuffle(Choice):
    # WRITE DESCRIPTION PLEASE!!!
    display_name = "Plane Color Shuffle"
    option_none = 0
    option_on = 1
    default = 0


class BasketballColorShuffle(Choice):
    # WRITE DESCRIPTION PLEASE!!!
    display_name = "Basketball Color Shuffle"
    option_none = 0
    option_on = 1
    default = 0


class FrisbeeColorShuffle(Choice):
    # WRITE DESCRIPTION PLEASE!!!
    display_name = "Frisbee Color Shuffle"
    option_none = 0
    option_on = 1
    default = 0


class PaddleColorShuffle(Choice):
    # WRITE DESCRIPTION PLEASE!!!
    display_name = "Paddle Color Shuffle"
    option_none = 0
    option_on = 1
    default = 0


class HeartColorShuffle(Choice):
    # WRITE DESCRIPTION PLEASE!!!
    display_name = "Heart Color Shuffle"
    option_none = 0
    option_on = 1
    default = 0


class TargetColorShuffle(Choice):
    # WRITE DESCRIPTION PLEASE!!!
    display_name = "Target Color Shuffle"
    option_none = 0
    option_on = 1
    default = 0


class SwordColorShuffle(Choice):
    # WRITE DESCRIPTION PLEASE!!!
    display_name = "Sword Color Shuffle"
    option_none = 0
    option_on = 1
    default = 0


@dataclass
class WSROptions(PerGameCommonOptions):
    # Logic Related Options
    plando_connections: WSRPlandoConnections
    stamp_goal: StampGoal
    champion_goal: ChampionGoal
    pro_status_goal: ProStatusGoal
    traps: Traps
    starting_items: StartingItems
    sports_unlock_state: SportsUnlockState
    include_hard_stamps: IncludeHardStamps
    include_long_stamps: IncludeLongStamps
    exluded_stamps: ExcludedStamps
    death_link: DeathLink

    # Cosmetic Related Options
    music_shuffle: MusicShuffle
    sfx_shuffle: SFXShuffle
    mii_shuffle: MiiShuffle
    champion_shuffle: ChampionShuffle
    text_shuffle: TextShuffle
    texture_shuffle: TextureShuffle
    water_color_shuffle: WaterColorShuffle
    bowling_ball_color_shuffle: BowlingBallColorShuffle
    ping_pong_ball_color_shuffle: PingPongBallColorShuffle
    plane_color_shuffle: PlaneColorShuffle
    basketball_color_shuffle: BasketballColorShuffle
    frisbee_color_shuffle: FrisbeeColorShuffle
    paddle_color_shuffle: PaddleColorShuffle
    heart_color_shuffle: HeartColorShuffle
    target_color_shuffle: TargetColorShuffle
    sword_color_shuffle: SwordColorShuffle

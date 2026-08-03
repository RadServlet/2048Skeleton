from utility import draw_text, draw_square
class tile:
    values = [2**i for i in range(1, 13)]
    colors = ['yellow', '#fcdb03', '#fcdb03', '#fcba03', '#fcc203', '#fca503', 
              '#fc9803', '#fc8403', '#fc6f03', '#fc6603', '#fc5a03', '#fc4e03']

    def __init__(self, VALUE, ID, BOARD, GAME, POS=[]):
        self.val = VALUE
        self.pos = POS
        self.tag = str(ID)
        self.board = BOARD
        self.game = GAME

    def update_val(self, add):
        self.val = add

    def update_pos(self, L) -> None:
        """
    Description:
    Updates the coordinate boundaries of a tile instance and renders its 
    visual elements (background shapes and text labels) onto the game board 
    canvas based on its functional tag and numeric or string value.

    Crucial Notices:
    - The `L` list must strictly contain four numeric elements representing [x1, y1, x2, y2].
    - Relies on pre-calculated coordinate midpoints to position the text layers.
    - High-value standard tiles exceeding 2048 use a fallback to the last color in the palette.
    - Empty tiles (value <= 0) suppress text rendering entirely.
    - Text indexing for standard tiles assumes `self.val` exists in `self.values`.

    Input:
    - L (list): A list of 4 integers or floats defining the bounding box [x_min, y_min, x_max, y_max].

    Output:
    - None: Modifies `self.pos` in place, executes canvas drawing functions, and returns None explicitly.

    Non-Trivial Classes:
    - Tile (self): The class instance containing attributes like `tag`, `val`, `board`, and `colors`.

    Called Methods:
    - Custom Methods:
        - draw_square(x1, y1, x2, y2, board, color, tag): Draws the background tile shape.
        - draw_text(x, y, text, board, color/ID): Renders text strings or values on the tile.
    - Trivial Methods:
        - isinstance(val, type): Built-in type checking check for string instances.
        - list.index(val): Standard list method to locate the index of the tile value.
        - str(val): Converts numeric tile values into printable strings.

    Algorithm:
    1. Store the incoming coordinate list `L` directly into the instance attribute `self.pos`.
    2. Calculate the geometric x-center, y-center, and y-thirds using the boundary coordinates.
    3. Evaluate `self.tag` to immediately intercept and render specific UI panels:
       - If 'sc', render a red square containing the current running game score text.
       - If 'rc', render a pink square containing the all-time highest score text.
    4. If it is a standard game tile, determine the target background color layout:
       - Assign cyan ('#03fcf0') if the tile value contains a loss message string.
       - Assign 'gray' and flag the tile as empty if the numerical value is 0 or lower.
       - Lookup the mapped index from `self.values` to pull from `self.colors` if under 4098.
       - Default to the final index of `self.colors` for any extreme values beyond 2048.
    5. Invoke `draw_square` to render the background using the determined color.
    6. Invoke `draw_text` to overlay the central value string only if the tile flag is not empty.
    7. Explicitly return None.

    Complexity:
    - Time Complexity: O(N) where N is the length of `self.values` due to the `.index()` lookup step.
    - Space Complexity: O(1) auxiliary space as it only allocates a few scalar coordinate variables.
        """


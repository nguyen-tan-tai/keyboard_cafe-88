import board
from kmk.modules.layers import Layers
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.mouse_keys import MouseKeys

keyboard = KMKKeyboard()

keyboard.debug_enabled = True
keyboard.col_pins = (board.GP23, board.GP22, board.GP21, board.GP20, board.GP19, board.GP18, board.GP17, board.GP11, board.GP13, board.GP10, board.GP9, board.GP8, board.GP6, board.GP5, board.GP4, board.GP3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.row_pins = (board.GP0, board.GP1, board.GP2, board.GP7, board.GP14, board.GP15)

keyboard.extensions.append(MediaKeys())
keyboard.modules.append(Layers())
keyboard.modules.append(MouseKeys())

FN = KC.MO(1)

keyboard.keymap = [
    [
        # C1      C2        C3       C4       C5       C6       C7         C8         C9        C10        C11       C12       C13        C14        C15         C16
        KC.ESC,   KC.F1,    KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,     KC.F7,     KC.F8,    KC.F9,     KC.F10,   KC.F11,   KC.F12,    KC.PSCR,   KC.INS,     KC.DEL,    #R1
        KC.ESC,   KC.TILD,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,     KC.N6,     KC.N7,    KC.N8,     KC.N9,    KC.N0,    KC.MINS,   KC.EQL,    KC.BSPC,    KC.HOME,   #R2
        KC.VOLU,  KC.TAB,   KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,      KC.Y,      KC.U,     KC.I,      KC.O,     KC.P,     KC.LBRC,   KC.RBRC,   KC.BSLS,    KC.END,    #R3
        KC.VOLD,  KC.CAPS,  KC.A,    KC.S,    KC.D,    KC.F,    KC.G,      KC.NO,     KC.H,     KC.J,      KC.K,     KC.L,     KC.SCLN,   KC.QUOT,   KC.ENT,     KC.PGUP,   #R4
        KC.MPLY,  KC.LSFT,  KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,      KC.B,      KC.N,     KC.M,      KC.COMM,  KC.DOT,   KC.SLSH,   KC.RSFT,   KC.UP,      KC.PGDN,   #R5
        KC.LCTL,  KC.LCTL,  KC.LGUI, KC.LALT, KC.SPC,  KC.NO,   FN,        KC.NO,     KC.SPC,   FN,        KC.APP,   KC.NO,    KC.RCTL,   KC.LEFT,   KC.DOWN,    KC.RGHT,   #R6
    ],                                                                                                                                                                      
    [                                                                                                                                                                       
        KC.TRNS,  KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS,   KC.TRNS,  KC.TRNS,   KC.TRNS,  KC.TRNS,  KC.TRNS,   KC.TRNS,   KC.TRNS,    KC.MUTE,   #R1
        KC.TRNS,  KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS,   KC.TRNS,  KC.TRNS,   KC.TRNS,  KC.TRNS,  KC.TRNS,   KC.TRNS,   KC.TRNS,    KC.VOLU,   #R2
        KC.TRNS,  KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS,   KC.TRNS,  KC.TRNS,   KC.TRNS,  KC.TRNS,  KC.TRNS,   KC.TRNS,   KC.TRNS,    KC.VOLD,   #R3
        KC.TRNS,  KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS,   KC.TRNS,  KC.TRNS,   KC.TRNS,  KC.TRNS,  KC.TRNS,   KC.TRNS,   KC.TRNS,    KC.TRNS,   #R4
        KC.TRNS,  KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS,   KC.TRNS,  KC.TRNS,   KC.TRNS,  KC.TRNS,  KC.TRNS,   KC.MB_LMB, KC.MS_UP,   KC.MB_RMB, #R5
        KC.TRNS,  KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS,   KC.TRNS,  KC.TRNS,   KC.TRNS,  KC.TRNS,  KC.TRNS,   KC.MS_LT,  KC.MS_DN,   KC.MS_RT,  #R6
        
    ],
   
]

if __name__ == '__main__':
    keyboard.go()

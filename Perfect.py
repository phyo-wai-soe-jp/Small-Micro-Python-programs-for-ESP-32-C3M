import time
from machine import Pin, PWM

# 1. Initialize PWM on Pin 21
buzzer = PWM(Pin(21))

# 2. Note frequencies (Hz) - C Major scale mapping
NOTES = {
    'REST': 0,
    'G4': 392, 'A4': 440, 'B4': 494,
    'C5': 523, 'D5': 587, 'E5': 659, 'F5': 698, 'G5': 784, 'A5': 880, 'B5': 988,
    'C6': 1047, 'D6': 1175, 'E6': 1319
}

# 3. Tempo Configuration for 12/8
# An eighth note gets 1 tick.
EIGHTH_TICK = 0.2  # Adjust this value to change overall speed

# Note lengths in terms of eighth-note ticks
DOTTED_HALF = 6
HALF = 4
DOTTED_QUARTER = 3
QUARTER = 2
EIGHTH = 1

# 4. Melody Sequence parsed from image_445dc3.jpg
melody = [
    # --- Line 1 (Measures 1 - 4) ---
    ('REST', DOTTED_HALF), ('REST', QUARTER), ('G4', EIGHTH), ('A4', EIGHTH), ('C5', EIGHTH), ('C5', EIGHTH), # M1 Intro
    ('C5', DOTTED_QUARTER), ('REST', EIGHTH), ('E5', EIGHTH), ('D5', EIGHTH), ('C5', QUARTER), ('E5', EIGHTH), # M2
    ('E5', EIGHTH), ('D5', EIGHTH), ('E5', EIGHTH), ('E5', QUARTER), ('E5', EIGHTH), ('C5', EIGHTH), ('C5', QUARTER), ('C5', EIGHTH), # M3
    ('C5', EIGHTH), ('D5', EIGHTH), ('E5', EIGHTH), ('D5', DOTTED_HALF), ('REST', DOTTED_QUARTER), # M4
    
    # --- Line 2 (Measures 5 - 8) ---
    ('D5', DOTTED_QUARTER), ('REST', EIGHTH), ('E5', EIGHTH), ('D5', EIGHTH), ('C5', QUARTER), ('E5', EIGHTH), # M5
    ('G5', DOTTED_QUARTER), ('REST', EIGHTH), ('E5', EIGHTH), ('D5', EIGHTH), ('C5', QUARTER), ('C5', EIGHTH), # M6
    ('C5', EIGHTH), ('D5', EIGHTH), ('E5', EIGHTH), ('F5', QUARTER), ('F5', EIGHTH), ('E5', QUARTER), ('D5', EIGHTH), ('D5', QUARTER), ('C5', EIGHTH), # M7
    ('C5', EIGHTH), ('D5', EIGHTH), ('E5', EIGHTH), ('D5', DOTTED_HALF), ('REST', DOTTED_QUARTER), # M8
    
    # --- Line 3 (Measures 9 - 12) ---
    ('D5', DOTTED_QUARTER), ('REST', EIGHTH), ('G5', EIGHTH), ('G5', EIGHTH), ('A5', EIGHTH), ('E5', EIGHTH), ('D5', EIGHTH), # M9
    ('E5', DOTTED_QUARTER), ('REST', QUARTER), ('E5', EIGHTH), ('E5', QUARTER), ('E5', EIGHTH), ('D5', EIGHTH), ('C5', EIGHTH), # M10
    ('E5', DOTTED_QUARTER), ('REST', QUARTER), ('E5', EIGHTH), ('E5', QUARTER), ('E5', EIGHTH), ('D5', EIGHTH), ('C5', EIGHTH), # M11
    ('F5', QUARTER), ('E5', EIGHTH), ('C5', QUARTER), ('G5', EIGHTH), ('E5', DOTTED_HALF), # M12
    
    # --- Line 4 (Measures 13 - 16) ---
    ('E5', QUARTER), ('F5', EIGHTH), ('E5', QUARTER), ('D5', EIGHTH), ('E5', QUARTER), ('D5', EIGHTH), ('C5', QUARTER), ('E5', EIGHTH), # M13
    ('E5', QUARTER), ('E5', EIGHTH), ('E5', QUARTER), ('E5', EIGHTH), ('E5', QUARTER), ('D5', EIGHTH), ('C5', QUARTER), ('E5', EIGHTH), # M14
    ('E5', QUARTER), ('E5', EIGHTH), ('E5', QUARTER), ('E5', EIGHTH), ('E5', QUARTER), ('D5', EIGHTH), ('C5', QUARTER), ('G5', EIGHTH), # M15
    ('E5', QUARTER), ('D5', EIGHTH), ('C5', QUARTER), ('G5', EIGHTH), ('E5', DOTTED_HALF), # M16
    
    # --- Line 5 (Measures 17 - 20: Section B) ---
    ('D5', DOTTED_HALF), ('REST', QUARTER), ('E5', EIGHTH), ('G5', EIGHTH), ('E5', EIGHTH), ('D5', EIGHTH), # M17
    ('C5', DOTTED_QUARTER), ('REST', QUARTER), ('C6', EIGHTH), ('B5', EIGHTH), ('A5', EIGHTH), ('B5', EIGHTH), ('E5', DOTTED_QUARTER), # M18
    ('G5', QUARTER), ('F5', EIGHTH), ('E5', QUARTER), ('D5', EIGHTH), ('C5', DOTTED_HALF), # M19
    ('REST', QUARTER), ('C6', EIGHTH), ('B5', EIGHTH), ('A5', EIGHTH), ('D5', EIGHTH), ('E5', DOTTED_HALF), # M20
    
    # --- Line 6 (Measures 21 - 23) ---
    ('E5', DOTTED_QUARTER), ('REST', EIGHTH), ('G5', EIGHTH), ('G5', EIGHTH), ('G5', QUARTER), ('A5', EIGHTH), # M21
    ('E5', QUARTER), ('D5', EIGHTH), ('C5', QUARTER), ('E5', EIGHTH), ('G5', EIGHTH), ('C6', EIGHTH), ('B5', EIGHTH), ('A5', EIGHTH), ('B5', EIGHTH), ('E5', EIGHTH), # M22
    ('C5', EIGHTH), ('D5', EIGHTH), ('E5', EIGHTH), ('G5', QUARTER), ('F5', EIGHTH), ('E5', QUARTER), ('F5', EIGHTH), # M23
    
    # --- Line 7 (Measures 24 - 27) ---
    ('E5', DOTTED_QUARTER), ('D5', DOTTED_QUARTER), ('F5', DOTTED_QUARTER), ('E5', DOTTED_QUARTER), # M24
    ('E5', DOTTED_QUARTER), ('D5', DOTTED_QUARTER), ('D5', DOTTED_QUARTER), ('C5', DOTTED_QUARTER), # M25
    ('C5', DOTTED_HALF), ('C5', DOTTED_HALF), # M26 Tied resolution note
    ('REST', DOTTED_HALF), ('REST', DOTTED_HALF) # M27 Outro Rest before C
]

# 5. Playback Engine
def play_tone(note, duration_ticks):
    freq = NOTES[note]
    total_duration = duration_ticks * EIGHTH_TICK
    
    if freq == 0:
        buzzer.duty(0) # Rest / Silence
    else:
        buzzer.freq(freq)
        buzzer.duty(512) # 50% duty cycle
        
    # Play note for 92% of its duration for phrasing clarity
    time.sleep(total_duration * 0.92)
    
    # Silence gap between distinct notes
    buzzer.duty(0)
    time.sleep(total_duration * 0.08)

def play_sheet_music():
    print("Playing image_445dc3.jpg 12/8 melody on GPIO 21...")
    try:
        for note, ticks in melody:
            play_tone(note, ticks)
    finally:
        # Turn off the PWM hardware safely on exit
        buzzer.deinit()
        print("Playback finished.")

# Execute performance loop
play_sheet_music()
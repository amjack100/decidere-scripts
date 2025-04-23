import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# American Football Positions
positions = [
    "Quarterback", "Running Back", "Wide Receiver", "Tight End",
    "Offensive Lineman", "Defensive Lineman", "Linebacker",
    "Cornerback", "Safety", "Kicker", "Punter"
]

# Generate random height in feet and inches
def generate_height():
    feet = random.randint(5, 6)
    inches = random.randint(0, 11)
    height_in_feet = feet + inches / 12.0
    return round(height_in_feet, 2)

# Generate random weight in pounds
def generate_weight():
    return random.randint(150, 350)  # Range of typical player weights

def generate_max_velocity():
    return round(random.uniform(16, 25), 1)

def generate_arm_strength_velocity():
    return round(random.uniform(50, 70), 1)

# Generate random arm strength distance in yards
def generate_arm_strength_distance():
    return round(random.uniform(40, 75), 1)

def generate_3_cone_drill():
    return round(random.uniform(5.5, 8.0), 2)

# Generate random 20 yard shuttle time
def generate_20_yard_shuttle():
    return round(random.uniform(3.5, 5.5), 2)

# Generate random 40 yard dash time
def generate_40_yard_dash():
    return round(random.uniform(4.2, 5.5), 2)

# Generate random 10 yard split time
def generate_10_yard_split():
    return round(random.uniform(1.3, 2.0), 2)
# Create a dataset
def generate_bench_reps():
    return random.randint(5, 45)

# Generate random 1 rep max press in pounds
def generate_1_rep_max_press():
    return random.randint(250, 550)

# Generate random 1 rep max squat in pounds
def generate_1_rep_max_squat():
    return random.randint(300, 750)

# Generate random power clean max in pounds
def generate_power_clean():
    return random.randint(200, 500)

def generate_vertical_jump():
    return round(random.uniform(20, 45), 1)

# Generate random broad jump in feet
def generate_broad_jump():
    return round(random.uniform(6, 13), 1)

def generate_arm_length():
    return round(random.uniform(25, 40), 1)

# Generate random hand size in inches
def generate_hand_size():
    return round(random.uniform(7.5, 10.5), 1)

def generate_catch_radius():
    return round(random.uniform(5, 15), 1)

# Generate random wingspan in inches
def generate_wingspan():
    return round(random.uniform(65, 85), 1)

# Generate random positions played
def generate_positions_played():
    return random.randint(1, 4)

def generate_male_name():
    return f"{fake.first_name_male()} {fake.last_name()}"

def generate_field_goal_distance():
    return random.randint(10, 65)

def generate_field_goal_accuracy():
    return round(random.uniform(0.55, 0.95), 2)

def generate_field_goal_consistency():
    return round(random.uniform(0, 3), 1)

def generate_punt_distance():
    return random.randint(25, 75)

def generate_punt_hang_time():
    return round(random.uniform(3.0, 5.5), 2)

def generate_punt_accuracy():
    return round(random.uniform(0.25, 0.50), 2)

def generate_punt_consistency():
    return random.randint(30, 60)

def create_football_dataset(num_players=1000):
    data = {
        "Name": [generate_male_name() for _ in range(num_players)],
        "Gender": ["Male" for _ in range(num_players)],
        "Position": [random.choice(positions) for _ in range(num_players)],
        "Height": [generate_height() for _ in range(num_players)],
        "Weight": [generate_weight() for _ in range(num_players)],
        "Arm Length (inches)": [generate_arm_length() for _ in range(num_players)],
        "Hand Size (inches)": [generate_hand_size() for _ in range(num_players)],
        "Wingspan (inches)": [generate_wingspan() for _ in range(num_players)],
        "Max Velocity (mph)": [generate_max_velocity() for _ in range(num_players)],
        "Arm Strength Velocity (mph)": [generate_arm_strength_velocity() for _ in range(num_players)],
        "Arm Strength Distance (yards)": [generate_arm_strength_distance() for _ in range(num_players)],
        "Catch Radius (feet)": [generate_catch_radius() for _ in range(num_players)],
        "3 Cone Drill (sec)": [generate_3_cone_drill() for _ in range(num_players)],
        "20 Yard Shuttle (sec)": [generate_20_yard_shuttle() for _ in range(num_players)],
        "40 Yard Dash (sec)": [generate_40_yard_dash() for _ in range(num_players)],
        "10 Yard Split (sec)": [generate_10_yard_split() for _ in range(num_players)],
        "Bench Reps at 225": [generate_bench_reps() for _ in range(num_players)],
        "1 Rep Max Press (lbs)": [generate_1_rep_max_press() for _ in range(num_players)],
        "1 Rep Max Squat (lbs)": [generate_1_rep_max_squat() for _ in range(num_players)],
        "Power Clean (lbs)": [generate_power_clean() for _ in range(num_players)],
        "Vertical Jump (inches)": [generate_vertical_jump() for _ in range(num_players)],
        "Broad Jump (feet)": [generate_broad_jump() for _ in range(num_players)],
        "Positions Played": [generate_positions_played() for _ in range(num_players)],
        "Field Goal Distance (yards)": [generate_field_goal_distance() for _ in range(num_players)],
        "Field Goal Accuracy (%)": [generate_field_goal_accuracy() for _ in range(num_players)],
        "Field Goal Consistency (avg misses)": [generate_field_goal_consistency() for _ in range(num_players)],
        "Punt Distance (yards)": [generate_punt_distance() for _ in range(num_players)],
        "Punt Hang Time (seconds)": [generate_punt_hang_time() for _ in range(num_players)],
        "Punt Accuracy (%)": [generate_punt_accuracy() for _ in range(num_players)],
        "Punt Consistency (yards)": [generate_punt_consistency() for _ in range(num_players)],
    }
    df = pd.DataFrame(data)
    return df

# Generate the dataset
df = create_football_dataset(num_players=1000)

# Display the first few rows
print(df.columns)
print(df.head())

df.to_csv('catapult_football_demo.csv', index=False)
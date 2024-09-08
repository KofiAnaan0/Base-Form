# Bundesliga Team JSON Generator

This project generates JSON data for Bundesliga teams, focusing on the team's recent seven matches. Each match includes details such as teams, goals, expected goals (x_goals), fouls, corners, half-time cards, and full-time cards.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Data Structure](#data-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
The **Bundesliga Team JSON Generator** script scrapes data related to Bundesliga teams and outputs a structured JSON file. Each JSON object contains the team name and their last seven matches, with key match statistics such as:
- Goals
- Expected goals (x_goals)
- Fouls
- Corners
- Half-time cards
- Full-time cards

This data can be used for football analytics, sports betting insights, or any other applications requiring match and team performance metrics.

## Features
- Fetches data for all Bundesliga teams.
- Provides detailed statistics for the most recent seven matches.
- Outputs data in JSON format for easy integration with other systems or analytics tools.
  
## Technologies Used
- **Python**: Core programming language used to scrape and generate the data.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/bundesliga-json-generator.git
   ```

2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the main script to generate JSON data:
   ```bash
   python generate_json.py
   ```
4. The script will output a JSON file with the following structure:
   ```bash
   python generate_json.py
   ```

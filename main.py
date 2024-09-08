import json
import os
import time
from playwright.sync_api import sync_playwright
from dataclasses import asdict, dataclass, field

@dataclass
class RecentMatches:
    """Holds RecentMatches data"""
    teams: dict = field(default_factory=dict)
    goals: dict = field(default_factory=dict)
    x_goals: dict = field(default_factory=dict)
    corners: dict = field(default_factory=dict)
    fouls: dict = field(default_factory=dict)
    HT_cards: dict = field(default_factory=dict)
    FT_cards: dict = field(default_factory=dict)

@dataclass
class HomeTeam:
    """Holds Team data"""
    name: str = None
    recent_matches: RecentMatches = field(default_factory=RecentMatches)

@dataclass
class DataStructure:
    """Holds Home Team data"""
    home_team: HomeTeam = field(default_factory=HomeTeam)

def save_to_json(data: DataStructure, filename: str):
    """Save data as json file"""
    if not os.path.exists("output"):
        os.makedirs("output")
    with open(f"output/{filename}.json", "w") as file:
        json.dump(asdict(data), file, indent=4)


def main():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Base URL
        page.goto("https://www.soccer24.com/germany/bundesliga/#/8l1ZdrsC/table/overall", timeout=120000)
        page.wait_for_timeout(10000)
        
        # Click on the link inside the specified div
        match_link_selector = 'div#g_1_zsmd0ggn a.eventRowLink'
        page.click(match_link_selector)
        print('Clicked on the match link for Dortmund vs. Heidenheim.')

        # Wait to observe the new page (optional)
        page.wait_for_timeout(5000)

        # Close browser instance when the job is done
        # browser.close()

if __name__ == "__main__":
    main()

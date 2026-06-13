"""Main menu and game interface."""

import os
import sys
from game.character import Service, RankCategory


class Menu:
    """Main menu system for the game."""

    def __init__(self):
        self.current_menu = "main"
        self.game_state = None

    def clear_screen(self):
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_header(self, title):
        """Display a formatted header."""
        self.clear_screen()
        print("=" * 80)
        print(f"{title.center(80)}")
        print("=" * 80)
        print()

    def display_main_menu(self):
        """Display the main menu."""
        self.display_header("BRITISH MILITARY LIFE SIMULATOR")
        print("Welcome to the British Military Life Simulator")
        print()
        print("1. New Game")
        print("2. Load Game")
        print("3. Settings")
        print("4. About")
        print("5. Exit")
        print()
        choice = input("Select an option (1-5): ").strip()
        return choice

    def display_service_selection(self):
        """Display service selection menu."""
        self.display_header("SELECT YOUR SERVICE")
        print("Choose which branch of the British Armed Forces to join:")
        print()
        print("1. British Army")
        print("2. Royal Navy")
        print("3. Royal Air Force")
        print("4. Royal Marines")
        print("5. Back")
        print()
        choice = input("Select a service (1-5): ").strip()
        return choice

    def display_entry_type_selection(self):
        """Display entry type selection."""
        self.display_header("SELECT ENTRY TYPE")
        print("How would you like to join the military?")
        print()
        print("1. Regular Entry (Age 18+)")
        print("2. Junior Entry (Age 16+)")
        print("   - Army: AFC Harrogate")
        print("   - RAF: RAF Halton")
        print("   - Navy: HMS Raleigh")
        print("   - Marines: CTC Lympstone")
        print("3. Direct Entry Officer (University Graduate)")
        print("4. Back")
        print()
        choice = input("Select entry type (1-4): ").strip()
        return choice

    def display_rank_selection(self, service):
        """Display rank category selection."""
        self.display_header("SELECT RANK CATEGORY")
        print(f"Starting path in {service.value}:")
        print()
        print("1. Officer (Commission)")
        print("2. Non-Commissioned Officer (NCO)")
        print("3. Enlisted Soldier/Sailor/Airman/Marine")
        print("4. Back")
        print()
        choice = input("Select rank category (1-4): ").strip()
        return choice

    def display_character_creation(self, service, entry_type):
        """Display character creation form."""
        self.display_header("CREATE YOUR CHARACTER")
        print(f"Service: {service.value}")
        print(f"Entry Type: {entry_type}")
        print()
        
        name = input("Enter your name: ").strip()
        if not name:
            print("Name cannot be empty. Using 'Soldier'.")
            name = "Soldier"

        gender = input("Select gender (M/F): ").strip().upper()
        if gender not in ['M', 'F']:
            gender = 'M'

        sexuality = input("Sexuality (Heterosexual/Homosexual/Bisexual/Other/Prefer not to say): ").strip()
        
        age = 16 if entry_type == "junior" else 18
        
        print(f"\nCharacter: {name}")
        print(f"Gender: {gender}")
        print(f"Sexuality: {sexuality}")
        print(f"Age: {age}")
        print()
        
        confirm = input("Confirm character creation? (Y/N): ").strip().upper()
        if confirm == 'Y':
            return {'name': name, 'gender': gender, 'sexuality': sexuality, 'age': age}
        return None

    def display_main_game_menu(self, character):
        """Display main game menu."""
        self.display_header(f"SERVICE RECORD - {character.name}")
        print(f"Service: {character.service.value}")
        print(f"Rank: {character.current_rank or 'Recruit'}")
        print(f"Age: {character.age}")
        print(f"Years of Service: {character.years_of_service}")
        print()
        print("1. View Career Options")
        print("2. View Personal Life")
        print("3. View Training Options")
        print("4. View Deployments")
        print("5. View Service Record")
        print("6. Interact with Family/Friends")
        print("7. Save Game")
        print("8. Load Game")
        print("9. Main Menu")
        print("10. Exit Game")
        print()
        choice = input("Select an option (1-10): ").strip()
        return choice

    def display_career_menu(self):
        """Display career options menu."""
        self.display_header("CAREER OPTIONS")
        print("1. View Current Posting")
        print("2. Request Posting Change")
        print("3. Apply for Specialization")
        print("4. Apply for Promotion")
        print("5. Apply for Command Position")
        print("6. Apply for Display Team")
        print("7. Request UKSF Selection")
        print("8. Apply for Flying Training (RAF/Navy/Army)")
        print("9. Consider Reservist Transfer")
        print("10. Consider Retirement")
        print("11. Back")
        print()
        choice = input("Select an option (1-11): ").strip()
        return choice

    def display_personal_life_menu(self):
        """Display personal life menu."""
        self.display_header("PERSONAL LIFE")
        print("1. View Family")
        print("2. View Relationships")
        print("3. Manage Hobbies")
        print("4. View Disciplinary Record")
        print("5. Schedule Leave")
        print("6. Drug Testing")
        print("7. Back")
        print()
        choice = input("Select an option (1-7): ").strip()
        return choice

    def display_training_menu(self):
        """Display training options."""
        self.display_header("TRAINING OPTIONS")
        print("1. Phase 1 Training")
        print("2. Phase 2 Training")
        print("3. Specialization Courses")
        print("4. Promotion Courses")
        print("5. Advanced Courses (JTAC, Diver, EOD, P Coy, AACC)")
        print("6. Flying Training (if applicable)")
        print("7. Leadership Courses")
        print("8. Back")
        print()
        choice = input("Select an option (1-8): ").strip()
        return choice


def display_error(message):
    """Display an error message."""
    print(f"\n[ERROR] {message}")
    input("Press Enter to continue...")


def display_success(message):
    """Display a success message."""
    print(f"\n[SUCCESS] {message}")
    input("Press Enter to continue...")


def display_info(message):
    """Display an info message."""
    print(f"\n[INFO] {message}")

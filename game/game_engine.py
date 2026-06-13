"""Core game engine."""

from game.character import Character, Service, RankCategory
from ui.menu import Menu, display_error, display_success
import json
import os


class GameEngine:
    """Main game engine controlling game flow."""

    def __init__(self):
        self.menu = Menu()
        self.current_character = None
        self.running = True
        self.ensure_save_dir()

    def ensure_save_dir(self):
        """Ensure saves directory exists."""
        if not os.path.exists('saves'):
            os.makedirs('saves')

    def run(self):
        """Main game loop."""
        while self.running:
            choice = self.menu.display_main_menu()
            
            if choice == '1':
                self.new_game()
            elif choice == '2':
                self.load_game()
            elif choice == '3':
                self.display_settings()
            elif choice == '4':
                self.display_about()
            elif choice == '5':
                self.running = False
                print("\nThank you for playing British Military Life Simulator!")
            else:
                display_error("Invalid selection. Please try again.")

    def new_game(self):
        """Start a new game."""
        self.menu.display_header("NEW GAME")
        
        # Service selection
        while True:
            service_choice = self.menu.display_service_selection()
            if service_choice == '1':
                service = Service.ARMY
                break
            elif service_choice == '2':
                service = Service.NAVY
                break
            elif service_choice == '3':
                service = Service.RAF
                break
            elif service_choice == '4':
                service = Service.MARINES
                break
            elif service_choice == '5':
                return
            else:
                display_error("Invalid selection.")
        
        # Entry type selection
        while True:
            entry_choice = self.menu.display_entry_type_selection()
            if entry_choice == '1':
                entry_type = "regular"
                break
            elif entry_choice == '2':
                entry_type = "junior"
                break
            elif entry_choice == '3':
                entry_type = "officer"
                break
            elif entry_choice == '4':
                return
            else:
                display_error("Invalid selection.")
        
        # Rank selection
        while True:
            rank_choice = self.menu.display_rank_selection(service)
            if rank_choice == '1':
                rank_category = RankCategory.OFFICER
                break
            elif rank_choice == '2':
                rank_category = RankCategory.NCO
                break
            elif rank_choice == '3':
                rank_category = RankCategory.ENLISTED
                break
            elif rank_choice == '4':
                return
            else:
                display_error("Invalid selection.")
        
        # Character creation
        char_data = self.menu.display_character_creation(service, entry_type)
        if char_data:
            self.current_character = Character(
                char_data['name'],
                service,
                rank_category,
                entry_type
            )
            self.current_character.age = char_data['age']
            self.current_character.sexuality = char_data['sexuality']
            
            display_success(f"Character {self.current_character.name} created!")
            self.play_game()

    def play_game(self):
        """Main game play loop."""
        while self.current_character and self.running:
            choice = self.menu.display_main_game_menu(self.current_character)
            
            if choice == '1':
                self.show_career_options()
            elif choice == '2':
                self.show_personal_life()
            elif choice == '3':
                self.show_training_options()
            elif choice == '4':
                self.show_deployments()
            elif choice == '5':
                self.show_service_record()
            elif choice == '6':
                self.interact_with_family()
            elif choice == '7':
                self.save_game()
            elif choice == '8':
                self.load_game()
            elif choice == '9':
                self.current_character = None
                return
            elif choice == '10':
                self.running = False
            else:
                display_error("Invalid selection.")

    def show_career_options(self):
        """Display career options."""
        self.menu.display_header("CAREER OPTIONS")
        choice = self.menu.display_career_menu()
        # TODO: Implement career options
        display_error("Career options not yet implemented.")

    def show_personal_life(self):
        """Display personal life options."""
        self.menu.display_header("PERSONAL LIFE")
        choice = self.menu.display_personal_life_menu()
        # TODO: Implement personal life options
        display_error("Personal life options not yet implemented.")

    def show_training_options(self):
        """Display training options."""
        self.menu.display_header("TRAINING OPTIONS")
        choice = self.menu.display_training_menu()
        # TODO: Implement training options
        display_error("Training options not yet implemented.")

    def show_deployments(self):
        """Display deployment information."""
        self.menu.display_header("DEPLOYMENTS")
        print("Deployment information not yet implemented.")
        input("Press Enter to continue...")

    def show_service_record(self):
        """Display service record."""
        self.menu.display_header("SERVICE RECORD")
        print(f"Name: {self.current_character.name}")
        print(f"Service: {self.current_character.service.value}")
        print(f"Age: {self.current_character.age}")
        print(f"Years of Service: {self.current_character.years_of_service}")
        print(f"Current Rank: {self.current_character.current_rank or 'Recruit'}")
        print(f"Current Posting: {self.current_character.current_posting or 'Not yet assigned'}")
        print(f"Specializations: {', '.join(self.current_character.specializations) or 'None'}")
        print(f"Health Status: {self.current_character.health_status}")
        print()
        input("Press Enter to continue...")

    def interact_with_family(self):
        """Interact with family and friends."""
        self.menu.display_header("FAMILY & RELATIONSHIPS")
        # TODO: Implement family interactions
        display_error("Family interactions not yet implemented.")

    def save_game(self):
        """Save current game."""
        if self.current_character:
            filename = f"saves/{self.current_character.name.lower().replace(' ', '_')}.json"
            try:
                with open(filename, 'w') as f:
                    json.dump(self.current_character.to_dict(), f, indent=2, default=str)
                display_success(f"Game saved to {filename}")
            except Exception as e:
                display_error(f"Failed to save game: {str(e)}")

    def load_game(self):
        """Load a saved game."""
        self.menu.display_header("LOAD GAME")
        # TODO: Implement game loading
        display_error("Load game not yet implemented.")

    def display_settings(self):
        """Display game settings."""
        self.menu.display_header("SETTINGS")
        print("Settings not yet implemented.")
        input("Press Enter to continue...")

    def display_about(self):
        """Display about information."""
        self.menu.display_header("ABOUT")
        print("British Military Life Simulator v0.1.0")
        print()
        print("A comprehensive text-based military life simulation game featuring")
        print("the British Armed Forces across all four services.")
        print()
        print("Features:")
        print("- Accurate military ranks and structure")
        print("- Career progression from recruitment to retirement")
        print("- Specialization and training courses")
        print("- Personal relationships and family")
        print("- Military deployments and operations")
        print()
        input("Press Enter to continue...")

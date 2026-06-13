#!/usr/bin/env python3
"""British Military Life Simulator - Main entry point."""

import sys
from game.game_engine import GameEngine


def main():
    """Start the game."""
    print("\n" + "=" * 80)
    print("BRITISH MILITARY LIFE SIMULATOR".center(80))
    print("Version 0.1.0".center(80))
    print("=" * 80 + "\n")
    print("Initializing game...\n")
    
    try:
        game = GameEngine()
        game.run()
    except KeyboardInterrupt:
        print("\n\nGame interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nFatal error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

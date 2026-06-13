"""Character creation and management system."""

import json
from datetime import datetime
from enum import Enum


class Service(Enum):
    """Military services."""
    ARMY = "British Army"
    NAVY = "Royal Navy"
    RAF = "Royal Air Force"
    MARINES = "Royal Marines"


class RankCategory(Enum):
    """Rank categories."""
    OFFICER = "Officer"
    NCO = "Non-Commissioned Officer"
    ENLISTED = "Enlisted"


class Character:
    """Main character class for the game."""

    def __init__(self, name, service, rank_category, entry_type="regular"):
        self.name = name
        self.service = service
        self.rank_category = rank_category
        self.entry_type = entry_type
        self.age = 18 if entry_type == "regular" else 16
        self.current_rank = None
        self.current_posting = None
        self.regiment = None
        self.specializations = []
        self.medals = []
        self.relationships = {}
        self.family = {}
        self.service_record = []
        self.qualifications = []
        self.creation_date = datetime.now()
        self.is_uksf = False
        self.is_reservist = False
        self.is_retired = False
        self.years_of_service = 0
        self.commission_type = None  # Regular, Late Entry, In-Service
        self.branch = None  # For RAF/Navy specific branches
        self.sexuality = "Not Specified"  # Personal attribute
        self.health_status = "Fit"
        self.disciplinary_record = []
        self.court_martial_record = []
        self.hobbies = []
        self.vices = []  # Potential character flaws
        self.children = []
        self.spouse = None

    def __str__(self):
        return f"{self.name} - {self.service.value} {self.rank_category.value}"

    def to_dict(self):
        """Convert character to dictionary for saving."""
        return {
            'name': self.name,
            'service': self.service.value,
            'rank_category': self.rank_category.value,
            'entry_type': self.entry_type,
            'age': self.age,
            'current_rank': self.current_rank,
            'current_posting': self.current_posting,
            'regiment': self.regiment,
            'specializations': self.specializations,
            'medals': self.medals,
            'years_of_service': self.years_of_service,
            'is_uksf': self.is_uksf,
            'is_reservist': self.is_reservist,
            'is_retired': self.is_retired,
            'health_status': self.health_status,
            'sexuality': self.sexuality,
            'qualifications': self.qualifications
        }

    @classmethod
    def from_dict(cls, data):
        """Create character from saved dictionary."""
        char = cls(
            data['name'],
            Service[data['service'].upper().replace(' ', '_')],
            RankCategory[data['rank_category'].upper().replace(' ', '_')],
            data['entry_type']
        )
        char.age = data.get('age')
        char.current_rank = data.get('current_rank')
        char.current_posting = data.get('current_posting')
        char.regiment = data.get('regiment')
        char.specializations = data.get('specializations', [])
        char.medals = data.get('medals', [])
        char.years_of_service = data.get('years_of_service', 0)
        char.is_uksf = data.get('is_uksf', False)
        char.is_reservist = data.get('is_reservist', False)
        char.is_retired = data.get('is_retired', False)
        char.health_status = data.get('health_status', 'Fit')
        char.sexuality = data.get('sexuality', 'Not Specified')
        char.qualifications = data.get('qualifications', [])
        return char

    def gain_specialization(self, specialization):
        """Add a new specialization."""
        if specialization not in self.specializations:
            self.specializations.append(specialization)
            return True
        return False

    def promote(self, new_rank):
        """Promote to new rank."""
        self.current_rank = new_rank
        self.service_record.append({
            'action': 'Promotion',
            'rank': new_rank,
            'date': datetime.now()
        })

    def add_medal(self, medal):
        """Award a medal."""
        self.medals.append({
            'medal': medal,
            'date_awarded': datetime.now()
        })

    def add_relationship(self, name, relationship_type):
        """Add a personal relationship."""
        self.relationships[name] = {
            'type': relationship_type,
            'status': 'Active',
            'interactions': 0
        }

    def add_child(self, name, age):
        """Add a child."""
        self.children.append({
            'name': name,
            'age': age,
            'mother' if self.gender == 'F' else 'father': self.name
        })

    def log_service_action(self, action, details):
        """Log an action in service record."""
        self.service_record.append({
            'action': action,
            'details': details,
            'date': datetime.now()
        })

    def add_discipline(self, offense, penalty):
        """Log disciplinary action."""
        self.disciplinary_record.append({
            'offense': offense,
            'penalty': penalty,
            'date': datetime.now()
        })

    def add_court_martial(self, charges, outcome):
        """Log court martial."""
        self.court_martial_record.append({
            'charges': charges,
            'outcome': outcome,
            'date': datetime.now()
        })

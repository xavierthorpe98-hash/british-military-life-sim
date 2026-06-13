# British Military Life Simulator

A comprehensive text-based military life simulation game featuring the British Armed Forces across all four services with accurate ranks, regiments, specializations, and career progression.

## Features

### Services
- **British Army** - Infantry, Cavalry, Artillery, Engineers, Signals, REME, Medical Corps, and support roles
- **Royal Navy** - Surface warfare, submariners, naval aviation, and logistics
- **Royal Air Force** - Fast jets, transport, helicopters, and support roles
- **Royal Marines** - Commando operations and specialist roles

### Career Features
- Accurate rank structures for all services and regiments
- Complete regimental, battalion, and corps organization
- Junior Entry options (AFC Harrogate - Army, RAF Halton - RAF, HMS Raleigh - Navy, CTC Lympstone - Marines)
- Accelerated promotion pathways
- Phase 1 & 2 training
- Specialization courses (JTAC, Diver, EOD, P Coy, AACC, Aircrew)
- UKSF Selection (SAS, SBS, SRR) with rank reversal
- Flying training and OCUs (RAF, Royal Navy, Army Aviation)
- Display team opportunities (Red Arrows, Red Devils, Black Cats, etc.)
- Late Entry Commissions
- In-Service Commissions
- Regimental Selection Boards
- Command positions across all ranks

### Personal Life System
- Character creation with job role selection
- Relationships, friends, family, and children
- Personal interactions and activities
- Hobbies and vices
- Court martials and discipline
- Drug testing
- Injury and death in service options
- Family continuation

### Deployments & Operations
- British military deployments (Cold War era through present)
- UKSF deployments and counter-terrorism operations
- Maritime counter-terrorism
- Search and rescue operations
- Foreign postings and NATO assignments
- French Foreign Legion option

### Medals & Decorations
- Campaign medals
- Gallantry awards
- Long service medals
- Medal ribbon system
- British rank insignia

### Post-Service Options
- Veteran careers
- Reservist conversion (Full-time to Reservist and vice versa)
- Reserve units across all 4 services
- Military pension
- Career to age 65

## Project Structure

```
british-military-life-sim/
├── README.md
├── main.py
├── config/
│   └── settings.py
├── data/
│   ├── ranks.json
│   ├── regiments.json
│   ├── specializations.json
│   ├── courses.json
│   ├── deployments.json
│   ├── medals.json
│   ├── postings.json
│   └── vehicles.json
├── game/
│   ├── __init__.py
│   ├── character.py
│   ├── career.py
│   ├── military_structure.py
│   ├── interactions.py
│   ├── relationships.py
│   ├── training.py
│   ├── deployments.py
│   └── game_engine.py
├── ui/
│   ├── __init__.py
│   ├── menu.py
│   ├── display.py
│   └── input_handler.py
└── saves/
    └── .gitkeep
```

## Installation

```bash
git clone https://github.com/xavierthorpe98-hash/british-military-life-sim.git
cd british-military-life-sim
python main.py
```

## Requirements
- Python 3.8+
- No external dependencies (uses only standard library)

## Development Phases

### Phase 1: Core Systems (Current)
- Character creation
- Military hierarchy and structure
- Basic career progression
- Rank systems

### Phase 2: Training & Specialization
- Phase 1 & 2 training
- Specialization courses
- UKSF selection
- Flying training

### Phase 3: Deployments & Interactions
- Deployment scenarios
- Personal relationships
- Military interactions
- Court martials

### Phase 4: Advanced Features
- Post-service careers
- Reservist system
- Command positions
- Complete career to retirement

## Game Version
0.1.0 - Initial Development

## License
MIT

## Author
Created by xavierthorpe98-hash

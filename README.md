# British Military Life Simulator

A comprehensive military career simulation game featuring the British Armed Forces across all four services: Army, Royal Navy, Royal Air Force, and Royal Marines.

## Features

### Military Services
- **British Army** - Infantry, Cavalry, Artillery, Engineers, Support
- **Royal Navy** - Surface, Submarine, Fleet Air Arm, Amphibious
- **Royal Air Force** - Fast Jets, Rotary Wing, Transport, Training
- **Royal Marines** - Commando Units, Reconnaissance, Mountain Warfare

### UKSF Operations
- Special Air Service (SAS)
- Special Boat Service (SBS)
- Special Reconnaissance Regiment (SRR)
- UKSF Support Group (SFSG)

### Career Progression
- Junior Entry (16+) at military academies
- Officer commissions via AOSB & Sandhurst
- NCO development and specialisations
- Late Entry Commission (to OF-2)
- In-Service Commission
- Command positions (platoon to strategic level)

### Training & Specialisation
- Phase 1 & Phase 2 training
- Specialist courses (JTAC, Diver, EOD, P Coy, AACC)
- Flying training & OCU conversions
- Regimental-specific training
- UKSF selection & operations

### Personal Life Simulation
- Relationships, family, children
- Hobbies, interests, vices
- Post-service careers
- Reservist options
- Medical & injury management

### Deployments & Operations
- Historical periods (1980s onwards)
- Global deployments
- Counter-terrorism operations
- Maritime counter-terror
- UKSF operations

### Achievements
- Medals & decorations
- Display teams (Red Arrows, Red Devils, Black Cats)
- Court martials & discipline
- Career milestones

## Project Structure

```
british-military-life-sim/
├── README.md
├── config/
│   ├── ranks.json
│   ├── insignia.json
│   ├── nato_codes.json
│   └── dates.json
├── src/
│   ├── character/
│   │   ├── character.js
│   │   ├── creation.js
│   │   └── progression.js
│   ├── military/
│   │   ├── army/
│   │   ├── navy/
│   │   ├── raf/
│   │   ├── marines/
│   │   └── uksf/
│   ├── career/
│   │   ├── courses.js
│   │   ├── specialisations.js
│   │   └── deployment.js
│   ├── personal/
│   │   ├── relationships.js
│   │   ├── family.js
│   │   └── lifestyle.js
│   ├── game/
│   │   ├── events.js
│   │   ├── interactions.js
│   │   └── game_loop.js
│   └── utils/
│       ├── utils.js
│       └── validators.js
├── data/
│   ├── regiments/
│   ├── units/
│   ├── squadrons/
│   ├── courses/
│   ├── deployments/
│   ├── medals/
│   └── locations.json
├── tests/
│   └── test_suite.js
└── docs/
    ├── GAME_MECHANICS.md
    ├── RANK_STRUCTURE.md
    ├── CAREER_PATHS.md
    └── API_REFERENCE.md
```

## Getting Started

```bash
# Clone repository
git clone https://github.com/xavierthorpe98-hash/british-military-life-sim.git

# Install dependencies
npm install

# Run game
npm start

# Run tests
npm test
```

## Documentation

- [Game Mechanics](docs/GAME_MECHANICS.md)
- [Rank Structure](docs/RANK_STRUCTURE.md)
- [Career Paths](docs/CAREER_PATHS.md)
- [API Reference](docs/API_REFERENCE.md)

## Roadmap

### Phase 1: Foundation
- [x] Project structure
- [ ] Character creation system
- [ ] Rank & insignia system
- [ ] Basic career progression

### Phase 2: Military Services
- [ ] British Army (regiments, battalions, corps)
- [ ] Royal Navy (surface ships, submarines, FAA)
- [ ] Royal Air Force (squadrons, OCUs, aircraft)
- [ ] Royal Marines (commando units, specialisation)

### Phase 3: Career Features
- [ ] Courses & specialisations
- [ ] UKSF selection & operations
- [ ] Command positions
- [ ] Deployments & operations

### Phase 4: Personal Simulation
- [ ] Relationships & family
- [ ] Personal interactions
- [ ] Post-service careers
- [ ] Medical & injury system

### Phase 5: Polish & Expansion
- [ ] Historical periods (1980s+)
- [ ] Display teams
- [ ] Court martials & discipline
- [ ] Medal & decoration system

## Contributing

This is an active development project. Contributions welcome for:
- Data accuracy (regiments, units, ranks, insignia)
- Game mechanics refinement
- Additional features & interactions
- Testing & bug fixes

## License

TBD

## Author

Xavier Thorpe (@xavierthorpe98-hash)

---

**Note**: This simulator aims for historical accuracy while providing engaging gameplay. All ranks, insignia, units, and procedures are based on current British Armed Forces structure.
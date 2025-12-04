"""
Element Groups Taxonomy - Core movement categories in pommel horse gymnastics.
Based on FIG Code of Points element group structure.
"""

ELEMENT_GROUPS = {
    "scissors_single_leg": {
        "id": "EG_I",
        "name": "Scissors & Single-Leg Work",
        "description": "Pendulum swings with separated legs, single-leg cuts and transfers",
        "visual_signature": "Split geometry with asymmetric leg positions",
        "movements": {
            "basic_scissor": {
                "pattern": "One leg forward, one back, switching over pommel",
                "amplitude": "Legs swing above shoulder height",
                "separation": "Maximum leg spread",
                "rhythm": "Pendulum timing"
            },
            "double_scissor": {
                "pattern": "Two consecutive scissors in sequence",
                "complexity": "Maintains momentum through switches",
                "visual": "Continuous split geometry"
            },
            "traveling_scissor": {
                "pattern": "Scissor that traverses length of horse",
                "example": "Mikulak (D value)",
                "spatial": "End-to-end translation"
            },
            "scissor_to_handstand": {
                "pattern": "Scissor culminating in vertical position",
                "difficulty": "D value",
                "visual": "Pendulum to vertical transition"
            }
        },
        "placement": "Typically at routine beginning for momentum generation",
        "form_requirements": [
            "Legs above shoulder height",
            "Maximum leg separation",
            "Pointed toes",
            "Hip thrust forward at center"
        ]
    },
    
    "circles_flairs": {
        "id": "EG_II",
        "name": "Circles & Flairs",
        "description": "Continuous rotational patterns - foundation of pommel horse work",
        "visual_signature": "Horizontal body rotation with legs as radius",
        "movements": {
            "double_leg_circle": {
                "pattern": "Both legs together swinging 360° around horse",
                "body_position": "Straight, horizontal to ground",
                "form": "Legs together, toes pointed, body extended",
                "rhythm": "Even, metronomic tempo",
                "critical_phases": {
                    "quarter": "Push initiation, direction generation",
                    "three_quarter": "Hand switch, continuity maintenance"
                }
            },
            "flair": {
                "pattern": "Circle with legs straddled wide",
                "visual": "Elevated hips, 'floating' appearance",
                "straddle": "Maximum leg separation during rotation",
                "purpose": "Direction changes, visual impact",
                "example": "Thomas flair"
            },
            "russian": {
                "pattern": "Circle maintaining front support throughout",
                "hand_movement": "Hands move to stay in front",
                "visual": "Continuous forward-facing position"
            },
            "spindle": {
                "pattern": "Body rotation during circle",
                "complexity": "Maintains tempo while rotating",
                "visual": "Spiral trajectory"
            }
        },
        "spatial_variations": {
            "between_pommels": "Widest support, beginner starting point",
            "single_pommel": "Advanced, requires precise balance",
            "saddle_circles": "Center section, higher difficulty value",
            "end_circles": "Apparatus ends, base difficulty"
        },
        "tempo_qualities": [
            "Metronomic rhythm",
            "Muscle memory execution",
            "Even velocity throughout",
            "No pauses or hesitations"
        ]
    },
    
    "travels": {
        "id": "EG_III",
        "name": "Travels",
        "description": "Circles that translate across the horse length",
        "visual_signature": "Rotational motion with lateral displacement",
        "movements": {
            "magyar": {
                "direction": "Forward travel",
                "difficulty": "D value",
                "pattern": "Circles progressing toward horse end",
                "visual": "Forward momentum with rotation"
            },
            "sivado": {
                "direction": "Backward travel",
                "difficulty": "D value",
                "pattern": "Circles progressing toward opposite end",
                "form": "Open hips and chest emphasized",
                "visual": "Reverse momentum with rotation"
            },
            "roth": {
                "pattern": "Single Russian travel",
                "difficulty": "D value",
                "technique": "Front support maintained during translation"
            },
            "wu_guonian": {
                "pattern": "Double Russian travel",
                "difficulty": "E value",
                "complexity": "Two rotations during translation"
            }
        },
        "spatial_coverage": [
            "Full length traversal most common",
            "Partial travels possible",
            "Zone transition management",
            "Momentum preservation critical"
        ],
        "technical_requirements": [
            "Maintain circle quality during translation",
            "Smooth zone transitions",
            "Consistent tempo throughout",
            "Precise hand placement timing"
        ]
    },
    
    "spindles_handstands": {
        "id": "EG_IV",
        "name": "Spindles & Handstands",
        "description": "Rotational variations and vertical positions",
        "visual_signature": "Dimensional complexity and static-dynamic contrast",
        "movements": {
            "spindle_basic": {
                "pattern": "Body rotation during circle work",
                "visual": "Twist added to circular motion",
                "difficulty_modifier": "Location affects value"
            },
            "full_spindle_end": {
                "location": "End of horse",
                "difficulty": "D value",
                "pattern": "Complete rotation on end section"
            },
            "full_spindle_saddle": {
                "location": "Saddle (center)",
                "difficulty": "F value (upgraded from D)",
                "complexity": "More challenging support position"
            },
            "kehr_variations": {
                "pattern": "360° turn on one arm and pommel",
                "sohn": "D value",
                "bezugo": "E value",
                "efficiency": "High value in single circle",
                "visual": "One-armed rotational pivot"
            },
            "handstand_element": {
                "pattern": "Vertical static position",
                "placement": "Start or end of routine",
                "form": "Control and stability required",
                "deduction_trigger": "Show of strength, pausing, lowering"
            }
        }
    },
    
    "dismounts": {
        "id": "EG_V",
        "name": "Dismounts",
        "description": "Exit elements - now their own element group (2025-28 cycle)",
        "visual_signature": "Final impression, routine punctuation",
        "scoring_innovation": "Counts twice - as element AND as EG credit",
        "types": {
            "russian_dismount": {
                "pattern": "Exit through Russian position",
                "highest_value": "Triple Russian (D value)",
                "visual": "Rotational exit"
            },
            "handstand_dismount": {
                "pattern": "Exit through vertical position",
                "more_common": True,
                "difficulty_factors": [
                    "Entry type",
                    "Pirouetting (rotation during handstand)",
                    "Turn degrees"
                ],
                "highest_value": "Stockli to handstand with 450° turn (E value)",
                "example": "1.25 rotations"
            }
        },
        "execution_requirements": [
            "Stuck landing essential",
            "No steps or hops",
            "Vertical alignment in handstand",
            "Clean entry from circle work"
        ],
        "strategic_importance": "Double scoring makes high-value dismounts critical"
    }
}


def get_element_group(group_id: str) -> dict:
    """Retrieve element group by ID."""
    for key, group in ELEMENT_GROUPS.items():
        if group.get("id") == group_id or key == group_id:
            return group
    return None


def get_all_element_groups() -> dict:
    """Return all element groups."""
    return ELEMENT_GROUPS


def get_movements_by_group(group_id: str) -> dict:
    """Get all movements within an element group."""
    group = get_element_group(group_id)
    if group:
        return group.get("movements", {})
    return {}

"""
Spatial Zones Taxonomy - Apparatus sections, positioning, and spatial relationships.
Defines the geometric vocabulary of pommel horse work.
"""

SPATIAL_ZONES = {
    "apparatus_sections": {
        "end_left": {
            "name": "Left End",
            "description": "Leftmost section of horse",
            "support_width": "Narrow, single pommel or leather",
            "difficulty_baseline": "Base value for end work",
            "common_uses": [
                "Circles on single pommel",
                "End spindles (D value)",
                "Dismount preparation"
            ],
            "stability": "Challenging - limited support area"
        },
        "saddle": {
            "name": "Saddle (Center)",
            "description": "Central section between pommels",
            "support_width": "Widest section, both pommels available",
            "difficulty_modifier": "Increases value of skills (e.g., D→F for spindle)",
            "common_uses": [
                "Beginner circle practice",
                "Wide support base",
                "High-value skill location"
            ],
            "stability": "Most stable - maximum support"
        },
        "end_right": {
            "name": "Right End", 
            "description": "Rightmost section of horse",
            "support_width": "Narrow, single pommel or leather",
            "difficulty_baseline": "Base value for end work",
            "common_uses": [
                "Circles on single pommel",
                "End spindles (D value)",
                "Dismount execution"
            ],
            "stability": "Challenging - limited support area"
        }
    },
    
    "support_configurations": {
        "between_pommels": {
            "position": "Hands on both pommels",
            "support_width": "40-45cm adjustable spacing",
            "stability": "Maximum - widest base",
            "typical_use": "Learning foundation, stable circles",
            "progression_stage": "Beginner starting point"
        },
        "single_pommel": {
            "position": "Both hands on one pommel",
            "support_width": "Minimal - pommel diameter only",
            "stability": "Advanced - requires precise balance",
            "typical_use": "High-value skills, FLOP sequences",
            "visual_impact": "Impressive control display"
        },
        "leather_only": {
            "position": "Hands on apparatus surface (no pommels)",
            "support_width": "Variable hand placement",
            "stability": "Most challenging",
            "typical_use": "Advanced circles, travels",
            "aesthetic": "Pure, unassisted rotation"
        },
        "one_pommel_one_leather": {
            "position": "Mixed support - one hand on pommel, one on leather",
            "support_width": "Asymmetric",
            "stability": "Moderate difficulty",
            "typical_use": "Transitions, travel elements",
            "dynamic": "Active hand repositioning"
        }
    },
    
    "trajectory_patterns": {
        "stationary_circle": {
            "description": "Rotation without translation",
            "path": "Fixed circular plane",
            "zone_usage": "Single section maintained",
            "visual": "Pure rotational motion"
        },
        "longitudinal_travel": {
            "description": "Movement along horse length",
            "path": "Linear translation with rotation",
            "zone_usage": "All three sections sequentially",
            "examples": ["Magyar (forward)", "Sivado (backward)"],
            "visual": "Lateral progression while rotating"
        },
        "transverse_circle": {
            "description": "Rotation across horse width",
            "path": "Perpendicular to length axis",
            "zone_usage": "Width of saddle or end",
            "visual": "Side-to-side rotation"
        },
        "diagonal_path": {
            "description": "Angled trajectory across apparatus",
            "path": "Oblique to length axis",
            "zone_usage": "Multiple sections at angles",
            "visual": "Complex spatial geometry"
        }
    },
    
    "spatial_requirements": {
        "zone_coverage": {
            "rule": "Must use all three sections of horse",
            "deduction": "Applied if sections unused",
            "strategic": "Plan routine for complete coverage",
            "visual_impact": "Full apparatus utilization"
        },
        "pommel_spacing": {
            "regulation": "40-45cm adjustable",
            "optimization": "Match to gymnast shoulder width",
            "beginner_preference": "Closer spacing for stability",
            "advanced_preference": "Wider for increased difficulty"
        },
        "body_clearance": {
            "requirement": "No apparatus contact with body/legs",
            "deduction_types": [
                "Brushing (light contact)",
                "Hitting (solid contact)"
            ],
            "form_emphasis": "Hip height maintenance",
            "spatial_control": "Precise body positioning"
        }
    },
    
    "dimensional_analysis": {
        "vertical_plane": {
            "hip_height": {
                "optimal": "Maximum elevation above apparatus",
                "effect": "Easier skill execution, better form",
                "technique": "Fast loop execution raises body",
                "visual": "'Floating' appearance"
            },
            "shoulder_position": {
                "requirement": "Erect shoulders",
                "effect": "Body alignment, control",
                "visual": "Extended, tall posture"
            },
            "leg_amplitude": {
                "scissors": "Above shoulder height required",
                "circles": "Extended horizontal",
                "flairs": "Wide straddle elevation",
                "deduction": "Lack of amplitude"
            }
        },
        "horizontal_plane": {
            "body_extension": {
                "requirement": "Straight body throughout",
                "critical_points": "Quarter and three-quarter positions",
                "form": "No pike or excessive arch",
                "muscle_engagement": "Full body tension, especially glutes"
            },
            "rotational_radius": {
                "leg_position": "Determines circle diameter",
                "together": "Tighter circles, faster tempo",
                "straddled": "Wider circles (flairs), more power",
                "visual": "Geometric precision"
            }
        },
        "sagittal_plane": {
            "front_back_orientation": {
                "front_support": "Body facing forward",
                "back_support": "Body facing backward",
                "side_support": "Body lateral to horse",
                "transitions": "Smooth orientation changes"
            }
        }
    }
}


APPARATUS_SPECS = {
    "dimensions": {
        "length": "160 cm (63 inches)",
        "width": "34-36 cm (13.4-14.2 inches)",
        "height": "115 cm (45.3 inches) from floor",
        "pommel_height": "12 cm (4.7 inches) above surface",
        "pommel_spacing": "40-45 cm (15.75-17.72 inches) adjustable"
    },
    "construction": {
        "body": "Metal frame with foam rubber",
        "cover": "Synthetic leather (modern) or natural leather",
        "pommels": "Plastic handles (modern)",
        "surface": "Firm but slightly cushioned"
    },
    "safety": {
        "mat_thickness": "10 cm surrounding",
        "mat_function": "Landing safety only (not apparatus forgiveness)"
    }
}


def get_zone_requirements() -> dict:
    """Return spatial requirements for valid routines."""
    return SPATIAL_ZONES["spatial_requirements"]


def get_support_config(config_name: str) -> dict:
    """Retrieve specific support configuration."""
    return SPATIAL_ZONES["support_configurations"].get(config_name, {})


def get_trajectory_pattern(pattern_name: str) -> dict:
    """Retrieve specific trajectory pattern."""
    return SPATIAL_ZONES["trajectory_patterns"].get(pattern_name, {})


def analyze_spatial_coverage(elements: list) -> dict:
    """Analyze whether routine covers all required zones."""
    zones_used = set()
    for element in elements:
        if "zone" in element:
            zones_used.add(element["zone"])
    
    return {
        "zones_covered": list(zones_used),
        "all_sections_used": len(zones_used) >= 3,
        "coverage_complete": "end_left" in zones_used and "saddle" in zones_used and "end_right" in zones_used
    }

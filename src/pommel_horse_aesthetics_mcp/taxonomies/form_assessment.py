"""
Form Assessment Taxonomy - Body position, execution quality, technical precision.
Defines the formal aesthetic criteria for pommel horse evaluation.
"""

FORM_ELEMENTS = {
    "body_extension": {
        "straight_body": {
            "requirement": "Completely extended throughout routine",
            "critical_points": [
                "Quarter position in circles",
                "Three-quarter position in circles",
                "Peak of swing in scissors"
            ],
            "muscle_engagement": "Full body tension, especially gluteus muscles",
            "visual": "Clean lines, no breaks in body shape",
            "deduction_triggers": [
                "Pike (hip break)",
                "Excessive arch",
                "Body sag"
            ]
        },
        "hip_position": {
            "optimal": "Straight hips, extended",
            "circles": "Hips high above apparatus",
            "flairs": "Maximum hip elevation for 'floating' appearance",
            "deduction": "Lack of extension in circles/flairs",
            "technique": "Fast execution raises hips naturally"
        },
        "chest_opening": {
            "requirement": "Open chest throughout",
            "critical_for": "Back loops and Sivado (backward travels)",
            "visual": "Expanded thoracic position",
            "effect": "Better body line, easier breathing"
        },
        "shoulder_alignment": {
            "requirement": "Erect shoulders",
            "function": "Body control and support",
            "visual": "Tall, lifted posture",
            "effect": "Maintains straight body position"
        }
    },
    
    "leg_form": {
        "together_vs_apart": {
            "legs_together": {
                "requirement": "All elements except scissors, flairs, single-leg",
                "visual": "Unified leg line",
                "aesthetic": "Clean, precise geometry",
                "regulation": "FIG guideline standard"
            },
            "legs_separated": {
                "allowed_in": [
                    "Scissors",
                    "Single-leg elements", 
                    "Flairs"
                ],
                "assessment": "Degree and control of separation important",
                "scissors": "Maximum spread required",
                "flairs": "Wide straddle for effect",
                "visual": "Intentional split geometry"
            }
        },
        "leg_extension": {
            "requirement": "Straight legs during entire routine",
            "no_bending": "Knees locked throughout",
            "visual": "Extended lines from hip to toe",
            "deduction": "Bent knees at any point"
        },
        "toe_pointing": {
            "requirement": "Pointed feet throughout",
            "aesthetic": "Extended line, refined appearance",
            "detail": "Even in dynamic movements",
            "deduction": "Flexed feet (common error)"
        },
        "amplitude": {
            "scissors": {
                "requirement": "Above shoulder height",
                "measurement": "Legs must swing high on pendulum",
                "deduction": "Lack of amplitude",
                "visual": "Dramatic height, impressive geometry"
            },
            "circles": {
                "requirement": "Horizontal extension maintained",
                "measurement": "Legs parallel to floor at peak",
                "visual": "Flat plane of rotation"
            },
            "flairs": {
                "requirement": "Maximum straddle with elevation",
                "measurement": "Wide split, hips high",
                "visual": "Expansive, elevated geometry"
            }
        }
    },
    
    "hand_technique": {
        "placement": {
            "even_placement": "Both hands symmetrically positioned",
            "quarter_counter": "Slight counter-turn at quarter position",
            "function": "Prevents hip over-turning",
            "precision": "Exact pommel grip"
        },
        "pushing": {
            "quarter_push": {
                "timing": "25% through circle",
                "purpose": "Direction generation",
                "emphasis": "Strong push on apparatus",
                "effect": "Circle quality determination"
            },
            "three_quarter_push": {
                "timing": "75% through circle", 
                "purpose": "Continuity generation",
                "emphasis": "Momentum for completion",
                "critical": "Most important push"
            }
        },
        "switching": {
            "timing": "Precise hand repositioning",
            "speed": "Quick but controlled",
            "placement": "Exact pommel/leather contact",
            "visual": "Imperceptible transitions"
        },
        "grip": {
            "security": "Firm pommel hold",
            "adjustment": "Micro-adjustments during rotation",
            "chalking": "Proper surface preparation",
            "slip_prevention": "Controlled glide, not slick"
        }
    },
    
    "apparatus_relationship": {
        "clearance": {
            "requirement": "No body/leg contact with apparatus",
            "violation_types": {
                "brushing": {
                    "description": "Light contact",
                    "deduction": "Minor",
                    "common_causes": "Low hip position, poor control"
                },
                "hitting": {
                    "description": "Solid contact",
                    "deduction": "Larger penalty",
                    "common_causes": "Loss of control, fatigue"
                }
            },
            "prevention": "High hip position, body control"
        },
        "support_efficiency": {
            "hand_only": "Entire weight on hands/arms",
            "no_body_support": "Cannot use torso/legs on apparatus",
            "technique": "Shoulder and arm strength essential",
            "endurance": "Sustained upper body engagement"
        }
    },
    
    "position_quality": {
        "front_support": {
            "description": "Body in push-up position facing forward",
            "alignment": "Shoulders over hands",
            "visual": "Forward-facing orientation",
            "use": "Most common position, circle starting point"
        },
        "back_support": {
            "description": "Body facing backward over apparatus",
            "alignment": "Hips over hands",
            "visual": "Backward-facing orientation", 
            "use": "Russian elements, specific skills"
        },
        "side_support": {
            "description": "Body lateral to apparatus",
            "alignment": "Body perpendicular to horse length",
            "visual": "Profile orientation",
            "use": "Scissors, transitions"
        },
        "handstand": {
            "description": "Vertical inverted position",
            "requirements": [
                "Vertical alignment",
                "Body extension",
                "Control (no strength show)",
                "Stable hold"
            ],
            "deductions": [
                "Show of strength",
                "Pausing",
                "Lowering from position"
            ]
        }
    }
}


EXECUTION_DEDUCTIONS = {
    "form_breaks": {
        "bent_knees": "Throughout routine",
        "flexed_feet": "Lack of toe pointing",
        "bent_arms": "During support phases",
        "pike_body": "Hip angle break",
        "arched_body": "Excessive spinal extension"
    },
    "technical_errors": {
        "lack_of_extension": "Circles and flairs not fully extended",
        "hip_breaks": "Hip angle collapse in circles/flairs",
        "lack_of_amplitude": "Scissors/swings below shoulder height",
        "insufficient_separation": "Scissor legs not wide enough",
        "show_of_strength": "Visible muscle strain in handstands",
        "pausing": "Any stop during routine",
        "lowering": "Descent from handstand position"
    },
    "apparatus_violations": {
        "brushing": "Light contact with apparatus",
        "hitting": "Solid contact with apparatus",
        "missing_zones": "Not using all three sections",
        "hand_slip": "Loss of pommel grip (major error)"
    },
    "rhythm_errors": {
        "tempo_break": "Inconsistent speed",
        "pause": "Complete stop in motion",
        "rushed_element": "Excessive speed loss of control",
        "sluggish_element": "Loss of momentum"
    }
}


AESTHETIC_QUALITIES = {
    "precision": {
        "geometric": "Exact angles and lines",
        "temporal": "Precise timing",
        "spatial": "Exact positioning",
        "overall": "Machine-like accuracy"
    },
    "control": {
        "body": "Complete physical mastery",
        "tempo": "Rhythm management",
        "amplitude": "Height/distance regulation",
        "transitions": "Seamless changes"
    },
    "difficulty": {
        "skill_selection": "High-value elements chosen",
        "combinations": "Complex sequences",
        "risk_level": "Challenging skills attempted",
        "composition": "Strategic routine construction"
    },
    "artistry": {
        "flow": "Liquid continuity",
        "dynamics": "Energy variations",
        "expression": "Individual style",
        "composition": "Routine architecture"
    }
}


SCORING_CONTEXT = {
    "execution_score": {
        "starting_value": 10.0,
        "method": "Deductions subtracted",
        "assessment": "Form, technique, errors",
        "judges": "Execution panel"
    },
    "difficulty_score": {
        "calculation": "Sum of 8 highest value elements (2025-28 cycle)",
        "element_groups": "Bonus for all 4 groups + dismount",
        "method": "Code of Points values",
        "innovation": "Dismount counts as element AND EG credit"
    },
    "total_score": {
        "formula": "D-score + E-score",
        "display": "Both scores shown separately",
        "comparison": "Higher combined total wins"
    }
}


def assess_form_quality(element_execution: dict) -> dict:
    """Assess form quality of an executed element."""
    deductions = []
    quality_score = 10.0
    
    # Check body extension
    if not element_execution.get("body_extended", True):
        deductions.append("lack_of_extension")
        quality_score -= 0.3
    
    # Check leg form
    if not element_execution.get("legs_straight", True):
        deductions.append("bent_knees")
        quality_score -= 0.3
    
    if not element_execution.get("toes_pointed", True):
        deductions.append("flexed_feet")
        quality_score -= 0.1
    
    # Check amplitude
    if element_execution.get("element_type") == "scissor":
        if not element_execution.get("above_shoulder", True):
            deductions.append("lack_of_amplitude")
            quality_score -= 0.3
    
    # Check apparatus contact
    if element_execution.get("brushing", False):
        deductions.append("brushing")
        quality_score -= 0.1
    
    if element_execution.get("hitting", False):
        deductions.append("hitting")
        quality_score -= 0.3
    
    return {
        "quality_score": max(0, quality_score),
        "deductions": deductions,
        "form_assessment": "clean" if not deductions else "errors_present"
    }


def get_deduction_category(error_type: str) -> str:
    """Categorize a specific error type."""
    for category, errors in EXECUTION_DEDUCTIONS.items():
        if error_type in errors or error_type in errors.values():
            return category
    return "unknown"

"""
Temporal Qualities Taxonomy - Rhythm, tempo, timing, phase dynamics.
Defines the temporal aesthetic vocabulary of pommel horse gymnastics.
"""

TEMPORAL_QUALITIES = {
    "rhythm_patterns": {
        "metronomic": {
            "description": "Even, clockwork-like tempo throughout",
            "characteristic": "Consistent beat, no acceleration/deceleration",
            "origin": "Years of muscle memory training",
            "mental_state": "Automatic execution, minimal conscious thought",
            "aesthetic": "Machine-like precision, hypnotic regularity",
            "ideal_for": "Circle work, basic sequences",
            "risk": "Overthinking disrupts rhythm"
        },
        "accelerating": {
            "description": "Gradual tempo increase through sequence",
            "characteristic": "Building momentum and speed",
            "purpose": "Energy accumulation for difficult skills",
            "aesthetic": "Building intensity, crescendo effect",
            "technical_use": "Leading into dismounts or high-value elements"
        },
        "decelerating": {
            "description": "Controlled tempo reduction",
            "characteristic": "Slowing while maintaining form",
            "purpose": "Precision control, setup for position changes",
            "aesthetic": "Deliberate control display",
            "caution": "Fatigue at routine end - maintain tempo"
        },
        "syncopated": {
            "description": "Varied rhythm with intentional tempo shifts",
            "characteristic": "Speed variations between element types",
            "complexity": "Advanced timing control",
            "aesthetic": "Dynamic, musical quality",
            "example": "Fast circles, slower scissors, fast travels"
        }
    },
    
    "continuity": {
        "unbroken_flow": {
            "requirement": "No pauses or stops during routine",
            "regulation": "Pausing results in deduction",
            "aesthetic_ideal": "Seamless motion from mount to dismount",
            "challenge": "Maintaining flow during transitions",
            "visual": "Liquid, continuous movement"
        },
        "transition_quality": {
            "smooth": {
                "description": "Imperceptible element changes",
                "technique": "Perfect timing of hand/body repositioning",
                "aesthetic": "Effortless appearance",
                "execution": "No tempo disruption"
            },
            "punctuated": {
                "description": "Distinct element boundaries",
                "technique": "Clear skill separation without pausing",
                "aesthetic": "Articulated, phrase-like",
                "execution": "Rhythm maintained across boundaries"
            }
        },
        "momentum_management": {
            "preservation": "Carry energy through sequence",
            "generation": "Build momentum from mount or scissors",
            "transfer": "Channel energy into next element",
            "loss_points": [
                "Poor hand switches",
                "Body position breaks",
                "Amplitude reduction"
            ]
        }
    },
    
    "phase_timing": {
        "critical_phases": {
            "quarter_position": {
                "timing": "25% through circle",
                "action": "Push initiation on apparatus",
                "function": "Direction generation for circle",
                "technique": "Emphasis on pushing horse",
                "effect": "Determines circle quality for remainder",
                "visual": "First major body position"
            },
            "half_position": {
                "timing": "50% through circle",
                "body_orientation": "Peak of rotation",
                "function": "Maximum extension point",
                "technique": "Maintain body line",
                "visual": "Profile view, full extension"
            },
            "three_quarter_position": {
                "timing": "75% through circle",
                "action": "Hand switch execution",
                "function": "Continuity generation for completion",
                "technique": "Push for momentum, precise hand placement",
                "critical": "Most important phase for flow",
                "visual": "Transition moment"
            },
            "completion_position": {
                "timing": "100% - return to start",
                "function": "Setup for next circle or element",
                "seamless": "No visible endpoint",
                "visual": "Return to front support"
            }
        },
        "swing_phases": {
            "upswing": {
                "description": "Leg rise portion of pendulum",
                "energy": "Acceleration phase",
                "form": "Maximum extension and height",
                "scissors": "Above shoulder height required"
            },
            "peak": {
                "description": "Highest point of swing arc",
                "moment": "Momentary suspension",
                "transition": "Direction change preparation",
                "visual": "Maximum amplitude display"
            },
            "downswing": {
                "description": "Leg descent portion",
                "energy": "Momentum building for next phase",
                "control": "Controlled descent, not collapse",
                "setup": "Position for next element"
            }
        }
    },
    
    "tempo_characteristics": {
        "velocity": {
            "fast": {
                "effect": "Higher body elevation",
                "benefit": "Easier skill execution",
                "appearance": "Dynamic, energetic",
                "suitable_for": "Circles, flairs, travels",
                "risk": "Control loss if too fast"
            },
            "moderate": {
                "effect": "Balanced control and amplitude",
                "benefit": "Precision maintenance",
                "appearance": "Controlled, composed",
                "suitable_for": "Most element types",
                "ideal": "Base tempo for routines"
            },
            "controlled": {
                "effect": "Maximum precision",
                "benefit": "Form perfection",
                "appearance": "Deliberate, powerful",
                "suitable_for": "Handstands, specific positions",
                "risk": "Momentum loss if too slow"
            }
        },
        "consistency": {
            "even_throughout": {
                "description": "Constant tempo across entire routine",
                "difficulty": "Requires exceptional conditioning",
                "aesthetic": "Machine-like precision",
                "score_benefit": "Minimal tempo deductions"
            },
            "tempo_zones": {
                "description": "Different speeds for different element groups",
                "strategy": "Match tempo to element requirements",
                "complexity": "Advanced control",
                "aesthetic": "Dynamic range, musical phrasing"
            }
        }
    },
    
    "endurance_dynamics": {
        "fatigue_patterns": {
            "routine_beginning": {
                "energy": "Peak freshness",
                "execution": "Sharpest form",
                "strategy": "Technical elements early"
            },
            "routine_middle": {
                "energy": "Sustained work",
                "challenge": "Maintain consistency",
                "risk": "Form degradation begins"
            },
            "routine_end": {
                "energy": "Maximum fatigue",
                "critical": "Most common error zone",
                "warning": "Don't relax before dismount",
                "strategy": "Focus through completion"
            }
        },
        "conditioning_requirements": {
            "muscular_endurance": "Continuous motion without breaks",
            "cardiovascular": "Elevated heart rate throughout",
            "mental_endurance": "Concentration from mount to dismount",
            "preparation": "Routine practice for duration tolerance"
        }
    },
    
    "temporal_aesthetics": {
        "flow_quality": {
            "liquid": "Seamless, water-like continuity",
            "mechanical": "Precise, clockwork regularity",
            "dynamic": "Energy variations, peaks and valleys",
            "sustained": "Unrelenting consistency"
        },
        "phrasing": {
            "element_phrases": "Groups of related skills as units",
            "breath_rhythm": "Gymnast breathing patterns",
            "musical_analogy": "Measures, phrases, movements",
            "compositional": "Intentional temporal structure"
        },
        "climax_placement": {
            "early_climax": "High difficulty at start",
            "mid_climax": "Peak skills in middle",
            "late_climax": "Building to dismount",
            "multiple_climaxes": "Several high-value moments"
        }
    }
}


TIMING_METRICS = {
    "routine_duration": {
        "typical_range": "30-60 seconds",
        "regulation": "No specific time requirement",
        "influenced_by": [
            "Skill difficulty",
            "Number of elements",
            "Tempo chosen",
            "Gymnast style"
        ]
    },
    "element_duration": {
        "single_circle": "1-2 seconds typical",
        "scissor": "2-3 seconds",
        "travel": "3-5 seconds",
        "dismount": "1-2 seconds"
    }
}


def get_rhythm_pattern(pattern_name: str) -> dict:
    """Retrieve specific rhythm pattern."""
    return TEMPORAL_QUALITIES["rhythm_patterns"].get(pattern_name, {})


def get_critical_phase(phase_name: str) -> dict:
    """Retrieve timing details for specific phase."""
    return TEMPORAL_QUALITIES["phase_timing"]["critical_phases"].get(phase_name, {})


def analyze_tempo_strategy(routine_structure: list) -> dict:
    """Analyze temporal strategy of routine structure."""
    analysis = {
        "continuity_maintained": True,
        "rhythm_pattern": "unknown",
        "fatigue_risk_zones": [],
        "temporal_aesthetic": []
    }
    
    # Check for pauses (continuity breaks)
    if any(el.get("pause", False) for el in routine_structure):
        analysis["continuity_maintained"] = False
    
    # Analyze tempo consistency
    tempos = [el.get("tempo", "moderate") for el in routine_structure]
    if len(set(tempos)) == 1:
        analysis["rhythm_pattern"] = "metronomic"
    else:
        analysis["rhythm_pattern"] = "syncopated"
    
    # Identify fatigue zones
    if len(routine_structure) > 8:
        analysis["fatigue_risk_zones"].append("routine_end")
    
    return analysis

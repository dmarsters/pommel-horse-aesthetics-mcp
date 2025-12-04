"""
Local execution entry point for pommel-horse-aesthetics-mcp server.
Run with: python -m pommel_horse_aesthetics_mcp
"""

from .server import mcp

if __name__ == "__main__":
    mcp.run()

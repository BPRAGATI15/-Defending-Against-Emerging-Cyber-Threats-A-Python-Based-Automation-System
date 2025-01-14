import os
import logging
import rich
from datetime import datetime
from typing import List
from rich.console import Console
from rich.table import Table

# Configure logging
logging.basicConfig(
    filename="cyber_threats.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
console = Console()

def log_event(event: str):
    """Log security-related events."""
    logging.info(event)

class Threat:
    def __init__(self, name: str, description: str, risk_level: str):
        self.name = name
        self.description = description
        self.risk_level = risk_level

    def __str__(self):
        return f"Threat: {self.name}\nDescription: {self.description}\nRisk Level: {self.risk_level}\n"

class CyberDefense:
    """A class to defend against cyber threats."""

    def __init__(self):
        self.threats: List[Threat] = []

    def add_threat(self, threat: Threat):
        """Add a new threat to monitor."""
        self.threats.append(threat)
        log_event(f"Threat added: {threat.name}")
        console.print(f"[green]Threat added: {threat.name}[/green]")

    def analyze_threats(self):
        """Analyze all tracked threats and provide insights."""
        high_risk_threats = [t for t in self.threats if t.risk_level == "High"]
        table = Table(title="Threat Analysis")
        table.add_column("Name", style="cyan", justify="left")
        table.add_column("Description", style="magenta", justify="left")
        table.add_column("Risk Level", style="red", justify="center")

        for threat in self.threats:
            table.add_row(threat.name, threat.description, threat.risk_level)

        console.print(table)

        if high_risk_threats:
            log_event("High-risk threats detected.")
            console.print("[bold red]High-Risk Threats Identified:[/bold red]")
            for threat in high_risk_threats:
                console.print(threat)
        else:
            console.print("[bold green]No high-risk threats identified.[/bold green]")

    def simulate_attack(self, threat_name: str):
        """Simulate an attack scenario for a given threat."""
        log_event(f"Simulating attack for: {threat_name}")
        for threat in self.threats:
            if threat.name == threat_name:
                console.print(f"[bold yellow]Simulating attack for {threat.name}...[/bold yellow]")
                console.print(f"[cyan]Description:[/cyan] {threat.description}")
                console.print("[bold green]Suggested Defense: Implement a robust incident response plan.[/bold green]")
                return
        console.print(f"[red]Threat '{threat_name}' not found.[/red]")

    def automate_analysis(self):
        """Automate threat analysis on a periodic basis."""
        console.print("[bold blue]Automating threat analysis...[/bold blue]")
        self.analyze_threats()
        log_event("Automated analysis completed.")

if __name__ == "__main__":
    # Example program to showcase defense against cyber threats
    defense_system = CyberDefense()

    # Add example threats
    defense_system.add_threat(Threat("Phishing Attack", "Deceptive emails to steal credentials.", "High"))
    defense_system.add_threat(Threat("Ransomware", "Malware that encrypts files until a ransom is paid.", "High"))
    defense_system.add_threat(Threat("Zero-Day Exploit", "Exploitation of unknown vulnerabilities.", "Medium"))

    # Automate analysis
    defense_system.automate_analysis()

    # Simulate attack for a specific threat
    defense_system.simulate_attack("Phishing Attack")

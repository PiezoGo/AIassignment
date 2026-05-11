import random


# ============================================================
# VACUUM CLEANER AGENT
# Environment : 3x3 grid of rooms (Dirty / Clean)
# Goal       : Clean all rooms
# ============================================================

class VacuumEnvironment:
    """Represents the 3x3 grid environment."""
    
    def __init__(self, rows=3, cols=3):
        self.rows = rows
        self.cols = cols
        self.agent_pos = (0, 0)          # Start at top-left
        self.total_cleans = 0
        self.total_moves = 0
        
        # Randomly set rooms as Dirty or Clean
        self.grid = {
            (r, c): random.choice(['Dirty', 'Clean'])
            for r in range(rows) for c in range(cols)
        }

    def display(self):
        """Display the current grid state."""
        print("\nEnvironment:")
        for r in range(self.rows):
            row_str = "  "
            for c in range(self.cols):
                cell = 'D' if self.grid[(r, c)] == 'Dirty' else 'C'
                if (r, c) == self.agent_pos:
                    row_str += f'[{cell}] '
                else:
                    row_str += f' {cell}  '
            print(row_str)
        print(f"   Cleans: {self.total_cleans} | Moves: {self.total_moves}")

    def is_all_clean(self):
        """Check if all rooms are clean."""
        return all(status == 'Clean' for status in self.grid.values())


class VacuumAgent:
    """Simple Reflex Vacuum Agent."""
    
    def __init__(self, environment):
        self.env = environment

    def perceive(self):
        """Get status of current room."""
        return self.env.grid[self.env.agent_pos]

    def act(self):
        """Perform one action. Returns False when task is complete."""
        if self.env.is_all_clean():
            print("\nAll rooms clean. Task complete!")
            return False

        status = self.perceive()
        pos = self.env.agent_pos

        if status == 'Dirty':
            # SUCK
            self.env.grid[pos] = 'Clean'
            self.env.total_cleans += 1
            print(f"Action: SUCK at {pos} -> Room cleaned")
        else:
            # MOVE toward nearest dirty room
            target = self.find_nearest_dirty()
            if target:
                self.env.agent_pos = self.step_toward(pos, target)
                self.env.total_moves += 1
                print(f"Action: MOVE {pos} -> {self.env.agent_pos}")

        return True

    def find_nearest_dirty(self):
        """Return the first dirty room found (row by row)."""
        for r in range(self.env.rows):
            for c in range(self.env.cols):
                if self.env.grid[(r, c)] == 'Dirty':
                    return (r, c)
        return None

    def step_toward(self, current, target):
        """Move one step closer to target."""
        cr, cc = current
        tr, tc = target

        if cr < tr:
            return (cr + 1, cc)      # Down
        elif cr > tr:
            return (cr - 1, cc)      # Up
        elif cc < tc:
            return (cr, cc + 1)      # Right
        elif cc > tc:
            return (cr, cc - 1)      # Left
        return current


# --- Main Simulation ---
def run_simulation():
    print("=== VACUUM CLEANER AGENT SIMULATION ===\n")
    
    env = VacuumEnvironment(rows=3, cols=3)
    agent = VacuumAgent(env)
    
    print("Initial State:")
    env.display()

    step = 0
    max_steps = 60

    while step < max_steps:
        step += 1
        print(f"\nStep {step}:")
        
        if not agent.act():
            break
            
        env.display()

    print("\n" + "="*50)
    print(f"Simulation ended after {step} steps.")
    print(f"Rooms cleaned : {env.total_cleans}")
    print(f"Moves made    : {env.total_moves}")


if __name__ == "__main__":
    run_simulation()
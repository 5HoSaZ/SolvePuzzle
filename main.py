from WaterJugs import WaterJugsSolver

solver = WaterJugsSolver()
solver.SetCapacity(3, 5, 8)
solver.SetEndState(0, 2, 4)
solver.Solve()

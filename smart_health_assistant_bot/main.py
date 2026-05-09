import tkinter as tk
from graph.builder import build_health_graph
from ui.app import HealthAssistantUI

if __name__ == "__main__":
    # Create the 'Brain'
    compiled_graph = build_health_graph()

    # Launch the 'Face'
    root = tk.Tk()
    app = HealthAssistantUI(root, compiled_graph)
    root.mainloop()
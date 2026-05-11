import os
import subprocess
import glob

def find_file(filename: str, search_path: str = "/home") -> str:
    """Cherche un fichier sur le PC par son nom"""
    matches = glob.glob(f"{search_path}/**/{filename}", recursive=True)
    if matches:
        return "\n".join(matches)
    return f"Aucun fichier '{filename}' trouvé dans {search_path}"

def read_file(filepath: str) -> str:
    """Lit le contenu d'un fichier texte"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Erreur : {e}"

def list_directory(path: str = ".") -> str:
    """Liste les fichiers d'un dossier"""
    try:
        files = os.listdir(path)
        return "\n".join(files)
    except Exception as e:
        return f"Erreur : {e}"

def open_file(filepath: str) -> str:
    """Ouvre un fichier avec l'application par défaut du système"""
    try:
        subprocess.Popen(["xdg-open", filepath])  # Linux
        # subprocess.Popen(["open", filepath])     # Mac
        # os.startfile(filepath)                   # Windows
        return f"Fichier ouvert : {filepath}"
    except Exception as e:
        return f"Erreur : {e}"
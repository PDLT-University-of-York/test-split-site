import re
from pathlib import Path

# 1. SET UP
# Grab name of this file, move up to root of vle-support/
PROJECT_ROOT = Path(__file__).parent.parent 

# 2. COPY PAGE CONTENTS: staff -> student 

# Configure file mappings ---
# Format: "STAFF_SOURCE_FILE": "STUDENT_DESTINATION_FILE"
FILE_MAPPINGS = {
    "docs/help/troubleshooting.md": "docs/student/help/troubleshooting.md"
}

# define function
def sync_mapped_files():
    """Copies content directly from Staff source files to Student destination files."""
    print("--- Syncing Mapped Staff Content to Student Pages ---")
    for src_rel, dest_rel in FILE_MAPPINGS.items():
        src_path = PROJECT_ROOT / src_rel
        dest_path = PROJECT_ROOT / dest_rel

        if not src_path.exists():
            print(f"Error: Source file '{src_rel}' does not exist.")
            continue

        # Ensure destination folder exists
        dest_path.parent.mkdir(parents=True, exist_ok=True)

        # Read source and write to destination
        src_content = src_path.read_text(encoding="utf-8")
        dest_path.write_text(src_content, encoding="utf-8")
        print(f"Synced: {src_rel}  ==>  {dest_rel}")

# 3. RUN ALL FUNCTIONS
if __name__ == "__main__":
    sync_mapped_files()
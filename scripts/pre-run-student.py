import re
from pathlib import Path

# 1. SET UP
# Grab name of this file, move up to root of vle-support/
PROJECT_ROOT = Path(__file__).parent.parent 

# 2a. COPY PAGE CONTENTS: staff -> student 

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

# 2b. REMOVE SEARCH EXCLUSION FOR STUDENT SITE
# added in staff build - this resets for student search
def remove_search_exclusions():
    """Removes search exclusions so Student pages are searchable in Student Hub."""
    student_dir = PROJECT_ROOT / "docs/student"
    
    if not student_dir.exists():
        return

    for file_path in student_dir.rglob("*.md"):
        content = file_path.read_text(encoding="utf-8")
        
        if "search:" in content:
            # Remove injected search exclude lines
            updated_content = content.replace("search:\n  exclude: true", "").replace("search: {exclude: true}", "")
            file_path.write_text(updated_content, encoding="utf-8")
            print(f"Restored search for Student build: {file_path.relative_to(PROJECT_ROOT)}")

# 3. RUN ALL FUNCTIONS
if __name__ == "__main__":
    sync_mapped_files()
    remove_search_exclusions()
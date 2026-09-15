import re
from pathlib import Path

# 1. SET UP
# Grab name of this file, move up to root of vle-support/
PROJECT_ROOT = Path(__file__).parent.parent 

# 2. EXCLUDE STUDENT DIRECTORY FROM STAFF SEARCH
# Entire directory to hide from Staff search
SEARCH_EXCLUDE_DIR = "docs/student"

# define function
def process_search_exclusions():
    """Injects search: {exclude: true} into existing front matter on Student pages."""
    print("--- Applying Search Exclusions ---")
    student_dir = PROJECT_ROOT / SEARCH_EXCLUDE_DIR

    if not student_dir.exists():
        return

    for file_path in student_dir.rglob("*.md"):
        content = file_path.read_text(encoding="utf-8")

        # Skip if search metadata is already configured anywhere in the file
        if "search:" in content:
            continue

        # Check if the file starts with YAML metadata block
        if content.startswith("---"):
            # Split by '---' to isolate the YAML metadata block
            # parts[0] = "", parts[1] = YAML content, parts[2+] = body content
            parts = content.split("---", 2)

            if len(parts) >= 3:
                yaml_block = parts[1].strip()
                body_content = parts[2]

                # Append the search exclusion setting inside the YAML block
                updated_yaml = f"{yaml_block}\nsearch:\n  exclude: true"
                new_content = f"---\n{updated_yaml}\n---{body_content}"

                file_path.write_text(new_content, encoding="utf-8")
                print(f"Updated front matter in: {file_path.relative_to(PROJECT_ROOT)}")
        else:
            # Fallback for pages missing front matter entirely
            new_content = f"---\nsearch:\n  exclude: true\n---\n\n{content}"
            file_path.write_text(new_content, encoding="utf-8")
            print(f"Created front matter in: {file_path.relative_to(PROJECT_ROOT)}")

# 3. RUN ALL FUNCTIONS
if __name__ == "__main__":
    process_search_exclusions()
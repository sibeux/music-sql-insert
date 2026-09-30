import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = BASE_DIR / "input.txt"
OUTPUT_FILE = BASE_DIR / "delete.sql"


def main():
    urls = [
        line.strip()
        for line in INPUT_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    if not urls:
        print("Tidak ada URL di input.txt")
        return

    images_json = json.dumps(
        urls,
        ensure_ascii=False,
        indent=4
    )

    sql = f"""SET @images = '{images_json}';

DELETE FROM albums
WHERE image IN (
    SELECT value
    FROM JSON_TABLE(
        @images,
        '$[*]' COLUMNS (
            value VARCHAR(255) PATH '$'
        )
    ) AS x
);

DELETE FROM musics
WHERE cover IN (
    SELECT value
    FROM JSON_TABLE(
        @images,
        '$[*]' COLUMNS (
            value VARCHAR(255) PATH '$'
        )
    ) AS x
);
"""

    OUTPUT_FILE.write_text(sql, encoding="utf-8")

    print(f"Generated {len(urls)} URLs")
    print(f"Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
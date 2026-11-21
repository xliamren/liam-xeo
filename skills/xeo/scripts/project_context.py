"""Read-only discovery of an explicit project SEO/GEO context entrypoint."""
import argparse
import json
from pathlib import Path


def discover(start=None, project_root=None):
    current = Path(project_root or start or Path.cwd()).expanduser().resolve()
    if not current.is_dir():
        raise ValueError(f'Not a project directory: {current}')
    while True:
        entry = current / '.xeo' / 'context.md'
        if entry.is_file():
            return {'project_root': str(current), 'context': str(entry.resolve())}
        if project_root is not None or (current / '.git').exists() or current.parent == current:
            raise FileNotFoundError(f'No .xeo/context.md within project boundary: {current}')
        current = current.parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--start', default=None)
    parser.add_argument('--project-root', default=None)
    args = parser.parse_args()
    try:
        result = discover(args.start, args.project_root)
    except (ValueError, FileNotFoundError) as error:
        parser.exit(2, f'{error}\n')
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    main()

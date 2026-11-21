import tempfile
import unittest
from pathlib import Path
from project_context import discover


class ProjectContextTests(unittest.TestCase):
    def test_nested_directory_and_distinct_projects(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ('one', 'two'):
                project = root / name
                (project / '.xeo').mkdir(parents=True)
                (project / '.xeo/context.md').touch()
                (project / 'src/deep').mkdir(parents=True)
                self.assertEqual(discover(project / 'src/deep')['project_root'], str(project.resolve()))

    def test_repository_boundary_prevents_parent_context_leak(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / '.xeo').mkdir()
            (root / '.xeo/context.md').touch()
            child = root / 'child'
            child.mkdir()
            (child / '.git').touch()  # Also covers submodule/worktree git files.
            with self.assertRaises(FileNotFoundError):
                discover(child)
            self.assertEqual(discover(project_root=root)['project_root'], str(root.resolve()))

    def test_explicit_root_does_not_search_parents(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / '.xeo').mkdir()
            (root / '.xeo/context.md').touch()
            child = root / 'child'
            child.mkdir()
            with self.assertRaises(FileNotFoundError):
                discover(project_root=child)


if __name__ == '__main__':
    unittest.main()

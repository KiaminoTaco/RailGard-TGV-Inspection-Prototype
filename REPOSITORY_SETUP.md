# Repository Setup Guide

This package provides the documentation and folder structure for the RailGard
GitHub repository.

## Before publishing

1. Review the technical PDF and remove any credentials or private information.
2. Add the actual CAD, drawings, schematics and source code to their folders.
3. Replace placeholder `.gitkeep` files as folders receive real content.
4. Review the README links after adding media.
5. Check large CAD/binary files before pushing.

## Suggested first commit

```bash
git add .
git commit -m "chore: initialize RailGard project structure"
git push
```

## Large files

For large CAD or binary assets, consider Git LFS rather than committing very
large files directly to normal Git history.

## Important

This package does not contain fabricated source code, CAD models, PCB files,
or test results. Those should come from the actual project files.

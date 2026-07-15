#!/bin/bash
# Print the path to the most recently modified .m4a in ~/Downloads, or exit 1 if none.
set -euo pipefail
latest=$(ls -t "$HOME"/Downloads/*.m4a 2>/dev/null | head -1)
if [ -z "$latest" ]; then
  echo "no .m4a files found in ~/Downloads" >&2
  exit 1
fi
echo "$latest"

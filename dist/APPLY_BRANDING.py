#!/usr/bin/env python3
"""Apply only the SlovAnLearn brand assets to an existing static website."""
from pathlib import Path
import shutil,sys
if len(sys.argv)!=2:
 raise SystemExit('Usage: python APPLY_BRANDING.py /path/to/website-folder')
source=Path(__file__).resolve().parent
site=Path(sys.argv[1]).expanduser().resolve()
if not (site/'index.html').is_file() and (site/'dist/index.html').is_file():site=site/'dist'
index=site/'index.html'
if not index.is_file():raise SystemExit('No index.html found in that folder or its dist/ subfolder.')
text=index.read_text(encoding='utf-8')
if '</head>' not in text.lower() or '</body>' not in text.lower():raise SystemExit('The file needs closing </head> and </body> tags; no changes were made.')
backup=index.with_name('index.html.pre-slovanlearn')
if not backup.exists():shutil.copy2(index,backup)
import re
if not re.search(r'<link\b[^>]*href=[\'"](?:\./)?slovanlearn-theme\.css[\'"]',text,re.I):
 text=re.sub('</head>', '<link rel="stylesheet" href="slovanlearn-theme.css">\n</head>',text,flags=re.I,count=1)
if not re.search(r'<script\b[^>]*src=[\'"](?:\./)?slovanlearn-branding\.js[\'"]',text,re.I):
 text=re.sub('</body>', '<script src="slovanlearn-branding.js"></script>\n</body>',text,flags=re.I,count=1)
for asset in ['slovanlearn-theme.css','slovanlearn-branding.js','slovanlearn-logo.png']:
 p=source/asset
 if not p.is_file():raise SystemExit('Missing branding asset: '+asset)
for asset in ['slovanlearn-theme.css','slovanlearn-branding.js','slovanlearn-logo.png']:shutil.copy2(source/asset,site/asset)
index.write_text(text,encoding='utf-8')
print('SlovAnLearn branding applied. Sign-in, configuration and study data files were not changed.')
print('Original homepage backup: '+str(backup))
